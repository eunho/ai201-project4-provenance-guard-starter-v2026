#!/usr/bin/env python3
"""
Provenance Guard — the web service.

    python app.py

Then, in another terminal:

    curl -X POST http://127.0.0.1:5000/ping \
      -H "Content-Type: application/json" \
      -d '{"message": "hello"}'

That's the example route. It works right now, before you've written anything.
**Leave it alone** — it's your control. When something breaks later, check that
`/ping` still answers: if it does, the problem is in your handler; if it
doesn't, it's the service itself.

Routes:

    POST /ping        the worked example. Already works. Don't edit it
    POST /submit      ← YOU BUILD THIS (Milestone 3, 4, 5)
    POST /appeal      ← YOU BUILD THIS (Milestone 5)
    GET  /log         the audit log. Already works
    GET  /health      is the service up, and is the model loaded
"""

import time
import uuid

from flask import Flask, jsonify, request

import audit
import config
import detector
import hardening
import scoring
import stylometry

app = Flask(__name__)

_verified_creators = set()


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────────
# Off until you turn it on. In unit 8, Milestone 1:
#
#   1. Set RATE_LIMITING_ENABLED = True in config.py (or AI201_RATE_LIMITS=1)
#   2. Choose your numbers there
#   3. Uncomment the @limiter.limit(...) line on /submit below
#
# The order doesn't matter. While limiting is off, that decorator is a no-op
# that quietly does nothing, so uncommenting it early costs you nothing — but
# it also means no 429 until you've done step 1.
#
# The storage backend is preconfigured, which stops Flask-Limiter printing a
# warning on every start. In-memory is right for one laptop and wrong for
# anything real — a restart forgets every count.

class _LimiterOff:
    """
    Stands in for the real limiter while rate limiting is off.

    It makes @limiter.limit(...) a decorator that returns the route
    untouched, so uncommenting the line before you flip the setting is
    harmless instead of a crash on startup.
    """

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """
        Who a request counts against.

        Falling back to the caller's address is the easy version. Unit 8's
        stretch asks about per-creator limits instead — and the difference
        matters: one script can look like a thousand callers, and one household
        can look like one.
        """
        payload = request.get_json(silent=True)
        # A body that parses as JSON but isn't an object — a bare list or
        # string — has no .get. Without this guard the key function raises
        # BEFORE the route runs, and a malformed request becomes a 500 that
        # looks like your handler crashed when your handler never ran.
        if not isinstance(payload, dict):
            return get_remote_address()
        creator = payload.get("creator_id")
        return creator if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """
        A rejected request still leaves a trace.

        ⚠️ An attack that shows up only as an absence is one you'll never find.
        """
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            payload = {}
        audit.log_rejection(
            creator_id=payload.get("creator_id", "unknown"),
            reason="rate_limited",
            limit=str(exc.description),
        )
        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── The worked example. Already works. Don't edit. ────────────────────────────

@app.post("/ping")
def ping():
    """
    Everything a route needs, in six lines.

    JSON arrives as a dict. You pull things out of it. You return a dict and
    the framework turns it into a response. That's the whole idea.
    """
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    """Is the service up, and has the model been downloaded yet?"""
    import detector

    loaded = detector._model is not None
    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── YOU BUILD THIS ────────────────────────────────────────────────────────────

