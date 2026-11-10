---
enabled_families: [post, article, comment, message]
enabled_platforms: [linkedin, reddit, slack, blog]
families:
  post:
    length:
      max_words: 250
platforms:
  reddit:
    community_rules+:
      - "{subreddit}: {rule}"
lint:
  banned_chars+: ["U+2013"]
  banned_phrases+: []
signatures:
  linkedin_fr: "{your French LinkedIn signature}"
  linkedin_en: "{your English LinkedIn signature}"
  email_fr: "{your email sign-off}"
---

# Formats

Your overrides of the shipped family and platform profiles. Only list what differs for you.

- `families` and `platforms`: override any field, for example a shorter post.
- A key ending in `+` adds to a list instead of replacing it.
- `lint`: your own banned characters, phrases and patterns, enforced by the lint script.
- `signatures`: the block added at the end of posts and emails, per platform and language.
- Tone and voice are not allowed here: they live in `voice.md`.

Custom families or platforms go in a `formats/` folder next to this file. Use `add-format` mode to create one.
