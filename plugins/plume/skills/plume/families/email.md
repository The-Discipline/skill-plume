---
name: email
kind: family
version: 1
description: An email to one person or a list, with an expected action or none.
reader_situation: In an inbox, deciding from the subject line and the first sentence whether to open, read now, read later or archive.
structure: [subject, opening, body, ask, signoff]
hook_default: light
hook_rule: The subject line says what this is about or what is asked. The first sentence carries the reason to read on. No staging, no teaser.
cta_by_intent:
  inform: none
  convince: soft
  ask: explicit
  announce: explicit
  reply: none
  relationship: none
length:
  min_words: 40
  max_words: 250
lists: limited
extra_critics: []
lint:
  max_paragraph_words: 70
  max_sentence_words: 30
  max_single_line_ratio: 0.5
  max_list_items: 5
  max_links: 2
  max_hashtags: 0
  emojis: false
---

# Email

## Structure
- **Subject:** specific, short, no clickbait.
- **Opening:** why you are writing, in one sentence. Context only if the reader needs it.
- **Body:** what they need to know to act or answer.
- **Ask:** one request, with a date if relevant. Easy to answer.
- **Sign-off:** the user's signature for email in this language.

## Deliverable
Subject line, then the body as plain text.
