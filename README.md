# Plume

**Writes like you. Reads like your audience.**

[![Plume - Listed on Claude AI Directory](https://www.claudeai.directory/badge/plume)](https://www.claudeai.directory/launches/plume)

A writing assistant skill for people who publish under their own name. Plume drafts, edits, repurposes and reviews LinkedIn posts, articles, emails, messages, bios and more, in your voice. Then it checks the result with critics that each lack something the writer has, so the problems a stranger would notice get caught before you publish.

> [!IMPORTANT]
> Plume is only as good as your voice pack: your voice, your bans, your audiences, your facts and, above all, pieces you actually published. Run `setup` first. Three published pieces are enough to start; Plume asks for more as you go.

## What it does

- **Writes** a piece from your raw material (something you lived, saw or measured), in your voice
- **Edits** your own draft with minimal changes, without smoothing your style
- **Repurposes** one source into several formats (an article into a LinkedIn post and a carousel)
- **Reviews** a text and gives prioritised findings, without rewriting
- **Checks for repetition:** if you already published on the same subject, it says so and asks for a new angle or a follow-up
- **Learns** from what you actually published: it compares its draft with your final version and proposes updates to your pack, which you approve one by one
- **Sets up** your voice pack: it extracts your voice from pieces you published, asks at most five questions for what it can't extract, and imports the voice bible or business data you already have

## What it doesn't do

- **Invent.** No made-up figures, clients, results, quotes or links. Missing facts become placeholders for you to fill.
- **Write without material.** If there's nothing concrete to work with, Plume asks up to three questions instead of filling the gap.
- **Change your voice per platform.** Formats change length, structure and syntax. Your voice stays the same everywhere.
- **Loop.** One revision round, then a blind comparison keeps the better version.
- **Bait engagement.** No "comment X to get the guide", no reflex "What do you think?", no hook formulas.
- **Post for you.** Plume writes, you publish. It doesn't connect to your accounts: most platforms only allow automated posting through approved apps, and your account is the one at risk.
- **Translate** for the sake of translating, or write generic copy for a brand without a voice pack.
- **Design visuals.** For slides it writes the copy and the layout intent; the images are yours.

## Who it's for

People who write regularly under their own name and want it to sound like them: freelancers, consultants, coaches, founders, executives. It's built for one person's voice. A team or a brand voice works if you build one pack for it.

## How it works

```mermaid
flowchart LR
    M["Your raw material"] --> B["Brief<br/>format, platform, intent"]
    B --> A["3 angles<br/>you pick one"]
    A --> W["Writer<br/>your examples first"]
    W --> L["Lint<br/>code, not opinion"]
    L --> R["Reader"]
    L --> V["Voice matcher"]
    L --> F["Fact checker"]
    R & V & F --> E["Editor<br/>one round, minimal changes"]
    E --> J{"Judge<br/>blind A/B"}
    J --> PR["Proofreader<br/>errors only"]
    PR --> O["Your piece"]
    O -. "what you published" .-> LN["Learn<br/>pack updates you approve"]
```

**The cast**
- **Angle finders:** three lenses in parallel (what it costs, what it contradicts, the lived moment)
- **Writer:** drafts from your published examples first, your rules second
- **Reader:** one specific person from your audiences, in their real situation (scrolling, searching, swiping). Never sees your rules or your intent.
- **Voice matcher:** sees only your published work, never your rules. Flags what doesn't sound like you.
- **Fact checker:** sees only your sources of truth. Flags anything it can't trace.
- **Editor:** one round of minimal fixes
- **Judge:** picks between two versions without knowing which one is the revision
- **Proofreader:** runs last, on the final text. Spelling, agreement, punctuation and French typography only, never style. Sure fixes are applied and listed as "proofread" in the change list; doubtful ones stay suggestions. It never touches what your voice pack says to keep.

The **lint** is a script: banned characters and phrases, invisible characters, AI tells ("not X, it's Y", generic openers, reflex questions), stock words in English and French (flagged, never replaced), too few concrete details (names, numbers, quotes), rhythm uniformity, lists of three, paragraph length, Markdown where the platform doesn't render it, hashtag and link counts. It also checks list markers and symbols against your choice for plain-text platforms (`glyphs.md`: one marker style per piece, real lists where the platform renders them), and flags fake bold or italic made of Unicode letters unless your pack opts in. It lists findings; it doesn't give a score.

Every output ends with "show the work": the lint report, each critique, the editor's changes, the judge's choice and the proofreader's corrections.

## Formats

A piece is defined by four things:
- **Family**, the kind of piece: post, article, email, message, comment, slides, thread, script, page, bio (LinkedIn headline and About, directory profile, speaker bio)
- **Platform**, where it's published: LinkedIn, Instagram, X, Threads, Reddit, Slack, Teams, WhatsApp, blog, email
- **Intent**, what it's for: inform, convince, ask, announce, reply, relationship
- **Language**

The family sets structure, length and the reader's situation. The platform only sets constraints: limits, formatting syntax, conventions, community rules. Intent sets the default hook and call to action. Plume infers all four and tells you what it chose in one line.

Platform limits (character counts, "see more" cut-offs) are left empty until verified, with a `last_checked` date, because they change.

## Your voice pack

Your pack is what Plume knows about your writing. You don't write it yourself: setup builds it from what you give (posts you published, a voice guide, a brand book, your offers page), in whatever format you have. It lives outside the skill, so updates never overwrite it. It has these sections:

- **Voice:** who you are, your convictions (what you believe, what you push back on, what you want to own), how you sound, your conventions (language variety, contractions, capitals, emojis, numbers)
- **Anti-patterns:** what is forbidden (blocked) and what to avoid (flagged), with weak and strong examples
- **Lexicon:** your expressions and signature lines
- **Readers:** the specific people the Reader critic plays
- **Facts:** offers, prices, links, proof. The only source for claims.
- **Formats:** your preferences (shorter posts, extra bans, signatures per platform, your list marker and symbols). Say them in plain words ("allow the word X", "use ▸ for lists") and Plume writes them in.
- **Examples:** pieces you published, by format and language. Three are enough to start (a "thin pack", and outputs say so); 10 to 15 is where it gets close.
- **Learn log:** the updates you accepted or rejected, with their evidence

Keep it wherever your assistant can read: one Notion page with these sections, a Google Doc, attached files, a project, or a folder of files. Plume looks for "Plume pack" or the name you give. A PDF can be read but not edited, so the first time Plume has changes to write, it offers to move the pack to an editable format of your choice. It updates the pack through the same connector when it can, otherwise it gives you the text to paste. Keep it private: it holds your positioning and facts.

For people who prefer files: the templates are in `plugins/plume/skills/plume/templates/` (one Markdown file per section), and a complete fictional pack is in `examples/pack-example/`.

## Install

After installing, read [Getting started](docs/getting-started.md): your first run, reading the output, and the habit that makes drafts closer.


**Claude app (web, desktop, mobile)**
1. Download `plume-latest.zip` from the latest release.
2. In Claude: Customize > Skills > "+" > Create skill > Upload a skill.
3. Make sure code execution is enabled, so the lint and the pack checks can run.

**Claude Code**
```bash
claude plugin marketplace add The-Discipline/skill-plume
claude plugin install plume@plume
```
Commands: `/plume` (Plume picks the mode), or a specific mode with `/plume:write`, `/plume:edit`, `/plume:repurpose`, `/plume:review`, `/plume:learn`, `/plume:setup`, `/plume:help`.

**ChatGPT desktop app:** upload the `plume` skill from Plugins > Skills, then call it with `@plume`.

**Codex:** copy the `plume` folder to `~/.agents/skills/`, then call it with `$plume`.

In Claude Code, each role runs as its own agent with a model chosen for the job: mid-tier for the angle finders and critics, top model for the writer, editor and judge. Elsewhere, roles run on the model you selected, one after another if the platform can't run independent agents, and the output says so ("Reduced Plume").

**Compatibility**
- Claude Code: full, recommended
- Claude app: supported
- ChatGPT desktop and Codex: expected to work, reduced mode, scripts to be tested
- ChatGPT web and mobile: needs an OpenAI plugin, not available yet
- Your voice pack can be in any format and works with any assistant that can read it

Status changes only after a real test on that platform.

## Use it

- "Write a LinkedIn post about the client who asked me to rebuild their CRM three times."
- "Turn this article into a LinkedIn post and a carousel."
- "Rewrite my LinkedIn headline and About for freelancers looking for a Notion consultant."
- "Make this sound like me." (with your draft)
- "Review this email before I send it."
- "Here's what I actually published." (after a write, to start learn mode)

## Measuring it

The metric is **edit distance to publish**: how much you change Plume's draft before posting. Learn mode reports it every time. If it doesn't go down over a few weeks, the pack or the pipeline needs work. See `evals/`.

## Status

**v0.7.2, untested on real briefs.**
- Built: skill and modes, 10 families, 10 platforms, role prompts, plugin agents and commands, merge, lint, learn diff and pack validation scripts, templates, a fictional example pack
- Scripts tested on the example pack (`scripts/test.sh`)
- Cross-platform metadata for ChatGPT and Codex (`agents/openai.yaml`), not tested there yet
- Proofreader added in 0.6.0: judged by reading, not yet on real texts. It is a language-model pass: for rigorous checking, use a dedicated grammar checker.
- Not yet done: a real voice pack, a real run, the eval set, verified platform limits, an OpenAI plugin for ChatGPT web and mobile

## Credits

Built by [Virgile Gouala](https://goua.la). Sister skill: [Prism](https://github.com/The-Discipline/skill-prism), a decision council for one-person businesses.

Ideas, not code, from Jake Schincariol's [linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill): a stock-word list, a specificity check and invisible-character cleanup in the lint, starting a voice from three posts, and a bio format.

License: [MIT](LICENSE).
