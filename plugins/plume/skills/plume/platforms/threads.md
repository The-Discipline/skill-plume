---
name: threads
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
  links: allowed, at most one
  emojis: avoid unless the pack allows them
community_rules: []
register_default: casual
lint:
  max_hashtags: 1
---

# Threads

Threads is Meta's text platform. For a chain of linked posts on X, use `x`. The family called `thread` applies to both.

- Posts render plain text only: no Markdown. Line breaks are kept.
- Limits and tag rules are left unverified. Check Threads' current help pages and set `last_checked`.
- A chain of posts uses the `thread` family: one idea per post, the first post works alone.
