---
name: s-quan-ly-quy-tac
description: >
  Write, audit, optimize, and lifecycle-manage Workspace Governance Rules using
  the CLEAR framework, CQS validation, and URLP (Unified Rule Lifecycle Pipeline).
  Use this skill for "viết quan-ly-quy-tac", "audit quan-ly-quy-tac", "optimize quan-ly-quy-tac", "MECE check",
  "fix rule quality", "tạo L0/L1", "nén rule", "kiểm tra xung đột rule".
  Also trigger during `/create-workspace` Phase 3 for Rule Factory,
  `/audit-workspace` Phase 4 for Governance scoring,
  or `/optimize-workspace` Round 2C for Rule enforcement.
  Even if the user only says "fix the rule file", trigger this to enforce CLEAR + CQS validation.
  Trang bị Abstract Syntax Tree (AST) Dependency Graphing, Boolean Logic Constraint Synthesis, và Backport Golden Extraction Engine.
---

# Kỹ Sư Tiêu Chuẩn & Luật Lệ (Standards Officer)

Senior Standards Officer — RESOLVER in Diagnostician→Resolver pipeline for Rule component layer. Receives findings from `qa` skill (Phase 4), executes: create quan-ly-quy-tac, 5-dim scoring, CLEAR assessment, repair/enrich deficient files. Rejects vague instructions, placeholders, and "paper tiger" quan-ly-quy-tac. Every rule must be deterministic enough for an agent to execute without clarification.

> [!IMPORTANT]
> **Scope Boundary:** This skill manages **Governance Rule files** ONLY (`.agents/quan-ly-quy-tac/L0-*`, `L1-*`, `L2-*`).
> Agent SI quality is handled by the Phantom Agent Registry (`L1-swarm-registry.md`) via `qa` skill.
> Skill quality is handled by `skill-writer`. Workflow quality is handled by `workflow-builder`.

## When to use this skill

- `/create-workspace` Phase 3 (writing giam-sat-tuan-thu quan-ly-quy-tac for new workspace).
- `/optimize-workspace` Round 2C (Rule HPRF injection, constraint logic, compression).
- `/audit-workspace` Phase 4 (Governance & Policy scoring).
- User nói "viết quan-ly-quy-tac", "fix rule file", "validate rule quality", "audit rule", "MECE check".
- User paste a Rule file và hỏi "cái này ổn không?".
- **KHÔNG dùng khi:** Workspace-level audits (dùng `qa` skill). Agent SI/Phantom Registry (dùng `qa`). Skill issues (dùng `skill-writer`). Workflow issues (dùng `workflow-builder`).

## How to use it

The `quan-ly-quy-tac` skill operates on a **Unified Rule Lifecycle Pipeline (URLP)** — 5 sequential routes mapping the full lifecycle of a workspace rule from inception to maturity:

```
ROUTE 1: BIRTH    →  Create/Refactor Rules (L0/L1 Factory)
ROUTE 2: AUDIT    →  Score Rules (L0 Parity + CLEAR + CQS + 5-Dim)
ROUTE 3: REPAIR   →  Fix Failing Rules (RR1-RR5 Protocols + Closed-Loop)
ROUTE 4: EVOLVE   →  Optimize Rule Architecture (MECE + Cross-Layer + Golden Extraction)
ROUTE 5: BACKPORT →  Extract Non-Domain Golden Rules & Sync-back to Master Repo
```

## When to clarify

- **Route 1 (BIRTH):** Ask target workspace domain. Ask if L0 should be copied from Master or custom.
- **Route 2 (AUDIT):** Ask if scoring is strict (all 5 dimensions) or focused. Ask depth: `--quick` or `--deep`.
- **Route 3 (REPAIR):** Ask if auto-repair is authorized. If rule is actively wired, confirm before modifying.
- **Route 4 (EVOLVE):** Ask if Red-Zone compression is approved. Ask if Cross-Layer scan should reference Master Repo L0 or local L0 copy.
- **Route 5 (BACKPORT):** Ask for explicit Human Approval before overwriting any file in the Master Repo (`MAS-Master-Repo/.agents/quan-ly-quy-tac/`).

## Decision quan-ly-quy-tac

