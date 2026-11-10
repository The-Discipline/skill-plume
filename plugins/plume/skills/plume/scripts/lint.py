"""Deterministic checks on a piece of text, using the merged profile.

Usage (from the skill folder):
  python3 scripts/lint.py draft.txt --family post --platform linkedin --pack /path/to/plume-pack
  python3 scripts/lint.py draft.txt --profile merged.json
  add --json for machine-readable output

Checks: banned characters, phrases and patterns; length; paragraph and sentence
length; rhythm uniformity; lists of three; list items; links; hashtags; emojis;
Markdown on platforms that do not render it; character limit; visible hook.
"""
import argparse
import json
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import merge_profile  # noqa: E402

EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]")
URL = re.compile(r"https?://\S+|www\.\S+")
HASHTAG = re.compile(r"(?<![\w&])#[\wÀ-ſ]+")
LIST_ITEM = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+")
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\u00C0-\u00DD\"'\u00AB(\[*_])")
TRIPLET = re.compile(r"\b[\w'À-ſ-]+(?: [\w'À-ſ-]+)?, [\w'À-ſ-]+(?: [\w'À-ſ-]+)?,? (?:and|or|et|ou) [\w'À-ſ-]+", re.I)
MARKDOWN = [
    (re.compile(r"\*\*[^*]+\*\*|__[^_]+__"), "Markdown bold"),
    (re.compile(r"^\s{0,3}#{1,6}\s", re.M), "Markdown heading"),
    (re.compile(r"\[[^\]]+\]\([^)]+\)"), "Markdown link"),
]
FAKE_BOLD = re.compile("[\U0001D400-\U0001D7FF]")


def char_of(entry):
    if isinstance(entry, str) and re.fullmatch(r"U\+[0-9A-Fa-f]{4,6}", entry):
        return chr(int(entry[2:], 16))
    return entry


def words(text):
    return re.findall(r"[\w'À-ſ-]+", text)


def cv(values):
    if len(values) < 2 or statistics.mean(values) == 0:
        return None
    return statistics.pstdev(values) / statistics.mean(values)


def find(findings, severity, check, message, line=None, quote=None):
    findings.append({"severity": severity, "check": check, "line": line, "message": message, "quote": quote})


