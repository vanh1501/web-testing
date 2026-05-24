# Workflow Repair Protocols & Enrichment Engine

> Reference document for the `tao-quy-trinh-moi` skill, Route 3 (RESOLVE).
> Contains deterministic fix recipes for all common workflow quality failures.
> Agent MUST match failure dimension to protocol before executing repair.

---

## Protocol Index

| ID | Trigger Condition | Target Dimension | Severity |
| --- | --- | --- | --- |
| WR1 | Missing or weak YAML frontmatter | W1 | Medium |
| WR2 | Missing metadata (Owner / Skill Target) | W2 | High |
| WR3 | Shallow execution (< 3 steps, no branching) | W3 | High |
| WR4 | Broken or missing skill wiring | W4 | Critical |
| WR5 | Zero-Native violation (inline domain logic) | W5 | Critical |
| WR6 | Over context budget (> 12K chars) | W6 | Medium |
| WE1 | Missing workflow for A-ESOAR R-step | Coverage | Critical |
| WE2 | Infrastructure workflow not domain-adapted | TYPE-INFRA | Medium |

---

## Repair Protocols

### WR1: Frontmatter Repair (W1 Failures)

**Trigger:** W1 score < 8.

**Protocol:**

1. Read the workflow body to understand its purpose, trigger conditions, and domain.
2. If no YAML frontmatter exists at all:
   - Generate frontmatter block:
   ```yaml
   ---
   description: [action verb] [domain context] — [trigger conditions]. Use when [user phrases].
   ---
   ```
3. If frontmatter exists but description is weak:
   - Rewrite description to include: (a) what the workflow does, (b) when to trigger, (c) what changes after execution.
4. Ensure description >= 10 words with actionable language.

### WR2: Metadata Injection (W2 Failures)

**Trigger:** W2 score < 12.

**Protocol:**

1. Load `.agents/agents.md` roster to find the correct Owner agent for this workflow's domain.
2. Load `SKILLS-INDEX.md` to find the correct Skill Target.
3. Inject metadata block after frontmatter:
   ```markdown
   - **👤 Owner:** [@Agent-ID from .agents/agents.md]
   - **🛠 Skill Target:** [skill-id from SKILLS-INDEX.md]
   ```
4. If no matching agent/skill exists:
   - Flag as: "OWNER/SKILL not found — manual assignment required."
   - DO NOT use `[Native]` or `[TBD]` as placeholders.
5. Add `## Goal` section if missing — derive from workflow name and body context.

### WR3: Execution Depth Enhancement (W3 Failures)

**Trigger:** W3 score < 12.

**Protocol:**

1. If workflow has < 3 steps:
   - Read value chain / A-ESOAR R-step this workflow maps to.
   - Decompose into sub-steps: Input Validation → Core Processing → Output Formatting → Quality Gate.
   - Each step must start with an imperative verb.
2. If no decision logic exists:
   - Identify branching opportunities: what could go wrong? What varies?
   - Add at least 1 conditional gate:
     ```markdown
     **Gate:** IF [condition] → proceed to Step N. ELSE → [fallback/escalation].
     ```
3. If no edge case handling:
   - Add `## Edge Cases` section with at least 2 scenarios.
4. Replace passive language with imperatives:
   - ❌ "You might want to check..." → ✅ "Check [specific thing]. If [condition] → [action]."

### WR4: Skill Wiring Repair (W4 Failures)

**Trigger:** W4 score < 12.

**Protocol:**

1. If no `## Assigned Skills` section:
   - Scan each execution step for domain knowledge requirements.
   - Map each requirement to a skill from `SKILLS-INDEX.md`.
   - Generate wiring section:
     ```markdown
     ## Assigned Skills
     | Step | Skill | Purpose |
     |---|---|---|
     | Step 1 | `skill-id` | [what it provides] |
     ```