- If user asks to "tạo rule", "viết L1", "create L0/L1" → **Route 1 (BIRTH)**
- If user asks to "đánh giá CLEAR", "chấm điểm rule", "audit quan-ly-quy-tac" → **Route 2 (AUDIT)**
- If `workspace-optimizer` delegates repair, or user says "fix rule" → **Route 3 (REPAIR)**
- If user asks to "kiểm tra MECE", "lọc trùng lặp rule", "nén L1", "optimize quan-ly-quy-tac" → **Route 4 (EVOLVE)**
- If user asks to "đồng bộ về master", "backport rule", "rút lõi template" → **Route 5 (BACKPORT)**
- If `qa` delegates Rule findings (Phase 4) → **Route 2 (AUDIT)** then handoff to **Route 3 (REPAIR)**
- If the domain for an L1 rule is unknown → HALT and execute `search_web` or ask user.

## Process

### Route 1: BIRTH — Create / Refactor Rules (L0/L1 Factory)

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

1. **8-File Skeleton Injection (Guardrails):** Khi tạo/sửa rule cho Workspace con, BẮT BUỘC ép khung xương 8-file chuẩn y hệt Master Repo:
   - 4 file `L0` (Constitution, Safety, Routing, Identity).
   - 2 file `L1` (Workspace Standards, Swarm Operations).
   - `L1-core-cheatsheet-fallback.md` và `L2-CHANGELOG.md`.
   - Cập nhật Tên Agent / Mission cho phù hợp ngành, giữ nguyên Ràng buộc (Constraints).
2. **Domain Intelligence Pipeline (DIP):** For Domain Workspaces ONLY. Load `references/domain-intelligence-pipeline.md` → Execute 3-Phase: Discovery (≥3 searches) → Translation (Research → CoD) → Validation (source trace, hallucination filter).
3. **Domain Decoupling (Trục xuất Nghiệp vụ):** CẤM lưu trữ logic chuyên ngành, SOP thao tác, hoặc phương pháp tư duy vào Rule. Nếu Workspace con có đống Rule lôm côm → BỨT RA và chuyển sang `KB/standards/cognitive-components/` hoặc `.agents/skills/`. Rule CHỈ chứa lệnh cấm và nguyên tắc an toàn.
4. **Roster Mutation:** Cập nhật file `L1-swarm-operations.md` để điền danh sách Roster thực tế của Workspace con. Cập nhật `l0-identity-and-scope.md` cho đúng Domain.
5. **Red-Zone Insurance:** BẮT BUỘC nén lõi vào `l1-core-cheatsheet-fallback.md`.
6. **Rules Structure (Chain of Draft):** BẮT BUỘC viết Rule bằng ngôn ngữ Điện tín (Telegraphic Shorthand) và **Boolean Logic Constraint Synthesis** (`IF -> THEN -> HALT`). Tuyệt đối KHÔNG viết văn xuôi giải thích, nhằm đảm bảo Agent có thể parsing logic một cách toán học không bị Hallucination. Ensure heading level 1, HPRF block, ≥2 sections. Tham chiếu `references/baseline-rule-checklist.md`.
7. **Root Linkage (IDE Wiring):** BẮT BUỘC load File `references/root-wiring-protocol.md` để thực thi đấu nối. Đặc vụ BẮT BUỘC phải TỰ ĐỘNG tiêm khối YAML `trigger: always_on` vào đầu các tệp L0 để IDE tự động nhận diện thành Custom Rules mà KHÔNG bắt User phải cấu hình bằng tay. Đồng thời đấu link các file L0 vào ngực tệp `GEMINI.md`.

**Route 1 Verification Evidence:**
- [ ] Exact 8-file Guardrail Skeleton injected (no random domain L1s left).
- [ ] DIP executed (Domain Workspace only): ≥3 sources, ≥2 risk dimensions documented.
- [ ] Domain Decoupling verified: 0% methodology/SOPs inside `.agents/quan-ly-quy-tac/`.
- [ ] `L1-swarm-operations.md` updated with custom Roster.
- [ ] `L1-core-cheatsheet-fallback.md` generated with `alwaysApply: false`.
- [ ] Chain of Draft enforced: All quan-ly-quy-tac use Telegraphic Shorthand and Boolean Constraints (no prose).

### Route 2: AUDIT — Score Rule Quality (5-Dim + CLEAR + CQS)

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

