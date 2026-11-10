#!/usr/bin/env bash
# Fails if any Markdown file in the repo contains an em dash.
set -euo pipefail
cd "$(dirname "$0")/.."
if grep -rn --include='*.md' $'—' . ; then
  echo "Em dashes found. Replace them with a period, comma, colon or parentheses."
  exit 1
fi
echo "Style check passed."
