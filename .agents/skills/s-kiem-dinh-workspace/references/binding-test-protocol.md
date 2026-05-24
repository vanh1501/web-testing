# Integration Binding Test Protocol (HARD GATE 4 PRE-CHECK)

> [!CAUTION]
> **This protocol is a MANDATORY hard block before Gate 4.** No exceptions.
> Builder MUST programmatically verify that every reference inside Agent SI files resolves to a real file on disk.

## Binding Test Execution Checklist

For EACH Agent SI file in `.agents/agents/` (recursive):

| Test | Verification Method | Pass Criteria |
|------|-------------------|---------------|
| KB Path Resolution | `Test-Path` every file listed under `## KB Connectivity` | All paths return `True` |
| Skill ID Match | Cross-reference `## Skills` entries against `00_SKILL_INDEX.md` | 100% exact name match |
| Workflow Reference | Cross-reference any `/workflow-name` against `.agents/workflows/` | Matching `.md` file exists |
| Memory Bus Keys | Cross-reference `## Memory Bus Contract` domains against `memory_bus/keys.yaml` | All domains registered |
| No Duplicate Sections | Count occurrences of `## KB Connectivity` per file | Exactly 1 per agent |
| No Stale Paths | Grep for `.context/knowledge/` across all agent files | 0 matches (path banned) |

## Execution Command Template
```powershell
# Example: Verify all KB references resolve
Get-ChildItem -Recurse ".agents/agents/*.md" | ForEach-Object {
    Select-String -Path $_.FullName -Pattern '\(KB/[^)]+\)' | ForEach-Object {
        $path = $_.Matches.Value -replace '[()]',''
        if (-not (Test-Path $path)) { Write-Warning "BROKEN: $($_.Filename) -> $path" }
    }
}
```

## Gate Decision
- ✅ ALL tests pass → Proceed to Gate 4
- ❌ ANY test fails → STOP. Fix broken references. Re-run binding test. Do NOT proceed.
