---
id: "WF-DATA-REPORT-01"
name: "w-phan-tich-va-bao-cao"
description: "Mega-Pipeline xử lý Dữ liệu và Báo cáo. Điều phối 4 route cốt lõi: Phân tích BI từ raw data, Báo cáo Tiến độ dự án (RAG), Báo cáo Tuần, Báo cáo Tháng. Skill load lazy theo route để tối ưu token."
version: v2.0
status: Production-Ready
semantic_triggers: ['phân tích số liệu', 'làm báo cáo', 'data analysis', 'BI dashboard', 'tính KPI', 'báo cáo tiến độ', 'báo cáo tuần', 'báo cáo tháng', 'standup', 'RAG status', 'executive summary']
owner: "PRO-W01"
skill_target: "00-phan-tich-du-lieu, 00-quan-ly-du-an, 00-tao-tai-lieu"
hitl_timeout: "24h"
retry_policy: {max_attempts: 3, backoff: exponential_1s_2s_4s, fallback: "log_to_ACTION-LOG_and_report_human"}
---

- **👤 Owner:** `[@PRO-W01]`
- **🛠 Skill Target:** `[00-phan-tich-du-lieu, 00-quan-ly-du-an, 00-tao-tai-lieu]`
- **⏱ HITL Timeout:** 24h (Route 2 Standup có timeout riêng 4h cho Standup live)
- **🔄 Circuit Breaker:** retry 3 lần, fallback → ACTION-LOG + human notify

# Quy Trình: /w-phan-tich-va-bao-cao (v2.0 — Mega Data & Report Pipeline)

## Purpose & Scope

**Purpose:** Hợp nhất nhu cầu báo cáo phòng ban vào 1 luồng duy nhất với 4 route chuyên biệt. Agent tự phân loại yêu cầu → route → load skill cần thiết → produce output.

**Scope:** Từ phân tích raw data (Excel/CSV) → báo cáo tiến độ daily/weekly → tổng hợp Executive monthly. KHÔNG bao gồm: nghiên cứu thị trường (dùng `00-nghien-cuu-thi-truong`), viết SOP (dùng `00-xay-dung-quy-trinh`).

## Trigger

User nói: "phân tích data", "Excel", "báo cáo tuần/tháng", "standup", "RAG status", "KPI", "tại sao chỉ số tăng/giảm".

## Prerequisites

- [ ] Data source available (file `Kho-Du-Lieu/Du-Lieu-Vao/` cho Route 1, hoặc `Du-An/{project}/TIEN-DO.md` cho Route 2-4)
- [ ] Operator xác định Route (hoặc system auto-detect)

## Routing — Step 0 (Định tuyến)

> Skill load **LAZY** theo route, không load 4 skill cùng lúc → tiết kiệm token.

| Tín hiệu từ User | Route | Skill load |
|------------------|-------|------------|
| File Excel/CSV thô + "tìm insight/KPI" | **Route 1: BI Analysis** | `00-phan-tich-du-lieu` (clean + KPI + Pyramid) |
| "Cập nhật tiến độ task", "Daily/Weekly Standup" | **Route 2: RAG Status** | `00-quan-ly-du-an` (RAG labeling) |
| "Báo cáo tuần", "Weekly Health" | **Route 3: Weekly Report** | `00-quan-ly-du-an` + `00-tao-tai-lieu` |
| "Báo cáo tháng", "Executive Summary" | **Route 4: Monthly Executive** | `00-phan-tich-du-lieu` + `00-tao-tai-lieu` |

**Auto-detection:** Nếu Operator paste file Excel → Route 1. Nếu nhắc "task status" → Route 2. Nếu nhắc tuần/tháng → Route 3/4.

**Decision:** Operator confirm route trước khi proceed.

---

### ROUTE 1: BI Analysis (Data → Insight)

> [!IMPORTANT] KARPATHY VERIFICATION MANDATE
> Mỗi Step: `[Step] -> verify: [Tiêu chí]`. CẤM Blind Looping.

**Step R1.1 — Data Quality Gate**
**Action:** Gọi `00-phan-tich-du-lieu` (sub: `clean_data.py --schema {domain}`). Domain: kd_mkt / back_hr / tech / back_ketoan.
**Verify:** Cleaning log có rows_after_cleaning > 0, missing_pct_max ≤20% (else warn).