1. **Pre-Check CQS Size Gate:** File < 0.5KB = Auto-FAIL (skeleton). File > 15KB = 🟡 WARNING (context bloat). Load `references/component-scoring-engine.md`.
2. **L0 Parity Check (MANDATORY):** Fetch the corresponding L0 rule from Master Repo (`MAS-Master-Repo/.agents/quan-ly-quy-tac/`). Compare 1:1 against the local workspace L0. Missing any Hard-Stops or Safety boundaries = 🔴 FAIL.
3. **5-Dimension Scoring (100 pts):** Score each Rule across R1-R5:
   - **R1 — HPRF & L0 Compliance (20 pts):** Override Priority block, tier classification, L0 Parity adherence.
   - **R2 — Structure & CoD Format (20 pts):** Heading hierarchy, ≥2 sections, Telegraphic Shorthand (Boolean Constraints, no prose), ≥2 quan-ly-quy-tac/section.
   - **R3 — CLEAR Score (20 pts):** Concrete, Leveled, Exampled, Actionable, Ranked (4 pts each).
   - **R4 — Content Specificity & Domain Grounding (25 pts):** Domain-specific vs generic, references specific files/paths, no placeholders. For Domain Workspaces: claims must be traceable to `search_web` sources (DIP Phase 3). Ungrounded domain claims = Auto-FAIL R4.
   - **R5 — Wiring Integrity (15 pts):** Referenced by ≥1 workflow or agent, no orphan quan-ly-quy-tac.
3. **CLEAR Framework Deep Dive:** Score each rule across 5 sub-dimensions (Concrete, Leveled, Exampled, Actionable, Ranked). Full rubric in `references/component-scoring-engine.md`.
4. **Root Cause Analysis:** For each failing dimension, identify the specific root cause and map to repair protocol (RR1-RR5).
5. **Triage & Report:** Generate scorecard using `assets/component-audit-report-template.md`. Classify findings using `references/finding-handoff-schema.md`.
6. **Handoff:** Return findings → Route 3 (REPAIR). Or if standalone → ask user "Repair Critical first?"

**Grade Thresholds:** A (85-100) ✅ | B (70-84) 🔶 | C (55-69) ⚠️ | D (40-54) 🔴 | F (<40) ❌

**Route 2 Verification Evidence:**
- [ ] L0 Parity Check executed against Master Repo.
- [ ] ALL Rules scored across 5 dimensions (no subset).
- [ ] CLEAR assessment applied (5 sub-dimensions explicitly scored).
- [ ] Report uses template structure — not freeform text.

### Route 3: REPAIR — Fix Failing Rules (Closed-Loop Pipeline)

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

1. **Accept Diagnosis:** Parse findings using `references/finding-handoff-schema.md` format. Map root causes to repair protocols RR1-RR5. Load `references/component-repair-protocols.md`.
2. **Propose Fix Strategy:** Generate action plan per rule file. Present for Human approval before executing.
3. **Execute Repairs:** Apply matched protocol in priority order:
   - **RR1 (HPRF Injection):** Analyze content → determine Tier (1=Constitution, 2=Standards, 3=Domain) → inject HPRF block.
   - **RR2 (Structure Repair):** Organize flat dumps into ≥2 logical sections, enforce heading hierarchy.
   - **RR3 (CLEAR Enhancement):** Replace vague terms → add MUST/SHOULD/MAY → add ✅/❌ examples → add file/tool paths → inject HPRF.
   - **RR4 (Domain Customization):** Replace verbatim baseline copies with domain-specific content. Load `references/domain-intelligence-pipeline.md` → Execute DIP Phase 2-3 for grounded domain constraints.
   - **RR5 (Orphan Resolution):** Run `grep_search` → if zero references found → add wiring or recommend deprecation.
   - **RR6 (CoD Conversion):** Scan rule file for prose sentences > 15 words → Compress each into `Condition -> [Action]` format. Remove pronouns, conjunctions, explanatory text.
4. **Closed-Loop Re-Score (MANDATORY):** Re-run Route 2 (AUDIT) scoring engine on ALL repaired quan-ly-quy-tac. Compare `before_score` vs `after_score` across each dimension.
5. **Circuit Breaker:** If `after_score < Grade B (70 pts)` after 2 repair iterations → HALT. Log failing rule to `Failed_Optimization_Log.md` and escalate to Human Review. Do NOT loop indefinitely.
6. **Delta Report:** Before/after comparison using `assets/component-audit-report-template.md` Template 2. This step MUST NOT execute without Step 4 completing first.

