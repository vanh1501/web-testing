#!/usr/bin/env python3
"""
MAS 4.0 Structural Pre-Scanner (Phase 0)
=========================================
Deterministic, non-LLM heuristic scanner for MAS workspace compliance.
Executes 6 physical checks in ~0.5s and outputs machine-readable JSON.

Usage:
    python structural_scanner.py [workspace_path] [--fix]

    --fix   : Auto-execute micro-healers for auto_fixable findings.

Output:
    structural_scan_report.json  (written to workspace tmp/)
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Fix Windows console encoding for emoji output
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')



# ─── Configuration ───────────────────────────────────────────────────────────

# NOTE: CONSTITUTIONAL_EXTENSIONS and CONSTITUTIONAL_FILES removed (dead code since v2.1).
# Root sweep now uses CANONICAL_ROOT_FILES exclusively.
CONSTITUTIONAL_DIRS = {
    '.agent', '.agents', '.cache', '.context', '.git', 'KB',
    'client_workspaces', 'local_datawarehouse', 'managed_workspaces',
    'output', 'outputs', 'tmp', 'setup_folder', 'courses', 'workspace-spec'
}
# Canonical 5-Zone set for child workspaces (strict mode)
CANONICAL_5ZONE = {'.agents', 'KB', 'courses', 'tmp', 'workspace-spec', 'Bang-Dieu-Khien', 'Du-An', 'Kho-Du-Lieu', 'So-Tay', 'Quan-Tri', 'scripts'}
CANONICAL_ROOT_FILES = {
    'AGENTS.md', 'GEMINI.md', 'README.md', 'QUALITY-LOG.md',
    'IMPROVEMENT-BACKLOG.md', 'progress.md', 'state.json',
    '.gitignore', 'ONBOARDING.md', 'PROJECT.md',
    'CENTRAL_REGISTRY.md', '.package-manifest.json'
}
FLOATING_EXTENSIONS = {'.md', '.yml', '.yaml', '.py', '.sh', '.csv', '.json', '.log', '.txt', '.bat', '.ps1'}
SKILL_SUBDIRS = {'assets', 'references', 'evals', 'scripts'}
HPRF_PATTERN = re.compile(r'>\s*\[!IMPORTANT\]\s*Override Priority:', re.IGNORECASE)
LINKED_SKILLS_PATTERN = re.compile(r'\[\[Linked Skills\]\]', re.IGNORECASE)
UNRENDERED_TEMPLATE_PATTERN = re.compile(r'(\{\{[A-Z0-9_]+\}\}|\[workspace root directory\])')

# ─── Scanner Functions ───────────────────────────────────────────────────────

def scan_root_sweep(ws: Path) -> list:
    """EC-1: Detect operational files floating at workspace root."""
    findings = []
    for item in ws.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            name = item.name
            if ext in FLOATING_EXTENSIONS and name not in CANONICAL_ROOT_FILES:
                findings.append({
                    "id": f"EC-1-{name}",
                    "severity": "SYSTEMIC-HALT",
                    "category": "ROOT_SWEEP",
                    "detail": f"Floating operational file at root: {name}",
                    "file": str(item.relative_to(ws)),
                    "auto_fixable": True,
                    "fix_pattern": "SHP-24",
                })
    return findings


def scan_hprf_check(ws: Path) -> list:
    """EC-2: Detect rule files missing HPRF Override Priority preamble."""
    findings = []
    rules_dir = ws / '.agents' / 'rules'
    if not rules_dir.exists():
        return findings

    for md_file in rules_dir.rglob('*.md'):
        if md_file.name == 'README.md' or md_file.name == 'CHANGELOG.md':
            continue
        try:
            content = md_file.read_text(encoding='utf-8')
            if not HPRF_PATTERN.search(content):
                findings.append({
                    "id": f"EC-2-{md_file.name}",
                    "severity": "LOCAL-FIX",
                    "category": "HPRF_CHECK",
                    "detail": f"Missing HPRF Override Priority block: {md_file.name}",
                    "file": str(md_file.relative_to(ws)),
                    "auto_fixable": True,
                    "fix_pattern": "SHP-06",
                })
        except Exception:
            pass
    return findings


def scan_skill_4tier(ws: Path) -> list:
    """EC-3: Detect skill folders missing canonical 4-Tier subdirectories."""
    findings = []
    skills_dir = ws / '.agents' / 'skills'
    if not skills_dir.exists():
        return findings

    for skill_folder in skills_dir.iterdir():
        if not skill_folder.is_dir():
            continue
        skill_md = skill_folder / 'SKILL.md'
        if not skill_md.exists():
            continue  # No SKILL.md = different problem (handled by CQS)

        missing = []
        for subdir in SKILL_SUBDIRS:
            if not (skill_folder / subdir).is_dir():
                missing.append(subdir)

        if missing:
            findings.append({
                "id": f"EC-3-{skill_folder.name}",
                "severity": "LOCAL-FIX",
                "category": "SKILL_4TIER",
                "detail": f"Skill '{skill_folder.name}' missing subdirs: {', '.join(missing)}",
                "file": str(skill_folder.relative_to(ws)),
                "missing_dirs": missing,
                "auto_fixable": True,
                "fix_pattern": "SHP-26",
            })
    return findings


def scan_skill_skeleton(ws: Path) -> list:
    """EC-13: Detect skeleton skills by SKILL.md file size.
    
    Two-tier threshold:
    - < 1KB  (1024 bytes): SYSTEMIC-HALT — empty shell, unusable.
    - < 10KB (10240 bytes): LOCAL-FIX — under-developed, needs enrichment.
    """
    findings = []
    skills_dir = ws / '.agents' / 'skills'
    if not skills_dir.exists():
        return findings

    SKELETON_HARD = 1024      # 1 KB — empty shell
    SKELETON_SOFT = 10240     # 10 KB — under-developed

    for skill_folder in skills_dir.iterdir():
        if not skill_folder.is_dir():
            continue
        if skill_folder.name.startswith('_'):
            continue  # Skip _archive, _deprecated, etc.
        skill_md = skill_folder / 'SKILL.md'
        if not skill_md.exists():
            findings.append({
                "id": f"EC-13-{skill_folder.name}-missing",
                "severity": "SYSTEMIC-HALT",
                "category": "SKILL_SKELETON",
                "detail": f"Skill '{skill_folder.name}' has no SKILL.md at all",
                "file": str(skill_folder.relative_to(ws)),
                "auto_fixable": False,
                "fix_pattern": "SHP-23",
                "manual_reason": "Must create SKILL.md with domain content via skill-writer Route 1",
            })
            continue

        size = skill_md.stat().st_size
        if size < SKELETON_HARD:
            findings.append({
                "id": f"EC-13-{skill_folder.name}-hard",
                "severity": "SYSTEMIC-HALT",
                "category": "SKILL_SKELETON",
                "detail": f"Skill '{skill_folder.name}' SKILL.md is {size} bytes (< 1KB) — empty shell",
                "file": str(skill_md.relative_to(ws)),
                "size_bytes": size,
                "threshold": SKELETON_HARD,
                "auto_fixable": False,
                "fix_pattern": "SHP-23",
                "manual_reason": "Skeleton too small to repair — rebuild via skill-writer Route 3 (ADDIE)",
            })
        elif size < SKELETON_SOFT:
            findings.append({
                "id": f"EC-13-{skill_folder.name}-soft",
                "severity": "LOCAL-FIX",
                "category": "SKILL_SKELETON",
                "detail": f"Skill '{skill_folder.name}' SKILL.md is {size} bytes ({size/1024:.1f}KB < 10KB) — under-developed",
                "file": str(skill_md.relative_to(ws)),
                "size_bytes": size,
                "threshold": SKELETON_SOFT,
                "auto_fixable": False,
                "fix_pattern": "SHP-23",
                "manual_reason": "Needs enrichment via skill-writer Route 3 (ADDIE) — add domain references, decision rules, guardrails",
            })
    return findings


def scan_agent_locks(ws: Path) -> list:
    """EC-5: Detect Agent SIs missing [[Linked Skills]] epistemic lock.
    
    MAS 5.0 Folder-Based Architecture:
        INDEX.md  = Master dispatcher (entry point, calls sub-files)
        IDENTITY.md = Identity sub-module (loaded by INDEX)
        SOUL.md   = Personality sub-module (loaded by INDEX)
        RULES.md  = Operations + Epistemic Locks (the ONLY file that must carry locks)
    
    Therefore: Only RULES.md is checked for [[Linked Skills]].
    """
    findings = []
    agents_dir = ws / '.agents' / 'agents'
    if not agents_dir.exists():
        return findings

    # Scan each Agent folder for its RULES.md (the sole carrier of Epistemic Locks)
    for agent_folder in agents_dir.iterdir():
        if not agent_folder.is_dir():
            continue
        rules_file = agent_folder / 'RULES.md'
        if not rules_file.exists():
            # Missing RULES.md entirely = critical finding
            findings.append({
                "id": f"EC-5-{agent_folder.name}",
                "severity": "LOCAL-FIX",
                "category": "AGENT_LOCKS",
                "detail": f"Agent '{agent_folder.name}' missing RULES.md entirely",
                "file": str(agent_folder.relative_to(ws)),
                "auto_fixable": False,
                "fix_pattern": "SHP-11",
                "manual_reason": "Agent folder exists but has no RULES.md — rebuild via factory",
            })
            continue
        try:
            content = rules_file.read_text(encoding='utf-8')
            if not LINKED_SKILLS_PATTERN.search(content):
                findings.append({
                    "id": f"EC-5-{agent_folder.name}",
                    "severity": "LOCAL-FIX",
                    "category": "AGENT_LOCKS",
                    "detail": f"Agent '{agent_folder.name}' RULES.md missing [[Linked Skills]] lock",
                    "file": str(rules_file.relative_to(ws)),
                    "auto_fixable": False,
                    "fix_pattern": "SHP-11",
                    "manual_reason": "Requires semantic analysis to determine correct skill list",
                })
        except Exception:
            pass
    return findings


def scan_ghost_skills(ws: Path) -> list:
    """EC-4 variant: Detect skills not referenced by any agent or workflow."""
    findings = []
    skills_dir = ws / '.agents' / 'skills'
    agents_dir = ws / '.agents' / 'agents'
    workflows_dir = ws / '.agents' / 'workflows'

    if not skills_dir.exists():
        return findings

    # Build corpus of all text in agents + workflows
    corpus = ""
    for search_dir in [agents_dir, workflows_dir]:
        if search_dir and search_dir.exists():
            for md_file in search_dir.rglob('*.md'):
                try:
                    corpus += md_file.read_text(encoding='utf-8')
                except Exception:
                    pass
    # Also include L1-swarm-registry.md or agents.md at root
    registry_files = [ws / '.agents' / 'rules' / 'L1-swarm-registry.md', ws / '.agents' / 'agents.md']
    for reg in registry_files:
        if reg.exists():
            try:
                corpus += reg.read_text(encoding='utf-8')
            except Exception:
                pass

    for skill_folder in skills_dir.iterdir():
        if not skill_folder.is_dir():
            continue
        skill_name = skill_folder.name
        if skill_name not in corpus:
            findings.append({
                "id": f"EC-4-{skill_name}",
                "severity": "LOCAL-FIX",
                "category": "GHOST_SKILL",
                "detail": f"Ghost skill (unwired): {skill_name}",
                "file": str(skill_folder.relative_to(ws)),
                "auto_fixable": False,
                "fix_pattern": "SHP-11",
                "manual_reason": "Requires semantic analysis to find the best agent/workflow host",
            })
    return findings


def scan_agent_pollution(ws: Path) -> list:
    """EC-6: Detect stray agent files at .agents/agents/ root (not in tier subdirs)."""
    findings = []
    agents_dir = ws / '.agents' / 'agents'
    if not agents_dir.exists():
        return findings

    # Read .agents/agents.md to build known roster
    agents_md = ws / '.agents/agents.md'
    known_agents = set()
    if agents_md.exists():
        try:
            content = agents_md.read_text(encoding='utf-8')
            known_agents = set(re.findall(r'\b(GOV-\w+)\b', content))
        except Exception:
            pass

    # Check files directly in agents/ root (not in tier subdirs)
    tier_subdirs = {'tier_2_orchestrator', 'tier_3_worker', 'tier_4_specialist_agent'}
    for item in agents_dir.iterdir():
        if item.is_file() and item.suffix == '.md' and item.name != 'README.md':
            # This file is at agents/ root — likely pollution
            stem = item.stem
            # Check if it's a known GOV- agent that just needs relocating
            is_known = any(stem.upper().startswith(prefix) for prefix in ['GOV-'])
            findings.append({
                "id": f"EC-6-{item.name}",
                "severity": "SYSTEMIC-HALT",
                "category": "AGENT_POLLUTION",
                "detail": f"Agent file at agents/ root (not in tier subdir): {item.name}",
                "file": str(item.relative_to(ws)),
                "auto_fixable": False,
                "fix_pattern": "SHP-25",
                "manual_reason": "Requires Human to confirm origin workspace and correct placement",
            })
    return findings


def scan_namespace_check(ws: Path) -> list:
    """EC-7: Detect wrong namespace (.agent instead of .agents)."""
    findings = []
    wrong_ns = ws / '.agent'
    correct_ns = ws / '.agents'
    if wrong_ns.exists() and wrong_ns.is_dir():
        findings.append({
            "id": "EC-7-namespace",
            "severity": "SYSTEMIC-HALT",
            "category": "NAMESPACE_CHECK",
            "detail": "Wrong namespace: '.agent' exists (should be '.agents')",
            "file": ".agent",
            "auto_fixable": True,
            "fix_pattern": "SHP-30",
        })
    if not correct_ns.exists():
        findings.append({
            "id": "EC-7-missing-agents",
            "severity": "SYSTEMIC-HALT",
            "category": "NAMESPACE_CHECK",
            "detail": "Missing '.agents' directory entirely",
            "file": "(root)",
            "auto_fixable": False,
            "fix_pattern": "SHP-30",
            "manual_reason": "Workspace may not be initialized",
        })
    return findings


def scan_orphan_zones(ws: Path) -> list:
    """EC-8: Detect root-level folders not in the canonical 5-Zone set or Zone 6 (Domain Extension Zones)."""
    findings = []
    
    # Load Domain Extension Zones (Zone 6)
    allowed_zones = set()
    zones_file = ws / '.context' / 'allowed-zones.json'
    if zones_file.exists():
        try:
            data = json.loads(zones_file.read_text(encoding='utf-8'))
            if isinstance(data, list):
                allowed_zones = set(data)
            elif isinstance(data, dict) and "allowed_zones" in data:
                allowed_zones = set(data["allowed_zones"])
        except Exception:
            pass

    combined_canonical = CANONICAL_5ZONE | CONSTITUTIONAL_DIRS | allowed_zones

    for item in ws.iterdir():
        if item.is_dir():
            name = item.name
            if name.startswith('.') and name not in ('.agents', '.git', '.cache', '.context'):
                findings.append({
                    "id": f"EC-8-{name}",
                    "severity": "LOCAL-FIX",
                    "category": "ORPHAN_ZONE",
                    "detail": f"Non-canonical hidden dir at root: {name}",
                    "file": name,
                    "auto_fixable": False,
                    "fix_pattern": "SHP-31",
                    "manual_reason": "Confirm if contents should merge into KB/ or be archived to tmp/_archive/",
                })
            elif not name.startswith('.') and name not in combined_canonical:
                findings.append({
                    "id": f"EC-8-{name}",
                    "severity": "LOCAL-FIX",
                    "category": "ORPHAN_ZONE",
                    "detail": f"Non-canonical folder at root: {name} (not in 5-Zone)",
                    "file": name,
                    "auto_fixable": False,
                    "fix_pattern": "SHP-31",
                    "manual_reason": "Confirm merge target (KB/, courses/, tmp/_archive/) with Human",
                })
    return findings


def scan_empty_dirs(ws: Path) -> list:
    """EC-9: Detect empty directories at any level (excluding tmp/)."""
    findings = []
    for root, dirs, files in os.walk(ws):
        root_path = Path(root)
        rel = root_path.relative_to(ws)
        # Skip tmp, _archive, .git
        parts = rel.parts
        if any(p in ('tmp', '_archive', '.git', '.cache') for p in parts):
            continue
        if not dirs and not files:
            findings.append({
                "id": f"EC-9-{str(rel).replace(os.sep, '_')}",
                "severity": "LOCAL-FIX",
                "category": "EMPTY_DIR",
                "detail": f"Empty directory: {rel}",
                "file": str(rel),
                "auto_fixable": True,
                "fix_pattern": "SHP-32",
            })
    return findings

def scan_mandatory_files(ws: Path) -> list:
    """EC-10: Verify mandatory baseline files exist at their canonical locations."""
    findings = []
    mandatory = {
        'AGENTS.md': ws / 'AGENTS.md',
        'GEMINI.md': ws / 'GEMINI.md',
        'progress.md': ws / 'progress.md',
        'README.md': ws / 'README.md',
    }
    for name, path in mandatory.items():
        if not path.exists():
            findings.append({
                "id": f"EC-10-{name}",
                "severity": "SYSTEMIC-HALT",
                "category": "MANDATORY_FILES",
                "detail": f"Missing mandatory baseline file: {name}",
                "file": str(path.relative_to(ws)),
                "auto_fixable": False,
                "fix_pattern": "SHP-33",
                "manual_reason": "File must be created with correct domain content",
            })
    # Check .agents/rules/ has at least 1 L0 file
    rules_dir = ws / '.agents' / 'rules'
    if rules_dir.exists():
        l0_files = [f for f in rules_dir.iterdir() if f.is_file() and f.name.lower().startswith('l0')]
        if len(l0_files) == 0:
            findings.append({
                "id": "EC-10-L0-rules",
                "severity": "SYSTEMIC-HALT",
                "category": "MANDATORY_FILES",
                "detail": "No L0 governance rule files found in .agents/rules/",
                "file": ".agents/rules/",
                "auto_fixable": False,
                "fix_pattern": "SHP-33",
                "manual_reason": "L0 rules must be created via rules skill Route 1",
            })
    else:
        findings.append({
            "id": "EC-10-rules-dir",
            "severity": "SYSTEMIC-HALT",
            "category": "MANDATORY_FILES",
            "detail": "Missing .agents/rules/ directory entirely",
            "file": ".agents/rules/",
            "auto_fixable": True,
            "fix_pattern": "SHP-26",
        })
    return findings


def scan_broken_references(ws: Path) -> list:
    """EC-11: Detect broken file path references in GEMINI.md and AGENTS.md."""
    findings = []
    ref_pattern = re.compile(r'(?:file:///|🔗\s*`?file:///)?([\w.\-/]+\.(?:md|yml|yaml|json))', re.IGNORECASE)
    root_files = ['GEMINI.md', 'AGENTS.md']
    for rf_name in root_files:
        rf_path = ws / rf_name
        if not rf_path.exists():
            continue
        try:
            content = rf_path.read_text(encoding='utf-8')
            refs = ref_pattern.findall(content)
            for ref in refs:
                ref_clean = ref.strip('`').strip()
                # Skip absolute paths, URLs, and Master Repo refs
                if ref_clean.startswith('http') or ref_clean.startswith('d:') or ref_clean.startswith('C:'):
                    continue
                target = ws / ref_clean
                if not target.exists():
                    findings.append({
                        "id": f"EC-11-{rf_name}-{Path(ref_clean).name}",
                        "severity": "LOCAL-FIX",
                        "category": "BROKEN_REF",
                        "detail": f"{rf_name} references non-existent file: {ref_clean}",
                        "file": rf_name,
                        "auto_fixable": False,
                        "fix_pattern": "SHP-34",
                        "manual_reason": f"Update reference in {rf_name} to correct path",
                    })
        except Exception:
            pass
    return findings


def scan_unrendered_templates(ws: Path) -> list:
    """EC-12: Detect unrendered template variables like {{WORKSPACE_NAME}} or [workspace root directory]."""
    findings = []
    
    # Check AGENTS.md, GEMINI.md
    for root_file in ['AGENTS.md', 'GEMINI.md']:
        rf_path = ws / root_file
        if rf_path.exists():
            try:
                content = rf_path.read_text(encoding='utf-8')
                matches = UNRENDERED_TEMPLATE_PATTERN.findall(content)
                if matches:
                    findings.append({
                        "id": f"EC-12-{root_file}",
                        "severity": "SYSTEMIC-HALT",
                        "category": "TEMPLATE_CHECK",
                        "detail": f"Unrendered template variable '{matches[0]}' found in {root_file}",
                        "file": root_file,
                        "auto_fixable": False,
                        "fix_pattern": "SHP-00",
                        "manual_reason": "Run session-manager or script to inject correct workspace metadata",
                    })
            except Exception:
                pass

    # Check files inside .agents/workflows and .agents/rules
    for search_dir in [ws / '.agents' / 'workflows', ws / '.agents' / 'rules']:
        if search_dir.exists():
            for md_file in search_dir.rglob('*.md'):
                try:
                    content = md_file.read_text(encoding='utf-8')
                    matches = UNRENDERED_TEMPLATE_PATTERN.findall(content)
                    if matches:
                        findings.append({
                            "id": f"EC-12-{md_file.name}",
                            "severity": "SYSTEMIC-HALT",
                            "category": "TEMPLATE_CHECK",
                            "detail": f"Unrendered template variable '{matches[0]}' found in {md_file.name}",
                            "file": str(md_file.relative_to(ws)),
                            "auto_fixable": False,
                            "fix_pattern": "SHP-00",
                            "manual_reason": "Run session-manager or script to inject correct workspace metadata",
                        })
                except Exception:
                    pass

    return findings



def scan_workflow_metadata(ws: Path) -> list:
    """EC-7: Detect workflows missing YAML metadata (description, semantic_triggers)."""
    findings = []
    workflows_dir = ws / '.agents' / 'workflows'
    if not workflows_dir.exists():
        return findings

    for md_file in workflows_dir.rglob('*.md'):
        try:
            text = md_file.read_text(encoding='utf-8')
            has_yaml = text.startswith('---')
            has_desc = re.search(r'^description:', text, re.MULTILINE)
            has_triggers = re.search(r'^semantic_triggers:', text, re.MULTILINE)
            
            if not has_yaml or not has_desc or not has_triggers:
                findings.append({
                    "id": f"EC-7-{md_file.name}",
                    "severity": "LOCAL-FIX",
                    "category": "WF_METADATA_CHECK",
                    "detail": f"Workflow missing YAML metadata (description/triggers): {md_file.name}",
                    "file": str(md_file.relative_to(ws)),
                    "auto_fixable": True,
                    "fix_pattern": "SHP-WF01",
                    "manual_reason": "Run inject_wf_metadata.py script to auto-heal",
                })
        except Exception:
            pass

    return findings


# ─── Main Orchestrator ───────────────────────────────────────────────────────

def run_full_scan(workspace_path: str) -> dict:
    """Execute all 9 heuristic scans and produce a structured report."""
    ws = Path(workspace_path).resolve()

    if not ws.exists():
        print(f"ERROR: Workspace path does not exist: {ws}")
        sys.exit(1)

    all_findings = []
    scan_functions = [
        ("NAMESPACE_CHECK", scan_namespace_check),
        ("ORPHAN_ZONE", scan_orphan_zones),
        ("EMPTY_DIR", scan_empty_dirs),
        ("ROOT_SWEEP", scan_root_sweep),
        ("MANDATORY_FILES", scan_mandatory_files),
        ("BROKEN_REF", scan_broken_references),
        ("HPRF_CHECK", scan_hprf_check),
        ("SKILL_4TIER", scan_skill_4tier),
        ("SKILL_SKELETON", scan_skill_skeleton),
        ("AGENT_LOCKS", scan_agent_locks),
        ("GHOST_SKILL", scan_ghost_skills),
        ("AGENT_POLLUTION", scan_agent_pollution),
        ("TEMPLATE_CHECK", scan_unrendered_templates),
        ("WF_METADATA", scan_workflow_metadata),
    ]

    print(f"=== MAS Structural Pre-Scanner (v2.3.0) ===")
    print(f"Target: {ws}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    for scan_name, scan_fn in scan_functions:
        findings = scan_fn(ws)
        status = "PASS" if len(findings) == 0 else f"FAIL ({len(findings)} issues)"
        icon = "✅" if len(findings) == 0 else "🔴"
        print(f"  {icon} {scan_name}: {status}")
        all_findings.extend(findings)

    # Build summary
    systemic = sum(1 for f in all_findings if f["severity"] == "SYSTEMIC-HALT")
    local = sum(1 for f in all_findings if f["severity"] == "LOCAL-FIX")

    report = {
        "scan_date": datetime.now().strftime('%Y-%m-%d'),
        "scan_time": datetime.now().strftime('%H:%M:%S'),
        "workspace_path": str(ws),
        "scanner_version": "2.2.0",
        "findings": all_findings,
        "summary": {
            "total_findings": len(all_findings),
            "systemic_halt": systemic,
            "local_fix": local,
            "scans_passed": 6 - sum(1 for _, fn in scan_functions if fn(ws)),
        },
    }

    # Recalculate scans_passed properly
    passed = 0
    for scan_name, scan_fn in scan_functions:
        if len(scan_fn(ws)) == 0:
            passed += 1
    report["summary"]["scans_passed"] = passed

    # Write report
    tmp_dir = ws / 'tmp'
    tmp_dir.mkdir(exist_ok=True)
    report_path = tmp_dir / 'structural_scan_report.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*50}")
    print(f"TOTAL: {len(all_findings)} findings ({systemic} SYSTEMIC-HALT, {local} LOCAL-FIX)")
    print(f"Report: {report_path}")

    return report


if __name__ == '__main__':
    ws_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    report = run_full_scan(ws_path)

    if report["summary"]["systemic_halt"] > 0:
        print("\n⚠️  SYSTEMIC-HALT findings detected. Manual review required.")
        sys.exit(1)
    elif report["summary"]["total_findings"] > 0:
        print("\n🟡 LOCAL-FIX findings detected. Auto-heal recommended.")
        sys.exit(0)
    else:
        print("\n🟢 All clear. Zero findings.")
        sys.exit(0)