@app.post("/submit")
@limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    """
    Take a piece of text, decide about it, log the decision, answer.
    """
    t_req_start = time.perf_counter()
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        total_latency_ms = round((time.perf_counter() - t_req_start) * 1000.0, 2)
        audit.log_rejection(creator_id="unknown", reason="malformed_json", latency_ms=total_latency_ms)
        return jsonify({
            "error": "bad_request",
            "message": "Request body must be a JSON object.",
            "latency_ms": total_latency_ms,
        }), 400

    text = payload.get("text")
    creator_id = payload.get("creator_id")

    if not isinstance(text, str) or not text.strip():
        cid = creator_id if isinstance(creator_id, str) and creator_id.strip() else "unknown"
        total_latency_ms = round((time.perf_counter() - t_req_start) * 1000.0, 2)
        audit.log_rejection(creator_id=cid, reason="missing_or_empty_text", latency_ms=total_latency_ms)
        return jsonify({
            "error": "bad_request",
            "message": "'text' field is required and must be a non-empty string.",
            "latency_ms": total_latency_ms,
        }), 400

    if not isinstance(creator_id, str) or not creator_id.strip():
        total_latency_ms = round((time.perf_counter() - t_req_start) * 1000.0, 2)
        audit.log_rejection(creator_id="unknown", reason="missing_or_empty_creator_id", latency_ms=total_latency_ms)
        return jsonify({
            "error": "bad_request",
            "message": "'creator_id' field is required and must be a non-empty string.",
            "latency_ms": total_latency_ms,
        }), 400

    if len(text) > 50000:
        total_latency_ms = round((time.perf_counter() - t_req_start) * 1000.0, 2)
        audit.log_rejection(creator_id=creator_id, reason="text_too_long", length=len(text), latency_ms=total_latency_ms)
        return jsonify({
            "error": "bad_request",
            "message": f"'text' exceeds maximum length of 50,000 characters ({len(text)} chars).",
            "latency_ms": total_latency_ms,
        }), 400

    # ── Stage 1: Linguistic input hygiene (Shape B hardening) ────────────────
    t_val_start = time.perf_counter()
    is_valid_hygiene, hygiene_err = hardening.validate_linguistic_hygiene(text)
    t_val_ms = (time.perf_counter() - t_val_start) * 1000.0

    if not is_valid_hygiene:
        total_latency_ms = round((time.perf_counter() - t_req_start) * 1000.0, 2)
        audit.log_rejection(creator_id=creator_id, reason="non_linguistic_input", error=hygiene_err, latency_ms=total_latency_ms)
        return jsonify({
            "error": "bad_request",
            "message": hygiene_err,
            "latency_ms": total_latency_ms,
        }), 400

    # ── Stage 2: Adversarial prompt-injection pre-filtering & neutralization ─
    t_prefilter_start = time.perf_counter()
    eval_text, injection_detected, injection_matches = hardening.sanitize_prompt_injections(text)
    t_prefilter_ms = (time.perf_counter() - t_prefilter_start) * 1000.0

    # ── Stage 3: Model inference watchdog with graceful degradation fallback ─
    t_model_start = time.perf_counter()
    degraded_fallback = False
    model_status = "ok"
    try:
        model_score, model_status, _ = hardening.safe_model_eval(eval_text)
    except ValueError as exc:
        total_latency_ms = round((time.perf_counter() - t_req_start) * 1000.0, 2)
        audit.log_rejection(creator_id=creator_id, reason="detector_error", error=str(exc), latency_ms=total_latency_ms)
        return jsonify({
            "error": "bad_request",
            "message": str(exc),
            "latency_ms": total_latency_ms,
        }), 400
    t_model_ms = (time.perf_counter() - t_model_start) * 1000.0

    # ── Stage 4: Stylometry and repetition scoring ───────────────────────────
    t_style_start = time.perf_counter()
    style_score = stylometry.style_signal(text)
    rep_score = stylometry.repetition_signal(text)
    t_style_ms = (time.perf_counter() - t_style_start) * 1000.0

    # ── Stage 5: Decision fusion ─────────────────────────────────────────────
    t_fusion_start = time.perf_counter()
    if model_score is None:
        # Circuit-breaker fallback: gracefully score using stylometric heuristic
        degraded_fallback = True
        combined_score = style_score
        guess, label = scoring.score_to_label(combined_score)
        label = f"{label} [Heuristic Degradation Fallback]"
        status = "degraded"
    else:
        combined_score = scoring.combine_signals(model_score, style_score, rep_score)
        guess, label = scoring.score_to_label(combined_score)
        status = "decided"

    content_id = str(uuid.uuid4())
    confidence = scoring.calculate_confidence(combined_score, guess)

    is_verified = creator_id in _verified_creators
    if is_verified:
        label = f"{label} [Verified Human Author]"
    t_fusion_ms = (time.perf_counter() - t_fusion_start) * 1000.0

    total_latency_ms = round((time.perf_counter() - t_req_start) * 1000.0, 2)
    timing_breakdown = {
        "validation_ms": round(t_val_ms, 2),
        "prefilter_ms": round(t_prefilter_ms, 2),
        "model_ms": round(t_model_ms, 2),
        "style_ms": round(t_style_ms, 2),
        "fusion_ms": round(t_fusion_ms, 2),
        "total_ms": total_latency_ms,
    }

    input_preview = text[:80] + "..." if len(text) > 80 else text
    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        confidence=confidence,
        model_score=model_score,
        style_score=style_score,
        combined_score=combined_score,
        label=label,
        status=status,
        verified_creator=is_verified,
        prompt_injection_detected=injection_detected,
        degraded_fallback=degraded_fallback,
        input_length=len(text),
        input_preview=input_preview,
        latency_ms=total_latency_ms,
        latency_breakdown=timing_breakdown,
    )

    return jsonify({
        "content_id": content_id,
        "creator_id": creator_id,
        "guess": guess,
        "confidence": confidence,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
        "combined_score": combined_score,
        "status": status,
        "verified_creator": is_verified,
        "prompt_injection_detected": injection_detected,
        "degraded_fallback": degraded_fallback,
        "latency_ms": total_latency_ms,
        "latency_breakdown": timing_breakdown,
    }), 200


