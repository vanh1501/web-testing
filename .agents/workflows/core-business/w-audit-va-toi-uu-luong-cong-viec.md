---
id: "WF-META-AUDIT-01"
name: "w-audit-va-toi-uu-luong-cong-viec"
description: "Meta-workflow audit và tối ưu workflow library & cấu trúc Workspace. 4 luồng: AUDIT (1 workflow), OPTIMIZE (fix workflow), META-AUDIT (toàn library), và STRUCTURAL AUDIT (kiểm định 5-Zone & chuẩn Versioning LATEST Pointer)."
version: v2.1
status: Production-Ready
semantic_triggers: ['audit workflow', 'kiểm tra workflow', 'đánh giá quy trình AI', 'score workflow', 'tối ưu workflow library', 'workflow scorecard', 'review luồng công việc', 'optimize workflow', 'audit workspace', 'kiểm định 5-zone', 'check versioning']
owner: "PRO-W07"
skill_target: "00-phan-tich-yeu-cau, 00-tao-tai-lieu, 00-chuan-hoa-tai-lieu"
hitl_timeout: "24h"
retry_policy: {max_attempts: 3, backoff: exponential_1s_2s_4s, fallback: "log_to_ACTION-LOG_and_report_human"}
---

- **👤 Owner:** `[@PRO-W07]`
- **🛠 Skill Target:** `[00-phan-tich-yeu-cau, 00-tao-tai-lieu, 00-chuan-hoa-tai-lieu]`
- **⏱ HITL Timeout:** 24h
- **🔄 Circuit Breaker:** retry 3 lần, fallback → ACTION-LOG + human
- **📚 KB Reference:** `kb-mas-v8-gold-criteria` v1.0.1 (Gold rubric) + Rubric Workflow Expert-Grade v2 (built-in)

# Quy Trình: /w-audit-va-toi-uu-luong-cong-viec (v2.0 — Meta-Workflow)

## Purpose & Scope

**Purpose:** Audit và optimize **workflow library** cùng **cấu trúc vật lý của Workspace**. Áp dụng dual-rubric cho workflow và nguyên tắc 5-Zone/LATEST Pointer cho cấu trúc thư mục. Tương đương "meta-audit".

**Scope:** Audit 1 workflow đơn lẻ, toàn library, hoặc quét toàn bộ 5-Zone của workspace để check versioning/cấu trúc rác. Optimize đề xuất P0/P1/P2 fixes. KHÔNG bao gồm: tự apply fix code, audit skill library (dùng pattern khác).

## Trigger

BOM/Admin nói: "audit workflow X", "kiểm tra workflow Y theo MAS V8", "score workflow library", "tối ưu workflow nào yếu nhất", "review luồng công việc".

## Prerequisites

- [ ] Workflow files tồn tại trong `.agents/workflows/` (hoặc folder workflow library)
- [ ] BOM có quyền read các workflow files
- [ ] (Optional) `kb-mas-v8-gold-criteria.md` v1.0.1+ có trong project knowledge

## Routing — Step 0 (4 luồng)

| Tín hiệu từ BOM | Luồng |
|-----------------|-------|
| "Audit workflow X", "Kiểm tra workflow Y" | **Luồng A: SINGLE AUDIT** (1 workflow) |
| "Tối ưu workflow X", "Workflow X điểm thấp, fix sao" | **Luồng B: SINGLE OPTIMIZE** (1 workflow) |
| "Audit toàn library", "Score 6 workflow", "Workflow nào tệ nhất" | **Luồng C: META-AUDIT** (toàn library) |
| "Audit workspace", "Kiểm tra 5-zone", "Check versioning" | **Luồng D: STRUCTURAL AUDIT** (Toàn Workspace) |

**Auto-clarify:** Nếu BOM nói "audit" mà không nêu rõ đối tượng → ask: "Audit 1 workflow cụ thể, toàn library, hay kiểm định cấu trúc 5-Zone của workspace?"

---

## Luồng A: SINGLE AUDIT (1 workflow)

> [!IMPORTANT] KARPATHY VERIFICATION MANDATE
> Mỗi Step: `[Step] -> verify: [Tiêu chí]`. CẤM Blind Looping.

