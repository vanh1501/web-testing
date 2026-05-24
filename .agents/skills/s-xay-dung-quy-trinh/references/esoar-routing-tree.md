# ESOAR Routing Decision Tree

Reference file cho OPTIMIZE mode. Load khi cần quyết định: root cause này → áp dụng ESOAR mode nào?

## When to Load

- OPTIMIZE mode Step 3 (ESOAR routing decision)
- User hỏi "nên automate hay simplify trước?"
- AUDIT mode → recommendation cần ESOAR direction

---

## ESOAR Mode Overview

ESOAR = 5 sequential approaches to process improvement:

1. **E**liminate — Loại bỏ activity hoàn toàn
2. **S**implify — Đơn giản hóa (loại step thừa, merge approvals)
3. **O**ptimize — Cải thiện flow (giảm wait, balance load)
4. **A**utomate — Tự động hóa step manual
5. **R**obotize — RPA/AI cho high-volume rule-based decisions

**Order rule** (critical): E → S → O → A → R. Reasoning:
- Eliminate trước = không cần fix cái không cần thiết
- Simplify sau = giảm target cho automation
- Automate complex/redundant process = double waste

**Anti-pattern**: jump straight to A (Automate) skipping E+S. Common mistake — kết quả là "automating waste".

---

## Decision Tree: Root Cause → ESOAR Mode

```
START: root cause của process underperformance

├── Q1: Activity này có tạo value cho customer (internal/external) không?
│   ├── NO → ELIMINATE
│   │   (Khi: report không ai đọc, approval không impact decision,
│   │    data thu thập không dùng, duplicate steps cross-team)
│   └── YES → continue Q2
│
├── Q2: Có complexity unnecessary không?
│   │      (multiple approvals cùng level, duplicate data entry,
│   │       conditional logic không apply trong 90%+ cases)
│   ├── YES → SIMPLIFY
│   └── NO → continue Q3
│
├── Q3: Có inefficient flow không?
│   │      (bottleneck, wait time, unbalanced load, handoff friction)
│   ├── YES → OPTIMIZE
│   └── NO → continue Q4
│
├── Q4: Manual work có repetitive + predictable không?
│   │      (same task >50 times/month, rule-based output)
│   ├── YES → AUTOMATE
│   └── NO → continue Q5
│
└── Q5: High-volume + rule-based + complex decisions?
        (>500 cases/month, multi-variable rules, judgment-like
         nhưng có thể encode)
    ├── YES → ROBOTIZE (RPA/AI)
    └── NO → root cause likely outside ESOAR scope
                (training, culture, system change needed)
```

---

## ELIMINATE — Detailed Guidance

### When to apply
- Activity creates zero value (ai cũng skip nếu được, ai cũng complain)
- Output không ai consume (report không ai đọc)
- Decision step không impact outcome (approval always YES)
- Redundant với activity khác

### Method
1. **Verify zero value**: ask "Nếu skip activity này, hậu quả gì?"
   - Hậu quả nhỏ/không có → confirmed candidate
   - Hậu quả lớn → not eliminate candidate, try Simplify
2. **Identify stakeholders impacted**: who's used to this activity?
3. **Pilot elimination**: skip activity 2-4 weeks trong 1 team, monitor
4. **Full elimination**: remove from SOP, communicate widely

### Worked example
**Symptom**: Monthly sales report tốn 4 hours mỗi rep gen, no one reads after Q1
**Diagnosis**: Report originally for old VP who left. New VP uses BI dashboard.
**Verify**: Ask 5 stakeholders "khi nào bạn dùng report này?" — 4/5 answer "không bao giờ"
**Action**: ELIMINATE. Save 4h × N reps × 12 months = significant FTE recovery.

### Common pitfalls
- **"Just in case" defense**: stakeholders sợ eliminate vì "lỡ cần thì sao" → ask cho example trong 12 months gần nhất. Nếu zero example → safe to eliminate.
- **Hidden consumer**: activity output có 1 person silently dùng → discover trước eliminate. Talk to all downstream.

---

## SIMPLIFY — Detailed Guidance

### When to apply
- Multiple approvals cùng authority level (3 managers ký nhưng cùng quyền)
- Duplicate data entry across systems
- Conditional logic không apply trong 90%+ cases (over-engineered for edge cases)
- Form fields no one fills meaningfully

### Method
1. **Map current complexity**: count steps, approvals, decision points, system touches
2. **Identify redundancy**: which can be merged/removed without losing control
3. **Test simplified version**: pilot trên 20% volume
4. **Roll out**: update SOP với new flow

### Worked example
**Symptom**: Báo giá B2B tốn 5 ngày, 4 approvers (Sales Manager, Pricing Manager, Finance, Legal)
**Diagnosis**: Sales Manager + Pricing Manager always agree (same data). Legal review only relevant cho contracts >500M, hiện tại review all.
**Simplification**:
- Merge Sales + Pricing approval (1 step thay vì 2)
- Legal review tự động bypass nếu deal <500M
- Result: 5 days → 2 days, 4 approvers → 2 approvers cho deals <500M

### Common pitfalls
- **Over-simplification**: simplify too aggressively → lose necessary controls. Always keep 1 review checkpoint for compliance-sensitive steps.
- **Compliance regression**: simplify step that was actually required by regulation → audit finding next year. Verify regulatory dependencies before cutting.

---

## OPTIMIZE — Detailed Guidance

### When to apply
- Bottleneck: 1 step takes >50% total cycle time
- Wait time: handoff between teams delays >24h
- Load imbalance: 1 person handles 80% volume, others idle
- Handoff friction: rework due to incomplete data passed

