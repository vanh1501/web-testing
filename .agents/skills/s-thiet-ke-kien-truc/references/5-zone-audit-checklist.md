# 5-Zone Audit Checklist — Physical Directory Compliance

> Reference document for the `architecture` skill (Route 2).
> Use during Phase 2 of `/audit-workspace` to verify physical workspace structure.

---

## Required Zone Paths

| Zone | Required Paths | Severity if Missing | Purpose |
|---|---|---|---|
| Zone 1 | `tmp/` | 🟡 Warning | Scratch/temporary files |
| Zone 2 | `artifacts/`, `artifacts/plans/`, `artifacts/reports/`, `artifacts/handoffs/` | 🔴 Critical | Workspace output artifacts |
| Zone 3 | `outputs/` | 🔴 Critical | Final deliverables |
| Zone 4a | `.agents/agents/` | 🔴 Critical | Agent System Instructions |
| Zone 4a | `.agents/quan-ly-quy-tac/` | 🔴 Critical | Governance quan-ly-quy-tac |
| Zone 4a | `.agents/workflows/` | 🔴 Critical | Operational workflows |
| Zone 4a | `.agents/skills/` | 🔴 Critical | Skill definitions |
| Zone 4a | `.agents/memory_bus/` | 🔴 Critical | State synchronization |
| Zone 4a | `.agents/tests/` | 🟡 Warning | Golden tests |
| Zone 5a | `.context/` | 🔴 Critical | Metadata only |
| Zone 5a | `.context/domain/` | 🔴 Critical | INDEX.md location |
| Zone 5b | `KB/` | 🔴 Critical | Domain knowledge |
| Zone 6  | `* (Domain Extension Zones)` | 🟢 Info | Cấu trúc bản địa hóa (Localized Folders) nếu được khai báo trong `.context/allowed-zones.json`. |
| Root | `.agents/agents.md` | 🔴 Critical | MAS hierarchy definition |
| Root | `README.md` | 🟡 Warning | Workspace documentation |
| Root | `QUALITY-LOG.md` | 🟡 Warning | Health timeline |

## Scan Algorithm

```
FOR EACH required_path IN zone_table:
    exists = Test-Path(workspace_root + required_path)
    IF NOT exists:
        ADD finding(severity=zone_table[required_path].severity, 
                     message="Missing: {required_path}")
```

## Data Placement Verification

```
# Check .context/ for domain data contamination
FOR EACH file IN .context/**/*.md:
    IF file contains methodology OR framework OR template OR exercise:
        ADD finding(severity=🔴 Critical, 
                     message="Domain data in .context/: {file} → Migrate to KB/")

# Check KB/ for metadata contamination  
FOR EACH file IN KB/**/*.md:
    IF file contains ONLY project info OR glossary OR config:
        ADD finding(severity=🟡 Warning,
                     message="Metadata in KB/: {file} → Should be in .context/")
```

## Minimum Content Checks

| Directory | Minimum Content | Severity |
|---|---|---|
| `.agents/agents/` | ≥ 2 files (Coordinator + ≥1 Worker) | 🔴 Critical |
| `.agents/quan-ly-quy-tac/` | ≥ 3 files (orchestration, swarm, safety) | 🔴 Critical |
| `.agents/workflows/` | ≥ 3 files (start-session, end-session + ≥1 domain) | 🔴 Critical |
| `.agents/skills/` | ≥ 1 folder with SKILL.md | 🟡 Warning |
| `KB/` | ≥ 1 domain knowledge file | 🔴 Critical |
| `.context/templates/` | ≥ 1 template file | 🟡 Warning |
