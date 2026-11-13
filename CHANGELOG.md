# Changelog

## Unreleased
- Docs: identity brief (`docs/identity.md`): names, descriptions, cast, visual concept, diagrams.
- Docs: landing page decisions in `CLAUDE.md`.

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
