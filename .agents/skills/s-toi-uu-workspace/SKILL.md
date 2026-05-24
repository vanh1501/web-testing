---
name: s-toi-uu-workspace
description: >
  Orchestrate safe, deterministic self-healing of MAS workspaces using a Top-Down Cascade + PDCA methodology.
  Trang bị thuật toán Delta Self-Healing (Idempotent Microservices Rollback) và Root-Cause Tracing có khả năng Auto-Rollback.
  Use this skill whenever the agent executes `/optimize-workspace`, "self-healing", "fix audit findings",
  "remediate workspace", "chữa lỗi audit", "tối ưu workspace".
  Also trigger when an Audit Report with Score C/D/F is detected and remediation is required.
  Even if the user simply says "fix it" after an audit, trigger this skill to ensure structured repair.
---

# Workspace Optimizer

You are a Senior Reliability Engineer specializing in agentic workspace self-healing. You ensure that every repair operation follows a strict Top-Down Cascade order (Root → Trunk → Branch → Leaf) and passes a Regression Guard before being committed.

Prevent "fix-one-break-three" anti-patterns by enforcing structured remediation planning, dependency-aware execution, and post-fix regression verification. Without this skill, agents default to random-order patching which causes cascade failures.

## When to use this skill

- `/optimize-workspace` workflow invoked.
- Audit Report shows Score C (70-84), D (50-69), hoặc F (<50).
- User nói "fix audit findings", "optimize", "self-heal", "remediate", "chữa lỗi audit", "tối ưu workspace".
- Governance skill flags Major/Critical blast radius requiring structured approach.
- **KHÔNG dùng khi:** Running audits (dùng `qa`). Creating workspaces (dùng `/create-workspace`). Individual component fixes (delegate to resolvers).

## How to use it

1. Phase P (Plan): Load Audit Report → classify findings by layer (ROOT→TRUNK→BRANCH→LEAF) → generate remediation plan.
2. Phase D (Do): Execute fixes P0→P1→P2→P3 order, delegating to specialized Resolvers.
3. Phase C (Check): Per-layer verify gate + Regression Guard.
4. Phase A (Act): Final re-audit → delta report → handoff.

## When to clarify

- If the Audit Report is missing or path is invalid → ask for the correct path.
- If findings span ALL 4 layers (Root + Trunk + Branch + Leaf) AND total fixes > 20 → ask Human: "Full remediation or targeted Critical-only pass?"
- If a fix requires deleting an Agent SI or Skill that is actively wired → escalate to Human.

## Decision quan-ly-quy-tac

- If `/optimize-workspace` is invoked → **Route 1 (OPTIMIZE PIPELINE)**
- If Audit Report score is C/D/F → **Route 1 (OPTIMIZE PIPELINE)**
- If user requests "fix audit findings" → **Route 1 (OPTIMIZE PIPELINE)**

## Process

Execute the **PDCA Self-Healing Loop** for each architectural layer, strictly in Top-Down order.

### Phase P — Plan (Triage & Prioritize)

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

1. **CQS Size Gate (Pre-Check):** If Audit Report < 0.5KB → Auto-FAIL (skeleton).
2. **Load Audit Report**: Read the designated `Executive_Audit_Report.md`. Extract the `## Remediation Plan` section.
2. **Classify by Layer**: Map each finding to its architectural layer:

   | Layer | Scope | Priority |
   |---|---|---|
   | ROOT | 5-Zone dirs, data placement, root files | P0 — Fix first |
   | TRUNK | Rules, memory contracts, .agents/agents.md, HPRF | P1 — Fix second |
   | BRANCH | KB wiring, INDEX sync, agent-KB connectivity | P2 — Fix third |
   | LEAF | Agent SI quality, workflows, skills, golden tests | P3 — Fix last |

3. **Generate Remediation Plan**: Load `references/remediation-priority-matrix.md` for the priority decision tree. Output a structured plan using `assets/remediation-plan-template.md`.
4. **Root-Cause Tracing (RCT):** Không chỉ nhận diện lỗi, bắt buộc phải "lội ngược dòng" tìm ra Agent hoặc Workflow nào sinh ra lỗi đó (Ví dụ: Lỗi rác HTML trong MD thì truy ngược ra Agent Dịch thuật). Báo cáo tác nhân gây lỗi và đề xuất khóa (Lock) tác nhân đó.
5. **Dependency Pre-Scan**: For each planned fix, invoke the `giam-sat-tuan-thu` skill (change-analysis) to assess blast radius. Any Critical-blast fix → flag for Human review.

