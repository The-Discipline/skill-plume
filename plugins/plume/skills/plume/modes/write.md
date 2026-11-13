# Mode: write

From raw material to a finished piece.

1. **Brief.** Build it (SKILL.md section 2). Apply the raw material gate.
2. **Profiles.** Merge family, platform and the user's overrides (`scripts/merge_profile.py`).
3. **Angles.** Only if the intent uses angles (`intents.md`) and the hook is not `none`. Run `roles/angles.md` three times in parallel (cost, contradiction, moment). Show the three angles with their hooks and let the user pick or combine. If the user said "just write it", pick the strongest, say which in one line, and continue.
4. **Examples.** From the pack's `examples/index.md`, keep the pieces with the same family and language, then the closest topics, then the most recent. Use 3 to 5, or all of them in a thin pack. Same platform is a bonus, not a requirement.
5. **Draft.** `roles/writer.md`.
6. **Lint.** Save the draft to a file and run `python3 scripts/lint.py <file> --family <f> --platform <p> --pack <pack>`. Without code execution, check the profile's lint rules by reading.
7. **Critics, in parallel:** `roles/reader.md`, `roles/voice-matcher.md`, `roles/fact-checker.md`, plus the family's `extra_critics`. Each receives only what its file says it may see.
8. **Editor.** `roles/editor.md`, mode `write`, with the lint report and all findings. One round.
9. **Re-lint** the revised version. If a high lint finding remains, fix that line only.
10. **Judge.** `roles/judge.md` on the draft and the revised version, in random order. Keep the winner.
11. **Deliver** (SKILL.md section 6). Add the signature block for this platform and language from `formats.md` if the family uses one.
