---
name: instagram
kind: platform
version: 1
last_checked: never
families: [post, slides, comment]
limits:
  max_chars: null
  truncation_chars: null
rendering:
  markdown: none
conventions:
  hashtags: few, at the end
  mentions: allowed, only when the person is actually involved
  links: not clickable in captions: point to the link in bio or to a comment
  emojis: allowed if the pack allows them
community_rules: []
register_default: casual
lint:
  max_links: 0
---

# Instagram

- Captions render plain text only: no Markdown, no headings. Line breaks are kept.
- The first line has to work before the caption is cut. Fill `truncation_chars` once verified; until then the lint shows the opening lines for review.
- The image or video carries the post. The caption adds what the visual can't say, and doesn't repeat it.
- Carousels use the `slides` family. The caption uses the `post` family rules, shorter.
- Plume writes the text. It does not make the images. Alt text, if the user wants it, is a plain sentence describing the image.
- Limits and hashtag habits change often. Verify them against Instagram's current help pages and set `last_checked`.
