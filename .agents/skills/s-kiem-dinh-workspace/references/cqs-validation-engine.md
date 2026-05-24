# CQS Validation Engine — Per-Component Auto-Checker

> Reference document for the `qa` skill.
> Implements the Component Quality Specification from `.context/standards/component-quality-spec.md`.
> Use during Phase 6 of `/audit-workspace` to validate EVERY component against CQS minimums.

---

## Quick Reference: Size Gates (Auto-FAIL)

| Component Type | Min Size | Max Size | Auto-FAIL Rule |
|---|---|---|---|
| Agent SI | 1.5 KB | 15 KB (25 KB = 🔴) | < 1.5 KB → Skeleton. Auto-FAIL. |
| Workflow | 0.8 KB | 15 KB | < 0.8 KB → Skeleton. Auto-FAIL. |
| Skill SKILL.md | 1 KB (hard) / 10 KB (soft) | 15 KB | < 1 KB → Skeleton (SYSTEMIC-HALT). < 10 KB → Under-developed (LOCAL-FIX). |
| Rule | 0.5 KB | 15 KB | < 0.5 KB → Skeleton. Auto-FAIL. |
| KB File | 500 bytes | No limit | < 500 bytes → Skeleton. Auto-FAIL. |

> **Key Principle**: If a file is below minimum size, it is 100% a skeleton. Skip content inspection — just FAIL it.

---

## Agent SI Validation (7-Section Check)

For each file in `.agents/agents/**/*.md`:

```
PASS_COUNT = 0

1. CHECK "## Identity" or "## Activation Trigger" exists → PASS_COUNT++
2. CHECK "## Capabilities" exists AND contains ≥ 2 bullet items → PASS_COUNT++
3. CHECK "## KB Connectivity" exists AND contains ≥ 1 file reference → PASS_COUNT++
4. CHECK "## Workflows" section exists with ≥ 1 workflow reference → PASS_COUNT++
5. CHECK "## I/O Contract" with "Input:" AND "Output:" subsections → PASS_COUNT++
6. CHECK "## Handoff Protocol" exists AND does NOT self-loop → PASS_COUNT++
7. CHECK "## Memory Bus Contract" with Read/Write permissions → PASS_COUNT++

IF PASS_COUNT < 5 → 🔴 Critical (Missing ≥ 2 required sections)
IF PASS_COUNT < 7 → 🟡 Warning (Incomplete but functional)
IF PASS_COUNT == 7 → ✅ PASS
```

### Agent SI Prohibition Check

```
SCAN file content for:
- "## Voice" or "## Persona" or "## Tone" (> 3 lines) → 🔴 Persona pollution
- Step-by-step execution logic (> 5 numbered steps) → 🔴 Workflow leakage
- Duplicate heading (same ## heading appears 2+) → 🔴 Structural error
- Reference to non-existent file (grep path, Test-Path) → 🔴 Dangling reference
```

---

## Workflow Validation (5-Section Check)

For each file in `.agents/workflows/*.md`:

```
PASS_COUNT = 0

1. CHECK YAML frontmatter exists with "description:" ≥ 10 words → PASS_COUNT++
2. CHECK "👤 Owner:" AND "🛠 Skill Target:" metadata present → PASS_COUNT++
3. CHECK "## Goal" section exists with ≥ 2 sentences → PASS_COUNT++
4. CHECK ≥ 3 executable steps (### Step or numbered steps) → PASS_COUNT++
5. CHECK output format or template reference exists → PASS_COUNT++

IF PASS_COUNT < 3 → 🔴 Critical
IF PASS_COUNT < 5 → 🟡 Warning
IF PASS_COUNT == 5 → ✅ PASS
```

### Workflow Prohibition Check

```
SCAN file content for:
- "🛠 Skill Target: [Native]" → 🔴 Zero-Native violation (CRITICAL Auto-FAIL)
- Embedded domain-specific execution logic (>10 lines containing domain verbs: "Parse", "Map", "Generate", "Design", "Compile") → 🔴 Critical Zero-Native Violation
- Missing "🛠 Skill Target:" metadata entirely → 🔴 CRITICAL Auto-FAIL (Missing Required Routing Metadata)
- Self-loop handoff (Owner == Handoff target) → 🔴 Routing error
- Missing YAML frontmatter entirely → 🔴 Missing metadata
- "TODO" or "TBD" or "sẽ bổ sung sau" → 🔴 Incomplete
```

---

## Skill Validation — 3-Tier Deep Content Analysis Engine

> This engine inspects skills at 3 progressive levels of depth.
> Tầng 1 catches broken skeletons. Tầng 2 scores structural maturity.
> Tầng 3 analyzes content extractability for remediation planning.

### Tầng 1: Structural Gate (Existence & Syntax)

For each folder in `.agents/skills/*/`:

```
STRUCT_PASS = 0

1. CHECK SKILL.md exists                                    → if not: 🔴 CRITICAL. STOP. (Skill folder without SKILL.md)
2. CHECK SKILL.md size ≥ 10 KB                              → if < 1 KB: 🔴 SYSTEMIC-HALT (empty shell). if < 10 KB: 🔴 LOCAL-FIX (under-developed, needs enrichment via skill-writer Route 3)
3. CHECK YAML frontmatter with "name:" AND "description:" ≥ 10 words → STRUCT_PASS++
4. CHECK "## ROLE" section exists                           → STRUCT_PASS++
5. CHECK "## PROCESS" or "## Instructions" section exists with ≥ 1 route → STRUCT_PASS++
6. CHECK "## RULES" section exists with ≥ 2 concrete quan-ly-quy-tac → STRUCT_PASS++

IF STRUCT_PASS < 2 → 🔴 CRITICAL (Legacy / Broken format — cannot proceed to Tầng 2)
IF STRUCT_PASS < 4 → 🟡 WARNING (Missing sections — proceed to Tầng 2 with penalty)
IF STRUCT_PASS == 4 → ✅ Structural PASS → proceed to Tầng 2
```

**Prohibition Check (Always runs):**
```
SCAN for "## Voice" or "## Persona" or "## Identity"       → 🔴 SI pollution (Persona belongs in Agent SIs only)
SCAN for > 5 consecutive numbered steps in non-PROCESS area → 🟡 Workflow leakage warning
SCAN for "TODO" or "TBD" or "sẽ bổ sung sau"              → 🔴 Incomplete placeholder detected
```

---

### Tầng 2: 4-Tier Compliance Audit (10-Point Scoring)

> Load `references/4tier-compliance-rubric.md` for the full rubric specification.

```
COMPLIANCE_SCORE = 0  # max = 10

# ── Physical Structure (4 pts) ──
CHECK references/ dir exists AND has ≥1 .md file with >500 bytes   → +1 pt
CHECK assets/ dir exists AND has ≥1 file (any format)              → +1 pt
CHECK evals/evals.json exists AND valid JSON with ≥2 test cases    → +1 pt
CHECK scripts/ dir exists (even if empty)                           → +1 pt

# ── SKILL.md Body Compliance (4 pts) ──
CHECK ## RESOURCES section exists with routing table format:
      Must contain "|" table with "Situation" and "Load" columns   → +1 pt
CHECK ## QA section exists with ≥3 checkbox items (- [ ])          → +1 pt
CHECK ## WHEN TO CLARIFY exists with ≥1 question                   → +1 pt
CHECK ## OUTPUT FORMAT section exists with format specification     → +1 pt

# ── Content Purity (2 pts) ──
CHECK SKILL.md total line count ≤ 500                              → +1 pt
CHECK No inline domain knowledge block > 10 consecutive
      non-heading lines outside ## PROCESS                          → +1 pt
```

**Compliance Grade:**

| Score | Grade | Classification | Remediation Action |
|---|---|---|---|
| 10/10 | ✅ FULL_COMPLIANT | No action needed | — |
| 7-9 | 🟡 PARTIAL | Minor gaps | Emit `🔴 [LOCAL-FIX]` — auto-fixable |
| 4-6 | 🔴 SIGNIFICANT | Major gaps, content may be extractable | → Proceed to **Tầng 3** Extractability Analysis |
| 0-3 | 🔴 SKELETON | Legacy or empty shell | Emit `🔴 [SYSTEMIC-HALT]` — manual creation from scratch |

**Evals Quality Gate (Sub-check):**
```
IF evals/evals.json exists:
  PARSE JSON → extract all "input" fields
  IF ANY input contains generic phrases:
    ("Execute skill with valid parameters" OR
     "Execute skill with missing dependencies" OR
     "valid input" OR "invalid input")
    → 🟡 GENERIC_EVALS_WARNING: Evals are placeholders, need domain-specific enrichment.
```

---

### Tầng 3: Extractability Analysis (Content Decomposition Assessment)

> Triggered ONLY when COMPLIANCE_SCORE < 7. Purpose: determine whether the
> SKILL.md content can be automatically decomposed into references/ and assets/.

