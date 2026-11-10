---
name: slides
kind: family
version: 1
description: A sequence of slides, such as a LinkedIn carousel or a short deck. One idea per slide.
reader_situation: Sees slide 1 in a feed or on a screen. Swipes only if slide 1 promises something and slide 2 keeps the promise.
structure: [cover, slides, last_slide, caption]
hook_default: required
hook_rule: Slide 1 states the promise or the tension in a few words. Slide 2 delivers the first part of it immediately.
cta_by_intent:
  inform: soft
  convince: soft
  ask: explicit
  announce: explicit
  reply: none
  relationship: none
length:
  min_words: 60
  max_words: 400
slides:
  min: 5
  max: 12
  max_words_per_slide: 35
lists: limited
extra_critics: [slide-alone]
lint:
  max_paragraph_words: 35
  max_sentence_words: 20
  max_single_line_ratio: 1.0
  max_list_items: 4
  max_links: 0
  max_hashtags: 3
  emojis: false
---

# Slides

## Structure
- **Cover:** the promise, very short.
- **Slides:** one idea each, readable alone, building on the previous one.
- **Last slide:** the takeaway or the CTA.
- **Caption:** the post that goes with the carousel, following the post family rules but shorter.

## Input and output format
Separate slides with a line containing only `---`.

## Deliverable
For each slide: title, body (within the word limit), visual note (what to show, hierarchy). Then the caption. Plume writes the copy and the layout intent, not the visuals.