**Step R1.2 — KPI Calculation**
**Action:** Gọi `00-phan-tich-du-lieu` (sub: `calc_kpi.py --catalog {domain}`).
**Verify:** Highlight 3-5 metric warn/critical, không spam 20+ metric.

**Step R1.3 — Pyramid Narrative (HITL Gate 1)**
**Action:** Gọi `00-phan-tich-du-lieu` (sub: pyramid render). Output Markdown báo cáo với Conclusion → 3 Findings → Recommendations + Caveats section.
**Verify:** Output Contract JSON có `ship_decision: ship/warn` + `confidence_level`.
**HITL Gate:** Nếu `confidence_level: low` → DỪNG, ask Operator verify trước khi ship cho BOD.

---

### ROUTE 2: RAG Status (Agile Standup)

**Step R2.1 — Pull Tasks**
**Action:** Đọc `Du-An/{project}/TIEN-DO.md` hoặc `tasks.md`.
**Verify:** Có ≥1 task trong scope.

**Step R2.2 — Standup Interview (HITL Gate 2)**
**Action:** Hỏi User 3 câu Standup: *Done? Doing? Blocked?*
**HITL Timeout:** 4h cho Standup live (vì Standup là sync session); nếu Operator không trả lời sau 4h → auto-archive session, send reminder.
**Decision:** Trả lời đủ 3 câu → proceed. Skip câu nào → log warning.

**Step R2.3 — RAG Labeling**
**Action:** Gọi `00-quan-ly-du-an` (sub: RAG label) gán GREEN/AMBER/RED cho từng task dựa trên Standup responses.
**Verify:** Mọi task có label.

**Step R2.4 — Mitigation Plan (HITL Gate 3)**
**Action:** Cho mọi task RED, ask Operator: "Hướng giải quyết?"
**HITL Timeout:** 24h. Sau timeout: log task as "RED + unresolved", escalate BOM admin.

**Step R2.5 — Export Status**
**Action:** Sinh `Quan-Tri/RAG-STATUS/{YYYY-MM-DD}.md` với RAG table + mitigation notes.
**Verify:** File created + path đúng.

---

### ROUTE 3: Weekly Health Report

**Step R3.1 — Aggregate Week Data**
**Action:** Scan tất cả `TIEN-DO.md` và `Quan-Tri/RAG-STATUS/*.md` trong 7 ngày qua.
**Verify:** Có ≥1 data point trong window.

**Step R3.2 — Compute Weekly Metrics**
**Action:** Gọi `00-quan-ly-du-an` (sub: weekly aggregate) — đếm task done/doing/blocked, % achievement vs plan.
**Verify:** Metrics computed.

**Step R3.3 — Render Report**
**Action:** Gọi `00-tao-tai-lieu` (document_type: executive_report, style: executive) → Markdown 5-section: Summary 5-line / Achievements / Risks / Next Week / Action Items.
**Verify:** Output có đủ 5 section.

**Step R3.4 — Mandatory Chain to chuan-hoa**
**Action:** Tự động chain `00-chuan-hoa-tai-lieu` để xuất file DOCX vào `Quan-Tri/BAO-CAO-TUAN/{YYYY-MM-DD}.docx`.

---

### ROUTE 4: Monthly Executive Summary

**Step R4.1 — Aggregate Month Data**
**Action:** Scan 4 báo cáo tuần + `ACTION-LOG.md` + KPI files của tháng.
**Verify:** Có ≥3 weekly reports trong window.

**Step R4.2 — Pyramid Synthesis**
**Action:** Gọi `00-phan-tich-du-lieu` (sub: pyramid render — angle "executive summary") → top 3 highlights + top 3 risks + comparison MoM.
**Verify:** Pyramid format + MoM comparison có.

**Step R4.3 — Executive Approve (HITL Gate 4)**
**Action:** Trình bày draft cho User review.
**HITL Timeout:** 24h. Sau timeout: send reminder, không auto-finalize (BOD report critical).

**Step R4.4 — Render + Ship**
**Action:** Gọi `00-tao-tai-lieu` (document_type: executive_report) → `00-chuan-hoa-tai-lieu` xuất `Kho-Du-Lieu/Ket-Qua/bao-cao-thang-{YYYY-MM}.pptx`.

