# Rule Repair Protocols (RR1-RR5)

> Reference document for the `quan-ly-quy-tac` skill, Route 3 (REPAIR).
> Contains deterministic fix recipes for Rule file quality failures.
> Each protocol maps to a specific failing dimension from the scoring engine.

---

## Protocol Index

| ID | Trigger | Target Dim | Severity |
| --- | --- | --- | --- |
| RR1 | Missing HPRF block | R1 | Critical |
| RR2 | Poor structure (flat, thin sections) | R2 | Medium |
| RR3 | Low CLEAR score | R3 | High |
| RR4 | Generic content (baseline copy-paste) | R4 | High |
| RR5 | Orphan rule file (nothing references it) | R5 | Medium |

---

### RR1: HPRF Injection

**Trigger:** R1 score < 15.

**Protocol:**
1. Analyze rule file content to determine tier:
   - Contains safety/compliance constraints → Tier 1 (Constitution)
   - Contains architectural/workflow standards → Tier 2 (Standards)
   - Contains domain-specific processing quan-ly-quy-tac → Tier 3 (Domain)
2. Inject HPRF block after YAML frontmatter:
   ```markdown
   > [!IMPORTANT] Override Priority:
   > Tier [1/2/3] — [Constitution/Standards/Domain].
   > In case of conflict with [lower tier] quan-ly-quy-tac, THIS file takes precedence.
   ```
3. If conflict resolution statement is missing → add explicit override clause.

### RR2: Structure Repair

**Trigger:** R2 score < 12.

**Protocol:**
1. If flat dump → organize into logical sections (2-4 sections minimum).
2. If thin sections (1 rule each) → merge related quan-ly-quy-tac or expand with specifics.
3. Add heading hierarchy: `#` title → `##` sections → quan-ly-quy-tac within sections.
4. Ensure each section contributes to a distinct giam-sat-tuan-thu concern.
5. Convert passive language to imperative: "You should try..." → "Do X."

### RR3: CLEAR Enhancement

**Trigger:** R3 score < 15 (CLEAR < 3/5).

> Load `references/rule-design-intelligence.md` Part 1 for detailed CLEAR spec and anti-patterns.

**Protocol per failing dimension:**
- **C (Concrete) fails:** Replace every "appropriate", "good", "better" with specific quantities/names.
  - ❌ "Use appropriate formatting" → ✅ "Use Markdown H2 headings for sections"
- **L (Leveled) fails:** Add MUST/SHOULD/MAY markers. Check MUST ≤ 30%.
  - ❌ "MUST do X. MUST do Y. MUST do Z." → ✅ "MUST do X. SHOULD do Y. MAY do Z."
- **E (Exampled) fails:** Add ✅/❌ example pairs for complex quan-ly-quy-tac.
  - Provide at least 1 correct and 1 incorrect example per conditional rule.
- **A (Actionable) fails:** Replace vague guidance with specific tool/folder/file references.
  - ❌ "Follow the standard process" → ✅ "Execute `/audit-workspace --strict`"
- **R (Ranked) fails:** Add HPRF block (→ triggers RR1).

### RR4: Domain Customization

**Trigger:** R4 score < 12.

**Protocol:**
1. Compare rule content against baseline templates (L0 files or `.context/templates/`).
2. Identify verbatim sections (>80% text overlap).
3. For each verbatim section → rewrite with domain-specific context:
   - Replace generic paths with actual workspace paths.
   - Add domain-specific constraints and thresholds.
   - Reference actual workforce roster IDs from `L1-swarm-registry.md`.
4. **MANDATORY:** Execute `search_web` with query "[workspace domain] standard operating procedures"
   to ground quan-ly-quy-tac in real industry standards. Do NOT hallucinate domain quan-ly-quy-tac.

### RR5: Orphan Resolution

**Trigger:** R5 score < 5.

**Protocol:**
1. Run `grep_search` across `.agents/workflows/`, `.agents/skills/`, `GEMINI.md`, and `L1-swarm-registry.md` for references to this rule file.
2. If zero references found:
   - Analyze if any workflow or skill SHOULD reference it → add wiring.
   - If truly orphan → recommend to user: deprecate or delete.
3. If rule should be referenced by `GEMINI.md` (L0 quan-ly-quy-tac) → execute Root Wiring Protocol.

---

## Repair Priority Matrix

```text
               HIGH Impact           LOW Impact
             (RR1 fails, RR3 fails)  (RR5 fails)
  ┌──────────────────────────┬──────────────────────────┐
  │     DO FIRST             │     BATCH LATER          │
EASY│  HPRF injection (RR1)   │  Orphan resolution (RR5) │
FIX │                         │                          │
  ├──────────────────────────┼──────────────────────────┤
  │     PLAN + CONFIRM       │     DEFER                │
HARD│  CLEAR enhance (RR3)    │  Domain custom. (RR4)    │
FIX │                         │  Structure repair (RR2)  │
  └──────────────────────────┴──────────────────────────┘
```
