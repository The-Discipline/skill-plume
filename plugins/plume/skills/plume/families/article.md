---
name: article
kind: family
version: 1
description: A long piece read on purpose, found through search, a link or a newsletter.
reader_situation: Arrived with a question or a curiosity, often from search. Skims headings first, then reads the parts that answer them. Bookmarks or leaves.
structure: [title, intro, sections, conclusion, cta]
hook_default: required
hook_rule: The title states the promise, the intro earns the second paragraph by naming the reader's problem or the tension in the first three sentences. No background, no "in today's world".
cta_by_intent:
  inform: soft
  convince: soft
  ask: explicit
  announce: explicit
  reply: none
  relationship: none
length:
  min_words: 800
  max_words: 2500
lists: allowed
extra_critics: [seo]
lint:
  max_paragraph_words: 120
  max_sentence_words: 35
  max_single_line_ratio: 0.3
  max_list_items: 8
  max_links: 10
  max_hashtags: 0
  emojis: false
---

# Article

## Structure
- **Title:** the promise, in the reader's words. Under 70 characters is a good target for search results.
- **Intro:** the problem or tension, why it matters to this reader, what the article delivers.
- **Sections:** H2 headings that answer real questions, each readable alone. Examples before abstractions.
- **Conclusion:** what to do or think next. Not a summary of the article.
- **CTA:** one, soft by default, often a link to an offer, a guide or a template from `facts.md`.

## Deliverable
- Title
- Meta description (one or two sentences)
- Outline of H2s
- Body in Markdown
- Suggested internal links (only URLs from `facts.md`)