### Bước A.1 — Load Workflow File
**Action:** Gọi `00-phan-tich-yeu-cau` (sub-mode: file_intake) đọc file workflow target.
**Verify:** File exists, ≥1KB content, có frontmatter YAML.

### Bước A.2 — Gold Criteria Check (4 tiêu chí structural)
**Action:** Apply rubric Gold (Workflow Engine):

| Tiêu chí | Check |
|----------|-------|
| **2.1 CQS Metadata** | Frontmatter có `owner` + `skill_target` non-empty? Callout 👤Owner + 🛠Skill Target sau frontmatter? |
| **2.2 Circuit Breaker** | Có `retry_policy` + fallback declared? Retry ≤3? |
| **2.3 HITL ≥24h** | Có `hitl_timeout` ≥24h declared? Mỗi HITL Gate có timeout? |
| **2.4 Zero-Native** | Body có verb thực thi nghiệp vụ ngoài context "gọi skill X để..."? |

**Verify:** Mỗi tiêu chí: PASS/FAIL/PARTIAL với evidence quote line từ file.

### Bước A.3 — Expert-Grade Rubric Check (7 trục, 100pt)

**Action:** Apply rubric Expert v2 — chấm điểm 7 trục theo built-in scoring guide:

| Trục | Pts | Tiêu chí con |
|------|-----|--------------|
| **A** Orchestration Logic | 30 | A1 Routing (8) / A2 Skill chaining correctness (8) / A3 Step atomicity (8) / A4 Exit conditions (6) |
| **B** Error Handling & Resilience | 18 | B1 Circuit Breaker (8) / B2 Failure mode coverage (6) / B3 Graceful degradation (4) |
| **C** HITL Design | 22 | C1 HITL ≥24h (8) / C2 Checkpoint placement (7) / C3 Approval path (7) |
| **D** Cross-skill Integration | 12 | D1 Skill Target accuracy no dangling (6) / D2 I/O handshake (4) / D3 Workflow chaining (2) |
| **E** BOM Operability | 8 | E1 Trigger clarity (5) / E2 Progress visibility (3) |
| **F** Observability & Audit | 4 | F1 Logging/state (3) / F2 Output Contract per step (1) |
| **G** Token/Cost Efficiency | 6 | G1 Step economy (3) / G2 Context management (2) / G3 Caching/reuse (1) |

**Verify:** Tổng điểm = sum 7 trục, mỗi tiêu chí có evidence + score rationale.

### Bước A.4 — Render Scorecard (HITL Gate 1)
**Action:** Gọi `00-tao-tai-lieu` (document_type: executive_report, style: executive) render Audit Report Markdown:
- Executive Summary (BLUF 2-3 câu)
- Master Scoreboard (Gold + Expert)
- Top 3-5 issues với evidence quote
- Verdict: A (≥95) / A- (90-94) / B (80-89) / C (70-79) / D (50-69) / F (<50)
- Remediation Plan P0 (Gold fail) + P1 (Expert <80) + P2 (polish)

**HITL Timeout:** 24h. BOM review trước khi proceed Luồng B.
**Decision:** Approve scorecard → ship file | Reject → re-audit với feedback.

### Bước A.5 — Ship Audit Report
**Action:** Chain `00-chuan-hoa-tai-lieu` xuất DOCX `Quan-Tri/AUDIT-WORKFLOWS/{workflow-name}-audit-{YYYY-MM-DD}.docx`.

---

## Luồng B: SINGLE OPTIMIZE (1 workflow)

### Bước B.1 — Load Audit Report
**Action:** Nhận input từ Luồng A scorecard (nếu vừa chạy) hoặc ask BOM cung cấp audit report cũ.
**Verify:** Có scorecard + remediation plan rõ.

### Bước B.2 — Root Cause Categorization (Socratic Challenge - HITL Gate 2)
**Action:** Đặt câu hỏi thách thức theo trục yếu nhất:
- Nếu A (Orchestration) yếu → "Routing decision có thực sự cần hay just-in-case?"
- Nếu C (HITL) yếu → "BOM thực sự cần human checkpoint ở đâu, hay đang spam approve?"
- Nếu D (Cross-skill) yếu → "Skill nào dangling? Đã fix tên trong library v2.0 chưa?"
- Nếu G (Token) yếu → "Có route nào load skill thừa? Có duplicate step với workflow khác?"

