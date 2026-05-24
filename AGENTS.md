# mindx-agent_v1

Workspace template cho phòng ban MindX — hỗ trợ BOM và key person vận hành quy trình công việc phòng ban với sự hỗ trợ của Agent.

## Tech stack

- IDE primary: Google Antigravity (Public Preview), portable to Cursor / Codex / Claude Code
- Instruction format: Antigravity Skills + Rules + Workflows
- Document format: Markdown (`.md`), Word (`.docx`), PowerPoint (`.pptx`), Excel (`.xlsx`)
- Open standard compatibility: AGENTS.md (Linux Foundation)
- Governance: MAS V9 Baseline (L0/L1/L2 Rule Architecture)

## Dev environment

Workspace này không có dev environment riêng — operator dùng Antigravity IDE trực tiếp:

- Setup: Mở thư mục workspace trong Antigravity
- Run: Gõ yêu cầu vào agent chat, hoặc slash command
- Verify: Doc `Bang-Dieu-Khien/BANG-DIEU-KHIEN.md` de kiem trang thai

## Testing

- Test thu cong: Chay bai tap trong `Du-An/Bai-Tap/` — verify hoan thanh 4 bai tap trong 1h
- Audit dinh ky: Workflow `/kiem-tra-suc-khoe` chay hang thang, ket qua vao `Quan-Tri/AUDIT/`
- Session health: Chay `/khoi-dong-phien` + `/dong-phien` moi phien de duy tri trang thai

## Code style

### Do

- Dat ten tep/thu muc theo `Quan-Tri/CHINH-SACH.md` Phan 1
- User-facing files tieng Viet, system files tieng Anh
- Mọi tệp output của dự án ghi trực tiếp vào `Du-An/{epic}/{project}/artifacts/`
- Moi quyet dinh ghi `So-Tay/SO-TAY-QUYET-DINH.md`
- Moi thay doi cau truc ghi `Quan-Tri/LICH-SU-THAY-DOI.md`

### Don't

- KHONG dan du lieu nghiep vu vao `.agents/` (instruction layer giu sach)
- KHÔNG ghi đè tệp không qua bước xác nhận (L2 Maker-Checker)
- KHÔNG đoán ý operator (L0 Governance — hỏi trước khi đoán)
- KHONG sua tep trong `Kho-Du-Lieu/Du-Lieu-Vao/` (chi doc)

## Boundaries

- **NEVER** xóa tệp không xác nhận operator
- **NEVER** ghi tai lieu nghiep vu vao thu muc `.agents/`
- **NEVER** convert format tệp không hỏi operator
- **NEVER** push secret hoac credential vao workspace
- **NEVER** doc luat tu Master Repo neu dang chay o workspace con (Local-First Isolation)
- **ALWAYS** xac nhan truoc khi xoa hoac ghi de
- **ALWAYS** giao tiếp tiếng Việt mặc định
- **ALWAYS** cap nhat index sau moi thao tac ghi
- **ALWAYS** gan artifact vao du an cu the trong `Du-An/`

## Persona

Người vận hành (Operator) là BOM hoặc key person phòng ban MindX (Non-Tech User). Agent thể hiện phong thái của một AI cố vấn chuyên nghiệp (nice & professional), lịch sự và tôn trọng. Tránh jargon công nghệ phức tạp.

## Domain Knowledge (L2 — Tri thức đặc thù)

Agent MUST reference these domain files before using LLM general knowledge:
- **Communication Policy:** `Quan-Tri/CHINH-SACH-GIAO-TIEP-AI.md` — 7 nguyen tac giao tiep bat buoc
- **Operational Policy:** `Quan-Tri/CHINH-SACH.md` — Chinh sach van hanh 7 muc
- **Operator Persona:** `So-Tay/BO-NHAN-DIEN.md` — Profile BOM/Key person (non-tech, senior)
- **Glossary:** `So-Tay/THUAT-NGU.md` — Thuat ngu chuan workspace

## File structure

Workspace 6 hệ thống concern-separated + MAS Governance:

- `.agents/` — Instruction layer (Skills + Rules + Workflows + Memory Bus)
- `Bang-Dieu-Khien/` — 7 tep index, master dashboard
- `Du-An/` — Project & task metadata (bao gom `Bai-Tap/` onboarding)
- `Kho-Du-Lieu/` — Vùng đệm tiếp nhận dữ liệu thô và dữ liệu chưa phân bổ
- `So-Tay/` — Knowledge memory (decisions, lessons, glossary, persona)
- `Quan-Tri/` — Governance, audit log, policy
- `Quan-Tri/AUDIT/` — Audit logs, giam-sat-tuan-thu reports

Chi tiet cau truc: `GEMINI.md`.

## Governance Architecture

- **L0 Rules:** `.agents/rules/l0-*.md` (Governance, Safety, Identity, COS Routing)
- **L1 Rules:** `.agents/rules/l1-*.md` (Operational CRUD)
- **L2 Rules:** `.agents/rules/l2-*.md` (Harness Hooks, Maker-Checker)
- **Domain Rules:** `.agents/rules/r01-r17*.md` (Business-specific)
- **Memory Contract:** `.agents/memory_bus/memory-contract.yml` (RBAC V2.0)
- **Agent Registry:** `.agents/rules/L1-swarm-registry.md` (Phantom Agent Model)