**Route 3 Verification Evidence:**
- [ ] Delta report generated with before/after scores.
- [ ] Grep checks run before deleting/modifying wired quan-ly-quy-tac.
- [ ] Re-Score (Step 4) executed — Route 3 MUST NOT terminate without re-scoring.
- [ ] Circuit Breaker triggered if < Grade B after 2 iterations.

### Route 4: EVOLVE — Optimize Rule Architecture (MECE + Cross-Layer)

> [!WARNING] Bạn phải trích xuất Socratic OTC Check trước khi thao tác Tool

1. **Skeleton Check:** Có đủ 8 file Guardrail? `MASTER-INDEX.md` link chuẩn? File rule ngoài 8-skeleton = 🔴 [HALT] → Route 1 Domain Decoupling.
2. **Component Leak Detection:** Quét rule files cho Cognitive/SOP leakage. Có = 🔴 WARNING → Bứt ra thành Skill/Component.
3. **MECE (Overlap & Gap Analysis):** Load `references/baseline-rule-checklist.md`.
   - **ME-Check:** L1 files dẫm chân nhau → Merge.
   - **CE-Check:** Đối chiếu 5 Chiều (Governance, Safety, Routing, Operations, Swarm). Thiếu file = 🔴 Gap.
4. **Red-Zone Compression:** File > 15KB → Băm 50% → `local_datawarehouse` + ép lõi vào `L1-core-cheatsheet-fallback.md`.
5. **Cross-Layer Conflict Detection (AST-Style Dependency Graphing):** Sử dụng thuật toán phân tích cây phụ thuộc Abstract Syntax Tree (AST) Dependency Graphing (bằng cách dùng `grep_search` và RAG mapping) quét nội dung các file L0 gốc (từ Master Repo hoặc bản sao tại workspace) so sánh chéo với toàn bộ file `L1-*`. Nếu phát hiện L1 mâu thuẫn trực tiếp với L0 (override priority conflict) → 🔴 [SYSTEMIC-HALT]. Nếu phát hiện L1 trùng lặp hoàn toàn với L0 (verbatim copy > 80%) → 🟡 WARNING + đề xuất xóa L1 dư thừa.
6. **Domain Risk Coverage Scan (Domain Workspace only):** Load `references/domain-intelligence-pipeline.md` → Execute DIP Phase 1 (Discovery) → Compare discovered risks against existing L1 quan-ly-quy-tac → Report uncovered risks as 🔴 Gaps.
7. **Golden Rule Candidate Extraction:** Identify newly created, non-domain specific quan-ly-quy-tac (e.g., enhanced safety mechanisms, anti-injection layers). Tag them as `[Golden Candidate]` and propose execution of **Route 5 (BACKPORT)**.

**Route 4 Verification Evidence:**
- [ ] MECE 5-Dimension Gap Analysis completed against baseline checklist.
- [ ] Red-Zone compression executed correctly if file > 15KB.
- [ ] Cross-Layer scan executed: L0 vs L1 conflict/duplication check completed.
- [ ] Domain Risk Coverage: DIP Phase 1 executed.
- [ ] Golden Candidates identified and proposed for Backport.

### Route 5: BACKPORT — Extract Golden Rules & Sync-back to Master Repo

> [!CAUTION] GHI ĐÈ MASTER REPO LÀ THAO TÁC RẤT NHẠY CẢM. BẮT BUỘC Socratic OTC Check VÀ Human Approval!

1. **Verify Golden Candidate:** Parse rule proposed from Route 4. Ensure it contains ZERO domain-specific jargon (e.g. "Lecturer", "Student", "LMS", "CRM"). If domain logic exists → Bứt ra (Decouple) and abstract it into generic giam-sat-tuan-thu/safety language.
2. **Target Identification:** Determine which Master Repo file (`MAS-Master-Repo/.agents/quan-ly-quy-tac/`) the rule belongs to (e.g., L0-Safety, L0-Constitution, L1-Crud).
3. **Draft Merge Proposal:** Create a diff plan showing exactly how the Golden Rule will be injected into the Master Repo template without breaking existing HPRF structures.
4. **Human Approval:** 🔴 [HALT] Request Human approval before executing Write/Multi-Replace to Master Repo.
5. **Execute Backport:** Write the extracted, sanitized rule into the Master Repo.
6. **Verify Parity:** Execute Route 2 (L0 Parity Check) to ensure the Master Repo is structurally sound after the injection.

