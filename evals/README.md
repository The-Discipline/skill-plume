# Evals

How to know whether a change to Plume actually helps. Dev only, never shipped in the skill.

## The metric

**Edit distance to publish:** how much the user changes Plume's draft before publishing. Computed by `diff_learn.py` (0 = published as drafted, 1 = fully rewritten, word level). Lower is better.

## The set

Build it from real history, not invented briefs:
- `briefs/<id>.md`: the brief and raw material the user had at the time
- `finals/<id>.md`: what they actually published
- 10 to 20 pieces, across the families they use most

Keep real sets out of the public repo (`packs/` and `plume-pack/` are ignored by git). Store them with the user's pack.

## The protocol

1. Run the version to test on every brief.
2. Compute the edit distance between each output and its published final.
3. Blind A/B: the user compares the old and new version's output for the same brief without knowing which is which.
4. Record results in `results.md`: version, family, mean edit distance, A/B wins.

A change ships when it lowers the edit distance or wins the A/B on most pieces, without raising either for any family.
