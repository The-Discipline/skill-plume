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
- **Stock words are flagged, never replaced** (`stock-words.md`, English and French, kept short). Replacing words automatically produces a different kind of generic text; the editor or the author decides. Users allow words they really use with `stock_words_allow`.
- **Specificity check:** concrete details (names, numbers, quotes, placeholders) per 100 words, above 60 words. A rough count to catch text with nothing lived or measured in it, not a quality score.
- **Invisible characters are always flagged.** Non-breaking spaces are not: French typography needs them.
- **The lint lists findings, it never scores.** A 0-100 "human" score is false precision, like Prism's rejected confidence scores.
- **Thin pack:** Plume runs from 3 published pieces (quick start in setup), says "Thin pack: N examples" until there are 5, and learn mode offers to add each published piece first. Asking for 10 to 15 up front was a barrier at install.
- **Bio family:** LinkedIn headline and About, directory and freelance platform profiles, speaker and author bios. Separate from `page`: a different reader situation (comparing profiles in seconds) and versions by length.
- **Glyphs (`glyphs.md`):** a short library of typed symbols with what screen readers announce. The user picks a list marker, numbering, arrow and allowed symbols in `formats.md`, globally or per platform. Real lists where the platform renders them, typed markers elsewhere; repurpose converts. One marker style per piece.
- **Fake bold and italic stay flagged as high** (accessibility, search, broken rendering). A pack can opt in with `fake_bold: allow`: then low per use, medium above 3 words or on a whole line. Never on by default.
- **Setup extracts first, asks last** (v0.4). People describe how they wish they sounded; published pieces show how they sound. Setup drafts voice, lexicon and anti-patterns from the pieces (comments included), then asks five questions at most, only for what can't be extracted.
- **Voice pack sections (v0.4):** Convictions in `voice.md` (believe, push back on, subjects to own: angles argue from them, never from opinions the user hasn't stated), Conventions in `voice.md` (language variety, contractions, capitals, emojis, numbers), Forbidden (lint blocks) vs Avoid (lint flags) in `anti-patterns.md`. The validator notes missing sections.
- **Repetition check before angles:** compare the raw material with published topics; if close, say so and ask for a new angle, a follow-up, or go ahead.
- **Business data can live outside the pack** (Grey matter / Matière grise, Prism context file). Setup imports offers, readers and positioning from it with source and date, and never asks again for what it says. Plume and Prism should read the same business source rather than each keep a copy.
- **No separate voice-bible builder skill.** Setup is the builder; two skills owning one pack format would drift.
- **Plume never posts.** Most platforms only allow automated posting through approved apps, and the user's account carries the risk.
- **LinkedIn first in positioning:** examples in the README and on the page lead with LinkedIn, where the demand is. The engine stays multi-platform.
- **Plain-Python scripts with a YAML subset parser** (`plume_yaml.py`), so they run in the Claude app's code execution without dependencies.
- **Agents in Claude Code:** angles and critics on sonnet; writer, editor, judge on opus. In the Claude app, roles run sequentially, labelled "Reduced Plume".

- **Cross-platform (Nov 2026):** one skill folder for Claude and OpenAI (ChatGPT desktop, Codex), both on the open Agent Skills standard. `agents/openai.yaml` inside the skill holds OpenAI display metadata; Claude Code plugin agents stay at plugin level. ChatGPT web and mobile only run plugin-bundled skills: an OpenAI plugin is a later step, built from OpenAI's docs. If a script can't run on a platform, the model applies the same checks and says so.
- **Description order:** use case and trigger words first, tagline last. Hosts shorten descriptions when many skills are installed.
- **Repo name:** `skill-plume`, in a series with `skill-prism`. No verb for the command ("plumatize" rejected): Plume has several modes, so the mode is the verb (`/plume:write`, `/plume:edit`).

## Landing page (goua.la)

- Standalone page in English, built from the Prismatize page structure and the goua.la design system. Links to Prism, no shared skills page.
- Built only after real runs. No sample proof: the proof section is the owner's own before/after (generic AI draft, Plume draft, published version) with its edit distance.
- The owner's voice is the demo (dogfooding in public).
- Signature ideas to show: the critics' blind spots as a who-sees-what grid, and one draft where lint flags, critic notes, the editor's diff and the judge's pick appear in turn.
- A free Notion "Plume pack" template ships with the page: it mirrors the pack files and links Plume to the owner's Notion business.
- Order: pack #1, real runs, Notion pack template, then the page.

## Release test checklist

On every platform marked supported or expected:
1. The skill installs without error.
2. It triggers from the description and from its explicit call.
3. Reference files load (a family profile, a role).
4. Scripts run (`validate_pack.py`, `lint.py`), or the fallback label appears.
5. Full or reduced mode is stated correctly.
6. The output ends with the "show the work" line.

## Rejected ideas

From a 10-file "brand writing skill" blueprint (Nov 2026; kept: evidence over identity, forbidden vs avoid, conventions, convictions, repetition check):
- Ten knowledge files: nobody fills them. Positioning, editorial strategy and product knowledge are business data, not voice.
- Adjusting tone per platform: the platform changes the format, never the voice.
- Self-review by the writer: it shares the writer's blind spots. Critics with less context instead.
- Best-performing content as a resource: engagement as a target pushes toward bait (see above).

From the review of linkedin-agent-skill (Nov 2026, ideas kept are credited in the README):
- Hook formula libraries: they make every post sound the same. Angles come from the user's material.
- A 0-100 "human" score: see locked decisions.
- Weekly content plans, inbox triage, DM sequences: managing a presence, not writing. Out of scope.
- Generating carousel PDFs: Plume writes the copy, not the visuals.
- Ranking published posts by engagement to pick examples: not now (owner's call). If it comes back, engagement is a tag on examples, never a target.

- One skill per format, or separate behaviours per format: replaced by data profiles over one engine.
- Per-language profiles: language belongs to the voice pack.
- Tone in format profiles: would split the voice per platform.
- A full multi-critic council with several rounds for every post.
- A critic that rewrites.
- Shipping formats nobody uses: Instagram was dropped.
- Names: Timbre (existing skill, and "timbré" means crazy), Cadence (existing skill), Encre (unpronounceable in English), Signet and Grain (owner chose Plume).

## Open questions

- Grey matter as the shared business source for Plume and Prism: its format, where it lives (Notion, Markdown), and how each skill reads it.

- License (Prism is MIT).
- Verify platform limits (LinkedIn truncation and character limit, others) and set `last_checked`.
- Build the owner's pack from the Writer and Critic projects (pack #1) with `setup` mode.
- Migrate the Noctursus voice skill into a Plume pack.
- Eval set: 10 to 20 real past briefs with published finals (`evals/`).
- Notion "Plume pack" template: how Plume reads it (Notion connector vs export to Markdown), and whether it doubles as the examples corpus below.
- Notion database as the examples corpus (fields: family, platform, language, topic, date, AI draft, final, edit distance) instead of a folder.
- Optional: run the Reader on another model family through an API in Claude Code, for real independence.
- A `document` family (proposals, case studies) if the owner needs it.
- Tune `min_specificity` (1.5 per 100 words) and the stock-word list on the owner's real pieces: they must not flag his published work.

## Writing rules for this repo

- No em dashes. `scripts/check-style.sh` enforces it on Markdown.
- Bullet points over tables.
- Each instruction appears once. Repetition dilutes the rules that matter.
