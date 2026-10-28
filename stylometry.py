"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies.

    Returns:
        Coefficient of variation (stdev / mean) of sentence word counts.
        Scale: float >= 0.0. Higher spread means higher burstiness (more human).
        Uniform lengths (low spread) indicate machine-like rhythm.
    """
    s = sentences(text)
    lens = [len(words(sent)) for sent in s if len(words(sent)) > 0]
    if len(lens) < 2:
        return 0.0
    mean_val = statistics.mean(lens)
    if mean_val == 0:
        return 0.0
    return round(statistics.stdev(lens) / mean_val, 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.

    Returns:
        A float between 0.0 and 1.0. Higher means more varied vocabulary.
    """
    w = words(text)
    if not w:
        return 0.0
    return round(len(set(w)) / len(w), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to word count.

    Returns:
        Punctuation occurrences per word token.
    """
    w = words(text)
    if not w:
        return 0.0
    punc_count = len(re.findall(r"[,;:—\-?!]", text))
    return round(punc_count / len(w), 4)


# ── Stretch feature: Third signal ───────────────────────────────────────────

def repetition_signal(text: str) -> float:
    """
    Signal three (Stretch): measures n-gram repetition and formulaic transitions.
    Higher means more likely AI.
    """
    w = words(text)
    if len(w) < 6:
        return 0.50
    bigrams = [f"{w[i]} {w[i+1]}" for i in range(len(w) - 1)]
    rep_rate = (len(bigrams) - len(set(bigrams))) / len(bigrams) if bigrams else 0.0
    
    ai_markers = [
        "in conclusion", "it is important", "firstly", "furthermore",
        "moreover", "delve", "testament", "careful consideration",
        "crucial to note", "on the other hand", "in summary"
    ]
    t_lower = text.lower()
    marker_hits = sum(1 for m in ai_markers if m in t_lower)
    
    score = 0.55 * min(rep_rate / 0.20, 1.0) + 0.45 * min(marker_hits / 2.0, 1.0)
    return round(min(max(score, 0.0), 1.0), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Combines sentence length spread, type-token ratio, and punctuation features.
    """
    s = sentences(text)
    cv = sentence_length_spread(text)
    ttr = type_token_ratio(text)
    
    # 1. Spread: low spread (< 0.25) -> uniform -> AI; high spread (> 0.55) -> Human
    if len(s) < 2:
        spread_ai = 0.50
    else:
        spread_ai = max(0.0, min(1.0, 1.0 - (cv / 0.60)))

    # 2. Vocabulary variety: lower TTR -> more formulaic -> AI
    ttr_ai = max(0.0, min(1.0, 1.0 - (ttr - 0.50) / 0.40))
    
    # 3. Punctuation profile: AI uses plain commas with no expressive marks (; — ? !)
    expressive_count = len(re.findall(r"[;—\-?!]", text))
    punc_ai = 0.65 if expressive_count == 0 else max(0.15, 0.65 - expressive_count * 0.15)
    
    score = 0.55 * spread_ai + 0.25 * ttr_ai + 0.20 * punc_ai
    return round(min(max(score, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"repetition_signal        {repetition_signal(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
