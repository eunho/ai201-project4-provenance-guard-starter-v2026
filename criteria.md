# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False Positive Rate on Authentic Human Writing

Across 20 distinct authentic human-written submissions (including at least 5 plain or ESL writing samples), at most 1 sample ($\le 5\%$) is classified as `high-confidence AI` (`guess == "ai"`).

**Why this target:**
Falsely accusing a human author of submitting AI-generated content inflicts severe damage: academic disciplinary action, loss of client trust, or public humiliation. A 5% upper ceiling across rigorous test trials forces the decision thresholds to route ambiguous, simple, or non-native writing into the neutral `unsure` category rather than making a reckless false accusation.

---

## 2. Score Separation Between AI and Human Text

The mean `combined_score` of 10 benchmark AI-generated articles and 10 benchmark human-authored articles must differ by at least 0.35 points on the 0.0–1.0 score continuum across all evaluation trials.

**Why this target:**
If the average scores of AI and human text differ by less than 0.35, the detector lacks adequate discriminatory separation, causing both classes to compress into overlapping bands. A minimum 0.35 spread ensures that high-confidence human writing and high-confidence AI writing occupy distinct ends of the spectrum, with `unsure` serving as an intentional buffer in the middle.

---

## 3. Full Label Reachability (Zero Dead Zones)

In an evaluation suite consisting of human-authored, mixed/edited, and synthetic AI inputs, all 3 output labels (`high-confidence human`, `unsure`, and `high-confidence AI`) must be produced at least 3 times each.

**Why this target:**
Verifies that the threshold configuration has no dead zones, unreachable ranges, or arithmetic edge-case cutoffs. A detector that never outputs `unsure` or fails to ever reach `high-confidence human` has defective thresholds that collapse complex probability into a binary coin toss.

---

## 4. Deterministic Appeal Recording and State Transition

100% (10 out of 10) of valid `POST /appeal` requests targeting existing `content_id`s must transition the submission status to `under_review` in `logs/audit.jsonl` and return an HTTP 200 response with confirmation data in under 200ms.

**Why this target:**
The appeal system is the sole due-process safeguard protecting writers against algorithmic misjudgment. If even a single appeal is dropped, fails silently, or fails to record to disk, an accused human writer is permanently disenfranchised with zero human recourse.

---

## 5. Robust Rejection of Malformed and Boundary Inputs

100% (10 out of 10) of invalid input scenarios (missing `text`, empty string `""`, non-string types, missing `creator_id`, or text exceeding 50,000 characters) must return a structured HTTP 400 Bad Request error with an informative error message, without raising an unhandled HTTP 500 exception or crashing the server.

**Why this target:**
Production services must never crash or leak internal tracebacks when receiving unexpected input. Explicitly rejecting malformed payloads guarantees that only verifiable, parseable submissions enter the evaluation pipeline and consume local model compute.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
