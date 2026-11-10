---
name: page
kind: family
version: 1
description: Web page copy (landing page, offer page, template description, bio, about page).
reader_situation: Evaluating whether to trust, buy, book or download. Scans headings and buttons, reads where doubt appears.
structure: [headline, subheadline, problem, offer, proof, objections, cta]
hook_default: required
hook_rule: The headline says what the reader gets, in their words. The subheadline says for whom and how.
cta_by_intent:
  inform: explicit
  convince: explicit
  ask: explicit
  announce: explicit
  reply: none
  relationship: none
length:
  min_words: 50
  max_words: 1200
lists: allowed
extra_critics: [seo]
lint:
  max_paragraph_words: 60
  max_sentence_words: 25
  max_single_line_ratio: 1.0
  max_list_items: 7
  max_links: 5
  max_hashtags: 0
  emojis: false
---

# Page

## Rules
- Proof comes from `facts.md` only: real figures, real clients (if allowed), real quotes. Missing proof is a placeholder, never invented.
- Answer the top objections explicitly (price, time, fit).
- One primary CTA, repeated if the page is long. Its destination comes from `facts.md`.

## Deliverable
Sections with their headings, body copy, button labels, and a meta title and description.
