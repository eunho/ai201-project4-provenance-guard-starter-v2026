# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 16:15
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `56445fe6-1391-4e92-a8bf-51cc1d1d25c5` | human | 0.780 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f8e89acc-fc75-430e-be90-d6179a1c899c` | human | 0.750 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `cb7a95d5-6baa-4830-b897-6bcd3c5365ea` | unsure | 0.590 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `34746685-cca6-4f72-9a82-80a2a9655d0c` | unsure | 0.500 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c2340e3a-72b6-4285-a70e-e76ac40cc6e4` | human | 0.840 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `4ae3cba8-abb9-45ed-a6df-10173176d09b` | unsure | 0.600 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `842eef09-c2a0-42ee-abc6-19e80efc1339` | unsure | 0.450 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `f2e94fa8-2d99-4140-aaf2-bbecccd28359` | human | 0.780 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `fd9c6d8e-2da9-4f06-a8a7-ce49c976c648` | unsure | 0.560 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `9acadc44-2d45-4257-a1dd-7a19cedd1d8b` | ai | 0.790 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `83b32923-20d0-4f8f-b7b9-c92c42adf898` | unsure | 0.540 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `4411a180-b540-4c73-9a4c-c0305db46b66` | unsure | 0.490 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `72499c76-f2f8-49da-bbf9-63f5f67d382f` | unsure | 0.470 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `2a6823e3-0cb2-4a56-b20e-a636c74f605b` | unsure | 0.540 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `650dbc6b-bfb7-48a4-93d4-ae4a595243ea` | unsure | 0.640 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `cc4ac107-810e-4734-b9b0-28f256a32af5` | unsure | 0.450 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `73645bab-1cac-4357-83f5-3e5de393bd65` | unsure | 0.630 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `86cc20cd-4ea0-405b-b828-66da6664fbcc` | human | 0.790 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `9c4a7b1e-7513-4a0b-9328-ee1e592a6188` | human | 0.770 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `e69294df-f941-4f56-ab2b-e35a756e8615` | human | 0.880 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `5c5dea50-8200-49ee-b89e-f98b5f3ecf3a` | unsure | 0.570 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `bd86b1c2-16de-4037-a084-12dae0a55dc9` | human | 0.710 | BROKE |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f02cc96d-250b-422d-93f5-b6d3bd1d5187` | unsure | 0.610 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `114c4231-4c79-41e3-b439-e134fbbdf90c` | unsure | 0.580 | BROKE |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `00349886-8f27-416b-a29e-17909affbf3d` | human | 0.790 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `04bfa301-7ed1-4d66-b268-b8a4cf1ef3f3` | unsure | 0.570 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `5693c249-1b93-49ee-99ff-c281f6b661aa` | ai | 0.730 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `fd641817-de19-4f96-a6bc-99dc5381e709` | ai | 0.810 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `2430d9ac-4cec-4382-b27d-1fed8ec3ef44` | ai | 0.770 | BROKE |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f7a97bb1-690f-4cd2-a8d9-35d41779b5ed` | human | 0.870 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `65902a2f-1c45-491f-9679-747d73638be6` | human | 0.870 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `52e54233-e723-4e05-84fc-e90f6b6bfee0` | human | 0.870 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9f54df81-4094-4886-b62b-6b1f7948e117` | human | 0.870 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a30cc259-ea05-432b-8f34-b58c40ffedb6` | human | 0.870 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1de9b9db-483b-4f90-86ac-cfb8ef04148a` | human | 0.870 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f2771866-79c9-4e94-a079-0091f5036295` | human | 0.870 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9cc808f0-3e1b-4190-95c0-77e6ae67b48b` | human | 0.870 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c444921f-5e5d-40b2-8d9b-e49cb44f9a4f` | human | 0.870 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8271293c-28e3-45f4-ba6a-a8cf329f8651` | human | 0.870 | HELD |
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
  "content_id": "56445fe6-1391-4e92-a8bf-51cc1d1d25c5",
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
  "content_id": "f8e89acc-fc75-430e-be90-d6179a1c899c",
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
  "content_id": "cb7a95d5-6baa-4830-b897-6bcd3c5365ea",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.59,
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
  "content_id": "34746685-cca6-4f72-9a82-80a2a9655d0c",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5,
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
  "content_id": "c2340e3a-72b6-4285-a70e-e76ac40cc6e4",
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
  "content_id": "4ae3cba8-abb9-45ed-a6df-10173176d09b",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.6,
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
  "content_id": "842eef09-c2a0-42ee-abc6-19e80efc1339",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.45,
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
  "content_id": "f2e94fa8-2d99-4140-aaf2-bbecccd28359",
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
  "content_id": "fd9c6d8e-2da9-4f06-a8a7-ce49c976c648",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.56,
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
  "content_id": "9acadc44-2d45-4257-a1dd-7a19cedd1d8b",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.79,
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
  "content_id": "83b32923-20d0-4f8f-b7b9-c92c42adf898",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.54,
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
  "content_id": "4411a180-b540-4c73-9a4c-c0305db46b66",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.49,
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
  "content_id": "72499c76-f2f8-49da-bbf9-63f5f67d382f",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.47,
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
  "content_id": "2a6823e3-0cb2-4a56-b20e-a636c74f605b",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.54,
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
  "content_id": "650dbc6b-bfb7-48a4-93d4-ae4a595243ea",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.64,
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
  "content_id": "cc4ac107-810e-4734-b9b0-28f256a32af5",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.45,
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
  "content_id": "73645bab-1cac-4357-83f5-3e5de393bd65",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.63,
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
  "content_id": "86cc20cd-4ea0-405b-b828-66da6664fbcc",
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
  "content_id": "9c4a7b1e-7513-4a0b-9328-ee1e592a6188",
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
  "content_id": "e69294df-f941-4f56-ab2b-e35a756e8615",
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
  "content_id": "5c5dea50-8200-49ee-b89e-f98b5f3ecf3a",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.57,
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
  "content_id": "bd86b1c2-16de-4037-a084-12dae0a55dc9",
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
  "content_id": "f02cc96d-250b-422d-93f5-b6d3bd1d5187",
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
  "content_id": "114c4231-4c79-41e3-b439-e134fbbdf90c",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.58,
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
  "content_id": "00349886-8f27-416b-a29e-17909affbf3d",
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
  "content_id": "04bfa301-7ed1-4d66-b268-b8a4cf1ef3f3",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.57,
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
  "content_id": "5693c249-1b93-49ee-99ff-c281f6b661aa",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.73,
  "model_score": 0.9976,
  "style_score": 0.405,
  "label": "This writing closely matches the statistical predictability, uniform cadence, and formulaic phrasing commonly generated by AI language models.",
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
  "content_id": "fd641817-de19-4f96-a6bc-99dc5381e709",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.81,
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
  "content_id": "2430d9ac-4cec-4382-b27d-1fed8ec3ef44",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.77,
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
  "content_id": "f7a97bb1-690f-4cd2-a8d9-35d41779b5ed",
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
  "content_id": "65902a2f-1c45-491f-9679-747d73638be6",
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
  "content_id": "52e54233-e723-4e05-84fc-e90f6b6bfee0",
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
  "content_id": "9f54df81-4094-4886-b62b-6b1f7948e117",
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
  "content_id": "a30cc259-ea05-432b-8f34-b58c40ffedb6",
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
  "content_id": "1de9b9db-483b-4f90-86ac-cfb8ef04148a",
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
  "content_id": "f2771866-79c9-4e94-a079-0091f5036295",
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
  "content_id": "9cc808f0-3e1b-4190-95c0-77e6ae67b48b",
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
  "content_id": "c444921f-5e5d-40b2-8d9b-e49cb44f9a4f",
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
  "content_id": "8271293c-28e3-45f4-ba6a-a8cf329f8651",
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
