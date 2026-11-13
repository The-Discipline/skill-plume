# Mode: setup

Build a user pack, or import an existing voice bible.

**Quick start** (the user wants to try Plume now): ask for three pieces they published and are happy with, who they write for, and their main offer with its link. Draft `voice.md` and `anti-patterns.md` from the three pieces, every line marked "inferred, to confirm". Fill `audiences.md` and `facts.md` with only what they said, index the three pieces, validate, and start writing. The pack is thin: learn mode grows it with each piece they publish.

**Full setup:**

1. **Ask for material:**
   - at least 3 published pieces, ideally 10 to 15 across the families the user writes most
   - any existing voice guide, style guide, anti-pattern list or prompt they already use
   - who they write for
   - their site, offers and booking link
2. **Import existing documents** into the template structure (`templates/`) without rewriting the user's words. Deduplicate, and list conflicts between documents for the user to settle instead of choosing silently.
3. **Draft from the examples** what the documents do not cover: recurring constructions, rhythm, vocabulary. Mark everything inferred as "inferred, to confirm".
4. **Audiences:** one to three specific personas.
5. **Facts:** only what the user provides or what is on their live site. No guessing prices or results.
6. **formats.md:** enabled families and platforms, signatures, the mechanical bans as lint rules.
7. **Examples:** save each piece under `examples/` and index it.
8. **Validate** with `python3 scripts/validate_pack.py <pack>` and show the remaining gaps.
9. Tell the user where the pack lives and that it stays private: it contains their positioning and facts.
