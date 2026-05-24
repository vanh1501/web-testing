# Rule Design Intelligence — Best Practices & Anti-Patterns

> Reference document for the `quan-ly-quy-tac` skill.
> Contains grounded know-how from industry best practices, academic research,
> and empirical lessons from MAS fleet operations.
> Agent MUST load this file when executing Route 1 (BIRTH) or Route 3 (REPAIR)
> to ensure quan-ly-quy-tac are designed with intelligence, not just structure.

---

## Part 1: The CLEAR Framework — Deep Specification

CLEAR is the canonical quality framework for evaluating and authoring giam-sat-tuan-thu quan-ly-quy-tac
in AI agent systems. Each dimension targets a specific failure mode of LLM instruction adherence.

### C — Concrete (Anti-Vagueness)

**Failure Mode:** LLMs interpret vague terms inconsistently across sessions.

**Anti-Patterns (BANNED phrases):**
- "appropriate", "as needed", "good quality", "professional", "better", "properly"
- "ensure quality", "handle carefully", "process data standardly"

**Fix Patterns:**
- ❌ "Use appropriate formatting" → ✅ "Use Markdown H2 headings for sections, bullet lists for quan-ly-quy-tac"
- ❌ "Handle errors properly" → ✅ "If error count > 3 in same step → HALT + log to `Failed_Optimization_Log.md`"
- ❌ "Ensure quality" → ✅ "Score ≥ 4/5 on CLEAR rubric before marking DONE"

**Measurement:** Count vague terms. If ≥3 per file → FAIL dimension.

### L — Leveled (Priority Stratification)

**Failure Mode:** When all quan-ly-quy-tac use "MUST", the agent treats everything as equally critical
and either freezes (overload) or ignores all constraints (learned helplessness).

**The 30% Rule:** MUST keywords should constitute ≤30% of total quan-ly-quy-tac in a file.
Distribute as: MUST (critical safety) → SHOULD (best practice) → MAY (optional enhancement).

**Hierarchy Model (from Policy-as-Code literature):**
```
Level 1: MUST    — Safety, security, data integrity (violation = HALT)
Level 2: SHOULD  — Quality standards, efficiency (violation = WARNING)
Level 3: MAY     — Enhancement, optimization (violation = NOTE)
```

**Fix Pattern:**
- ❌ "MUST use proper tone. MUST format correctly. MUST cite sources."
- ✅ "MUST cite sources for all factual claims. SHOULD format with H2 headings. MAY add summary box."

### E — Exampled (Disambiguation via Few-Shot)

**Failure Mode:** Complex quan-ly-quy-tac without examples are interpreted differently
by different LLM sessions, creating non-deterministic behavior.

**When Examples Are Required:**
- Rules involving conditional logic (if-then-else)
- Rules with format specifications
- Rules that distinguish between two similar concepts

**Format:** Always pair ✅ (correct) with ❌ (incorrect):
```markdown
✅ Correct: `## KB Connectivity` section lists 3 specific file paths
❌ Incorrect: `## KB Connectivity` says "consult relevant KB files"
```

### A — Actionable (Tool/Path Specificity)

**Failure Mode:** Agent knows WHAT to do but not HOW or WHERE.

**Anti-Patterns:**
- "Consult the relevant documentation" (Which file? Which section?)
- "Use the standard template" (What is the template path?)
- "Follow the approved process" (Which workflow?)

**Fix Pattern:** Every rule MUST reference at least one of:
- A specific file path (e.g., `references/component-repair-protocols.md`)
- A specific tool (e.g., `grep_search`, `view_file`, `search_web`)
- A specific output location (e.g., `artifacts/handoffs/`)

### R — Ranked (Conflict Resolution)

**Failure Mode:** When two quan-ly-quy-tac contradict, the agent either picks randomly
or halts entirely. Both outcomes are unacceptable.

**HPRF (Hierarchical Priority Resolution Framework):**
```
Tier 1: Constitution (L0) — Safety, identity, hard-stops
Tier 2: Standards (L0/L1) — Architectural patterns, quality gates
Tier 3: Domain (L1) — Industry-specific, workspace-specific quan-ly-quy-tac
```

**Conflict Resolution Protocol:**
1. Higher tier ALWAYS overrides lower tier.
2. Within same tier: more specific rule overrides general rule.
3. If conflict cannot be resolved: HALT + escalate to Human.

---

## Part 2: Rule Architecture Design Patterns

### Pattern 1: Layered Policy Chain (L0 → L1 → L2)

Borrowed from **Open Policy Agent (OPA)** and **Policy-as-Code** architecture:

```
L0 (Global Base Policy)    ← Immutable. Copied from Master Repo.
  ↓ inherits
