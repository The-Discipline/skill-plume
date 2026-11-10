---
name: post
kind: family
version: 1
description: A public post in a feed, read by people who did not come for it.
reader_situation: Scrolling a feed between two other things. Decides in the first two lines whether to stop. Will not click "see more" for a weak opening.
structure: [hook, development, takeaway, cta, signature]
hook_default: required
hook_rule: Open on what a fact reveals, contradicts or costs, never on the bare fact. The hook must stand alone before the platform's truncation point.
cta_by_intent:
  inform: soft
  convince: soft
  ask: explicit
  announce: explicit
  reply: none
  relationship: none
length:
  min_words: 80
  max_words: 300
lists: limited
extra_critics: []
lint:
  max_paragraph_words: 60
  max_sentence_words: 30
  max_single_line_ratio: 0.5
  max_list_items: 5
  max_links: 1
  max_hashtags: 3
  emojis: false
---

# Post

## Structure
- **Hook:** one or two lines that make the reader stop. A tension, a cost, a contradiction, a moment.
- **Development:** the story or the reasoning, in short paragraphs. Prefer narration over lists.
- **Takeaway:** what the reader keeps. Not a moral, not a slogan.
- **CTA:** only if the intent calls for it, one at most.
- **Signature:** the user's signature block for this platform and language, from the pack.

## Deliverable
The post as plain text, line breaks included, ready to paste. Then placeholders and assumptions if any.
