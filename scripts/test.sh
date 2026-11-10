#!/usr/bin/env bash
# Runs the scripts against the example pack. Fails on any error.
set -euo pipefail
cd "$(dirname "$0")/.."
S=plugins/plume/skills/plume/scripts
P=examples/pack-example
python3 -I $S/validate_pack.py $P
python3 -I $S/merge_profile.py --family post --platform linkedin --pack $P > /dev/null
for f in plugins/plume/skills/plume/families/*.md; do
  fam=$(basename "$f" .md)
  python3 -I $S/merge_profile.py --family "$fam" > /dev/null
done
for f in plugins/plume/skills/plume/platforms/*.md; do
  python3 -I -c "import sys; sys.path.insert(0,'$S'); import plume_yaml; d,_=plume_yaml.read('$f'); assert d['kind']=='platform', '$f'"
done
python3 -I $S/lint.py examples/test-draft.txt --family post --platform linkedin --pack $P
python3 -I $S/diff_learn.py examples/test-draft.txt $P/examples/2026-09-onboarding.md > /dev/null
echo "All script tests passed."
