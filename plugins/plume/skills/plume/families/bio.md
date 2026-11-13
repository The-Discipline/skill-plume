---
name: bio
kind: family
version: 1
description: Short self-presentation. LinkedIn headline and About, freelance platform or directory profile, speaker bio, author bio.
reader_situation: Deciding in a few seconds whether this person is relevant, often next to other profiles in a search result or a directory. Reads the first line, scans for their own problem, checks proof.
structure: [headline, who you help and with what, how you do it, proof, how to work together]
hook_default: required
hook_rule: The first line says who you help and with what, in the reader's words, not your job title alone.
cta_by_intent:
  inform: soft
  convince: explicit
  ask: explicit
  announce: soft
  reply: none
  relationship: none
length:
  min_words: 10
  max_words: 350
lists: limited
extra_critics: []
lint:
  max_paragraph_words: 80
  max_sentence_words: 25
  max_single_line_ratio: 1.0
  max_list_items: 5
  max_links: 1
  max_hashtags: 0
  emojis: false
---

# Bio

## Rules
- Ask where it goes before writing: the destination sets the person (first person for LinkedIn and your own site, third person for a speaker or author bio) and the length.
- Proof comes from `facts.md` only: clients you may name, certifications, numbers. Missing proof is a placeholder.
- Use the words your clients search for, not your internal vocabulary. In a directory, those words are how you get found.
- No inflated titles, no list of every skill. One offer, one audience, one way to work with you.
- Character limits (LinkedIn headline, directory fields) stay unverified in the platform profile. Ask the user for the field's limit when it matters.

## Deliverable
The versions the destination needs, each labelled:
- **Headline:** one line
- **Short:** one or two sentences, for directories and event pages
- **Long:** the full About or profile text
Write only the versions asked for, or the ones the destination uses.
