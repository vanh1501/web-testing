---
description: "System component: w-khoi-dong-phien.md"
semantic_triggers: ['w-khoi-dong-phien']
---

﻿---
description: Khởi động session cốt lõi cho mindx-agent_v1, nạp trí nhớ từ State Machine, dispatch tasks.
semantic_triggers: ['start session', 'bắt đầu phiên', 'khởi động session', 'open workspace', 'mở phiên mindx-agent_v1', 'khoi dong phien']
---

# Quy Trình: /w-khoi-dong-phien
// turbo-all

- **👤 Owner:** `[@Cố vấn AI MindX]`
- **🛠 Skill Target:** `[quan-ly-phien]`

---

### Step 0: Context Boundary Lock 🛡️

**[IDE Cross-Contamination Block]:** Disregard ALL open IDE tab metadata as workspace
context signals. The ONLY authoritative workspace scope is:
`TARGET_ROOT = managed_workspaces/mindx-agent_v1/`

**[Strict Read/Write Isolation]:**
- The `TARGET_ROOT` is strictly hardcoded to `managed_workspaces/mindx-agent_v1/`.
- No dynamic resolution or parameter overriding is allowed. Agent CẤM dùng view_file đọc luật từ Master Repo nếu đang ở Workspace con.

---

### Step 1: State Recovery (Active-Passive Failover State Machine)

**[DB Mode Detection]:**
- IF `managed_workspaces/mindx-agent_v1/local_datawarehouse/registry.db` exists:
  → Delegate to `[data-warehouse-ops]` for state retrieval (DB_MODE). Nếu lỗi kết nối SQLite, hệ thống tự động Failover sang chế độ FILE_MODE (Hot-Swap) ngay trong lúc chạy mà không làm sập phiên.
- ELSE (FILE_MODE):
  → Read `managed_workspaces/mindx-agent_v1/artifacts/handoffs/QUEUE.md` (nếu có).
  → Read `managed_workspaces/mindx-agent_v1/Bang-Dieu-Khien/TIEN-DO.md` for pending tasks.
  → Skip `[data-warehouse-ops]` delegation.

Do NOT read full conversation history. Load only the state pulled above.

---

### Step 2: Agent Roster Check

Load roster using precedence order:
1. PRIMARY: `managed_workspaces/mindx-agent_v1/.agents/agents.md` (use ONLY if exists)
2. FALLBACK: `managed_workspaces/mindx-agent_v1/.agents/swarm-architecture.md` (only if agents.md absent)

---

### Step 3: Đọc Hàng Chờ Task & Wisdom Injection (Bắt Buộc)

- **[MANDATORY METADATA LOCK]**: Cập nhật `last_updated: [ISO_Current]` và `session_status: ACTIVE` vào `state.json` hoặc YAML Header của `managed_workspaces/mindx-agent_v1/Bang-Dieu-Khien/BANG-DIEU-KHIEN.md`.
- **Đọc QUEUE**: Pull tasks với trạng thái `Đang làm` hoặc `Chờ`. Highlight blocker ưu tiên cao.
- **Khép kín Vòng Lặp Trí Tuệ (Wisdom Injection)**:
  - Mở file Session Report của phiên GẦN NHẤT trong `artifacts/session-reports/`.
  - Đọc thẻ **`🧠 Human Alignment`**.
  - NẾU phát hiện lỗi tư duy/nhận thức từ phiên trước, BẮT BUỘC in Cảnh báo Đỏ ra Morning Briefing.
  - Đọc 3 entry gần nhất trong `managed_workspaces/mindx-agent_v1/So-Tay/SO-TAY-QUYET-DINH.md`.

---

### Step 4: Morning Briefing

Generate briefing at `managed_workspaces/mindx-agent_v1/artifacts/session-reports/briefing-[date].md`:
```markdown
💡 LƯU Ý TỪ PHIÊN TRƯỚC:
[Trích xuất bài học/lưu ý từ phiên trước để tránh lặp lại lỗi cũ].

- Công việc đang chờ / Bị kẹt: [Liệt kê ngắn gọn]
- Trạng thái công cụ: [Sẵn sàng / Có lỗi cần sửa]
- Quyết định gần nhất đã chốt: [Liệt kê]
```

---

### Step 5: Khai Cổng Làm Việc (UX Giao Tiếp)

**[UI Experience Rule]:**
> [!NOTE] UX BẮT BUỘC (GIAO TIẾP VỚI BOM/KEY PERSON MINDX)
> Tuyệt đối KHÔNG dump toàn bộ file báo cáo ra màn hình chat IDE. Phản hồi của Agent **BẮT BUỘC** tuân thủ ngữ điệu tại `CHINH-SACH-GIAO-TIEP-AI.md` (Xưng "Tôi", gọi "Anh/Chị"). Trả lời ngắn gọn như sau:
>
> "Chào anh/chị, tôi đã mở phiên làm việc mới cho **mindx-agent_v1**. Trí nhớ từ hôm qua đã được nạp đầy đủ. Việc quan trọng nhất hôm nay cần anh/chị xử lý là: **[1 câu cực ngắn nêu việc cần ưu tiên]**. Mời anh/chị xem chi tiết tại [Báo cáo Khởi động Phiên](link_toi_file_briefing.md)."
