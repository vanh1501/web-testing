# Audit 5 Dimensions — Scoring Rubric

Reference file cho AUDIT mode. Load khi user trigger health check/portfolio review.

## When to Load

- AUDIT mode active
- OPTIMIZE mode đang trong Step 1 (AS-IS mini-audit)
- User hỏi "process X có healthy không?"

---

## 5 Dimensions Overview

Mỗi quy trình được score trên 5 độc lập dimensions, scale 1-5. Total /25.

| # | Dimension | Câu hỏi cốt lõi | Evidence source |
|---|-----------|-----------------|----------------|
| 1 | **Effectiveness** | Process có đạt target outcome không? | KPI dashboard, achievement reports |
| 2 | **Efficiency** | Process tốn time/cost hợp lý vs benchmark? | Time logs, resource utilization |
| 3 | **Compliance** | Process tuân thủ regulation/policy? | Audit log, deviation count |
| 4 | **Adaptability** | Process chịu được volume spike/scope change? | Stress test results, historical pattern |
| 5 | **Ownership clarity** | Process có 1 named owner accountable? | RACI doc, escalation history |

**Total score interpretation**:
- 🔴 Red (≤10) → Immediate remediation required
- 🟡 Yellow (11-17) → Monitor + improvement roadmap
- 🟢 Green (18-25) → Healthy, periodic review

**Override rule**: bất kỳ single dim ≤2 → escalate regardless of total score.

---

## Dimension 1: Effectiveness

### Definition
Process có đạt target outcome đã định không? Đo % KPI achievement vs target.

### Scoring rubric

| Score | Criteria | Evidence |
|-------|----------|----------|
| **5** | KPI achievement >95%, sustained across 12+ months | Monthly KPI dashboard với target line |
| **4** | KPI achievement 85-95% | Same as above |
| **3** | KPI achievement 70-85% | Same as above |
| **2** | KPI achievement 50-70%, hoặc inconsistent | Dashboard + investigation notes |
| **1** | KPI achievement <50%, hoặc KPI chưa được define | KPI doc thiếu hoặc miss prevalent |

### Evidence source checklist
- [ ] KPI definition document (target + measurement method)
- [ ] Monthly/quarterly KPI tracking (≥6 months data ideal)
- [ ] Target setting rationale (data-driven vs gut feel)

### Common pitfalls
- **KPI gaming**: KPI tăng nhưng business outcome flat → score Effectiveness thấp (1-2) regardless of process KPI
- **No KPI defined**: process operating "by feel" → auto-score 1
- **Vanity metrics**: KPI đẹp nhưng không link business outcome → require lineage trace

---

## Dimension 2: Efficiency

### Definition
Process tốn time/cost reasonable vs benchmark? Đo cycle time + resource usage.

### Scoring rubric

| Score | Criteria | Evidence |
|-------|----------|----------|
| **5** | Cycle time ≤benchmark, resource usage optimal | Time logs + benchmarking data |
| **4** | Cycle time within 110% benchmark | Same |
| **3** | Cycle time 110-150% benchmark | Same |
| **2** | Cycle time 1.5-2x benchmark | Same |
| **1** | Cycle time >2x benchmark, hoặc no measurement | Time logs missing or shows extreme outliers |

### Evidence source checklist
- [ ] Cycle time measurement (entry-to-exit time per case)
- [ ] Benchmark data (industry average, internal historical, competitor)
- [ ] Resource utilization (FTE × time spent)

### Maturity-adjusted scoring
- **L0-L1 departments**: thường thiếu cycle time data → score này có thể SKIP. Flag explicit: "Adaptability and Efficiency cannot be scored due to missing baseline. Recommendation: setup measurement first."
- **L2+ departments**: should have data. Score 1 nếu data exists but cycle time >2x benchmark.

### Common pitfalls
- **Bottleneck blind**: average cycle time looks OK nhưng có 1 step là bottleneck (P90 cycle time x3 P50) → score lower
- **Hidden rework**: cycle time logged không include rework cycles → undercount

---

## Dimension 3: Compliance

### Definition
Process tuân thủ regulation/policy + internal rules? Đo audit findings + deviation count.

### Scoring rubric

| Score | Criteria | Evidence |
|-------|----------|----------|
| **5** | Zero deviation in last 12 months, audit findings = 0 | Compliance audit log |
| **4** | <3 minor deviations, 0 major findings | Same |
| **3** | <10 minor, <2 major findings | Same |
| **2** | Multiple major findings, repeated minor patterns | Same + investigation reports |
| **1** | Systematic non-compliance, regulator/auditor concerns | Same + external citations |

### Evidence source checklist
- [ ] Internal audit log (annual hoặc semi-annual)
- [ ] External regulator findings (nếu áp dụng — tax, labor, industry-specific)
- [ ] Deviation tracking system (per-incident log)

### Domain-specific compliance areas
- **Finance**: VN GAAP, tax filing deadlines, audit committee requirements
- **HR**: VN labor law, social insurance, payroll regulation
- **Sales**: contract terms, pricing policy, channel agreement
- **Operations**: safety, environmental, product quality standards

