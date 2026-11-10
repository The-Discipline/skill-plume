# CLAUDE.md: Plume

Context for any Claude Code session working on this repo. Read it fully before changing anything.

## Maintenance rule (from the owner)

**Every change updates the documentation in the same commit:**
- `README.md`: what it does, what it doesn't, who it's for, how it works, formats, install, and the **Status** section
- `CHANGELOG.md`: a new entry
- this file: new decisions, rejected ideas, open questions
- the version in `plugins/plume/.claude-plugin/plugin.json`

Run `scripts/check-style.sh` and `scripts/test.sh` before every commit.

## What Plume is

A writing assistant skill that writes in the user's own voice. It replaces the owner's two Claude projects ("The writer" and "The critic"), which shared the same context and drifted apart. Sister skill to Prism (decisions). Owner: Virgile Gouala (goua.la). Product from day one, shared with multiple people: the owner's own pack is pack #1, the Noctursus voice skill is the first external pack to migrate.

- Name: Plume, everywhere (product, skill, plugin, ZIP). Commands `/plume:<mode>`.
- Tagline: "Writes like you. Reads like your audience."
- Never use "plumer" as a verb in French ("se faire plumer" means getting ripped off).
- Known collision: an existing "Plume AI" writing assistant. Accepted by the owner. Check trademarks before launch.

## Locked decisions (with the reason)

- **Critics are defined by what they can't see** (context asymmetry, from Prism's Buyer). Reader: no voice pack, no rules. Voice matcher: published examples only, no rules. Fact checker: sources of truth only. A critic with the writer's full context shares its blind spots.
- **Examples over rules.** The writer drafts from 3 to 5 published pieces of the same family and language first. Rules produce compliant, generic text.
- **Mechanical checks are code** (`lint.py`), not LLM judgement. Its result wins on mechanical points.
- **One revision round, then a blind pairwise judge.** The owner's own experience: three critique passes showed diminishing returns. Pairwise comparison is more reliable than scoring and guards against over-polishing.
- **Edit mode preserves the user's voice.** Only flagged changes plus typos. If the judge prefers the original, return it with suggestions.
- **Learn mode is the only way the pack changes from evidence.** It diffs the AI draft with the published version, proposes changes with evidence, and writes only what the user accepts. It never touches shipped files.
- **No invented facts.** Placeholders instead. Sources: raw material and `facts.md` only.
- **Raw material gate.** Write and repurpose need something concrete from the user, or ask up to three questions.
- **Three layers:** engine (SKILL.md invariants) > user overrides (`formats.md` in the pack) > shipped family and platform defaults. The user pack lives outside the skill so updates never overwrite it.
- **Family vs platform:** the family sets structure, length, reader situation, hook and CTA defaults. The platform sets only constraints (limits, rendering syntax, conventions, community rules, default register). If structure differs, it's a family (a LinkedIn carousel is `slides`).
- **Intent is a brief field, never a format:** inform, convince, ask, announce, reply, relationship. It sets the CTA default, whether angles run, and the Reader's question.
- **Hook and CTA** are inferred from family and intent, stated in one line, overridable. One CTA max. CTA destinations only from `facts.md`.
- **Forbidden fields in any profile:** tone, voice, style, persona, personality. Voice lives in `voice.md`.
- **Engine bans can be extended, never removed** (the em dash is banned for everyone).
- **Platform limits stay `null` until verified**, with `last_checked`. Never hard-code numbers from memory.
- **Plain-Python scripts with a YAML subset parser** (`plume_yaml.py`), so they run in the Claude app's code execution without dependencies.
- **Agents in Claude Code:** angles and critics on sonnet; writer, editor, judge on opus. In the Claude app, roles run sequentially, labelled "Reduced Plume".

## Rejected ideas

- One skill per format, or separate behaviours per format: replaced by data profiles over one engine.
- Per-language profiles: language belongs to the voice pack.
- Tone in format profiles: would split the voice per platform.
- A full multi-critic council with several rounds for every post.
- A critic that rewrites.
- Shipping formats nobody uses: Instagram was dropped.
- Names: Timbre (existing skill, and "timbré" means crazy), Cadence (existing skill), Encre (unpronounceable in English), Signet and Grain (owner chose Plume).

## Open questions

- License (Prism is MIT).
- Verify platform limits (LinkedIn truncation and character limit, others) and set `last_checked`.
- Build the owner's pack from the Writer and Critic projects (pack #1) with `setup` mode.
- Migrate the Noctursus voice skill into a Plume pack.
- Eval set: 10 to 20 real past briefs with published finals (`evals/`).
- Notion database as the examples corpus (fields: family, platform, language, topic, date, AI draft, final, edit distance) instead of a folder.
- Optional: run the Reader on another model family through an API in Claude Code, for real independence.
- A `document` family (proposals, case studies) if the owner needs it.

## Writing rules for this repo

- No em dashes. `scripts/check-style.sh` enforces it on Markdown.
- Bullet points over tables.
- Each instruction appears once. Repetition dilutes the rules that matter.
