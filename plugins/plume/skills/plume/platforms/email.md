---
name: email
kind: platform
version: 1
last_checked: never
families: [email]
limits:
  max_chars: null
  truncation_chars: null
rendering:
  markdown: none
conventions:
  hashtags: none
  mentions: none
  links: few, written in full or as clear text
  emojis: avoid
community_rules: []
register_default: neutral
lint:
  max_hashtags: 0
---

# Email client

- Plain text by default: no Markdown symbols. If the user writes in an HTML editor, formatting is applied there.
- The preview line in most inboxes shows the start of the first sentence, so it carries the reason to open.
