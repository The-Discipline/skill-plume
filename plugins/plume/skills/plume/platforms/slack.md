---
name: slack
kind: platform
version: 1
last_checked: never
families: [message, comment]
limits:
  max_chars: null
  truncation_chars: null
rendering:
  markdown: slack
conventions:
  hashtags: none
  mentions: "@person only when you need them to act or see it"
  links: allowed
  emojis: allowed, sparingly
community_rules:
  - In community workspaces, follow the channel's purpose and pinned rules.
register_default: casual
lint:
  max_hashtags: 0
---

# Slack

- Formatting syntax: `*bold*`, `_italic_`, `~strike~`, `` `code` ``, `>` for quotes, `-` or `•` for lists.
- Double asterisks do not render as bold when typed in Slack. Use single asterisks.
- Threads: a reply in a thread uses the `comment` or `message` family with intent `reply`.
