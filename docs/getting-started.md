# Getting started with Plume

How to get drafts that sound like you, and how to make them closer every week. For installation, see the [README](../README.md#install).

## 1. Your first run

Ask for what you need ("write a LinkedIn post about...", or `/plume` in Claude Code). Without a voice pack, Plume first asks for three things:

1. three posts you've published and like (pasted, or a link it can open)
2. who you're writing for, in one line
3. your main offer, with its link

That's about two minutes. Plume then writes your piece, ending with "Thin pack: 3 examples", and offers to keep what it learned as your **voice pack**, wherever you choose: files, a project, Notion, Google Drive.

- **You already have a voice guide or a brand book:** send it too. Plume compares it with your posts and tells you where they differ. Until you decide, your posts win: the guide says how you want to sound, the posts how you sound.
- **You've never published:** Plume writes in a neutral voice, labelled as such. Come back after three posts.

For a complete pack, ask for setup (`/plume:setup`). Bring 10 to 15 published pieces, comments included. Plume drafts your voice from them, then asks five questions at most, about what it can't see in your writing: your convictions, your readers, what's forbidden versus only to avoid.

## 2. Give it something real

Plume won't invent your experience. A topic alone gets you up to three questions, not a draft.

- Weak: "A post about Notion for freelancers."
- Better: "A post about the client who asked me to rebuild their CRM three times. The first two worked; nobody used them. This time we built one view, what the sales lead checks on Monday morning."

Raw material is something you lived, saw or measured: a client story, a number, a sentence someone said. Notes in any order are fine.

## 3. Read the output

- **The brief line, at the top:** format, platform, intent, language, hook and call to action, as Plume understood them. If one is wrong, say so and it rewrites.
- **The piece:** ready to paste, formatted for the platform.
- **Placeholders,** like `[figure: share of the team opening it weekly]`: facts Plume didn't have. Fill them with real numbers, or cut the sentence. Never publish one as is.
- **"Thin pack: N examples":** your pack has fewer than five published pieces. It works, and gets closer as you add more (section 4).

Ask "show the work" to see what happened before you got the text:

- the lint report: AI tells, stock words, invisible characters, rhythm, formatting
- each critic's findings: the Reader (one of your readers, who knows nothing about your rules), the Voice matcher (who only knows your published work), the Fact checker (who only knows your facts)
- the editor's changes, and which version the judge kept
- the proofreader's corrections (tagged "proofread") and its doubtful points, which are only suggestions

When a draft feels off, the critics' notes usually say why.

To only fix errors in a text, say "proofread this". Plume runs the proofreader alone and gives you the corrected text with each change listed. Tell it how you want French typography in your voice pack (full rules with non-breaking spaces, or plain spaces); if you don't, spacing is never flagged.

## 4. The habit that makes it work

After you publish, show Plume the version you actually posted ("here's what I published"). This is **learn mode**:

- Plume compares its draft with your final version and reports the **edit distance**: how much you changed.
- It proposes updates to your pack, each with the edits that justify it. You accept or reject them one by one. Nothing changes without your yes.
- It offers to add the published piece to your examples. In a thin pack, this is what makes the next draft closer.

If the edit distance doesn't go down over a few weeks, the pack needs work: run setup again with more pieces.

## 5. Pick the right mode

- **write:** from notes or a story to a finished piece. "Write a post about..."
- **edit:** your own draft, minimal changes, your style kept. "Make this sound like me", "tighten this".
- **repurpose:** one source into other formats. "Turn this article into a LinkedIn post and a carousel."
- **review:** feedback only, no rewrite. "What do you think of this email?"
- **learn:** your published version, to improve the pack.
- **setup:** build or update your voice pack.

Formats: post, article, email, message, comment, slides, thread, script, page, bio (LinkedIn headline and About, directory profile, speaker bio). Platforms: LinkedIn, Instagram, X, Threads, Reddit, Slack, Teams, WhatsApp, blog, email.

## 6. Your voice pack

- **Where:** anywhere your assistant can read: attached files, a project, a `plume-pack/` folder, Notion, Google Drive. Any readable format works; Markdown is the easiest to keep up to date.
- **What matters most:** your published pieces. Then your convictions (what you believe, what you push back on) and your bans. The [templates](../plugins/plume/skills/plume/templates/) show every section; the [example pack](../examples/pack-example/) shows a filled one.
- **Your list markers and symbols** for plain-text platforms like LinkedIn: set them once in `formats.md` (`glyphs`).
- **Keep it private:** it holds your positioning and your numbers.

## 7. When it goes wrong

- **It asks questions instead of writing:** your request had no raw material. Add one concrete thing.
- **It doesn't sound like you:** check the "Thin pack" line and add published pieces, then use learn mode after each post.
- **The lint flags a word you really use:** add it to `stock_words_allow` in your pack's `formats.md`.
- **"Reduced Plume" in the result:** your platform can't run independent critics, so they ran one after another. Use Claude Code for the full pipeline.
- **"Lint done by the model":** code execution is off, so the checks were done by reading. In the Claude app, turn code execution on.

Plume writes; you publish. It never posts or sends anything for you.