**HITL Timeout:** 24h.
**Verify:** BOM trả lời + xác định root cause priorities.

### Bước B.3 — Generate Optimization Delta (Before/After)
**Action:** Gọi `00-tao-tai-lieu` (document_type: business_proposal, style: operational) sinh bảng So sánh:
- Section nào sẽ thay đổi? (frontmatter / Steps / Edge cases / Output Contract)
- Score expected delta (vd: 65 → 82, +17)
- Effort estimate (giờ)
- Skill references cần fix nếu dangling

**Verify:** Delta có ≥3 sections changes, score delta dương, effort estimate có range.

### Bước B.4 — Approve Optimization (HITL Gate 3)
**Action:** Trình bày Delta plan cho BOM.
**Decision:** Approve → Bước B.5 | Reject → quay B.3 với feedback.
**HITL Timeout:** 24h. Critical decision, không auto-approve.

### Bước B.5 — Generate Rebuilt Workflow File
**Action:** Gọi `00-tao-tai-lieu` sinh phiên bản workflow rebuilt theo Delta plan. Output Markdown file `Kho-Du-Lieu/Ket-Qua/workflow-optimized/{workflow-name}-v{N+1}.md`.

**LƯU Ý QUAN TRỌNG:** Workflow KHÔNG tự ghi đè file gốc. BOM manual review file rebuilt + commit/replace.

### Bước B.6 — Post-Optimize Verify (Optional)
**Action:** Gợi ý BOM chạy lại Luồng A trên file rebuilt để confirm score expected. Vòng lặp PDCA.

---

## Luồng C: META-AUDIT (toàn library)

### Bước C.1 — Library Inventory
**Action:** Scan `.agents/workflows/*.md` (hoặc folder workflow library).
**Verify:** Có ≥1 file. Inventory: file count + size breakdown.

### Bước C.2 — Batch Audit (loop Luồng A cho từng file)
**Action:** Loop qua từng workflow file, chạy Bước A.2 + A.3 (Gold + Expert) → tổng hợp scores.
**Circuit Breaker:** Nếu >2 file fail load (corrupt), HALT, ask BOM verify.

### Bước C.3 — Library Health Report (Master Scoreboard)
**Action:** Gọi `00-tao-tai-lieu` (document_type: executive_report) render Library Audit Report:
- Master Scoreboard (N workflow × 7 trục + verdict)
- Top 5 systemic issues across library (cross-reference, HITL, Circuit Breaker, etc.)
- Library avg score
- Rank workflows: Pass (≥80) / Polish (70-79) / Rebuild (<70)
- Phase plan: P0 production-blocker + P1 senior-grade + P2 polish, với effort estimate

### Bước C.4 — BOM Review (HITL Gate 4)
**Action:** Trình bày Library Health Report.
**Decision:** Approve report → ship | Want deep-dive workflow X → trigger Luồng A cho file X.
**HITL Timeout:** 24h.

### Bước C.5 — Ship + Recommend Phased Rebuild
**Action:** Chain `00-chuan-hoa-tai-lieu` xuất `Quan-Tri/AUDIT-WORKFLOWS/library-health-{YYYY-MM-DD}.docx`. Gợi ý BOM: "Phase 3 rebuild đề xuất bắt đầu với workflow X (score thấp nhất + dependency nhiều)."

---

## Luồng D: WORKSPACE STRUCTURAL AUDIT (5-Zone & Versioning)

### Bước D.1 — Quét toàn vẹn 5-Zone
**Action:** Gọi Agent/Skill (hoặc dùng terminal script) lặp qua cấu trúc thư mục gốc của workspace.
**Verify:** 
- Đảm bảo chỉ có 5 thư mục cốt lõi (`Bang-Dieu-Khien`, `Du-An`, `Kho-Du-Lieu`, `Quan-Tri`, `So-Tay`) và `.agents`.
- Flag đỏ (FAIL) nếu phát hiện file/folder rác ngoài Root hoặc file nghiệp vụ bị vứt nhầm vào `.agents/`.