## HITL Gates Summary

| Gate | Route | Timeout | Action on timeout |
|------|-------|---------|-------------------|
| Gate 1 (BI low confidence) | R1.3 | 24h | Reminder + pause; sau 48h archive draft |
| Gate 2 (Standup live) | R2.2 | **4h** (special — Standup là sync) | Auto-archive + send reminder |
| Gate 3 (RED mitigation) | R2.4 | 24h | Log "unresolved" + escalate BOM |
| Gate 4 (Monthly approve) | R4.3 | 24h | Reminder; KHÔNG auto-finalize |

## Circuit Breaker Policy

| Failure mode | Detection | Retry | Fallback |
|--------------|-----------|-------|----------|
| Data file corrupt | `clean_data.py` exception | 1 lần (try alternative encoding) | Report user, request clean data |
| Data >20% missing | Cleaning log warning | 0 | Flag confidence=low, proceed nhưng warn BOM |
| Skill timeout | 60s no response | 3 lần | ACTION-LOG + human |
| Python env missing | ImportError | 1 lần (pip install) | Fallback: export Python code cho user tự chạy |

## Edge Cases & Recovery

1. **Data file rỗng/<100 rows** → Route 1 REFUSE, ask user supplement
2. **Outlier >5σ** → Skill flag, ask user verify trước remove (không auto)
3. **Conflicting metric definitions** (vd 2 nguồn ROAS khác) → REFUSE, ask user chọn canonical
4. **Scope creep Route 2** (User thêm task mới giữa Standup) → Warn rủi ro vỡ Timeline trước khi accept
5. **Period boundary unclear** (vd "tháng 5" = calendar hay fiscal?) → Ask user clarify
6. **Route 1 Python sandbox cần access ngoài**: TUYỆT ĐỐI chỉ Read-Only, không ghi đè file gốc
7. **Báo cáo tháng nhưng <3 báo cáo tuần** → Warn data sparse, proceed nhưng confidence=medium

## Output Contract (Idempotent JSON)

```json
{
  "workflow_id": "WF-DATA-REPORT-01",
  "route_executed": "R1 | R2 | R3 | R4",
  "run_status": "success | halt_at_gate | halt_at_failure",
  "skills_invoked": ["00-phan-tich-du-lieu", "00-tao-tai-lieu"],
  "data_source": "/path/to/input",
  "deliverable_files": [
    {"path": "Kho-Du-Lieu/Ket-Qua/report-Q1-2026.md", "type": "markdown"},
    {"path": "Kho-Du-Lieu/Ket-Qua/report-Q1-2026.pptx", "type": "pptx"}
  ],
  "metrics_summary": {
    "highlights_count": 4,
    "confidence_level": "high | medium | low"
  },
  "hitl_gates_triggered": ["Gate 4"],
  "circuit_breaker_activated": false,
  "next_workflow_suggested": "none (báo cáo final)"
}
```

## Cross-Workflow Chaining

- **Receives from:** `00-phan-tich-nhiem-vu` (sub-task "phân tích data" / "báo cáo")
- **Hands off to:** `00-san-xuat-tai-lieu` nếu cần custom format (vd brand pitch deck)
- **Internal chain:** Route 3 (tuần) → Route 4 (tháng) khi đến cuối tháng

## Validation

- [ ] Insight BI có data chứng thực (không Hallucinate)
- [ ] Báo cáo lưu đúng path `Kho-Du-Lieu/Ket-Qua/` hoặc `Quan-Tri/`
- [ ] Route 2 Standup không bao giờ đóng session khi User chưa trả lời 3 câu (trong window 4h)
- [ ] HITL Gates có timeout declared
- [ ] Confidence level declared trong Output Contract

## Resources

- Skill: `00-phan-tich-du-lieu` (sub-actions: clean_data.py, calc_kpi.py, pyramid render)
- Skill: `00-quan-ly-du-an` (sub-actions: RAG labeling, weekly aggregate)
- Skill: `00-tao-tai-lieu` + `00-chuan-hoa-tai-lieu` (chained for Route 3, 4)
- Output paths: `Quan-Tri/RAG-STATUS/`, `Quan-Tri/BAO-CAO-TUAN/`, `Kho-Du-Lieu/Ket-Qua/`