```
# ── Step 1: Line Classification ──
FOR EACH line in SKILL.md:
  IF line is inside ## ROLE, ## PURPOSE, ## PROCESS, ## RULES,
     ## QA, ## WHEN TO CLARIFY, ## ACTIVATION SIGNALS,
     ## OUTPUT FORMAT, ## RESOURCES:
    → Classify as ROUTING_LINE (R)
  ELSE:
    → Classify as PASSIVE_LINE (P)

routing_lines = count(R)
passive_lines = count(P)
passive_ratio = passive_lines / total_lines

# ── Step 2: Content Pattern Detection ──
SCAN for embedded content patterns:
  has_embedded_tables     = (≥1 Markdown table with |---|---| outside ## RESOURCES)
  has_embedded_formulas   = (Math expressions: $...$, scoring matrices, threshold%)
  has_embedded_templates  = (Output format blocks > 10 lines, ```code blocks```)
  has_embedded_examples   = (Worked examples, "Ví dụ:", "Example:" blocks > 5 lines)
  has_embedded_dicts      = (Term lists, verb banks, registries > 8 items)

# ── Step 3: Extraction Target Mapping ──
extraction_targets = []
FOR EACH detected pattern:
  IF pattern is unambiguous (entirely self-contained block):
    → ADD to extraction_targets with:
      type: "reference" (knowledge) or "asset" (template/output)
      dest: "references/[inferred-topic].md" or "assets/[inferred-name].md"
      source_lines: "L{start}-L{end}"
      auto_fixable: true
  IF pattern is ambiguous (interleaved with routing logic):
    → ADD to extraction_targets with:
      auto_fixable: false
      manual_review_reason: "Content at L{start}-L{end} mixes routing logic
                             with domain knowledge. Cannot safely separate."

# ── Step 4: Final Verdict ──
IF ALL targets have auto_fixable == true:
  → VERDICT: 🔴 [LOCAL-FIX] — Emit to /optimize-workspace SHP-23 Auto-Mode
IF ANY target has auto_fixable == false:
  → VERDICT: 🔴 [SYSTEMIC-HALT] — Emit REMEDIATION_REQUEST.md for Human review
IF passive_ratio < 0.1 AND COMPLIANCE_SCORE >= 4:
  → VERDICT: 🟡 [WARNING] — SKILL.md is routing-focused but missing 4-Tier folders.
     Auto-scaffold folders + trigger KB/Web enrichment.
```

**Extractability Edge Cases:**

| Edge Case | Detection Criteria | Verdict | Action |
|---|---|---|---|
| **Skeleton SKILL.md** | Size < 1KB | `🔴 SYSTEMIC-HALT` | Cannot extract from nothing. Manual creation required. |
| **Under-developed SKILL.md** | Size 1KB–10KB | `🔴 LOCAL-FIX` | Needs enrichment via skill-writer Route 3 (ADDIE). |
| **Bloated SKILL.md** | Line count > 500 AND passive_ratio > 0.6 | `🔴 LOCAL-FIX` | High extractability. Auto-mode viable. |
| **Legacy format** | Missing ≥3 of (ROLE, PROCESS, RESOURCES, QA, RULES) | `🔴 LOCAL-FIX` | Rewrite to canonical + extract. Auto-fixable if content sufficient. |
| **4-Tier folders exist but EMPTY** | Dir exists, 0 files or all files < 500 bytes | `🟡 WARNING` | Skeleton scaffolding. Trigger KB-fulfillment + Web Search enrichment. |
| **4-Tier has content but NO RESOURCES table** | references/ non-empty AND `## RESOURCES` missing in SKILL.md | `🔴 LOCAL-FIX` | Generate routing table from existing folder contents. |
| **Ambiguous content** | passive_ratio between 0.3-0.6 AND ≥1 pattern with auto_fixable=false | `🔴 SYSTEMIC-HALT` | Cannot safely auto-extract. Request Human clarification. |
| **Evals generic** | evals.json contains placeholder test descriptions | `🟡 WARNING` | Evals need domain-specific enrichment. |

---

### GHOST CHECK Algorithm

```
FOR EACH folder_name IN .agents/skills/:
    is_referenced = FALSE
    
    # Search workflows
    GREP folder_name IN .agents/workflows/*.md
    IF matches > 0 → is_referenced = TRUE
    
    # Search agent SIs
    GREP folder_name IN .agents/agents/**/*.md  
    IF matches > 0 → is_referenced = TRUE
    
    # Search .agents/agents.md
    GREP folder_name IN .agents/agents.md
    IF matches > 0 → is_referenced = TRUE
    
    IF NOT is_referenced → 🔴 GHOST SKILL DETECTED: {folder_name}
```

### MISSING SKILL CHECK Algorithm

```
FOR EACH workflow IN .agents/workflows/*.md:
    EXTRACT all "🛠 Skill Target: [skill-name]" entries
    IF NO entries FOUND:
        🔴 CRITICAL AUTO-FAIL: {workflow} is missing Skill Target metadata.
    FOR EACH skill_name:
        IF NOT EXISTS .agents/skills/{skill_name}/SKILL.md:
            🔴 MISSING REQUIRED SKILL: {skill_name} (demanded by {workflow})
```

---

## Rule Validation (3-Section Check)

For each file in `.agents/quan-ly-quy-tac/*.md`:

```
1. CHECK heading level 1 exists
2. CHECK "> [!IMPORTANT] Override Priority:" block with Tier level
3. CHECK ≥ 2 numbered sections with ≥ 2 quan-ly-quy-tac each

IF missing HPRF block → 🔴 Critical (rule loses conflict resolution)
IF < 2 sections → 🟡 Warning (thin rule)
```

---

## KB File Validation

For each file in `KB/**/*.md`:

```
1. CHECK file size ≥ 500 bytes (else → 🟡 possible skeleton)
2. CHECK heading level 1 exists
3. CHECK ≥ 3 sections with content
4. CHECK file is referenced by ≥ 1 Agent SI or INDEX.md entry (else → 🟡 orphan KB)
```