def lint(text, profile):
    fam = profile.get("family") or {}
    plat = profile.get("platform") or {}
    rules = profile.get("lint") or {}
    findings = []
    lines = text.splitlines()

    # Banned characters, phrases, patterns (line by line)
    chars = [char_of(c) for c in rules.get("banned_chars") or []]
    phrases = [p for p in rules.get("banned_phrases") or [] if p]
    patterns = {}
    for name, rx in (rules.get("patterns") or {}).items():
        try:
            patterns[name] = re.compile(rx)
        except re.error as e:
            find(findings, "low", "config", f"invalid pattern '{name}': {e}")
    for n, line in enumerate(lines, 1):
        for c in chars:
            if c and c in line:
                find(findings, "high", "banned_char", f"banned character U+{ord(c[0]):04X}", n, line.strip()[:120])
        low = line.lower()
        for p in phrases:
            if p.lower() in low:
                find(findings, "high", "banned_phrase", f"banned phrase '{p}'", n, line.strip()[:120])
        for name, rx in patterns.items():
            m = rx.search(line)
            if m:
                find(findings, "medium", "pattern", f"pattern '{name}'", n, m.group(0)[:120])
        if FAKE_BOLD.search(line):
            find(findings, "high", "fake_bold", "Unicode mathematical letters used as fake bold or italic", n, line.strip()[:120])

    # Slides are split on lines containing only ---
    is_slides = fam.get("name") == "slides"
    slides = [s.strip() for s in re.split(r"(?m)^\s*---\s*$", text)] if is_slides else []
    slides = [s for s in slides if s]

    # Length
    total_words = len(words(text))
    length = fam.get("length") or {}
    lo, hi = length.get("min_words"), length.get("max_words")
    if lo and total_words < lo:
        find(findings, "low", "length", f"{total_words} words, below the family's {lo}")
    if hi and total_words > hi:
        find(findings, "medium", "length", f"{total_words} words, above the family's {hi}")
    if is_slides:
        sl = fam.get("slides") or {}
        if sl.get("min") and len(slides) < sl["min"]:
            find(findings, "medium", "slides", f"{len(slides)} slides, below {sl['min']}")
        if sl.get("max") and len(slides) > sl["max"]:
            find(findings, "medium", "slides", f"{len(slides)} slides, above {sl['max']}")
        for i, s in enumerate(slides, 1):
            wc = len(words(s))
            if sl.get("max_words_per_slide") and wc > sl["max_words_per_slide"]:
                find(findings, "medium", "slides", f"slide {i}: {wc} words, above {sl['max_words_per_slide']}", quote=s[:80])

    # Paragraphs
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip() and not re.fullmatch(r"-{3,}", p.strip())]
    para_words = [len(words(p)) for p in paras]
    mpw = rules.get("max_paragraph_words")
    for p, wc in zip(paras, para_words):
        if mpw and wc > mpw:
            find(findings, "medium", "paragraph", f"paragraph of {wc} words, above {mpw}", quote=p[:80])
    if len(paras) >= 4:
        single = sum(1 for p in paras if "\n" not in p and len(SENTENCE_SPLIT.split(p)) == 1)
        ratio = single / len(paras)
        msr = rules.get("max_single_line_ratio")
        if msr is not None and ratio > msr:
            find(findings, "medium", "rhythm", f"{ratio:.0%} of paragraphs are a single sentence (max {msr:.0%}): mechanical one-liners")
        pcv = cv(para_words)
        if pcv is not None and rules.get("min_paragraph_cv") and pcv < rules["min_paragraph_cv"]:
            find(findings, "medium", "rhythm", f"paragraph lengths are very uniform (variation {pcv:.2f})")

    # Sentences
    prose = "\n".join(l for l in lines if not LIST_ITEM.match(l))
    sentences = [s for s in SENTENCE_SPLIT.split(re.sub(r"\s*\n\s*", " ", prose)) if words(s)]
    sw = [len(words(s)) for s in sentences]
    msw = rules.get("max_sentence_words")
    for s, wc in zip(sentences, sw):
        if msw and wc > msw:
            find(findings, "low", "sentence", f"sentence of {wc} words, above {msw}", quote=s[:100])
    if len(sentences) >= 6:
        scv = cv(sw)
        if scv is not None and rules.get("min_sentence_cv") and scv < rules["min_sentence_cv"]:
            find(findings, "medium", "rhythm", f"sentence lengths are very uniform (variation {scv:.2f}): read it aloud")

    # Lists of three
    triplets = TRIPLET.findall(text)
    mt = rules.get("max_triplets")
    if mt is not None and len(triplets) > mt:
        find(findings, "medium", "triplets", f"{len(triplets)} lists of three (max {mt}): check they carry content, not rhythm", quote=" | ".join(triplets[:4]))

    # Lists
    items = [l for l in lines if LIST_ITEM.match(l)]
    policy = fam.get("lists")
    if policy == "avoid" and items:
        find(findings, "medium", "lists", f"{len(items)} list items in a family that avoids lists")
    mli = rules.get("max_list_items")
    if mli is not None and policy != "avoid" and len(items) > mli:
        find(findings, "low", "lists", f"{len(items)} list items, above {mli}")

    # Links, hashtags, emojis
    links = URL.findall(text)
    if rules.get("max_links") is not None and len(links) > rules["max_links"]:
        find(findings, "medium", "links", f"{len(links)} links, above {rules['max_links']}")
    tags = HASHTAG.findall(text)
    if rules.get("max_hashtags") is not None and len(tags) > rules["max_hashtags"]:
        find(findings, "low", "hashtags", f"{len(tags)} hashtags, above {rules['max_hashtags']}", quote=" ".join(tags[:6]))
    if rules.get("emojis") is False and EMOJI.search(text):
        find(findings, "medium", "emojis", "emojis present, not allowed for this format")

    # Rendering
    rendering = (plat.get("rendering") or {}).get("markdown")
    if rendering == "none":
        for rx, label in MARKDOWN:
            if rx.search(text):
                find(findings, "high", "rendering", f"{label} on a platform that renders plain text")
    if rendering in ("slack", "whatsapp") and re.search(r"\*\*[^*]+\*\*", text):
        find(findings, "medium", "rendering", "double asterisks: this platform uses *single* asterisks for bold")

    # Character limit and hook
    limits = plat.get("limits") or {}
    if limits.get("max_chars") and len(text) > limits["max_chars"]:
        find(findings, "high", "limit", f"{len(text)} characters, above the platform's {limits['max_chars']}")
    hook = None
    trunc = limits.get("truncation_chars")
    if (fam.get("hook_default") or "none") != "none":
        visible = text[:trunc] if trunc else "\n".join(lines[:3])
        hook = {"visible": visible, "truncation_chars": trunc}
        if trunc:
            first = SENTENCE_SPLIT.split(text.strip())[0] if text.strip() else ""
            if len(first) > trunc:
                find(findings, "medium", "hook", f"first sentence is {len(first)} characters, cut at {trunc}")

    order = {"high": 0, "medium": 1, "low": 2}
    findings.sort(key=lambda f: (order[f["severity"]], f["line"] or 0))
    stats = {
        "words": total_words,
        "characters": len(text),
        "paragraphs": len(paras),
        "sentences": len(sentences),
        "slides": len(slides) if is_slides else None,
        "sentence_variation": round(cv(sw), 2) if cv(sw) is not None else None,
    }
    return {"stats": stats, "findings": findings, "hook": hook, "warnings": profile.get("warnings", [])}


def render(report):
    out = []
    s = report["stats"]
    out.append(f"Stats: {s['words']} words, {s['characters']} characters, {s['paragraphs']} paragraphs, {s['sentences']} sentences" + (f", {s['slides']} slides" if s["slides"] else ""))
    for w in report["warnings"]:
        out.append(f"Profile warning: {w}")
    if not report["findings"]:
        out.append("No findings.")
    for f in report["findings"]:
        where = f"line {f['line']}: " if f["line"] else ""
        quote = f"  >> {f['quote']}" if f["quote"] else ""
        out.append(f"[{f['severity']}] {f['check']}: {where}{f['message']}{quote}")
    if report["hook"]:
        h = report["hook"]
        label = f"first {h['truncation_chars']} characters" if h["truncation_chars"] else "opening lines (truncation not verified for this platform)"
        out.append(f"Visible hook, {label}:\n{h['visible']}")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--profile", help="merged profile JSON from merge_profile.py")
    ap.add_argument("--family")
    ap.add_argument("--platform")
    ap.add_argument("--pack")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if args.profile:
        with open(args.profile, encoding="utf-8") as f:
            profile = json.load(f)
    elif args.family:
        profile = merge_profile.merge(args.family, args.platform, args.pack)
    else:
        raise SystemExit("give --profile or --family")
    with open(args.file, encoding="utf-8") as f:
        text = f.read()
    report = lint(text, profile)
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else render(report))


if __name__ == "__main__":
    main()
