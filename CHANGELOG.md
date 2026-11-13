# Changelog

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
