"""Check that a user pack is complete and well-formed.

Usage (from the skill folder):
  python3 scripts/validate_pack.py /path/to/plume-pack
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plume_yaml  # noqa: E402
import merge_profile  # noqa: E402

REQUIRED = ["voice.md", "anti-patterns.md", "audiences.md", "facts.md"]
OPTIONAL = ["lexicon.md", "formats.md", "examples/index.md", "learn-log.md"]
PLACEHOLDER = re.compile(r"\{[^}]+\}|TODO|TO FILL", re.I)
INDEX_LINE = re.compile(r"^-\s*([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|\s*(\S+)\s*$")


def check(pack):
    problems, notes = [], []
    if not os.path.isdir(pack):
        return [f"not a folder: {pack}"], []
    for name in REQUIRED + OPTIONAL:
        path = os.path.join(pack, name)
        required = name in REQUIRED
        if not os.path.exists(path):
            (problems if required else notes).append(f"missing {'required' if required else 'optional'} file {name}")
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        _, body = plume_yaml.frontmatter(text)
        if len(body.strip()) < 40 and name not in ("learn-log.md",):
            (problems if required else notes).append(f"{name} is nearly empty")
        left = len(PLACEHOLDER.findall(body))
        if left:
            notes.append(f"{name}: {left} template placeholders still to fill")

    schema = merge_profile.load_schema()
    fam_fields = set(schema.get("family_fields") or [])
    plat_fields = set(schema.get("platform_fields") or [])
    forbidden = set(schema.get("forbidden") or [])
    fpath = os.path.join(pack, "formats.md")
    if os.path.exists(fpath):
        try:
            data, _ = plume_yaml.read(fpath)
        except ValueError as e:
            problems.append(f"formats.md frontmatter does not parse: {e}")
            data = {}
        for kind, fields in (("families", fam_fields), ("platforms", plat_fields)):
            for name, over in (data.get(kind) or {}).items():
                for key in (over or {}):
                    base = key.rstrip("+")
                    if base in forbidden:
                        problems.append(f"formats.md {kind}.{name}.{base}: forbidden field (voice lives in voice.md)")
                    elif base not in fields:
                        notes.append(f"formats.md {kind}.{name}.{base}: unknown field, will be ignored by the lint")

    custom_dir = os.path.join(pack, "formats")
    if os.path.isdir(custom_dir):
        for fn in sorted(os.listdir(custom_dir)):
            if fn.endswith(".md"):
                data, _ = plume_yaml.read(os.path.join(custom_dir, fn))
                if data.get("kind") not in ("family", "platform"):
                    problems.append(f"formats/{fn}: kind must be family or platform")
                for bad in forbidden & set(data):
                    problems.append(f"formats/{fn}: forbidden field '{bad}'")

    ipath = os.path.join(pack, "examples", "index.md")
    if os.path.exists(ipath):
        count = 0
        with open(ipath, encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                if not line.startswith("- "):
                    continue
                m = INDEX_LINE.match(line.strip())
                if not m:
                    problems.append(f"examples/index.md line {n}: expected '- family | platform | language | date | topic | path'")
                    continue
                count += 1
                path = os.path.join(pack, m.group(6))
                if not os.path.exists(path):
                    problems.append(f"examples/index.md line {n}: file not found {m.group(6)}")
        if count < 5:
            notes.append(f"only {count} indexed examples: voice matching works better with 5 or more per family you use")
    return problems, notes


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pack")
    args = ap.parse_args()
    problems, notes = check(args.pack)
    for p in problems:
        print(f"PROBLEM: {p}")
    for n in notes:
        print(f"note: {n}")
    print("Pack OK." if not problems else f"{len(problems)} problem(s).")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
