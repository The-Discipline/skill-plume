"""Review a skill repository. Lists findings, changes nothing.

Usage: python3 skill_review.py <repo>

Checks:
  frontmatter    every SKILL.md has name and description; description length; name matches folder
  size           SKILL.md and model-facing files over the recommended size
  refs           paths mentioned in Markdown (`roles/x.md`, `scripts/y.py`...) that don't exist
  versions       plugin.json, marketplace.json, CHANGELOG and README status agree
  repeats        the same sentence in two model-facing files (an instruction should live once)
  chars          em dashes and other banned characters
  leftovers      template placeholders, TODO, TBD in shipped files
  tracked        files that should not be in git (__pycache__, .DS_Store, dist/)
  stale          words given on the command line (--stale) still present
"""
import argparse, json, os, re, subprocess, sys
from collections import defaultdict

MODEL_DIRS = ("skills",)          # files under a skills/ folder are read by the model
MAX_SKILL_LINES = 500             # Anthropic's guidance for SKILL.md bodies
MAX_DESC = 1024                   # Agent Skills limit for description
BANNED = {"—": "em dash"}
PATH_RE = re.compile(r"`((?:[\w.-]+/)*[\w.-]+\.(?:md|py|sh|json|yaml|yml|txt))`")
SENT_RE = re.compile(r"(?<=[.!?])\s+")


def find(f, sev, check, msg, path=None, line=None):
    f.append((sev, check, msg, path, line))


def tracked(repo):
    out = subprocess.run(["git", "-C", repo, "ls-files"], capture_output=True, text=True).stdout
    return [l for l in out.splitlines() if l]


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, text[m.end():]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--stale", nargs="*", default=[])
    ap.add_argument("--ignore", nargs="*", default=[], help="file names that live outside the repo (user files)")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    files = tracked(repo)
    f = []

    # tracked junk
    for p in files:
        if "__pycache__" in p or p.endswith(".DS_Store") or p.startswith("dist/"):
            find(f, "medium", "tracked", "should not be in git", p)

    md = [p for p in files if p.endswith(".md")]
    texts = {p: open(os.path.join(repo, p), encoding="utf-8").read() for p in md}

    # frontmatter and size
    for p, t in texts.items():
        if os.path.basename(p) == "SKILL.md":
            fm, body = frontmatter(t)
            for k in ("name", "description"):
                if not fm.get(k):
                    find(f, "high", "frontmatter", f"missing {k}", p)
            if fm.get("name") and fm["name"] != os.path.basename(os.path.dirname(p)):
                find(f, "medium", "frontmatter", f"name '{fm['name']}' differs from folder '{os.path.basename(os.path.dirname(p))}'", p)
            d = fm.get("description", "")
            if len(d) > MAX_DESC:
                find(f, "high", "frontmatter", f"description is {len(d)} characters (max {MAX_DESC})", p)
            n = body.count("\n")
            if n > MAX_SKILL_LINES:
                find(f, "medium", "size", f"SKILL.md body is {n} lines (guidance: under {MAX_SKILL_LINES})", p)
            words = len(body.split())
            find(f, "info", "size", f"SKILL.md body: {n} lines, {words} words", p)

    # refs: backticked paths that resolve nowhere in the repo
    names = set(files) | {os.path.basename(x) for x in files}
    suffixes = defaultdict(set)
    for x in files:
        parts = x.split("/")
        for i in range(len(parts)):
            suffixes["/".join(parts[i:])].add(x)
    for p, t in texts.items():
        for n, line in enumerate(t.splitlines(), 1):
            for ref in PATH_RE.findall(line):
                r = ref[2:] if ref.startswith("./") else ref
                if r in suffixes or r in names or os.path.basename(r) in a.ignore:
                    continue
                if any(tok in r for tok in ("{", "<", "*")) or r.startswith(("~", "/")):
                    continue
                find(f, "medium", "refs", f"`{ref}` not found in the repo", p, n)

    # versions
    vers = {}
    for p in files:
        if p.endswith("plugin.json") or p.endswith("marketplace.json"):
            try:
                j = json.load(open(os.path.join(repo, p)))
            except Exception as e:
                find(f, "high", "versions", f"invalid JSON: {e}", p); continue
            if "version" in j:
                vers[p] = j["version"]
            for pl in j.get("plugins", []) or []:
                if "version" in pl:
                    vers[p + " (plugins[])"] = pl["version"]
    ch = texts.get("CHANGELOG.md", "")
    m = re.search(r"^##\s*\[?v?(\d+\.\d+\.\d+)", ch, re.M)
    if m:
        vers["CHANGELOG.md (top)"] = m.group(1)
    rd = texts.get("README.md", "")
    m = re.search(r"\*\*v(\d+\.\d+\.\d+)", rd)
    if m:
        vers["README.md (status)"] = m.group(1)
    if len(set(vers.values())) > 1:
        find(f, "high", "versions", "versions disagree: " + ", ".join(f"{k}={v}" for k, v in vers.items()))
    else:
        find(f, "info", "versions", "versions: " + (", ".join(f"{k}={v}" for k, v in vers.items()) or "none found"))

    # repeats across model-facing files
    seen = defaultdict(list)
    for p, t in texts.items():
        if not any(f"/{d}/" in f"/{p}" for d in MODEL_DIRS):
            continue
        _, body = frontmatter(t)
        body = re.sub(r"```.*?```", " ", body, flags=re.S)
        for s in SENT_RE.split(re.sub(r"\s+", " ", body)):
            k = re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()
            if len(k.split()) >= 8:
                seen[k].append(p)
    for k, ps in seen.items():
        if len(set(ps)) > 1:
            find(f, "low", "repeats", f"same sentence in {len(set(ps))} files: \"{k[:90]}\"", ", ".join(sorted(set(ps))))

    # chars, leftovers, stale words
    for p in files:
        if not p.endswith((".md", ".py", ".sh", ".json", ".yaml", ".yml", ".html", ".css", ".js")):
            continue
        try:
            t = open(os.path.join(repo, p), encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        if "check-style" in p:
            continue
        shipped = "/templates/" not in p and "check-style" not in p and "stock-words" not in p
        for n, line in enumerate(t.splitlines(), 1):
            for ch_, label in BANNED.items():
                if ch_ in line:
                    find(f, "high", "chars", label, p, n)
            if shipped and p.endswith(".md") and re.search(r"\b(TODO|TBD|FIXME|XXX)\b", line):
                find(f, "low", "leftovers", line.strip()[:100], p, n)
            for w in a.stale:
                if re.search(re.escape(w), line, re.I):
                    find(f, "medium", "stale", f"'{w}': {line.strip()[:100]}", p, n)

    order = {"high": 0, "medium": 1, "low": 2, "info": 3}
    f.sort(key=lambda x: (order[x[0]], x[1], x[3] or ""))
    for sev, check, msg, path, line in f:
        loc = f"{path}:{line}" if line else (path or "")
        print(f"[{sev}] {check}: {msg}" + (f"  ({loc})" if loc else ""))
    counts = defaultdict(int)
    for x in f:
        counts[x[0]] += 1
    print(f"\n{counts['high']} high, {counts['medium']} medium, {counts['low']} low")


if __name__ == "__main__":
    main()
