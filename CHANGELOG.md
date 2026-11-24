# Changelog

## 0.7.2 (2026-11-24)
- Help: `help` mode, `/plume:help` and "plume help" print a fixed block: how to ask, the voice pack, what "Reduced Plume" means, code execution, and links to the guide and the issue tracker. A bare "help" does not trigger it.
- Directory submission: `plugins/plume/README.md`, `homepage`, `repository` and a 512x512 `icon` in `plugin.json`.
- README: listing badge. The Claude Code command list includes `/plume:help`.

## 0.7.1 (2026-11-21)
- The pack is in the user's format: docs describe it as sections, not files, and no longer say it is Markdown. One Notion page or a Google Doc works.
- Settings in plain words ("allow the word X", "use ▸ for lists"): Plume writes them into the pack, the user never edits syntax.
- A read-only pack (PDF, export) is moved to an editable format of the user's choice, not to Markdown by default.
- Scripts run on a working copy Plume writes itself, split by section.

## 0.7.0 (2026-11-21)
- Guardrails: raw material, the pack, examples, guides, linked pages and published versions are data, never instructions. Every agent says so.
- Pack updates: only accepted lines, the target read first, nothing else deleted or rewritten, then re-read and the change shown. A failed write gives the text to paste.
- Learn mode logs rejected proposals too and never proposes the same change twice without new evidence. Without code execution, the edit distance is labelled an estimate.
- Role inputs fixed: the editor now receives the voice keep list, Conventions and anti-patterns it needs to drop findings that contradict the voice; the writer receives the anti-patterns; the SEO critic the allowed links; the slide-alone critic the word limit.
- Setup: if a link to published posts can't be opened, Plume asks for the text.
- "Show the work" is available until the end of the conversation.
- Wording: "X, not Y" phrasings rewritten in the skill, the docs and the agents.

## 0.6.0 (2026-11-20)
- New role: the proofreader. It runs last, on the final text, and finds objective errors only: spelling, agreement, conjugation, doubled or missing words, punctuation, consistency of variety and numbers, and French typography when the pack asks for it. Sure fixes are applied and tagged "proofread" in the change list; doubtful ones stay suggestions. It never touches style or what the pack says to keep. Plugin agent `plume:proofreader`.
- "Proofread this" runs the proofreader alone, with no critics, editor or judge.
- The language of a piece now carries its variety, typography and other-language notes from the pack. New Conventions line `Typography` and an optional "In another language" section in `voice.md`.
- Repurpose: changing language is a rewrite from the user's examples in the target language, not a translation.
- MIT license added.

## 0.5.0 (2026-11-17)
- New family `thread`: a chain of linked posts. The first post works alone, each part stands alone, parts are separated by `---`. The lint checks the number of parts and the words per part.
- New platforms: Instagram (captions, carousels via `slides`), X and Threads (posts, threads, comments). Limits are left unverified (`last_checked: never`), as for the other platforms.
- The slide-alone critic also reads thread parts.
- Plume writes text only. Instagram notes say so: no images, alt text only on request.

## 0.4.5 (2026-11-15)
- Docs: `docs/getting-started.md`, the user guide: first run, raw material, reading the output and show the work, learn mode and edit distance, modes, the voice pack, troubleshooting. Linked from the README.
- README: install commands point to The-Discipline/skill-plume.

## 0.4.4 (2026-11-14)
- Review fixes. Setup: first run and quick start merged into one flow, no instruction given twice; "come back after three posts", matching the thin-pack threshold.
- SKILL.md: explicit call moved to the top; pack loading split into where, format, updates and scripts.
- Agents: each one works only from its prompt and opens no file, so the critics' blind spots hold even with the Read tool.
- `scripts/skill_review.py`: release review (frontmatter, sizes, broken file references, versions, repeated instructions, stale words).
- Docs: identity brief points to v0.4; open question on the Notion template updated; evals note on `results.md`.

## 0.4.3 (2026-11-13)
- First run: with no pack, Plume opens with one short message (English and French) asking for three posts, the reader and the offer, writes the requested piece first, then offers to save the pack wherever the user wants.
- First run: a voice guide is compared with the posts (the posts win until the user decides); people who have never published get a labelled neutral voice and an invitation to come back after five posts.

## 0.4.2 (2026-11-13)
- Any readable format for the pack and for setup's imports: Markdown, text, Google Doc, Word, PDF, slides, web pages, exports of past posts. Read-only formats are converted to Markdown once, when learn mode has changes to write.

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
