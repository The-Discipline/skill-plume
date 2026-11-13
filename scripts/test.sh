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
# New checks must fire: specificity on a generic text, stock words and invisible characters
python3 -I $S/lint.py examples/test-generic.txt --family post | grep -q "specificity" || { echo "specificity check did not fire"; exit 1; }
printf 'We leveraged a seamless\xe2\x80\x8b synergy.\n' > /tmp/plume-test.txt
python3 -I $S/lint.py /tmp/plume-test.txt --family message | grep -q "invisible_char" || { echo "invisible character check did not fire"; exit 1; }
python3 -I $S/lint.py /tmp/plume-test.txt --family message | grep -q "stock_word" || { echo "stock word check did not fire"; exit 1; }
# Glyphs: the pack's marker is enforced, fake bold is high unless the pack opts in
printf 'Two points:\n\n\xe2\x96\xb8 first \xe2\x9c\x93\n\xe2\x80\xa2 second\n' > /tmp/plume-glyphs.txt
python3 -I $S/lint.py /tmp/plume-glyphs.txt --family post --platform linkedin --pack $P | grep -q "your marker is" || { echo "list marker check did not fire"; exit 1; }
python3 -I $S/lint.py /tmp/plume-glyphs.txt --family post --platform linkedin --pack $P | grep -q "glyph" && { echo "allowed glyph was flagged"; exit 1; }
printf 'A \xf0\x9d\x97\xaf\xf0\x9d\x97\xbc\xf0\x9d\x97\xb9\xf0\x9d\x97\xb1 word here.\n' > /tmp/plume-bold.txt
python3 -I $S/lint.py /tmp/plume-bold.txt --family post | grep -q "\[high\] fake_bold" || { echo "fake bold not high by default"; exit 1; }
python3 -I $S/merge_profile.py --family post > /tmp/plume-prof.json
python3 -I -c "import json; p=json.load(open('/tmp/plume-prof.json')); p['glyphs']['fake_bold']='allow'; json.dump(p, open('/tmp/plume-prof.json','w'))"
python3 -I $S/lint.py /tmp/plume-bold.txt --profile /tmp/plume-prof.json | grep -q "\[low\] fake_bold" || { echo "fake bold opt-in not applied"; exit 1; }
python3 -I $S/lint.py $P/examples/2026-08-bio.md --family bio --platform linkedin --pack $P > /dev/null
python3 -I $S/diff_learn.py examples/test-draft.txt $P/examples/2026-09-onboarding.md > /dev/null
echo "All script tests passed."
