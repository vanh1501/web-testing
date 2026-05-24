#!/usr/bin/env python3
"""
Micro-Healer: HPRF Injector (SHP-06)
======================================
Scans .agents/rules/**/*.md and injects the HPRF Override Priority
block immediately after YAML frontmatter (or at the top if none).
Idempotent — skips files that already have the block.
"""

import re
import sys
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

HPRF_PATTERN = re.compile(r'>\s*\[!IMPORTANT\]\s*Override Priority:', re.IGNORECASE)
SKIP_FILES = {'README.md', 'CHANGELOG.md'}

# Tier classification heuristics
TIER_1_KEYWORDS = ['constitution', 'protocol', 'global', 'safety', 'guardrail', 'memory-contract']
TIER_2_KEYWORDS = ['orchestration', 'coordinator', 'standards', 'governance', 'worker-roles']
# Default to Tier 3 for domain/input rules


def classify_tier(filename: str, content: str) -> int:
    name_lower = filename.lower()
    content_lower = content[:500].lower()
    
    for kw in TIER_1_KEYWORDS:
        if kw in name_lower or kw in content_lower:
            return 1
    for kw in TIER_2_KEYWORDS:
        if kw in name_lower or kw in content_lower:
            return 2
    return 3


def inject_hprf(filepath: Path) -> bool:
    content = filepath.read_text(encoding='utf-8')
    
    if HPRF_PATTERN.search(content):
        return False  # Already has HPRF
    
    tier = classify_tier(filepath.name, content)
    hprf_block = f'> [!IMPORTANT] Override Priority: Tier {tier}\n\n'
    
    # Insert after YAML frontmatter if present
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            new_content = parts[0] + '---' + parts[1] + '---\n\n' + hprf_block + parts[2].lstrip()
        else:
            new_content = hprf_block + content
    else:
        new_content = hprf_block + content
    
    filepath.write_text(new_content, encoding='utf-8')
    return True


def heal_hprf(workspace_path: str) -> list:
    ws = Path(workspace_path).resolve()
    rules_dir = ws / '.agent' / 'rules'
    
    if not rules_dir.exists():
        print("  ⚠️ No .agents/rules/ directory found.")
        return []
    
    injected = []
    for md_file in rules_dir.rglob('*.md'):
        if md_file.name in SKIP_FILES:
            continue
        if inject_hprf(md_file):
            tier = classify_tier(md_file.name, md_file.read_text(encoding='utf-8'))
            injected.append({"file": md_file.name, "tier": tier})
            print(f"  ✅ Injected Tier {tier} HPRF into {md_file.relative_to(ws)}")
    
    if not injected:
        print("  ✅ All rules already have HPRF blocks.")
    return injected


if __name__ == '__main__':
    ws = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(f"=== SHP-06: HPRF Injector Healer ===")
    heal_hprf(ws)