### Phase D — Do (Execute Fixes)

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

5. **Execute Layer-by-Layer**: Process fixes strictly in P0 → P1 → P2 → P3 order. Within each layer:
   - Apply the matching **Self-Healing Pattern** from `references/self-healing-patterns-root-trunk.md` (SHP-01 → SHP-09) or `references/self-healing-patterns-branch-leaf.md` (SHP-10 → SHP-26). Load ONLY the file matching the current layer.
   - Never improvise a fix pattern. If no pattern matches → STOP, log as `UNKNOWN_PATTERN`, escalate.
   - **Resolver Delegation**: For component-specific deep fixes, delegate to the specialized Resolver:

   | Layer | SHP Patterns | Delegate Resolver | Route |
   |---|---|---|---|
   | ROOT | SHP-01 (zones), SHP-02 (data vault), SHP-03 (root), **SHP-25 (Orphan DAM Taxonomy)** | `architecture` / `qa` | Route 4 (RESOLVE) |
   | TRUNK | SHP-04, SHP-05 (memory), SHP-06 (HPRF), SHP-07 (roster), **SHP-26 (Perf Drift)** | `architecture` + `giam-sat-tuan-thu` | Route 4 / HPRF injection |
   | BRANCH | SHP-08 (INDEX), SHP-09 (KB wiring) | `kb-architect` | Route 3 (RESOLVE) |
   | LEAF—Skills | SHP-11, SHP-12, SHP-16, SHP-17, SHP-19, SHP-22, SHP-23/24 | `skill-writer` | Route 3 (ADDIE Remediation) |
   | LEAF—Workflows | SHP-13, SHP-15, SHP-18, SHP-20, SHP-21 | `workflow-builder` | Route 3 (RESOLVE) |
   | LEAF—Agent SIs | SHP-10 (bloat) | `quan-ly-quy-tac` | Route 5 (RESOLVE) |
   | LEAF—Reference gaps | E2/E3 enrichment from any Resolver | `knowledge-forge` | Full pipeline |

6. **Delta Self-Healing Snapshot & Idempotent Rollback:**
   - **Tạo Snapshot:** BẮT BUỘC chụp Auto-Healer Snapshot trước khi gọi Resolver đi sửa file.
   - **Idempotency Execution:** Mọi script sửa lỗi phải được thiết kế Idempotent (chạy 1 lần hay 100 lần đều ra 1 kết quả an toàn, không tạo rác trùng lặp).
   - **Đánh giá Delta:** Tính toán Delta Score trước và sau khi vá.
   - **Rollback:** Nếu sau khi sửa mà `giam-sat-tuan-thu` báo Cảnh báo Đỏ (Blast Radius Breach) hoặc rớt Delta Score, Skill tự động kích hoạt tiến trình Microservices Rollback Strategy (hoàn nguyên state cục bộ thay vì sập toàn hệ thống).
7. **Cross-Layer Propagation**: After each fix, run `grep_search` to find all downstream files referencing the changed entity. Update ALL downstream references in the same atomic operation. Never fix one file orphan-style.
8. **Circuit Breaker:** If layer verification fails after 2 repair iterations → HALT. Log failure and escalate to Human. Do NOT loop indefinitely.

### Phase C — Check (Verify & Regression Guard)

7. **Per-Layer Verify Gate**: After completing all fixes in one layer, re-run the corresponding Audit Phase checks (Phase 2 for ROOT, Phase 3 for TRUNK, etc.).
   - Pass → proceed to next layer.
   - Fail → STOP. Log the regression. Do NOT proceed to next layer.
8. **Regression Guard**: Load `references/regression-guard-checklist.md`. Execute the 8-point checklist to verify no collateral damage was introduced.

### Phase A — Act (Close & Report)

