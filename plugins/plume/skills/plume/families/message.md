---
name: message
kind: family
version: 1
description: A message in a conversation tool (Slack, Teams, WhatsApp), to a person or a group the author knows.
reader_situation: In the middle of other conversations, reading quickly on a phone or between tasks. Knows the author.
structure: [point, context, ask]
hook_default: none
hook_rule: No hook. The first line says what this is about.
cta_by_intent:
  inform: none
  convince: soft
  ask: explicit
  announce: soft
  reply: none
  relationship: none
length:
  min_words: 5
  max_words: 150
lists: limited
extra_critics: []
lint:
  max_paragraph_words: 50
  max_sentence_words: 25
  max_single_line_ratio: 1.0
  max_list_items: 5
  max_links: 2
  max_hashtags: 0
  emojis: true
---

# Message

## Structure
- **Point:** first, in one line.
- **Context:** only what the reader needs.
- **Ask:** if there is one, clear and easy to answer.

Rendering follows the platform's syntax (Slack, Teams and WhatsApp differ). No signature unless the pack sets one.

## Deliverable
The message, rendered for the platform.
