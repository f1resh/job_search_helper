#!/usr/bin/env python3
"""
Sync agent skills from the canonical .agents/skills/ folder to .claude/skills/.

.agents/skills/ is the single source of truth. Claude Code only discovers skills
in .claude/skills/, so this script mirrors the source folder there: it copies new
and changed files and removes files that no longer exist in the source.
"""

import sys
import argparse
import filecmp
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / ".agents" / "skills"
TARGET_DIR = REPO_ROOT / ".claude" / "skills"


def list_files(root: Path) -> set:
    if not root.exists():
        return set()
    return {p.relative_to(root) for p in root.rglob("*") if p.is_file()}


def find_differences(source: Path, target: Path):
    source_files = list_files(source)
    target_files = list_files(target)

    missing = sorted(source_files - target_files)
    extra = sorted(target_files - source_files)
    changed = sorted(
        rel for rel in source_files & target_files
        if not filecmp.cmp(source / rel, target / rel, shallow=False)
    )
    return missing, changed, extra


def sync(source: Path, target: Path) -> int:
    missing, changed, extra = find_differences(source, target)

    for rel in missing + changed:
        destination = target / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / rel, destination)
        print(f"[COPY] {rel.as_posix()}")

    for rel in extra:
        (target / rel).unlink()
        print(f"[REMOVE] {rel.as_posix()}")

    # Drop directories left empty after removals
    if target.exists():
        for directory in sorted((d for d in target.rglob("*") if d.is_dir()), reverse=True):
            if not any(directory.iterdir()):
                directory.rmdir()

    total = len(missing) + len(changed) + len(extra)
    if total == 0:
        print("[OK] .claude/skills is already in sync with .agents/skills")
    else:
        print(f"[SUCCESS] Synced {total} file(s) from .agents/skills to .claude/skills")
    return 0


def check(source: Path, target: Path) -> int:
    missing, changed, extra = find_differences(source, target)
    if not (missing or changed or extra):
        print("[OK] .claude/skills is in sync with .agents/skills")
        return 0

    for rel in missing:
        print(f"[MISSING] {rel.as_posix()}")
    for rel in changed:
        print(f"[CHANGED] {rel.as_posix()}")
    for rel in extra:
        print(f"[EXTRA] {rel.as_posix()}")
    print("[ERROR] .claude/skills is out of sync. Run: python Scripts/sync_skills.py", file=sys.stderr)
    return 1


def main():
    parser = argparse.ArgumentParser(description="Mirror .agents/skills (source) into .claude/skills.")
    parser.add_argument("--check", action="store_true", help="Only report differences; exit 1 if out of sync")
    args = parser.parse_args()

    if not SOURCE_DIR.is_dir():
        print(f"[ERROR] Source folder not found: {SOURCE_DIR}", file=sys.stderr)
        sys.exit(1)

    sys.exit(check(SOURCE_DIR, TARGET_DIR) if args.check else sync(SOURCE_DIR, TARGET_DIR))


if __name__ == "__main__":
    main()
