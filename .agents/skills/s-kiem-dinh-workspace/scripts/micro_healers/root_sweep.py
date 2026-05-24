#!/usr/bin/env python3
"""
Micro-Healer: Root Sweep (SHP-24)
==================================
Moves floating operational files from workspace root to tmp/.
Idempotent — safe to re-run.
"""

import os
import shutil
import sys
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

CONSTITUTIONAL_FILES = {
    'README.md', '.agents/agents.md', 'PROJECT.md', 'QUALITY-LOG.md',
    'ONBOARDING.md', 'IMPROVEMENT-BACKLOG.md',
    '.gitignore',
}
FLOATING_EXTENSIONS = {'.py', '.sh', '.csv', '.json', '.log', '.txt', '.bat', '.ps1'}


def heal_root_sweep(workspace_path: str) -> list:
    ws = Path(workspace_path).resolve()
    tmp = ws / 'tmp'
    tmp.mkdir(exist_ok=True)

    moved = []
    for item in ws.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            if ext in FLOATING_EXTENSIONS and item.name not in CONSTITUTIONAL_FILES:
                dest = tmp / item.name
                shutil.move(str(item), str(dest))
                moved.append({"from": item.name, "to": f"tmp/{item.name}"})
                print(f"  ✅ Moved {item.name} → tmp/{item.name}")
    
    if not moved:
        print("  ✅ Root is clean. Nothing to move.")
    return moved


if __name__ == '__main__':
    ws = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(f"=== SHP-24: Root Sweep Healer ===")
    heal_root_sweep(ws)
