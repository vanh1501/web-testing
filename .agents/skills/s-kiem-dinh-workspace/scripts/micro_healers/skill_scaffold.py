#!/usr/bin/env python3
"""
Micro-Healer: Skill Scaffold (SHP-26)
=======================================
Ensures every skill folder in .agents/skills/ has the canonical 4-Tier
subdirectory structure: assets/, references/, evals/, scripts/.
Creates missing directories with .gitkeep placeholders.
Idempotent — safe to re-run.
"""

import sys
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

REQUIRED_SUBDIRS = ['assets', 'references', 'evals', 'scripts']


def heal_skill_scaffold(workspace_path: str) -> list:
    ws = Path(workspace_path).resolve()
    skills_dir = ws / '.agent' / 'skills'

    if not skills_dir.exists():
        print("  ⚠️ No .agents/skills/ directory found.")
        return []

    healed = []
    for skill_folder in sorted(skills_dir.iterdir()):
        if not skill_folder.is_dir():
            continue
        # Only process folders that have a SKILL.md
        if not (skill_folder / 'SKILL.md').exists():
            continue

        created = []
        for subdir in REQUIRED_SUBDIRS:
            target = skill_folder / subdir
            if not target.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                gitkeep = target / '.gitkeep'
                gitkeep.touch()
                created.append(subdir)

        if created:
            healed.append({"skill": skill_folder.name, "created": created})
            print(f"  ✅ {skill_folder.name}: created {', '.join(created)}")

    if not healed:
        print("  ✅ All skills have complete 4-Tier structure.")
    return healed


if __name__ == '__main__':
    ws = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(f"=== SHP-26: Skill Scaffold Healer ===")
    heal_skill_scaffold(ws)
