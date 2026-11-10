"""Compare an AI draft with the version the user actually published.

Usage (from the skill folder):
  python3 scripts/diff_learn.py draft.txt published.txt
  add --json for machine-readable output

Outputs the edit distance (0 = unchanged, 1 = fully rewritten, word level),
length changes, and the list of changes for the model to find recurring patterns.
"""
import argparse
import difflib
import json
import re

TOKEN = re.compile(r"\w+|[^\w\s]", re.UNICODE)


def tokens(text):
    return TOKEN.findall(text)


def compare(draft, final, max_changes=60):
    a, b = tokens(draft), tokens(final)
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    changes = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        changes.append({
            "op": op,
            "before": " ".join(a[i1:i2]),
            "after": " ".join(b[j1:j2]),
            "context": " ".join(a[max(0, i1 - 6):i1]),
        })
    removed = {}
    for c in changes:
        for t in c["before"].split():
            if not t.isalnum():
                removed[t] = removed.get(t, 0) + 1
    return {
        "edit_distance": round(1 - sm.ratio(), 3),
        "words_before": len([t for t in a if t.isalnum()]),
        "words_after": len([t for t in b if t.isalnum()]),
        "paragraphs_before": len([p for p in re.split(r"\n\s*\n", draft) if p.strip()]),
        "paragraphs_after": len([p for p in re.split(r"\n\s*\n", final) if p.strip()]),
        "punctuation_removed": removed,
        "change_count": len(changes),
        "changes": changes[:max_changes],
    }


def render(r):
    out = [
        f"Edit distance: {r['edit_distance']} (0 = published as drafted, 1 = fully rewritten)",
        f"Words: {r['words_before']} -> {r['words_after']}. Paragraphs: {r['paragraphs_before']} -> {r['paragraphs_after']}.",
        f"Changes: {r['change_count']}",
    ]
    if r["punctuation_removed"]:
        out.append("Punctuation removed: " + ", ".join(f"{k} x{v}" for k, v in r["punctuation_removed"].items()))
    for c in r["changes"]:
        out.append(f"- {c['op']}: \"{c['before']}\" -> \"{c['after']}\"   (after: ...{c['context']})")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft")
    ap.add_argument("published")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    with open(args.draft, encoding="utf-8") as f:
        draft = f.read()
    with open(args.published, encoding="utf-8") as f:
        final = f.read()
    r = compare(draft, final)
    print(json.dumps(r, ensure_ascii=False, indent=2) if args.json else render(r))


if __name__ == "__main__":
    main()