### Bước D.2 — Quét chuẩn Versioning (LATEST Pointer)
**Action:** Quét tên file của toàn bộ file tài liệu định dạng `.md`, `.docx`, `.xlsx` trong các thư mục chính (ngoại trừ thư mục `Archive`).
**Verify:** 
- Báo lỗi (Violation) nếu phát hiện tên file vật lý chứa hậu tố version (vd: `*_v1.2.md`, `*_FINAL.docx`). Chuẩn bắt buộc là file vật lý phải dùng tên không suffix, version ghi trong ruột.
- Kiểm tra sự tồn tại của thư mục con `05-Archive/` (hoặc `Archive/`) tại các zone lưu trữ tài liệu để đảm bảo old versions có nơi cư trú.

### Bước D.3 — Rà quét Broken Links (Cross-references)
**Action:** Quét nội dung các file Markdown để tìm regex link `[.*](.*.md)`.
**Verify:** Cảnh báo nguy cơ gãy link nếu link trỏ đến tên file có đuôi version cụ thể thay vì file "LATEST".

### Bước D.4 — Xuất báo cáo Workspace Health Score (HITL Gate 5)
**Action:** Gọi `00-tao-tai-lieu` (document_type: executive_report) render Báo cáo:
- Tóm tắt tỷ lệ tuân thủ 5-Zone (%).
- Danh sách file rác cần xóa/di chuyển.
- Danh sách file vi phạm quy tắc Versioning cần đổi tên.
**Decision:** Approve → ship report | Reject → ignore.
**HITL Timeout:** 24h.

---

## HITL Gates Summary

| Gate | Luồng | Step | Timeout | Action on timeout |
|------|-------|------|---------|-------------------|
| Gate 1 — Audit Approve | A | A.4 | 24h | Reminder; sau 48h archive draft |
| Gate 2 — Socratic Root Cause | B | B.2 | 24h | Log gap + proceed với assumption |
| Gate 3 — Optimization Approve | B | B.4 | 24h | KHÔNG auto-approve (critical) |
| Gate 4 — Library Report Review | C | C.4 | 24h | Reminder; sau 48h ship default |
| Gate 5 — Structural Report | D | D.4 | 24h | Reminder; sau 48h ship default |

## Circuit Breaker Policy

| Failure mode | Detection | Retry | Fallback |
|--------------|-----------|-------|----------|
| Workflow file không parse được | YAML / Markdown error | 1 lần (try fix encoding) | Skip file + log error, continue audit other files |
| Skill `00-phan-tich-yeu-cau` timeout | 60s no response | 3 lần | ACTION-LOG + ask human |
| Rubric score conflict (Gold pass nhưng Expert <80) | Built-in cross-check | 0 (expected case) | Report both scores, BOM judge |
| KB `kb-mas-v8-gold-criteria` missing | File not found | 1 lần (try alternative path) | Use built-in rubric inline, warn BOM update KB |

## Edge Cases & Recovery

1. **Workflow file mới (chưa có baseline cũ)** → Audit straightforward, không cần compare previous version
2. **Workflow file ngoài chuẩn folder** → Ask BOM cung cấp path explicit
3. **Score conflict Gold vs Expert** (vd Gold pass 100% nhưng Expert 65) → Present both, BOM hiểu rằng structural OK nhưng quality logic kém
4. **Library 1 workflow duy nhất** → Skip Luồng C META-AUDIT, chạy Luồng A đơn
5. **BOM yêu cầu audit skill thay vì workflow** → REFUSE, suggest pattern audit skill library tách biệt
6. **Workflow rebuilt fail Gold sau Luồng B** → Iterate Luồng B 1 lần nữa với feedback specific
7. **Cross-reference dangling không fix được** (skill mentioned không tồn tại trong library) → Flag GAP, suggest BOM tạo skill mới hoặc remove reference

## Output Contract (Idempotent JSON)

