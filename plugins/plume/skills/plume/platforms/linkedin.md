---
name: linkedin
kind: platform
version: 1
last_checked: never
families: [post, slides, comment, article, message, bio]
limits:
  max_chars: null
  truncation_chars: null
rendering:
  markdown: none
conventions:
  hashtags: few, at the end
  mentions: allowed, only when the person is actually involved
  links: at most one in the body
  emojis: avoid unless the pack allows them
community_rules: []
register_default: neutral
lint:
  max_hashtags: 3
---

# LinkedIn

- Posts render plain text only: no Markdown, no headings. Line breaks are kept.
- Lists are typed: the user's list marker from `glyphs.md`, numbering as plain `1.`.
- Unicode "bold" or "italic" letters are flagged as high: screen readers read them letter by letter, and search does not find those words. A pack can opt in for a few words (`fake_bold: allow`, see `glyphs.md`).
- The hook must work before the "see more" cut. Fill `truncation_chars` once verified; until then the lint shows the opening lines for review instead of checking a number.
- Carousels use the `slides` family. The caption uses the `post` family rules.
- Limits are left `null` on purpose. Verify them against LinkedIn's current help pages and set `last_checked`.
