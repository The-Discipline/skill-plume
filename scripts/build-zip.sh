#!/usr/bin/env bash
# Builds dist/plume.zip for upload in the Claude app (Customize > Skills).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/plume.zip
(cd plugins/plume/skills && zip -qr ../../../dist/plume.zip plume -x '*/__pycache__/*')
echo "Built dist/plume.zip"
