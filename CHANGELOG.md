# Changelog

## 0.4.1 (2026-11-13)
- The voice pack and the business source can live in any place the assistant can reach: files, any connected app (Notion, Google Drive...), a web page. Notion is an example, no longer the only named app. Updates go back through the same connector when possible, otherwise as text to paste.

## 0.4.0 (2026-11-13)
- Setup extracts first: voice, lexicon and anti-patterns are drafted from published pieces (comments included), then five questions at most for what can't be extracted.
- Setup imports business data (offers, readers, positioning) from an existing source: a Grey matter / Matière grise Notion page, a Prism context file, the user's site. Each imported line keeps its source and date.
- `voice.md` template: Convictions (believe, push back on, subjects to own) and Conventions (language variety, contractions, capitals, emojis, numbers).
- `anti-patterns.md` template: Forbidden (lint blocks) vs Avoid (lint flags, with the preferred word).
- Write mode: repetition check against published topics before the angles. Angle finders receive the convictions and the close topics.
- Validator notes missing Convictions, Conventions, Forbidden and Avoid sections.
- Example pack updated to the new sections.

## 0.3.1 (2026-11-13)
- Glyph library (`glyphs.md`): typed list markers, arrows and symbols for plain-text platforms, each with what screen readers announce.
- Pack choice in `formats.md` under `glyphs`: list marker, numbering, arrow, allowed symbols, globally or per platform.
- Lint: mixed list markers, markers that differ from yours, typed markers on platforms with real lists, symbols outside your choice. Library glyphs no longer count as emojis.
- Fake bold and italic: still high by default; opt-in `fake_bold: allow` makes it low per use, medium above 3 words or on a whole line.
- Writer and repurpose use real lists where the platform renders them, your marker elsewhere.
- Example pack uses ▸ with ✓ and ✗ allowed. Tests cover the glyph checks and the opt-in.

## 0.3.0 (2026-11-13)
- Lint: invisible characters (zero-width spaces, soft hyphens, byte order marks) flagged as high.
- Lint: stock words in English and French (`stock-words.md`), flagged per line, never replaced; a medium finding above `max_stock_words`. Users allow their own words with `stock_words_allow`.
- Lint: specificity check, concrete details per 100 words (`min_specificity`, `specificity_min_words`). Stats show the count.
- New `bio` family: LinkedIn headline and About, directory profiles, speaker and author bios. Enabled on LinkedIn and blog.
- Thin pack: setup quick start from three published pieces; the validator reports full, thin or too thin; outputs say "Thin pack" under five examples; learn mode offers to add the published piece first.
- Invariant: Plume never posts or sends on the user's behalf.
- Description and README lead with LinkedIn use cases.
- Example pack: a bio example (three examples, thin pack). Tests cover the new checks.
- Docs: identity brief (`docs/identity.md`), landing page decisions in `CLAUDE.md`, credits for ideas from linkedin-agent-skill.

## 0.2.0 (2026-11-10)
- Cross-platform: `agents/openai.yaml` for ChatGPT and Codex (display name, description, default prompt), platform-neutral wording, explicit calls documented (`@plume`, `$plume`, `/plume:<mode>`).
- Fallback when scripts can't run on a platform: the model applies the checks and labels it.
- Description rewritten with use case and triggers first.
- Compatibility section and a per-release test checklist.
- Install commands point to the `skill-plume` repo.

## 0.1.0 (2026-11-10)
- First version.
- Skill with seven modes: write, edit, repurpose, review, learn, setup, add-format.
- Roles: three angle finders, writer, Reader, voice matcher, fact checker, editor, blind judge, plus extra critics (SEO, slide-alone, read-aloud).
- Eight families (post, article, email, message, comment, slides, script, page) and seven platforms (LinkedIn, Reddit, Slack, Teams, WhatsApp, blog, email). Platform limits left unverified.
- Intents: inform, convince, ask, announce, reply, relationship, with hook and CTA defaults.
- Scripts: profile merge with locked and forbidden fields, lint, learn diff with edit distance, pack validation, YAML subset parser.
- User pack templates and a fictional example pack.
- Claude Code plugin: seven agents with a model per role, six slash commands.
