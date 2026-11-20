# Mode: edit

The user's own draft. The goal is a better version of their text, not a Plume text.

1. **Brief.** Infer family, platform, intent and language from the draft and the request.
2. **Profiles.** Merge as in write mode.
3. **Lint** the user's draft.
4. **Critics, in parallel:** reader, voice matcher, fact checker, plus the family's extra critics.
5. **Editor**, mode `edit`: only what a finding flags, plus typos. Keep the user's constructions, even unusual ones, unless a finding is high severity.
6. **Judge** the user's original against the edited version, in random order. If the original wins, return it with the findings as suggestions instead of applying them.
7. **Proofread.** `roles/proofreader.md` on the kept version. Apply the certain findings and tag each "proofread" in the change list. Doubtful findings are suggestions. If the original won at step 6, apply nothing: every finding goes in as a suggestion.
8. **Deliver:** the edited text, then the change list (one line per change, with the reason), so the user can reject any change.

**Proofread only.** When the user asks only to proofread, correct or check the spelling: do steps 1 and 2, run the proofreader on the draft, and deliver the corrected text with the change list. No critics, no editor, no judge.
