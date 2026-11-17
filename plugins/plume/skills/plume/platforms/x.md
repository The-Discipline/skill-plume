---
name: x
kind: platform
version: 1
last_checked: never
families: [post, thread, comment]
limits:
  max_chars: null
  truncation_chars: null
rendering:
  markdown: none
conventions:
  hashtags: none or one
  mentions: allowed, only when the person is actually involved
  links: at most one, preferably in the last part of a thread
  emojis: avoid unless the pack allows them
community_rules: []
register_default: casual
lint:
  max_hashtags: 1
---

# X

- Posts render plain text only: no Markdown. Line breaks are kept.
- A single post has a length limit that depends on the account. It is left `null` until someone verifies it for the user's account and sets `last_checked`.
- Long ideas use the `thread` family: one idea per post, the first post works alone.
- Quote posts and replies use the `comment` family.
