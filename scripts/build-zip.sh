#!/usr/bin/env bash
# Builds dist/plume-<version>.zip and dist/plume-latest.zip for upload in the Claude app (Customize > Skills).
# The ZIP root is the skill folder. The version comes from plugins/plume/.claude-plugin/plugin.json.
set -euo pipefail
cd "$(dirname "$0")/.."
version=$(sed -n 's/.*"version": *"\([^"]*\)".*/\1/p' plugins/plume/.claude-plugin/plugin.json | head -1)
[ -n "$version" ] || { echo "No version found in plugin.json" >&2; exit 1; }
mkdir -p dist
rm -f dist/plume-*.zip
(cd plugins/plume/skills && zip -qr "../../../dist/plume-$version.zip" plume -x '*/__pycache__/*')
cp "dist/plume-$version.zip" dist/plume-latest.zip
echo "Built dist/plume-$version.zip and dist/plume-latest.zip"