**Route 5 Verification Evidence:**
- [ ] Rule abstracted (100% Non-Domain).
- [ ] Diff plan generated.
- [ ] Human Approval obtained.
- [ ] Multi_replace/Write_to_file executed on Master Repo.

## Output format

- **Route 1 (BIRTH):** Generated/refactored file content as markdown. Root wiring confirmation.
- **Route 2 (AUDIT):** Rule Scorecard (5-Dim table) + CLEAR score breakdown + CQS compliance report + L0 Parity Results.
- **Route 3 (REPAIR):** Delta Report per rule (before/after) + remaining human TODOs.
- **Route 4 (EVOLVE):** MECE analysis report + Cross-Layer conflict matrix + Golden Candidates List.
- **Route 5 (BACKPORT):** Sync-back diff report + Confirmation of Master Repo update.

## Resources

| Situation | Load |
| --- | --- |
| Need 5-Dim Rule scoring rubric (Route 2) | `references/component-scoring-engine.md` |
| Need repair protocols RR1-RR5 (Route 3) | `references/component-repair-protocols.md` |
| Need standardized Finding→Repair handoff format (Route 3) | `references/finding-handoff-schema.md` |
| Need output templates for audit reports and delta | `assets/component-audit-report-template.md` |
| Need baseline file checklist for Rule creation | `references/baseline-file-checklist.md` và `KB/standards/Workspace_Architectural_Blueprints/kb-antigravity-workspace-standard.md` (Phần 4) |
| Need guidelines for modifying GEMINI.md and binding quan-ly-quy-tac | `references/root-wiring-protocol.md` |
| Need troubleshooting guide for common build issues | `references/builder-troubleshooting.md` |
| Need rule design best practices and anti-patterns | `references/rule-design-intelligence.md` |
| Need CQS per-component specifications | `.context/standards/component-quality-spec.md` |
| Need external domain knowledge to create L1 quan-ly-quy-tac | **Load `references/domain-intelligence-pipeline.md`** then execute DIP 3-Phase with `search_web` |

## Quality checklist

- [ ] **Route 1:** Does Rule file have HPRF block and ≥2 sections with ≥2 quan-ly-quy-tac each?
- [ ] R1: `search_web` invoked for domain grounding? DIP executed?
- [ ] R2: L0 Parity Check done? ALL 5 CLEAR dims scored? CQS size gate applied?
- [ ] R3: Correct RR protocol matched? Delta report generated? Grep checks done? Re-Score executed?
- [ ] R4: Cross-Layer (L0 vs L1) executed? MECE Overlap Check done? Golden Candidates identified?
- [ ] R5: Rule abstracted to non-domain? Human Approval obtained before Master Repo write?

## Guardrails

- `Execute_Without_CLEAR` -> [HALT].
- `Domain_Logic_In_Rules` -> [DENY]. Offload to Skills/KB.
- `Compress_Without_Archive` -> [SYSTEMIC-HALT] if > 15KB.
- `Placeholder_Rules ("TODO")` -> [BANNED].
- `Delete_Wired_Rules_Without_Grep` -> [BANNED].
- `Hallucinate_Domain_Standards` -> [BANNED]. MUST use `search_web` via DIP.
- `Route3_Without_ReScore` -> [BANNED].
- `L1_Contradicts_L0` -> [SYSTEMIC-HALT] without Human Override.
- `Skip_L0_Parity_Check` -> [DENY]. Master Repo L0 is the ground truth.
- `Skip_CQS_Size_Gate` -> [DENY]. File < 0.5KB = skeleton.
- `Copy_Baseline_Without_Customization` -> [DENY].
- `Author_L1_Without_DIP` -> [DENY] for Domain Workspaces.
- `Propose_Before_Execute` -> [REQUIRE] fix strategy before repair.
- `Deep_Read_Before_Archive` -> [REQUIRE] 100% classification of legacy quan-ly-quy-tac.
- `Backport_With_Domain_Logic` -> [DENY]. Master Repo quan-ly-quy-tac MUST be agnostic.
- `Backport_Without_Human_Approval` -> [DENY]. NEVER auto-write to Master Repo templates.
