---
description: "System component: w-dong-phien.md"
semantic_triggers: ['w-dong-phien']
---

﻿---
description: Đóng session an toàn cho mindx-agent_v1, cập nhật tiến độ nội hạt, trích xuất KI và Telemetry.
semantic_triggers: ['end session', 'kết thúc phiên', 'đóng session', 'close workspace', 'khóa phiên mindx-agent_v1', 'dong phien']
---

# Quy Trình: /w-dong-phien
// turbo-all

- **👤 Owner:** `[@Cố vấn AI MindX]`
- **🛠 Skill Target:** `[quan-ly-phien]`

---

### Step 0: Context Boundary Lock 🛡️

**[Local Write Rule]:** All state writes in this session close MUST target:
`TARGET_ROOT = managed_workspaces/mindx-agent_v1/`
Writing to any path outside this scope is FORBIDDEN.
**[Global Fallback Prohibited]:** Nghiêm cấm ngầm định fallback về Master Repo.

---

### Step 1: Stop Dispatching

Freeze all pending Task dispatch. Allow in-flight tasks 15 minutes to settle.

---

### Step 2: Collect Reports

Scan all Tier Agents for: current task status + blocker list + output file locations (tập trung tại `Kho-Du-Lieu/Ket-Qua/`).

---

### Step 2.5: Auto-Pilot Bảo Trì Hệ Thống (Health Check & Cleanup)

**[AUTO-PILOT RULE]**: Để giảm tải Cognitive Load cho Non-Tech User, BẮT BUỘC tự động chạy ngầm 3 nghiệp vụ bảo trì sau trước khi lưu trạng thái:
1. **Khám sức khỏe:** Gọi kỹ năng `kiem-tra-suc-khoe` (hoặc kiểm tra tính toàn vẹn 5-Zone) quét toàn bộ workspace.
2. **Vệ sinh:** Tự động dọn dẹp các file rác, file tạm sinh ra trong phiên.
3. **Đồng bộ Index:** Tự động cập nhật mục lục tại `Bang-Dieu-Khien/BANG-DIEU-KHIEN.md`.

---

### Step 3: Update Local Progress Tracker & Stale Sweep

- **[MANDATORY METADATA UPDATE]**: Cập nhật `last_updated: [ISO_Current]` vào YAML Frontmatter của `managed_workspaces/mindx-agent_v1/Bang-Dieu-Khien/TIEN-DO.md` và `BANG-DIEU-KHIEN.md`.
- **[GARBAGE COLLECTOR]**: Quét cột In-Progress/Pending. Task nào ngâm > 48h TRỰC TIẾP chuyển sang trạng thái 🚨 `STALE/BLOCKED`.
- Ghi entry vào `managed_workspaces/mindx-agent_v1/So-Tay/SO-TAY-QUYET-DINH.md` nếu có quyết định quan trọng.
- Write session summary to `managed_workspaces/mindx-agent_v1/Bang-Dieu-Khien/TIEN-DO.md`:
  - Sections: Completed / In-Progress / Pending / Decisions Made
  - [LOCAL WRITE ONLY — NEVER write to a different workspace's progress.md]

---

### Step 4: Session Report & DIKW Triage (Epistemic Injection)

1. **Ghi Report:** APPEND nội dung vào `managed_workspaces/mindx-agent_v1/artifacts/session-reports/Session_[YYYY-MM-DD].md`:
   - Kết quả công việc (Đã hoàn thành gì, còn vướng mắc ở đâu).
   - Bài học & Quyết định (Các hướng xử lý đã chốt, kinh nghiệm rút ra).
   - Cập nhật Tiến độ (Tình trạng dự án hiện tại).

2. **[EPISTEMIC INJECTION — Lõi tiến hóa Tri thức]**:
   - **GỌI CROSS-WORKSPACE SKILL:** `@epistemic-engineer` (Trạm trung chuyển Master Repo).
   - **Lệnh thực thi:** Tiến hành Route 1 (TRIAGE) đối với toàn bộ Knowledge Extracts vừa tạo. Áp dụng màng lọc A-ESOAR & DIKW. Bất kỳ Insight nào đạt chuẩn Wisdom hoặc TIER-2 phải được tiêm (Inject) thẳng vào thư mục `managed_workspaces/mindx-agent_v1/So-Tay/` (ví dụ: `BAI-HOC-KINH-NGHIEM.md` hoặc `SO-TAY-QUYET-DINH.md`) để làm Luật cho phiên sau.

3. **[Telemetry Drip (OTel LLM Observability)]**:
- Bóc tách chỉ số và APPEND Object JSON vào `managed_workspaces/mindx-agent_v1/Quan-Tri/AGENT-LOG.md` (hoặc `QUALITY-LOG.md`):
  ```json
  {
    "gen_ai.system": "mindx-agent_v1",
    "langfuse.trace.session_id": "[YYYY-MM-DD_HHMM]",
    "langfuse.observation.metadata.human_alignment_flag": "[TRUE/FALSE]",
    "gen_ai.usage.rework_loops_total": "[Tổng số Tries fail]",
    "timestamp": "[ISO 8601]"
  }
  ```

---

### Step 5: Chốt Ca Làm Việc (UX Giao Tiếp)

**[UI Experience Rule]:**
> [!NOTE] UX BẮT BUỘC (GIAO TIẾP VỚI BOM/KEY PERSON MINDX)
> Tuyệt đối KHÔNG dump toàn bộ log/report ra màn hình chat. BẮT BUỘC tuân thủ ngữ điệu tại `CHINH-SACH-GIAO-TIEP-AI.md` (Xưng "Tôi", gọi "Anh/Chị", KHÔNG xưng Sếp/Em). Phản hồi ngắn gọn như sau:
>
> "Anh/chị nghỉ tay nhé. Tôi đã tự động chạy ngầm 3 bước bảo trì (Khám sức khỏe, Dọn rác, Đồng bộ), chốt sổ công việc và khóa phiên làm việc an toàn. 
> Mời anh/chị xem chi tiết tại [Báo cáo Tổng kết Phiên](link_toi_file_session_report.md). Ngày mai anh/chị gõ `/01-khoi-dong-phien` để chúng ta tiếp tục công việc nhé."
