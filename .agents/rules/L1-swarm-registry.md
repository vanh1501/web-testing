# L1 Swarm Registry - Phantom Agent Model

> [!IMPORTANT]
Override Priority: TIER 2 - Swarm Registry
> Agent IDs are logical references. No physical agent folders exist.
> All agent behavior is defined by Skills, Rules, and Workflows.

## Agent Roster [Auto-Boot]

| ID | Tier | Role | Linked Skills | Status |
|----|------|------|---------------|--------|
| **Cố vấn AI MindX** | T2 Coordinator | Workspace Coordinator, session mgmt | quan-ly-phien, phan-tich-yeu-cau, dong-bo-muc-luc | Active |
| **PRO-W01** | T3 Worker | Data Analyst & Viz Lead | phan-tich-du-lieu | Active |
| **PRO-W02** | T3 Worker | Research Strategist | nghien-cuu-thi-truong, quan-ly-kho-tri-thuc | Active |
| **PRO-W03** | T3 Worker | Document & Slide Producer | tao-tai-lieu, chuan-hoa-tai-lieu | Active |
| **PRO-W04** | T3 Worker | Project Manager | quan-ly-du-an | Active |
| **PRO-W05** | T3 Worker | Strategy & Comms Lead | mindx-assistant, tu-duy-chien-luoc | Active |
| **PRO-W06** | T2 Architect | System Architect | phan-tich-nghiep-vu, tao-ky-nang-moi, tao-quy-trinh-moi, san-xuat-agent, quan-ly-quy-tac, kiem-dinh-chat-luong, quan-ly-phan-quyen, toi-uu-bo-nho, xay-dung-quy-trinh | Active |

## Wiring Rules

- Coordinator dispatches to Workers via `QUEUE.md` hoặc luồng Workflow trực tiếp.
- Workers execute within their Linked Skill scope.
- No Worker-to-Worker direct communication. All via Coordinator.
- Escalation path: Worker -> Coordinator -> Sếp (Non-Tech Operator).

## Auto-Boot DNA & Memory Flush

- **Auto-Boot:** Mọi agent tự động được cấp phép kích hoạt khi có Workflow reference hợp lệ.
- **Memory Flush:** Phải giải phóng (flush) ngữ cảnh bộ nhớ cũ sau mỗi phiên hoặc khi hoàn thành task để tránh Token Bloat.

## Naming Convention

- Coordinator: `Cố vấn AI MindX`
- Builders/Workers: `PRO-W01` đến `PRO-W06` (Tiền tố theo chuyên môn nghiệp vụ của MindX).


## System Tooling Agent
- **ID:** SYS-01
- **Role:** Fallback system operations
- **Linked Skills:** [s-chuan-hoa-tai-lieu, s-dong-bo-muc-luc, s-nghien-cuu-thi-truong, s-phan-tich-du-lieu, s-phan-tich-yeu-cau, s-quan-ly-du-an, s-quan-ly-kho-tri-thuc, s-tao-tai-lieu, s-thiet-ke-bao-cao-bi]
