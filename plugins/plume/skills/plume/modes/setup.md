# Mode: setup

Build a user pack, or import an existing voice bible.

1. **Ask for material:**
   - 5 to 20 published pieces, ideally across the families the user writes most
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