@app.post("/appeal")
def appeal():
    """
    A writer says you got it wrong.
    """
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({
            "error": "bad_request",
            "message": "Request body must be a JSON object.",
        }), 400

    content_id = payload.get("content_id")
    reasoning = payload.get("reasoning")

    if not isinstance(content_id, str) or not content_id.strip():
        return jsonify({
            "error": "bad_request",
            "message": "'content_id' is required and must be a non-empty string.",
        }), 400

    if not isinstance(reasoning, str) or not reasoning.strip():
        return jsonify({
            "error": "bad_request",
            "message": "'reasoning' is required and must be a non-empty string.",
        }), 400

    entries = audit.entries_for(content_id)
    if not entries:
        return jsonify({
            "error": "not_found",
            "message": f"No submission found for content_id '{content_id}'. Check the ID and try again.",
        }), 404

    creator_id = entries[0].get("creator_id", "unknown")
    appeal_entry = audit.log_appeal(
        content_id=content_id,
        creator_id=creator_id,
        reasoning=reasoning.strip(),
    )

    return jsonify({
        "ok": True,
        "content_id": content_id,
        "creator_id": creator_id,
        "status": "under_review",
        "message": "Appeal recorded successfully. This submission has been moved to under_review.",
        "timestamp": appeal_entry.get("timestamp"),
    }), 200


# ── Stretch Features ─────────────────────────────────────────────────────────

@app.get("/content/<content_id>")
def get_content(content_id):
    """
    Stretch feature: Return one item's current status and audit history.
    """
    entries = audit.entries_for(content_id)
    if not entries:
        return jsonify({
            "error": "not_found",
            "message": f"No submission found for content_id '{content_id}'.",
        }), 404

    initial = entries[0]
    latest = entries[-1]
    status = latest.get("status", "decided")
    creator_id = initial.get("creator_id")

    return jsonify({
        "content_id": content_id,
        "creator_id": creator_id,
        "status": status,
        "guess": initial.get("guess"),
        "confidence": initial.get("confidence", 0.5),
        "label": initial.get("label"),
        "model_score": initial.get("model_score"),
        "style_score": initial.get("style_score"),
        "combined_score": initial.get("combined_score"),
        "verified_creator": creator_id in _verified_creators,
        "history": entries,
    }), 200


@app.post("/verify-creator")
def verify_creator():
    """
    Stretch feature: A writer earns a verified-human credential through an extra step.
    """
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "bad_request", "message": "JSON body required."}), 400

    creator_id = payload.get("creator_id")
    if not isinstance(creator_id, str) or not creator_id.strip():
        return jsonify({"error": "bad_request", "message": "'creator_id' is required."}), 400

    creator = creator_id.strip()
    _verified_creators.add(creator)
    audit.log_decision(
        content_id=f"cert_{creator}",
        creator_id=creator,
        status="verified_human",
        event="creator_verified",
        notes="Creator earned verified-human credential through attestation."
    )
    return jsonify({
        "ok": True,
        "creator_id": creator,
        "status": "verified_human",
        "message": f"Creator '{creator}' is now registered as a verified human author.",
    }), 200


# ── Already works ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    """
    The audit log, most recent last.

        curl "http://127.0.0.1:5000/log?limit=10"

    You need this in unit 8 to paste entries into your README, and you need it
    now to see whether your logging is actually working.
    """
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({"count": len(entries), "entries": entries})


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()
    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()
    # debug=True hands out an interactive debugger, so it's local-only — see config.py
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
