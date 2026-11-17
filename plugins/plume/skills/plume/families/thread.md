---
name: thread
kind: family
version: 1
description: A short chain of linked posts, such as an X or Threads thread. Each part stands alone and pulls the reader to the next.
reader_situation: Sees the first post in a feed. Opens the thread only if it promises something and the second post keeps the promise. Many readers see one part out of context.
structure: [opener, parts, closer, signature]
hook_default: required
hook_rule: The first post states the promise or the tension and works with nothing after it. The second post delivers the first part of it immediately.
cta_by_intent:
  inform: soft
  convince: soft
  ask: explicit
  announce: explicit
  reply: none
  relationship: none
length:
  min_words: 60
  max_words: 450
parts:
  min: 3
  max: 12
  max_words_per_part: 50
lists: avoid
extra_critics: [slide-alone]
lint:
  max_paragraph_words: 50
  max_sentence_words: 25
  max_single_line_ratio: 1.0
  max_list_items: 3
  max_links: 1
  max_hashtags: 1
  emojis: false
---

# Thread

## Structure
- **Opener:** the promise or the tension, in one or two lines. It must work alone.
- **Parts:** one idea each, readable on its own, building on the previous one. Prefer a concrete detail per part over a general statement.
- **Closer:** the takeaway, or the CTA when the intent calls for one.
- **Signature:** the user's signature for this platform and language, from the pack, on the last part only.

## Input and output format
Separate parts with a line containing only `---`. Numbering ("1/", "2/") only when the user's pack asks for it.

## Deliverable
The parts, separated by `---`, ready to paste one by one. Then placeholders and assumptions if any.