```json
{
  "workflow_id": "WF-META-AUDIT-01",
  "luong_executed": "A_SINGLE_AUDIT | B_SINGLE_OPTIMIZE | C_META_AUDIT | D_STRUCTURAL_AUDIT",
  "run_status": "success | halt_at_gate | halt_at_failure",
  "audit_target": {
    "type": "single_workflow | library | workspace_structure",
    "scope": "w-00-w-phan-tich-va-bao-cao.md | all_workflows | 5_zones"
  },
  "luong_A_data": {
    "gold_criteria": {
      "2.1_CQS": "PASS | FAIL | PARTIAL",
      "2.2_CB": "PASS | FAIL",
      "2.3_HITL": "PASS | FAIL",
      "2.4_Zero_Native": "PASS | FAIL"
    },
    "expert_score": {
      "A_orchestration": 27,
      "B_error_handling": 15,
      "C_hitl": 20,
      "D_cross_skill": 11,
      "E_bom_operability": 7,
      "F_observability": 3,
      "G_token_efficiency": 4,
      "total": 87
    },
    "verdict": "A | A- | B | C | D | F"
  },
  "luong_B_data": {
    "root_cause_categories": ["cross_reference_drift", "hitl_missing"],
    "score_delta_expected": "+17 (65 → 82)",
    "effort_estimate_hours": 4,
    "file_rebuilt_path": "Kho-Du-Lieu/Ket-Qua/workflow-optimized/..."
  },
  "luong_C_data": {
    "library_avg_score": 74,
    "workflows_count": 7,
    "verdicts_distribution": {"pass": 2, "polish": 1, "rebuild": 4},
    "top_systemic_issues": [...],
    "phase_plan_effort_hours": {"P0": 8, "P1": 13, "P2": 7}
  },
  "luong_D_data": {
    "5_zone_compliance": "PASS | FAIL",
    "files_with_version_suffix_count": 3,
    "broken_link_risks_count": 1,
    "recommended_actions": ["Move 2 files to Archive", "Rename 3 files to drop version"]
  },
  "deliverable_files": [
    "Quan-Tri/AUDIT-WORKFLOWS/{name}-audit-{date}.docx"
  ],
  "hitl_gates_triggered": ["Gate 1"],
  "circuit_breaker_activated": false,
  "next_workflow_suggested": "Luồng B OPTIMIZE cho workflow điểm thấp nhất"
}
```

## Cross-Workflow Chaining

- **Self-loop:** Luồng A audit → Luồng B optimize → Luồng A re-audit (PDCA cycle cho workflow)
- **Library-loop:** Luồng C audit toàn library → BOM chọn workflow → Luồng A deep-dive → Luồng B optimize
- **Internal chain:** Mọi luồng đều end với `00-chuan-hoa-tai-lieu` để ship DOCX

## Validation

- [ ] Luồng A: Gold + Expert score đầy đủ với evidence
- [ ] Luồng A: Verdict A-F declared dựa trên Expert total + Gold gate
- [ ] Luồng B: Delta plan có before/after rõ + effort estimate
- [ ] Luồng B: File rebuilt KHÔNG ghi đè file gốc (manual commit required)
- [ ] Luồng C: Master Scoreboard có tất cả workflow trong library
- [ ] Mọi HITL Gate có timeout declared ≥24h
- [ ] JSON Output Contract đầy đủ

## Resources

- KB: `kb-mas-v8-gold-criteria.md` v1.0.1 (Gold rubric — Phần 2 Workflow Engine)
- Built-in: Rubric Workflow Expert-Grade v2 (định nghĩa trong Bước A.3 table)
- Skill: `00-phan-tich-yeu-cau` (file intake + WBS analysis)
- Skill: `00-tao-tai-lieu` (render Markdown audit report)
- Skill: `00-chuan-hoa-tai-lieu` (ship DOCX final)
- Output paths: `Quan-Tri/AUDIT-WORKFLOWS/`, `Kho-Du-Lieu/Ket-Qua/workflow-optimized/`

## Notes

- Workflow này là **self-referential**: có thể audit chính nó. Khi BOM gọi "audit workflow audit-va-toi-uu-luong-cong-viec", Luồng A sẽ audit file SKILL.md của workflow này.
- Pattern này replicate trực tiếp từ `00-xay-dung-quy-trinh` Luồng 2 AUDIT + Luồng 3 OPTIMIZE — áp dụng cho workflow thay vì business process.
- Vòng lặp PDCA: BOM nên chạy Luồng A định kỳ (vd 30-60 ngày) cho workflow critical để catch drift.
