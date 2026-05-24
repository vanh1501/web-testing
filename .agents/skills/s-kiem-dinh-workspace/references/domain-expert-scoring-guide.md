# Domain Expert Scoring Guide — Epistemic Rigor Assessment

> Reference document for the `qa` skill (Route 3: Domain Expert Scoring).
> Implements Phase 6.5 of `/audit-workspace`.
> Evaluates whether skills contain REAL domain expertise or are hollow definitions.

---

## The 3 Epistemic Tests

### Test 1: Canonical Trifecta Check (Bắt lỗi thiếu khung)

**Purpose**: Verify that domain-specific skills reference the minimum required industry frameworks for their declared domain.

**Algorithm**:
```
FOR EACH skill IN .agents/skills/*/:
    1. READ skill's YAML description → extract domain_name
    2. READ skill's references/*.md → extract framework_names
    3. Compare framework_names against KNOWN_TRIFECTA[domain_name]
    4. IF missing ≥ 1 pillar framework → 🔴 Critical (Amateurish Epistemic Gap)
    5. IF all pillar frameworks present → ✅ PASS
```

**Known Trifecta Examples** (Meta-Knowledge Heuristics):

| Domain | Required Pillar Frameworks (≥ 2 of these) |
|---|---|
| External Market Analysis | PESTEL, Porter Five Forces, CPM/Competitive Profile |
| Financial Analysis | DuPont, Ratio Analysis, Cash Flow Statement |
| Marketing Strategy | STP, Marketing Mix (4P/7P), Customer Journey |
| OBE Curriculum Design | Bloom Taxonomy, Constructive Alignment, NQF/VQF |
| Quality Assurance | PDCA, Six Sigma, Statistical Process Control |
| Strategic Management | SWOT, BCG Matrix, Ansoff Matrix |
| HR Management | Competency Framework, Performance Management, Succession Planning |
| Data Engineering | ETL Pipeline, Data Quality Framework, Schema Validation |

> **If the domain is NOT in this table**: Agent must use general knowledge to identify whether the skill references ≥ 2 established frameworks. If unclear → 🟡 Warning (not auto-fail).

---

### Test 2: Quantification Test (Bắt lỗi rác định nghĩa)

**Purpose**: Reject skills that contain only flat, theoretical definitions. Real expert knowledge includes formulas, scoring matrices, thresholds, or quantitative decision quan-ly-quy-tac.

**Algorithm**:
```
FOR EACH skill's references/*.md AND assets/*.md:
    SCAN for quantification markers:
    - Mathematical formulas (e.g., "LTV:CAC", "Score = X * W1 + Y * W2")
    - Scoring matrices (e.g., "Rate 1-5 on these criteria")
    - Threshold percentages (e.g., "≥ 80% coverage required")
    - Decision tables with numeric conditions
    - Concrete examples with specific numbers
    
    COUNT = number of quantification markers found
    
    IF COUNT == 0 → 🔴 Critical (Flat Knowledge Detected — no quantitative rigor)
    IF COUNT < 3 → 🟡 Warning (Weak quantification)
    IF COUNT >= 3 → ✅ PASS (Adequately quantified)
```

**Examples of PASSING vs FAILING content**:

| ✅ PASS (Quantified) | ❌ FAIL (Flat Definition) |
|---|---|
| "CLO must use Bloom Level ≥ 3 verb. Mức I = L1-L2, Mức P = L3-L4, Mức M = L5-L6" | "CLO should align with Bloom taxonomy levels" |
| "Score = Σ(criterion_i × weight_i), threshold ≥ 7.0/10" | "Score the outcome based on quality criteria" |
| "TLTK: ≥ 5 references, max 30% published before 2015" | "Include appropriate references in the syllabus" |

---

### Test 3: Obligation to Challenge Test (Đo lường Red-Team)

**Purpose**: Verify that skills have built-in mechanisms to challenge their own output, preventing hallucination and bias.

**Algorithm**:
```
FOR EACH skill's SKILL.md AND references/*.md:
    SCAN for challenge markers:
    - "Failure Mode" or "Risk" or "Edge Case" section
    - "Triangulation" or "Cross-validation" or "Đối chiếu chéo"
    - "Bias" or "Limitation" or "Giới hạn"
    - "Red Team" or "Devil's Advocate" or "Phản biện"
    - "3-Strike" or escalation protocol
    - Explicit rejection criteria ("REJECT if...", "CẤM...", "KHÔNG chấp nhận...")
    
    HAS_CHALLENGE = any markers found
    
    IF NOT HAS_CHALLENGE → 🟡 Warning (Hallucination Risk — no self-challenge mechanism)
    IF HAS_CHALLENGE → ✅ PASS
```

---

## Aggregate Epistemic Score

```
FOR EACH skill:
    trifecta = run_test_1()    # PASS / WARNING / CRITICAL
    quantification = run_test_2()  # PASS / WARNING / CRITICAL
    challenge = run_test_3()   # PASS / WARNING

    IF any test == CRITICAL → Skill Epistemic Score = 🔴 FAIL
    IF all tests == PASS → Skill Epistemic Score = ✅ EXCELLENT
    ELSE → Skill Epistemic Score = 🟡 ADEQUATE
```

This score feeds into the "Agent & Skill Quality" category of the 100-point scoring rubric.