### Method
1. **Identify bottleneck**: time per step, where does cycle time accumulate
2. **Apply Theory of Constraints**: focus improvement on bottleneck only
3. **Re-balance load**: redistribute work, parallelize where possible
4. **Improve handoff quality**: standardize data passed between steps

### Worked example
**Symptom**: Customer complaint resolution average 7 days, target 3 days
**Diagnosis**: Step 3 (technical investigation) average 4 days. Bottleneck.
**Optimize**:
- Add 1 tech specialist (capacity boost)
- Parallelize: while tech investigates, CS prepares response draft (saves 1 day)
- Standardize complaint intake (Step 1) để Step 3 không thiếu data → reduce rework
- Result: 7 days → 2.5 days

### Common pitfalls
- **Optimize non-bottleneck**: improve Step 1 từ 1 day → 0.5 day, but bottleneck Step 3 không change → zero total time saved. Always identify bottleneck first.
- **Local optimization vs global**: optimizing step A causes step B downstream to slow (load shift). Check end-to-end impact.

---

## AUTOMATE — Detailed Guidance

### When to apply
- Manual repetitive task: same activity >50 times/month
- Rule-based output: deterministic input → output mapping
- High accuracy needed: human error rate >5%
- Time-sensitive: needs to run 24/7 or peak times

### Method
1. **Confirm E+S done first**: KHÔNG automate waste
2. **Document rules explicitly**: every conditional, every exception
3. **Choose tool**: macros, scripts, low-code platforms, RPA tools
4. **Phased rollout**: parallel run (manual + automated) 2-4 weeks, compare outputs
5. **Cutover**: when accuracy verified

### Worked example
**Symptom**: Monthly sales commission calc tốn 3 days, kế toán làm manual Excel
**Diagnosis**:
- E check: commission calc essential? YES, can't eliminate.
- S check: complexity necessary? Yes — multi-tier rates, multi-channel.
- O check: bottleneck? Single person doing it.
- A: Manual? Yes, repetitive, rule-based → automate candidate.
**Action**: Build automated calc tool (formulas + reference rate table). 3 days → 30 mins.

### Common pitfalls
- **Automating waste**: skip E+S → automate complex process that should be simplified first → tool harder to maintain, brittle
- **Edge case explosion**: automation logic tries to cover all exceptions → unmaintainable. Better: automate 80% common cases, manual escalation 20%.
- **No fallback**: tool breaks → entire process halts. Keep manual fallback procedure.

---

## ROBOTIZE — Detailed Guidance

### When to apply
- High volume: >500 cases/month
- Multi-variable rules: 10+ conditions per decision
- Complex pattern matching needed
- Decisions look like judgment but có thể encode (loan approval, fraud detection, customer scoring)

### Method
1. **Confirm A done first**: KHÔNG robotize unless simpler automation insufficient
2. **Data quality assessment**: RPA/AI needs clean structured data
3. **Build training set**: historical decisions với outcomes
4. **Pilot on subset**: small volume parallel run
5. **Human-in-the-loop**: maintain review for high-stakes decisions

### Worked example
**Symptom**: B2B credit approval mất 2-5 days per case, 800 cases/month
**Diagnosis**:
- E+S+O+A done → still 1 day average
- Volume high (800/month), rule-based (financial criteria)
- → Robotize candidate
**Action**: RPA scoring tool. Auto-approve clear cases (<50M and clean credit), escalate borderline (50-500M), human review high-stakes (>500M). 2-5 days → 1 hour for 70% cases.

### Common pitfalls
- **Black box decisions**: AI tool có thể bias hoặc opaque. Cần explainability cho regulated industries.
- **Over-trusting automation**: humans rubber-stamp AI decisions → defeats purpose of human review. Train reviewers actively challenge.
- **Maintenance debt**: AI models drift over time → require retraining cadence.

---

## Order Rule Exceptions

E → S → O → A → R is default. Exceptions:

1. **Time-bounded automation**: regulator requires automation by deadline (e.g., e-invoicing) → AUTOMATE first, then ESO refinements after.

2. **Greenfield process** (CREATE mode, not OPTIMIZE): không có existing waste để E/S, design optimized + automated từ đầu nếu volume justifies.

3. **Strategic differentiation**: process là competitive advantage → invest A/R even if E/S would suffice. (Rare — most processes don't justify this.)

---

## Decision Worksheet Template

Khi tư vấn user, fill table này:

| Step | Question | User answer | ESOAR mode candidate |
|------|----------|-------------|---------------------|
| Q1 | Activity zero-value? | YES/NO | Eliminate if YES |
| Q2 | Complexity unnecessary? | YES/NO | Simplify if YES |
| Q3 | Inefficient flow? | YES/NO | Optimize if YES |
| Q4 | Manual repetitive predictable? | YES/NO | Automate if YES |
| Q5 | High-volume rule-based decisions? | YES/NO | Robotize if YES |

Multiple YES → tackle in ESOAR order (left to right).

All NO → root cause likely outside ESOAR scope. Investigate:
- Training/skill gap?
- Culture/motivation?
- System architecture (not process)?
- Strategy alignment (process trying to do wrong thing)?

---

## Cross-Mode Patterns

### After ELIMINATE
Re-audit removed activity 30/60/90 days. If hậu quả emerge (e.g., compliance gap surfaces) → re-introduce with simplified version. Skip ELIMINATE in next iteration.

### After AUTOMATE
Schedule quarterly review: automation still relevant? Volume still high? Rules still valid? Automation drift = silent failure.

### After ROBOTIZE
Maintenance cadence required: model retrain quarterly, accuracy monitoring monthly, governance review semi-annually.