9. **Final Re-Audit**: Execute `/audit-workspace` in full to generate a fresh score.
10. **Delta Report**: Compare pre-optimize score vs post-optimize score. Log to `QUALITY-LOG.md`.
11. **Handoff**: If Score ≥ B → mark workspace as `Operational`. If Score C → schedule follow-up optimize. If Score D/F → escalate to Human.

## Output format

The primary output is the **Remediation Execution Report** appended to `QUALITY-LOG.md`:
```
## Optimize Session [YYYY-MM-DD]
- **Pre-Score**: [Grade] ([Score]/100)
- **Post-Score**: [Grade] ([Score]/100)
- **Fixes Applied**: [count]
- **Regressions Detected**: [count]
- **Layer Summary**:
  - ROOT: [count] fixes, [PASS/FAIL]
  - TRUNK: [count] fixes, [PASS/FAIL]
  - BRANCH: [count] fixes, [PASS/FAIL]
  - LEAF: [count] fixes, [PASS/FAIL]
- **Escalated to Human**: [list or "None"]
```

## Resources

| Situation | Load |
|---|---|
| Need priority decision tree for ordering fixes (P0-P3 + 14 LEAF sub-steps) | `references/remediation-priority-matrix.md` |
| Need fix recipes for ROOT/TRUNK failures (SHP-01 → SHP-09) | `references/self-healing-patterns-root-trunk.md` |
| Need fix recipes for BRANCH/LEAF failures (SHP-10 → SHP-26) | `references/self-healing-patterns-branch-leaf.md` |
| Need post-fix regression verification checklist (8-point) | `references/regression-guard-checklist.md` |
| Need blank remediation plan template | `assets/remediation-plan-template.md` |
| Need manual-mode remediation request template (SHP-23) | `assets/remediation-request-template.md` |
| Need ROOT/TRUNK structural repair (P0, P1) | Delegate to `architecture` Route 4 |
| Need BRANCH KB repair (P2) | Delegate to `kb-architect` Route 3 |
| Need LEAF Skill repair / Structural missing 4-Tier (P3) | Delegate to `skill-writer` Route 3 (ADDIE Sub-flow) |
| Need LEAF Workflow repair (P3) | Delegate to `workflow-builder` Route 3 |
| Need LEAF Agent SI/Rule repair (P3) | Delegate to `quan-ly-quy-tac` Route 5 |
| Need reference enrichment (any layer) | Delegate to `knowledge-forge` |

## Quality checklist

- [ ] Did the agent process layers in strict P0 → P1 → P2 → P3 order?
- [ ] Did every layer pass its Verify Gate before the next layer started?
- [ ] Were all downstream references updated (no orphan fixes)?
- [ ] Was the `giam-sat-tuan-thu` skill invoked for blast radius on Major/Critical fixes?
- [ ] Does the final Re-Audit score improve or hold compared to pre-optimize?

## Rules

## Guardrails

- `Fix_Without_Plan` → [HALT]. Must generate remediation plan first.
- `Out_Of_Order_Execution` → [HALT]. Must follow P0 → P1 → P2 → P3.
- `Unknown_Fix_Pattern` → [ESCALATE]. Log as UNKNOWN_PATTERN.
- `Delete_Active_Wired_Component` → [ESCALATE]. Human approval required.
- `Missing_Audit_Report` → [HALT]. Cannot proceed without Executive_Audit_Report.md.
- `Skip_CQS_Gate` → [DENY]. Audit Report < 0.5KB = skeleton.
- `Repeated_Component_Failure > 3` → [CIRCUIT BREAKER]. HALT optimize, escalate.

## Rules

- `Fix_Leaf_Before_Root` → [DENY]. Never fix a LEAF-layer issue while a ROOT-layer issue is open.
- `Improvise_Fix_Pattern` → [DENY]. Must use documented patterns in `self-healing-patterns-root-trunk.md` or `self-healing-patterns-branch-leaf.md`.
- `Delete_Without_Blast_Radius` → [DENY]. Never delete file without `giam-sat-tuan-thu` change-analysis.
- `Skip_Regression_Guard` → [DENY]. Always execute the 8-point regression checklist.
- `Orphan_Fixes` → [DENY]. Always propagate changes to ALL downstream references atomically.
- `Start_Without_Snapshot` → [DENY]. Always generate `/snapshot` before optimize session.
