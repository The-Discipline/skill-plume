---
version: 1
library:
  bullet:
    char: "U+2022"
    reads_as: "bullet"
  small_triangle:
    char: "U+25B8"
    reads_as: "black right-pointing small triangle"
  small_square:
    char: "U+25AA"
    reads_as: "black small square"
  white_bullet:
    char: "U+25E6"
    reads_as: "white bullet"
  middle_dot:
    char: "U+00B7"
    reads_as: "middle dot"
  arrow:
    char: "U+2192"
    reads_as: "rightwards arrow"
  heavy_arrow:
    char: "U+279C"
    reads_as: "heavy round-tipped rightwards arrow"
  check:
    char: "U+2713"
    reads_as: "check mark"
  cross:
    char: "U+2717"
    reads_as: "ballot x"
defaults:
  list_marker: "U+2022"
  numbered: "1."
  arrow: "U+2192"
  allowed: []
  fake_bold: flag
  fake_bold_max_words: 3
native_lists: [standard, slack, teams]
---

# Glyphs

Typed symbols for platforms that render plain text (LinkedIn, email, WhatsApp). On platforms that render real lists (blog, Reddit, Slack, Teams), Plume writes real lists and converts typed markers back.

## The library

Each glyph is listed with what most screen readers announce, usually its Unicode name. A marker is read aloud at every line, so a plain one is kinder than a decorative one.

- `bullet` (•): "bullet". The default list marker.
- `small_triangle` (▸), `small_square` (▪), `white_bullet` (◦): alternative markers, read by their long names.
- `middle_dot` (·): a separator inside a line ("Paris · remote").
- `arrow` (→), `heavy_arrow` (➜): "rightwards arrow". For a consequence or a next step, not as a list marker on every line.
- `check` (✓), `cross` (✗): "check mark", "ballot x". For do/don't lists.

Numbered lists stay plain: `1.` or `1)`. They show as typed text on LinkedIn and read as numbers.

## Your choice (`formats.md` in your pack)

```
glyphs:
  list_marker: "•"
  numbered: "1."
  arrow: "→"
  allowed: ["✓", "✗"]
  fake_bold: flag
```

- `list_marker`, `numbered`, `arrow`: what the writer uses. Literal characters or code points (`U+2022`).
- `allowed`: other glyphs you use. Any library glyph or decorative symbol outside your choice is flagged.
- Per platform: `platforms: linkedin: glyphs: ...` overrides the global choice for one platform.

## Checks (lint)

- One list marker style per piece.
- On plain-text platforms, list lines use your `list_marker` (or `numbered`).
- On platforms with real lists, typed markers are flagged: use `- `.
- Decorative glyphs outside your choice are flagged.
- Library glyphs don't count as emojis.

## Fake bold and italic

Unicode "mathematical" letters that imitate bold or italic. Flagged as high by default: screen readers read them letter by letter or skip them, platform search doesn't find those words, and they break on some devices.

Opt-in, in your pack only: `fake_bold: allow`. The lint then flags each use as low, and as medium above `fake_bold_max_words` (default 3) or when it styles a whole line. Keep it for a word or two of emphasis, never for a word people would search for.
