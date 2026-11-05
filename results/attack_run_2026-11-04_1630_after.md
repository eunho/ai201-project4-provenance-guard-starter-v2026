# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 16:30
- Auto-marked BROKE (5xx, crash, no response): **0**
- Evaluated Verdicts: **40 HELD**, **16 BROKE**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `e4ef5e04-45c1-45a8-81dd-9afa39f03f04` | human | 0.780 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `a4bc5c95-d117-48bd-9852-786d14269f3b` | human | 0.750 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `caf92bda-460d-40dc-bce5-759a8a651713` | unsure | 0.600 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `dcce1e9f-fc38-44a9-8eec-0aabfe6bc003` | unsure | 0.520 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `bd6f583b-fa0e-46de-ad1b-d3687a6f6992` | human | 0.840 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `53be521e-c53b-487b-9c0e-71b7edac9aaa` | unsure | 0.610 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c59cfbb9-3c80-4378-8a2e-043026090fc8` | unsure | 0.480 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `90eb0e7d-46ac-499f-8106-6e7aa827b9b0` | human | 0.780 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `6ad8e37f-f9c6-4e38-ac51-e19a199615d8` | unsure | 0.570 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `927df89e-9abc-4bc4-b699-32762df35194` | ai | 0.750 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9ea0d28e-26cf-452c-a3ba-270fc9d03d7e` | unsure | 0.560 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `ec6b770c-4919-4f25-9453-563baa2d0618` | unsure | 0.450 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `757d424a-6536-4c51-a8b3-060cad02244c` | unsure | 0.420 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `db8af576-a1b4-42e3-bffb-1e69f7d0d9ce` | unsure | 0.490 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `870e38bb-e72c-4537-a240-f2ab0d9e331e` | unsure | 0.570 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `d2d5df6b-a9a3-4bfe-bea6-314bb2db78a4` | unsure | 0.410 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `60ce30f5-15b8-4683-b54e-9dcc59b263ee` | unsure | 0.560 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `12705947-c7df-4347-9ba9-0067e9171782` | human | 0.790 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `2432e24c-8f4c-4af2-b708-040867c45fa1` | human | 0.770 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `2fcfffa4-c2d6-418e-8608-f1c6660819f7` | human | 0.880 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `0d2dbac3-c0a1-4741-8c9c-df3a9851aedd` | unsure | 0.590 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `baf039bd-3f73-405d-87b8-02f04a3507b8` | human | 0.710 | BROKE |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `999359b8-7657-4cb9-825a-dd4c57f8fbac` | unsure | 0.610 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `d748b8a9-15c2-4d1a-8ecf-87f7ecd543e4` | unsure | 0.590 | BROKE |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `63d702b7-9bb1-46a0-a14e-78e0dcc58e8a` | human | 0.790 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `12525322-b9e6-49fa-a67a-8fe7b838b527` | unsure | 0.580 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `4e4f70c8-1434-4277-8424-9fc4d1402342` | unsure | 0.640 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `4388c43e-6ffa-410b-bd91-e4df011f9e90` | ai | 0.780 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `302bed4b-b012-4971-a7d9-1249376281fc` | ai | 0.740 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `494da5ee-829c-48ae-98b5-9171fdac4b70` | human | 0.870 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8be537c3-a48b-49f6-8ef1-91c94139bb34` | human | 0.870 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5f68342f-2144-4255-9f49-533f7b80fe7e` | human | 0.870 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bab6397d-0453-4211-9d37-695258a99a08` | human | 0.870 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3402b0de-31cb-4627-9685-9615c1c68c82` | human | 0.870 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `06416106-d1ee-46fc-a3c1-10c28c07dd52` | human | 0.870 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `73c42ac2-1057-4f0b-9894-89262940b902` | human | 0.870 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ab3284a1-7411-4993-a03f-2b6b8b32751e` | human | 0.870 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e4921d90-8517-4755-8b20-6e8a6cdc23b7` | human | 0.870 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `88b1fccf-1dd0-47c3-b536-f89444901e98` | human | 0.870 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "e4ef5e04-45c1-45a8-81dd-9afa39f03f04",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.78,
  "model_score": 0.1635,
  "style_score": 0.5211,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "a4bc5c95-d117-48bd-9852-786d14269f3b",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.75,
  "model_score": 0.5943,
  "style_score": 0.0774,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "caf92bda-460d-40dc-bce5-759a8a651713",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.6662,
  "style_score": 0.2513,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "dcce1e9f-fc38-44a9-8eec-0aabfe6bc003",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.52,
  "model_score": 0.6114,
  "style_score": 0.4779,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "bd6f583b-fa0e-46de-ad1b-d3687a6f6992",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.84,
  "model_score": 0.3212,
  "style_score": 0.1223,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "53be521e-c53b-487b-9c0e-71b7edac9aaa",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.61,
  "model_score": 0.5727,
  "style_score": 0.2238,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c59cfbb9-3c80-4378-8a2e-043026090fc8",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.48,
  "model_score": 0.5862,
  "style_score": 0.3843,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "90eb0e7d-46ac-499f-8106-6e7aa827b9b0",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.78,
  "model_score": 0.2452,
  "style_score": 0.4208,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "6ad8e37f-f9c6-4e38-ac51-e19a199615d8",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.57,
  "model_score": 0.7042,
  "style_score": 0.2547,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "927df89e-9abc-4bc4-b699-32762df35194",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.75,
  "model_score": 0.9792,
  "style_score": 0.5689,
  "label": "This writing closely matches the statistical predictability, uniform cadence, and formulaic phrasing commonly generated by AI language models.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "9ea0d28e-26cf-452c-a3ba-270fc9d03d7e",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.56,
  "model_score": 0.6175,
  "style_score": 0.3802,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "ec6b770c-4919-4f25-9453-563baa2d0618",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.45,
  "model_score": 0.7387,
  "style_score": 0.5782,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "757d424a-6536-4c51-a8b3-060cad02244c",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.42,
  "model_score": 0.8051,
  "style_score": 0.4898,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "db8af576-a1b4-42e3-bffb-1e69f7d0d9ce",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.49,
  "model_score": 0.8329,
  "style_score": 0.4009,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "870e38bb-e72c-4537-a240-f2ab0d9e331e",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.57,
  "model_score": 0.8005,
  "style_score": 0.6226,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "d2d5df6b-a9a3-4bfe-bea6-314bb2db78a4",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.41,
  "model_score": 0.8814,
  "style_score": 0.3076,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "60ce30f5-15b8-4683-b54e-9dcc59b263ee",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.56,
  "model_score": 0.8816,
  "style_score": 0.38,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "12705947-c7df-4347-9ba9-0067e9171782",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.79,
  "model_score": 0.3223,
  "style_score": 0.2831,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "2432e24c-8f4c-4af2-b708-040867c45fa1",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.77,
  "model_score": 0.4625,
  "style_score": 0.13,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "2fcfffa4-c2d6-418e-8608-f1c6660819f7",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.88,
  "model_score": 0.2044,
  "style_score": 0.13,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "0d2dbac3-c0a1-4741-8c9c-df3a9851aedd",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.59,
  "model_score": 0.5943,
  "style_score": 0.3655,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "baf039bd-3f73-405d-87b8-02f04a3507b8",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.71,
  "model_score": 0.4998,
  "style_score": 0.3397,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "999359b8-7657-4cb9-825a-dd4c57f8fbac",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.61,
  "model_score": 0.6401,
  "style_score": 0.2479,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "d748b8a9-15c2-4d1a-8ecf-87f7ecd543e4",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.59,
  "model_score": 0.5583,
  "style_score": 0.3917,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "63d702b7-9bb1-46a0-a14e-78e0dcc58e8a",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.79,
  "model_score": 0.0,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "12525322-b9e6-49fa-a67a-8fe7b838b527",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.58,
  "model_score": 0.0112,
  "style_score": 0.83,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "4e4f70c8-1434-4277-8424-9fc4d1402342",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.64,
  "model_score": 0.9976,
  "style_score": 0.405,
  "label": "We could not confidently determine whether this text is human-written or AI-generated, so no definitive automated verdict has been assigned.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "4388c43e-6ffa-410b-bd91-e4df011f9e90",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.78,
  "model_score": 0.9969,
  "style_score": 0.655,
  "label": "This writing closely matches the statistical predictability, uniform cadence, and formulaic phrasing commonly generated by AI language models.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "302bed4b-b012-4971-a7d9-1249376281fc",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.74,
  "model_score": 0.9064,
  "style_score": 0.655,
  "label": "This writing closely matches the statistical predictability, uniform cadence, and formulaic phrasing commonly generated by AI language models.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "494da5ee-829c-48ae-98b5-9171fdac4b70",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.87,
  "model_score": 0.0287,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "8be537c3-a48b-49f6-8ef1-91c94139bb34",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.87,
  "model_score": 0.0287,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "5f68342f-2144-4255-9f49-533f7b80fe7e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.87,
  "model_score": 0.0287,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "bab6397d-0453-4211-9d37-695258a99a08",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.87,
  "model_score": 0.0287,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "3402b0de-31cb-4627-9685-9615c1c68c82",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.87,
  "model_score": 0.0287,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "06416106-d1ee-46fc-a3c1-10c28c07dd52",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.87,
  "model_score": 0.0287,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "73c42ac2-1057-4f0b-9894-89262940b902",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.87,
  "model_score": 0.0287,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "ab3284a1-7411-4993-a03f-2b6b8b32751e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.87,
  "model_score": 0.0287,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "e4921d90-8517-4755-8b20-6e8a6cdc23b7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.87,
  "model_score": 0.0287,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "88b1fccf-1dd0-47c3-b536-f89444901e98",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.87,
  "model_score": 0.0287,
  "style_score": 0.405,
  "label": "This writing displays the natural sentence rhythms, vocabulary variation, and expressive structure characteristic of an authentic human writer.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
