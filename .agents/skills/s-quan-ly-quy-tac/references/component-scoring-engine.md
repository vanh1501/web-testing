# Rule Scoring Engine — 5-Dimension Rubric (100 Points)

> Reference document for the `quan-ly-quy-tac` skill, Route 2 (AUDIT).
> Contains the scoring algorithm for Rule files.
> Agent MUST load this file when executing deep assessment delegated by `qa` or standalone.

---

## Pre-Check: CQS Size Gate

| Condition | Result |
| --- | --- |
| File size < 0.5 KB | Auto-FAIL — skeleton file |
| File size 0.5 KB – 15 KB | ✅ Proceed to scoring |
| File size > 15 KB | 🟡 WARNING — possible context bloat. Flag for Route 4 Red-Zone. |

## R1 — HPRF Compliance (25 pts)

```text
+10 : HPRF Override Priority block exists at file top
+10 : Tier classification is correct (Constitution=T1, Standards=T2, Domain=T3)
+5  : Conflict resolution rule stated ("In case of conflict, this file overrides...")

Penalties:
-15 : No HPRF block at all — rule has no conflict resolution
-5  : HPRF block exists but tier is misclassified
```

## R2 — Structure Quality (20 pts)

```text
+5  : Has heading level 1 (single # title)
+5  : Has ≥ 2 major sections
+5  : Each section has ≥ 2 concrete quan-ly-quy-tac
+5  : Uses imperative language ("Do X", not "You should try...")

Penalties:
-5  : No clear sections — flat dump of quan-ly-quy-tac
-5  : Sections have only 1 rule each (thin content)
```

## R3 — CLEAR Score (25 pts)

Apply the 5-dimension CLEAR framework (5 pts each):

```text
+5  : C (Concrete) — No vague words ("appropriate", "good", "better")
+5  : L (Leveled) — Uses MUST/SHOULD/MAY with MUST ≤ 30% of quan-ly-quy-tac
+5  : E (Exampled) — Complex quan-ly-quy-tac have ✅/❌ example pairs
+5  : A (Actionable) — Agent knows exactly which tool/folder/file to use
+5  : R (Ranked) — HPRF tier declared, conflict resolution explicit
```

> For detailed CLEAR specification, anti-patterns, and fix patterns,
> load `references/rule-design-intelligence.md` Part 1.

## R4 — Content Specificity (20 pts)

```text
+10 : Rules are domain-specific (not generic copy-paste from baseline)
+5  : Rules reference specific files, paths, or tools
+5  : No placeholder content ("[điền vào đây]", "TODO")

Penalties:
-10 : Rules are verbatim copies of baseline templates (>80% overlap with L0)
-5  : Contains placeholder content
-3  : Rules are so generic they apply to any workspace
```

## R5 — Wiring Integrity (10 pts)

```text
+5  : Rule file is referenced by ≥1 workflow, skill, or GEMINI.md
+5  : No orphan quan-ly-quy-tac (quan-ly-quy-tac that nothing references)

Penalties:
-5  : Rule file exists but nothing in the system references it
```

## Grade Thresholds

| Score | Grade | Label | Action |
| --- | --- | --- | --- |
| 85–100 | **A** | ✅ Production-ready | Monitor only |
| 70–84 | **B** | 🔶 Good, minor gaps | Quick patch |
| 55–69 | **C** | ⚠️ Functional but weak | Repair → Route 3 |
| 40–54 | **D** | 🔴 Significant issues | Full rework → Route 3 |
| < 40 | **F** | ❌ Non-functional | Rebuild → Route 1 |