### Common pitfalls
- **"Chưa bị bắt" ≠ compliant**: absence of findings không = compliance. Check whether audit actually happened.
- **Internal vs external compliance**: 2 separate scores. Lower of two = final score.

---

## Dimension 4: Adaptability

### Definition
Process chịu được volume spike, scope change, exception case không? Đo via stress test hoặc historical pattern.

### Scoring rubric

| Score | Criteria | Evidence |
|-------|----------|----------|
| **5** | Handled 3x normal volume in past 12 months without redesign | Historical spike data |
| **4** | Handled 2x normal volume successfully | Same |
| **3** | Handled 1.5x normal volume với minor strain | Same + qualitative reports |
| **2** | Break point ≤1.5x normal volume | Same + incident logs |
| **1** | Cannot handle any volume spike OR no spike history | No data hoặc immediate breakdown |

### Evidence source checklist
- [ ] Volume history (peak vs normal periods, e.g., Tết, year-end, campaign launches)
- [ ] Incident logs during peak periods
- [ ] Process redesign frequency (frequent redesign = low adaptability)

### Maturity-adjusted scoring
- **L0-L1**: thường skip này (chưa đủ history data). Note: "Adaptability cannot be scored. Require minimum 12-month operating history."
- **L2+**: should have. Pay attention to Tết Q1 + year-end Q4 spike patterns trong VN context.

### Common pitfalls
- **Heroic recovery**: process "handled" spike vì 1 person làm overtime → score 1-2 (bus-factor risk, not real adaptability)
- **Scope creep handling**: process designed cho 1 product line, có handle product 2,3,4 chưa? Test trên expansion scenarios.

---

## Dimension 5: Ownership Clarity

### Definition
Process có 1 named owner accountable không? RACI có gap không?

### Scoring rubric

| Score | Criteria | Evidence |
|-------|----------|----------|
| **5** | 1 named owner + named backup + clear escalation, RACI complete | RACI doc + escalation tree |
| **4** | 1 named owner, backup ambiguous | Same |
| **3** | Owner identified ở role level (not name), RACI mostly complete | Same |
| **2** | Owner mơ hồ ("team X"), RACI có gaps (missing R hoặc A on some activities) | Same — gaps documented |
| **1** | Orphan process (no clear owner), multiple A or no A | Same — investigation notes |

### Evidence source checklist
- [ ] RACI matrix document (formal, signed)
- [ ] Escalation tree (when issue arises, who decides)
- [ ] Onboarding doc cho new joiners explicit process owner

### VN context — Shadow Influence Check
Standard RACI có thể trông OK nhưng thực thi méo mó vì hierarchy bypass:
- Ask: "Khi process có conflict, RACI nói X quyết nhưng thực tế ai *thực sự* ra quyết định?"
- Nếu shadow influence ≠ RACI → flag hidden ownership ambiguity. Score 2-3 even if doc looks complete.

### Common pitfalls
- **Hoa hồng RACI**: ai cũng Consulted → ownership diluted → score 2-3
- **Family business override**: family member silent override → score lower với note
- **Recent re-org**: ownership chưa stabilized post-restructure → temporary score lower với revisit timeline

---

## Maturity-Adjusted Scoring Profiles

### L0-L1 Departments (Ad-hoc / Basic)
Score chỉ 3 dimensions: Effectiveness + Compliance + Ownership
Skip: Efficiency + Adaptability (insufficient baseline data)
Max score: 15 (3 dims × 5). Red threshold = ≤6.

**Why skip**: chấm Efficiency without baseline = arbitrary. Chấm Adaptability without history = guesswork.

### L2 Departments (Standardized)
Score all 5 dimensions. Standard rubric applies.

### L3+ Departments (Optimized/Enterprise)
Score all 5 dimensions + supplementary checks:
- Cross-process integration health
- KPI lineage trace (process → business outcome)
- Change management maturity (how frequently does process evolve)

---

## Heat Map Visualization Pattern

After scoring, output heat map table:

```
| Process | Eff | Eff | Comp | Adapt | Own | Total | Zone | Trend |
|---------|-----|-----|------|-------|-----|-------|------|-------|
| KD-11   |  4  |  3  |  5   |  3    |  4  |  19   | 🟢   | ↑     |
| KD-07   |  3  |  2  |  4   |  2    |  3  |  14   | 🟡   | →     |
| HR-03   |  2  |  -  |  3   |  -    |  2  |  7/15 | 🔴   | ↓     |
```

`-` = not scored (maturity-adjusted). Trend = vs previous audit period.

---

## Output Recommendations Pattern

Per red zone process, structured recommendation:

```
### [Process Code] — Red Zone (Score [N]/25)

**Weak dimensions**:
- [Dim name]: [Score] — [Why low]

**Root cause hypothesis** (apply Critical Thinking):
- [Hypothesis 1] supported by [evidence]
- [Hypothesis 2] supported by [evidence]

**Recommended action**:
- Immediate (≤30 days): [Specific action]
- Medium-term (30-90 days): [Specific action]
- Recommendation: trigger OPTIMIZE mode cho process này

**Owner**: [Named individual]
**Re-audit date**: [+90 days]
```

Push user to specific next steps. KHÔNG abstract recommendations.
