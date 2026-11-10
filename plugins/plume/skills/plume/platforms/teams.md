---
name: teams
kind: platform
version: 1
last_checked: never
families: [message, comment]
limits:
  max_chars: null
  truncation_chars: null
rendering:
  markdown: teams
conventions:
  hashtags: none
  mentions: "@person only when needed"
  links: allowed
  emojis: allowed, sparingly
community_rules: []
register_default: neutral
lint:
  max_hashtags: 0
---

# Microsoft Teams

- Teams accepts Markdown-style formatting in messages (`**bold**`, `*italic*`, lists), with some differences by client. Keep formatting minimal.
- Corporate context: default register is more neutral than Slack.
