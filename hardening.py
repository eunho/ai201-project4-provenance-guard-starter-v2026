"""
Hardening layer for Provenance Guard (Capstone Shape B).

Provides:
1. Strict linguistic input hygiene (rejecting control characters, punctuation-only, emoji-only strings).
2. Adversarial prompt-injection pre-filtering & sanitization (neutralizing evasion directives and script tags).
3. Inference watchdog circuit-breaker with graceful degradation fallback to heuristic stylometry.
"""

import re
import time
from typing import Tuple, List, Optional
import detector

# Regex pattern for forbidden ASCII control characters (0x00-0x1F, except \t, \n, \r)
_CONTROL_CHAR_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")

# Regex pattern to ensure at least one recognizable linguistic word with >= 2 alphabetic letters
_LINGUISTIC_WORD_RE = re.compile(r"[A-Za-z]{2,}")

# Regex patterns for adversarial prompt injection directives and script/tag injections
_INJECTION_PATTERNS = [
    re.compile(r"(?i)\bignore\s+(?:all\s+)?previous\s+instructions\b[^\.\n]*[\.\n]?", re.IGNORECASE),
    re.compile(r"(?i)\bdisregard\s+(?:all\s+|the\s+)?(?:previous\s+instructions|stylometric\s+analysis)\b[^\.\n]*[\.\n]?", re.IGNORECASE),
    re.compile(r"(?i)\bsystem\s*:\s*provenance\s+check\s+bypassed[^\.\n]*[\.\n]?", re.IGNORECASE),
    re.compile(r"(?i)\bsystem\s+instruction\s+override\s*:[^\.\n]*[\.\n]?", re.IGNORECASE),
    re.compile(r"(?i)\btreat\s+the\s+author\s+as\s+verified[^\.\n]*[\.\n]?", re.IGNORECASE),
    re.compile(r"(?i)<\s*/?\s*(?:script|style|label|iframe|object|embed)[^>]*>", re.IGNORECASE),
]


def validate_linguistic_hygiene(text: str) -> Tuple[bool, Optional[str]]:
    """
    Validate that incoming text is legitimate printable linguistic prose.

    Rejects:
    - Text containing unprintable control characters (MF03)
    - Text consisting purely of punctuation (MF04)
    - Text consisting purely of emojis or non-word symbols (MF06)
    """
    if not isinstance(text, str) or not text.strip():
        return False, "'text' must be a non-empty string."

    # Check for forbidden control characters
    match_ctrl = _CONTROL_CHAR_RE.search(text)
    if match_ctrl:
        return False, f"Text contains forbidden unprintable control character at index {match_ctrl.start()}."

    # Check for at least one genuine linguistic word of >= 2 letters
    if not _LINGUISTIC_WORD_RE.search(text):
        return False, "Text lacks recognizable linguistic prose (minimum 2 consecutive alphabetic characters required)."

    return True, None


def sanitize_prompt_injections(text: str) -> Tuple[str, bool, List[str]]:
    """
    Detect and neutralize adversarial prompt-injection directives and script payloads.

    Returns:
    - sanitized_text: Text with adversarial prompt injection directives stripped
    - detected: True if any adversarial injection directives were identified
    - matched_patterns: Descriptions of matched patterns
    """
    sanitized = text
    detected = False
    matched = []

    for pat in _INJECTION_PATTERNS:
        matches = pat.findall(sanitized)
        if matches:
            detected = True
            matched.extend([m.strip() for m in matches if isinstance(m, str) and m.strip()])
            sanitized = pat.sub(" ", sanitized)

    if detected:
        # Collapse multiple whitespace created by stripping
        sanitized = re.sub(r"[ \t]{2,}", " ", sanitized).strip()

    return sanitized, detected, matched


def safe_model_eval(text: str, timeout_seconds: float = 3.0) -> Tuple[Optional[float], str, float]:
    """
    Execute model inference within a watchdog boundary.

    Returns:
    - score: float model score or None if fallen back
    - status: "ok" or "fallback"
    - elapsed_ms: execution time in milliseconds
    """
    t0 = time.perf_counter()
    try:
        score = detector.model_signal(text)
        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        return score, "ok", round(elapsed_ms, 2)
    except (RuntimeError, ValueError, Exception) as exc:
        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        # Graceful fallback: return None score and fallback status
        return None, f"fallback:{type(exc).__name__}", round(elapsed_ms, 2)
