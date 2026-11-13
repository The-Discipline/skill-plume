---
name: blog
kind: platform
version: 1
last_checked: never
families: [article, page, bio]
limits:
  max_chars: null
  truncation_chars: null
rendering:
  markdown: standard
conventions:
  hashtags: none
  mentions: none
  links: internal links to the user's own pages from facts.md
  emojis: avoid
community_rules: []
register_default: neutral
lint:
  max_hashtags: 0
---

# Blog or website

- Markdown or HTML, depending on the user's site. Default to Markdown.
- Internal links only to URLs listed in `facts.md`.
