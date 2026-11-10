---
name: comment
kind: family
version: 1
description: A public reply under someone else's post or thread.
reader_situation: Reading the original post first, then the comments. The original author and their audience are the readers.
structure: [response, contribution]
hook_default: none
hook_rule: No hook. Respond to what the original author actually said in the first sentence.
cta_by_intent:
  inform: none
  convince: none
  ask: soft
  announce: none
  reply: none
  relationship: none
length:
  min_words: 15
  max_words: 120
lists: avoid
extra_critics: []
lint:
  max_paragraph_words: 60
  max_sentence_words: 30
  max_single_line_ratio: 1.0
  max_list_items: 0
  max_links: 0
  max_hashtags: 0
  emojis: false
---

# Comment

## Rules
- Respond to the original point, then add one thing: an experience, a nuance, a question, a counterexample.
- Never self-promotional. No links unless the original author asked for resources.
- Never "Great post!" without substance.

## Deliverable
The comment as plain text.
