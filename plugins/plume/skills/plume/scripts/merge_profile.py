"""Merge a family profile, a platform profile and the user's overrides.

Usage (from the skill folder):
  python3 scripts/merge_profile.py --family post --platform linkedin --pack /path/to/plume-pack

Prints the merged profile as JSON. Warnings list ignored or rejected overrides.
"""
import argparse
import copy
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plume_yaml  # noqa: E402

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_schema():
    data, _ = plume_yaml.read(os.path.join(SKILL_DIR, "schema.md"))
    return data


def deep_merge(base, over, locked, forbidden, warnings, path="", top=True):
    out = copy.deepcopy(base)
    for key, val in (over or {}).items():
        append = key.endswith("+")
        name = key[:-1] if append else key
        where = f"{path}{name}"
        if top and name in locked:
            warnings.append(f"ignored locked field '{where}'")
            continue
        if name in forbidden:
            warnings.append(f"rejected forbidden field '{where}' (voice lives in voice.md)")
            continue
        if append:
            current = out.get(name) or []
            extra = val if isinstance(val, list) else [val]
            out[name] = list(current) + list(extra)
        elif isinstance(val, dict) and isinstance(out.get(name), dict):
            out[name] = deep_merge(out[name], val, locked, forbidden, warnings, where + ".", top=False)
        else:
            out[name] = copy.deepcopy(val)
    return out


def find_profile(kind, name, pack):
    """User's custom profile wins over the shipped one with the same name."""
    if pack:
        custom = os.path.join(pack, "formats", f"{name}.md")
        if os.path.exists(custom):
            data, body = plume_yaml.read(custom)
            if data.get("kind") == kind:
                return data, body, custom
    shipped = os.path.join(SKILL_DIR, "families" if kind == "family" else "platforms", f"{name}.md")
    if os.path.exists(shipped):
        data, body = plume_yaml.read(shipped)
        return data, body, shipped
    return None, None, None


def merge(family, platform=None, pack=None):
    schema = load_schema()
    locked = set(schema.get("locked") or [])
    forbidden = set(schema.get("forbidden") or [])
    warnings = []

    fam, _, fam_src = find_profile("family", family, pack)
    if fam is None:
        raise SystemExit(f"unknown family '{family}'. Shipped: {', '.join(sorted(os.listdir(os.path.join(SKILL_DIR, 'families'))))}")
    plat, plat_src = None, None
    if platform:
        plat, _, plat_src = find_profile("platform", platform, pack)
        if plat is None:
            warnings.append(f"unknown platform '{platform}', using family rules only")

    overrides = {}
    if pack and os.path.exists(os.path.join(pack, "formats.md")):
        overrides, _ = plume_yaml.read(os.path.join(pack, "formats.md"))

    for name, prof in (("family", fam), ("platform", plat)):
        for bad in forbidden & set((prof or {}).keys()):
            warnings.append(f"{name} profile contains forbidden field '{bad}', ignored")
            prof.pop(bad, None)

    fam_default_lint = copy.deepcopy(fam.get("lint") or {})
    plat_default_lint = copy.deepcopy((plat or {}).get("lint") or {})
    fam_over = (overrides.get("families") or {}).get(family) or {}
    fam = deep_merge(fam, fam_over, locked, forbidden, warnings, f"families.{family}.")
    plat_over = {}
    if plat:
        plat_over = (overrides.get("platforms") or {}).get(platform) or {}
        plat = deep_merge(plat, plat_over, locked, forbidden, warnings, f"platforms.{platform}.")
        if plat.get("families") and family not in plat["families"]:
            warnings.append(f"platform '{platform}' does not list family '{family}'")

    # Lint precedence: engine < family default < platform default
    #   < user family override < user platform override < user global lint
    quiet = []
    lint = copy.deepcopy(schema.get("engine_lint") or {})
    for layer in (fam_default_lint, plat_default_lint, fam_over.get("lint") or {},
                  plat_over.get("lint") or {}, overrides.get("lint") or {}):
        lint = deep_merge(lint, layer, set(), forbidden, quiet, "lint.", top=False)
    warnings.extend(w for w in quiet if w not in warnings)
    # Engine bans can be extended, never removed.
    engine_chars = set((schema.get("engine_lint") or {}).get("banned_chars") or [])
    missing = engine_chars - set(lint.get("banned_chars") or [])
    if missing:
        lint["banned_chars"] = list(lint.get("banned_chars") or []) + sorted(missing)
        warnings.append("engine banned characters restored (they cannot be removed)")

    enabled_f = overrides.get("enabled_families")
    if enabled_f and family not in enabled_f:
        warnings.append(f"family '{family}' is not in the user's enabled_families")
    enabled_p = overrides.get("enabled_platforms")
    if platform and enabled_p and platform not in enabled_p:
        warnings.append(f"platform '{platform}' is not in the user's enabled_platforms")

    signatures = overrides.get("signatures") or {}
    return {
        "family": fam,
        "platform": plat,
        "lint": lint,
        "signatures": signatures,
        "sources": {"family": fam_src, "platform": plat_src, "pack": pack},
        "warnings": warnings,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--family", required=True)
    ap.add_argument("--platform")
    ap.add_argument("--pack")
    args = ap.parse_args()
    print(json.dumps(merge(args.family, args.platform, args.pack), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
