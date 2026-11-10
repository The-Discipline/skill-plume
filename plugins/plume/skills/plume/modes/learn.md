# Mode: learn

The only way the pack improves from evidence. Input: the AI draft (from this conversation or a file) and the version the user actually published.

1. Save both to files and run `python3 scripts/diff_learn.py <draft> <published>`.
2. Read the changes and group them into patterns. A pattern needs at least two occurrences, in this piece or across the learn log. One-off edits are content, not voice.
3. For each pattern, propose one pack update:
   - **target file:** anti-patterns.md, lexicon.md, voice.md, formats.md (lint rules), or the examples
   - **exact change:** the line to add or modify
   - **evidence:** the edits that justify it
   Prefer a lint rule (`formats.md` under `lint`) when the pattern is mechanical: a character, a phrase, a construction.
4. The user accepts or rejects each proposal. Write only the accepted ones, and append each to `learn-log.md` with the date and evidence.
5. Offer to add the published piece to `examples/` and to `examples/index.md` (family, platform, language, date, topic).
6. Report the edit distance. Over time, it is the metric that shows whether Plume improves.

Never write to the shipped skill files from this mode. Learn only changes the user's pack.
