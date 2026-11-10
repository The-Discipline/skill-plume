---
name: reddit
kind: platform
version: 1
last_checked: never
families: [post, comment]
limits:
  max_chars: null
  truncation_chars: null
rendering:
  markdown: standard
conventions:
  hashtags: none
  mentions: rare
  links: only when useful and allowed by the subreddit
  emojis: avoid
community_rules:
  - Read the subreddit rules before posting. Many forbid self-promotion outside specific threads.
  - Lead with usefulness. Readers are suspicious of anything that looks like marketing.
  - Disclose affiliation when mentioning your own product or service.
register_default: casual
lint:
  max_hashtags: 0
---

# Reddit

- Markdown renders (bold, lists, links, headings in posts).
- Titles matter more than hooks inside the body: the title is what people vote on.
- Subreddit-specific rules belong in the user's pack (`formats.md`, `platforms.reddit.community_rules+`), because they depend on where each user posts.