2. If skill references are broken (skill doesn't exist):
   - Search `SKILLS-INDEX.md` for similar skill by keyword.
   - If found → update reference. If not found → flag as "MISSING SKILL — creation required via `tao-ky-nang-moi` Route 1."
3. If `[Native]` Skill Targets found:
   - Identify what domain logic is being executed natively.
   - Propose extraction to existing or new skill.
   - This is a Zero-Native prerequisite — WR4 often triggers WR5.

### WR5: Zero-Native Extraction (W5 Failures)

**Trigger:** W5 score < 10.

**Protocol:**

1. Scan workflow body for inline domain logic blocks (> 10 consecutive lines of non-routing content).
2. For each detected block:
   - Classify content type: parsing logic, mapping quan-ly-quy-tac, scoring formulas, decision trees.
   - Determine target: existing skill (extract TO it) or new skill needed.
3. If existing skill can absorb the logic:
   - Move content to the skill's `references/` or main body.
   - Replace inline logic with skill delegation:
     ```markdown
     Step N: Invoke `[skill-id]` with input [X]. Receive output [Y].
     ```
4. If new skill is needed:
   - Flag for `tao-ky-nang-moi` Route 1 (CREATE).
   - Generate a brief spec: "Skill needed for [extracted logic description]."
5. After extraction, verify workflow body contains only orchestration logic (routing, sequencing, gating).

### WR6: Context Budget Reduction (W6 Failures)

**Trigger:** W6 score < 5 (file > 12,000 characters).

**Protocol:**

1. Identify the largest content sections by character count.
2. Extraction candidates (ranked by size):
   - Detailed examples → move to skill references
   - Long edge case descriptions → move to `## Edge Cases` appendix document
   - Domain-specific lookup tables → move to KB or skill references
3. Split strategies:
   - If workflow has > 2 independent branches → split into sub-workflows with a routing parent.
   - If workflow is single-path but verbose → condense prose into tables and bullet points.
4. Verify: post-reduction file size < 12,000 characters.

---

## Enrichment Scenarios

### WE1: Missing Workflow Generation (Coverage Gap)

**Condition:** A-ESOAR analysis shows an R-step without a corresponding workflow.

**Action:**
1. Read the R-step definition from BRD/SCOPE.
2. Identify: input source, processing logic, output target, responsible agent.
3. Generate workflow using the 5-Section Architecture:
   ```markdown
   ---
   description: [R-step description]. Use when [trigger].
   ---
   ## Input Required
   ## Execution Steps
   ## Output Format
   ## Edge Cases
   ## Troubleshooting
   ```
4. Wire metadata (Owner, Skill Target, Assigned Skills).
5. Run Pre-Flight CQS Check before saving.

### WE2: Infrastructure Workflow Domain Adaptation

**Condition:** `start-session.md`, `end-session.md`, or `w-luu-phien.md` is a verbatim copy of the baseline template.

**Detection:** Compare first 20 lines against baseline template. If >80% match → flagged as unadapted.

**Action:**
1. Read workspace domain context (.agents/agents.md, SCOPE brief).
2. Customize generic sections:
   - Replace `[workspace-name]` placeholders with actual name.
   - Add domain-specific "Morning Briefing" items to `start-session`.
   - Add domain-specific "Quality Log" entries to `end-session`.
   - Add domain-specific "Memory Bus" channels to `checkpoint-session`.
3. Mark as adapted — update version tag if present.

---

## Batch Processing

When assessing/repairing multiple workflows, use this priority:

```text
               HIGH Impact            LOW Impact
             (W4, W5 fails)        (W1, W6 fails)
  ┌──────────────────────────┬──────────────────────────┐
  │     DO FIRST             │     BATCH LATER          │
  │  Skill wiring (WR4)     │  Frontmatter fix (WR1)   │
EASY│  Metadata inject (WR2)  │  Budget trim (WR6)       │
FIX │                          │                          │
  ├──────────────────────────┼──────────────────────────┤
  │     PLAN + CONFIRM       │     DEFER                │
HARD│  Zero-Native extract    │  Domain adaptation (WE2) │
FIX │  (WR5)                  │                          │
  │  Missing workflow (WE1)  │                          │
  └──────────────────────────┴──────────────────────────┘
```

**Critical Rule:** NEVER auto-create a new workflow (WE1) without user confirmation. Present the R-step analysis and proposed workflow structure first.
