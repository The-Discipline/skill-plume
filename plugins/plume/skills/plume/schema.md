---
version: 1
locked: [name, kind, version]
forbidden: [tone, voice, style, persona, personality]
family_fields: [name, kind, version, description, reader_situation, structure, hook_default, hook_rule, cta_by_intent, length, slides, lists, extra_critics, lint]
platform_fields: [name, kind, version, last_checked, families, limits, rendering, conventions, community_rules, register_default, lint]
engine_lint:
  banned_chars: ["U+2014"]
  banned_phrases: []
  patterns:
    negation_correction_en: "(?i)\b(is|are|was|it'?s|this is|that'?s) not (just |only |about |merely )?[^.,;]{1,40}, (it'?s|it is|but|they'?re)\b"
    generic_opener_en: "(?i)^(in today'?s (fast-paced|rapidly|ever-changing)|in a (rapidly|constantly) changing world|more than ever)"
    generic_opener_fr: "(?i)^(dans un monde en (constante|perp[eé]tuelle) [eé]volution|plus que jamais|[aà] l'heure o[uù])"
    reflex_question_en: "(?i)^\s*(what do you think|thoughts|agree)\s*\?\s*$"
    reflex_question_fr: "(?i)^\s*(et vous,? qu'en pensez-vous|qu'en pensez-vous|vous en pensez quoi)\s*\?\s*$"
    negation_correction_fr: "(?i)\bce n'est pas [^.,;]{1,40}, c'est\b"
    not_x_but_y_fr: "(?i)\bpas (seulement |juste )?[^.,;]{1,30}, mais\b"
  max_triplets: 2
  min_sentence_cv: 0.25
  min_paragraph_cv: 0.15
---

# Profile schema

Machine-readable part above, read by the scripts. Human explanation below.

## Kinds

- **family** (`families/*.md`): structure, reader situation, hook and CTA defaults, length, lint thresholds. One per kind of piece: post, article, email, message, comment, slides, script, page.
- **platform** (`platforms/*.md`): only constraints. Limits, rendering syntax, conventions, community rules, default register. A platform never sets structure. If two platforms need a different structure, they are different families.

## Family fields

- `name`, `kind: family`, `version`: locked
- `description`: one line
- `reader_situation`: what the reader is doing when the piece reaches them. Feeds the Reader critic.
- `structure`: ordered list of parts
- `hook_default`: required, light or none
- `hook_rule`: what the opening must do
- `cta_by_intent`: map of intent to none, soft or explicit
- `length`: `min_words`, `max_words` (for slides, see `slides`)
- `slides`: `min`, `max`, `max_words_per_slide` (slides family only)
- `lists`: allowed, limited or avoid
- `extra_critics`: roles added for this family (seo, slide-alone, read-aloud)
- `lint`: thresholds: `max_paragraph_words`, `max_sentence_words`, `max_single_line_ratio`, `max_list_items`, `max_links`, `max_hashtags`, `emojis`

## Platform fields

- `name`, `kind: platform`, `version`: locked
- `last_checked`: date the facts were verified (`never` until someone checks)
- `families`: families this platform applies to
- `limits`: `max_chars`, `truncation_chars`. Use `null` when not verified. The lint skips null limits.
- `rendering`: `markdown` (none, standard, slack, whatsapp, teams), plus notes
- `conventions`: hashtags, mentions, links, emojis
- `community_rules`: list of rules (Reddit subreddits, Slack communities)
- `register_default`: formal, neutral or casual. The user's voice still wins.
- `lint`: platform-level thresholds, merged over the family's

## Forbidden fields

`tone`, `voice`, `style`, `persona`, `personality`: rejected in any profile or override. Voice lives in the user pack's `voice.md`, nowhere else.

## User overrides (`formats.md` in the pack)

Frontmatter with:
- `families:` map of family name to overridden fields
- `platforms:` map of platform name to overridden fields
- `lint:` global additions (`banned_chars`, `banned_phrases`, `patterns`)
- `enabled_families`, `enabled_platforms`: optional lists
- `signatures:` map of `<platform>_<language>` to the signature block

Merge rules:
- Field by field, recursively. An override of `length.max_words` keeps `length.min_words`.
- A key ending in `+` appends to a list instead of replacing it: `banned_phrases+: ["game-changer"]`.
- Locked fields are ignored with a warning. Forbidden fields are rejected with a warning.

Custom families and platforms go in the pack's `formats/` folder, one file each, same fields, `kind` set.

Characters in `banned_chars` can be written literally or as code points (`U+2014` for the em dash, `U+2013` for the en dash, `U+2026` for the ellipsis character). The engine bans the em dash for everyone.

## YAML subset

The scripts use a small parser so they run anywhere with plain Python. Stay within: `key: value`, nested maps by 2-space indent, block lists (`- item`), inline lists (`[a, b]`), quoted strings, numbers, true/false, null. Full-line comments only. Long prose goes in the body, not the frontmatter.
