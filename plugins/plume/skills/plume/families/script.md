---
name: script
kind: family
version: 1
description: Text written to be spoken (video, talk, webinar, podcast intro).
reader_situation: A listener who cannot reread. Decides in the first seconds whether to keep watching or listening.
structure: [hook, promise, segments, recap, cta]
hook_default: required
hook_rule: The first two sentences say what the listener gets and why now. Spoken, not written.
cta_by_intent:
  inform: soft
  convince: soft
  ask: explicit
  announce: explicit
  reply: none
  relationship: none
length:
  min_words: 100
  max_words: 1800
lists: avoid
extra_critics: [read-aloud]
lint:
  max_paragraph_words: 80
  max_sentence_words: 22
  max_single_line_ratio: 1.0
  max_list_items: 0
  max_links: 0
  max_hashtags: 0
  emojis: false
---

# Script

## Rules
- Short sentences, spoken rhythm, repetition allowed when it helps the listener.
- Signpost transitions out loud ("Second thing.").
- Duration estimate: assume roughly 130 to 150 spoken words per minute and state the estimate.

## Deliverable
The script with segment markers, the duration estimate, and stage notes in brackets if useful.
