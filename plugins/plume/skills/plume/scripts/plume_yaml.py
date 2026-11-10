"""Tiny YAML-subset parser and frontmatter reader. Plain Python, no dependencies.

Supported: key: value, nested maps by indentation, block lists (- item),
inline lists ([a, b]), quoted strings, ints, floats, true/false, null.
Full-line comments only.
"""
import re

_KEY = re.compile(r"^([A-Za-z0-9_\-]+\+?):(?:\s+(.*))?$")


def _split_commas(s):
    out, cur, quote = [], "", None
    for ch in s:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            cur += ch
        elif ch == ",":
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return out


def scalar(s):
    s = s.strip()
    if s in ("", "~", "null", "None"):
        return None
    if s in ("true", "True"):
        return True
    if s in ("false", "False"):
        return False
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        return [scalar(x) for x in _split_commas(inner)] if inner else []
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        return s


def _is_item(text):
    return text == "-" or text.startswith("- ")


def _block(lines, i, indent):
    if i >= len(lines):
        return None, i
    if _is_item(lines[i][1]):
        out = []
        while i < len(lines) and lines[i][0] == indent and _is_item(lines[i][1]):
            out.append(scalar(lines[i][1][2:]))
            i += 1
        return out, i
    out = {}
    while i < len(lines) and lines[i][0] == indent:
        text = lines[i][1]
        m = _KEY.match(text)
        if not m:
            raise ValueError(f"cannot parse line: {text!r}")
        key, rest = m.group(1), m.group(2)
        i += 1
        if rest is None or rest.strip() == "":
            if i < len(lines) and lines[i][0] > indent:
                val, i = _block(lines, i, lines[i][0])
            elif i < len(lines) and lines[i][0] == indent and _is_item(lines[i][1]):
                val, i = _block(lines, i, indent)
            else:
                val = None
        else:
            val = scalar(rest)
        out[key] = val
    return out, i


def loads(text):
    lines = []
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        lines.append((indent, raw.strip()))
    if not lines:
        return {}
    val, _ = _block(lines, 0, lines[0][0])
    return val or {}


def frontmatter(text):
    """Return (data, body). Data is {} when there is no frontmatter."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    data = loads(text[3:end])
    body = text[end + 4:].lstrip("\n")
    return data, body


def read(path):
    with open(path, encoding="utf-8") as f:
        return frontmatter(f.read())
