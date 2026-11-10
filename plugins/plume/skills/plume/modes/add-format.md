# Mode: add-format

Create a custom family or platform in the user's pack. Never improvise rules for an unknown format.

1. Ask: is it a new kind of piece (family) or a new place to publish an existing kind (platform)? Rule: if the structure differs, it is a family. If only limits and syntax differ, it is a platform.
2. Ask for 3 to 5 pieces the user published in this format, and any platform constraints they know.
3. Copy the closest shipped profile as a starting point and fill every field in `schema.md` for that kind. Leave unverified platform limits as `null`.
4. Save it to the pack's `formats/<name>.md` with `kind` set.
5. Validate with `python3 scripts/validate_pack.py <pack>`.
6. Index the example pieces with the new family or platform name.