L1 (Domain Context)        ← Mutable. Customized per workspace.
  ↓ inherits
L2 (Operational/Session)   ← Ephemeral. Created during session.
```

**Key Principle:** L1 can EXTEND L0 but NEVER CONTRADICT L0.
If an L1 rule conflicts with L0 → 🔴 SYSTEMIC-HALT.

### Pattern 2: Specification Pattern (Rule Atomicity)

Each rule should be a self-contained, testable unit:
```
RULE_ID: [unique identifier]
CONDITION: [when this rule applies]
ACTION: [what the agent must do]
VERIFICATION: [how to confirm compliance]
```

### Pattern 3: Chain of Responsibility (Evaluation Order)

Rules are evaluated in a chain. On conflict:
1. Evaluate L0 quan-ly-quy-tac first → if match, apply and stop.
2. Evaluate L1 quan-ly-quy-tac → if match, apply and stop.
3. If no rule matches → apply default behavior from `L1-core-cheatsheet-fallback.md`.

### Pattern 4: Circuit Breaker (Anti-Loop)

If a rule causes repeated failures (>3 times in same session):
1. OPEN the circuit (disable the rule temporarily).
2. Log to `Failed_Optimization_Log.md`.
3. Escalate to Human for review.
4. HALF-OPEN: Test with next task. If passes → CLOSE circuit.

---

## Part 3: Common Anti-Patterns in Rule Systems

| # | Anti-Pattern | Description | Detection | Fix |
|---|---|---|---|---|
| AP-01 | **Skeleton Rule** | File exists but contains only headers, no actionable content | Size < 0.5KB | Route 3: Full content authoring |
| AP-02 | **Verbatim Clone** | L1 is a 100% copy of L0 with no domain customization | Diff L0 vs L1: >80% overlap | Route 4: Domain mutation or delete L1 |
| AP-03 | **Vague Counsel** | Rules use "appropriate", "careful", "professional" | Count vague terms ≥3 | Route 3: RR3 (CLEAR Enhancement) |
| AP-04 | **Priority Flood** | Every rule is marked MUST (>30% MUST ratio) | Count MUST / total quan-ly-quy-tac | Route 3: RR3 — distribute MUST/SHOULD/MAY |
| AP-05 | **Orphan Rule** | Rule file exists but nothing references it | grep_search = 0 hits | Route 3: RR5 (wire or deprecate) |
| AP-06 | **Cross-Layer Conflict** | L1 contradicts L0 on same topic | Cross-Layer scan | Route 4: Step 4 (SYSTEMIC-HALT) |
| AP-07 | **Context Bloat** | Single rule file > 15KB | Size check | Route 4: Red-Zone Compression |
| AP-08 | **Missing Examples** | Complex conditional quan-ly-quy-tac have no ✅/❌ pairs | CLEAR E-dimension = 0 | Route 3: RR3 (add example pairs) |
| AP-09 | **Tool Blindness** | Rules say "do X" without specifying which tool/path | CLEAR A-dimension = 0 | Route 3: RR3 (add tool references) |
| AP-10 | **Flat Dump** | All quan-ly-quy-tac in one section, no logical grouping | Section count < 2 | Route 3: RR2 (Structure Repair) |

---

## Part 4: Rule Quality Metrics & Benchmarks

### Fleet-Wide Benchmarks (from MAS Fleet Operations)

| Metric | Target | Warning | Critical |
|---|---|---|---|
| Average Rule Score | ≥ 80/100 | < 70 | < 55 |
| CLEAR Pass Rate | ≥ 4/5 dimensions | 3/5 | < 3/5 |
| MUST Ratio | ≤ 30% | 30-50% | > 50% |
| Vague Term Density | 0 per file | 1-2 per file | ≥ 3 per file |
| L0-L1 Overlap | < 20% | 20-50% | > 80% (clone) |
| Rule File Size | 1-15KB | > 15KB | < 0.5KB |
| Orphan Rate | 0% | 1-10% | > 10% |

### Domain Grounding Quality Check

Before finalizing any L1 rule, verify:
1. Was `search_web` executed to find industry-standard SOPs for this domain?
2. Does the rule reference at least 1 external framework, standard, or compliance requirement?
3. Could a domain expert distinguish this L1 from a generic template?

If answer to any is "No" → R4 (Content Specificity) score must be penalized.
