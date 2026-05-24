---
title: "L1 Workspace Standards"
domain_tags: ["standards", "operations", "workspace"]
summary: "Chuẩn vận hành workspace: output format, memory, project management"
applicable_agents: ["ALL"]
trigger: always_on
---

# L1 — Workspace Standards

> [!IMPORTANT] Override Priority: Tier 1 (Strategic)
> Cấp độ kiểm soát tối cao của Workspace. Mọi Workflow và Skills đều phải tuân thủ nghiêm ngặt chuẩn đầu ra và cấu trúc nhớ của L1 này. Mọi nỗ lực ghi đè sẽ dẫn tới Audit Failure.

## Output Standards

### PHẢI (Mandatory)
- PHẢI dùng Pyramid Principle cho mọi output >200 từ
- PHẢI check CENTRAL_REGISTRY.md KIs trước khi bắt đầu task cần nghien-cuu-thi-truong/analysis
- PHẢI dùng template từ `.context/templates/` khi có template phù hợp cho output type
- PHẢI self-check quality (quality-rubric.md Quick Check) trước khi deliver
- PHẢI acknowledge uncertainty: "Insight này confidence [H/M/L] vì [reason]"

### NÊN (Important)
- NÊN suggest next step sau mỗi output: "Bước tiếp theo bạn có thể..."
- NÊN offer 2-3 options khi có quyết định cần user chọn
- NÊN cite source khi reference số liệu/fact external
- NÊN format output phù hợp audience (executive vs team vs external)

### CẤM (Prohibited)
- CẤM hallucinate data — không có thì nói rõ "cần bổ sung data"
- CẤM vượt scope mà không report COORD trước
- CẤM deliver output score <4/5 mà không cải thiện
- CẤM bypass template khi template tồn tại cho output type đó
- CẤM Worker liên lạc trực tiếp Worker khác — phải qua COORD

## Memory Standards (Kiến trúc Lưu trữ Phân tầng)

### 1. Dữ liệu Vận hành & Quản trị (Lưu trong Workspace)
Tất cả các tài liệu có giá trị lưu trữ dài hạn của hệ thống phải được lưu đúng cấu trúc 5-Zone:
- **`Quan-Tri/AUDIT/`**: Chứa toàn bộ các báo cáo kiểm định chất lượng, báo cáo Optimize, và Audit Logs của hệ thống (Tuyệt đối không tạo thư mục `artifacts/` hay `domain/` ở thư mục gốc).
- **`Quan-Tri/BAO-CAO-TUAN/`**: Chứa các báo cáo tuần, tiến độ sức khỏe workspace.
- **`Quan-Tri/AGENT-LOG.md`**: Log hoạt động của các Agent.
- **`So-Tay/`**: Tương đương với Knowledge/Domain layer. Chứa các quy định, KIs đã chắt lọc (distill), glossary và Persona. (Sổ cái kinh nghiệm `CENTRAL_REGISTRY.md` lưu tại `Quan-Tri/`).

### 2. Dữ liệu Tạm thời & Nhật ký Phiên (Lưu bởi IDE)
- **Tuyệt đối KHÔNG lưu** các tệp rác sinh ra trong quá trình Chat (như `task.md`, `walkthrough.md`, `implementation_plan.md` hay raw session logs) vào trong thư mục Workspace.
- Các tài liệu này (Session Reports, Kế hoạch thực thi tạm thời) **PHẢI ĐƯỢC IDE TỰ ĐỘNG LƯU** vào ổ cứng ẩn tại: `C:\Users\Admin\.gemini\antigravity\brain\<conversation-id>\`.
- Lệnh cấm: **KHÔNG ĐƯỢC TẠO** các thư mục mang tên `brain/`, `artifacts/`, `domain/` tại thư mục gốc của Workspace. Cấu trúc 5-Zone là bất khả xâm phạm.

### Context Engineering (TokenOps & Circuit Breaker)
- **[20K Token Circuit Breaker]**: Nếu một Agent nhận File đầu vào (Input/References) vượt quá 20K Tokens, BẮT BUỘC NGẮT LUỒNG (System Halt) và từ chối đọc nguyên gốc. Tự động chuyển file cho skill `toi-uu-bo-nho` thực thi Semantic Compression.
- **[Semantic Compression]**: Chỉ trích xuất (Splice) thông tin phục vụ task hiện tại. KHÔNG lưu trữ rác dữ liệu vượt mức. Cấm cắt gọt (Truncate) luật lõi (L0/L1) dưới mọi hình thức.

## Project Folder Standards

### Epic → Project → Task Structure
```
projects/
├── {epic-name}/                    # Epic = nhóm projects cùng mục tiêu
│   ├── _epic-brief.md              # Mô tả epic, objectives, success criteria
│   ├── {project-name}/             # Project cụ thể
│   │   ├── brief.md                # Project brief (template-based)
│   │   ├── tasks.md                # Task list / WBS
│   │   ├── status/                 # Status reports theo period
│   │   │   └── {YYYY-MM-DD}.md    # Từng report
│   │   ├── artifacts/              # Deliverables (reports, slides, data)
│   │   └── notes.md                # Meeting notes, decisions, context
│   └── {another-project}/
└── {another-epic}/
```

### Naming Convention
- Epic: lowercase, hyphenated, mô tả mục tiêu: `digital-transformation`, `q2-initiatives`
- Project: lowercase, hyphenated, mô tả cụ thể: `crm-implementation`, `website-redesign`
- Status files: date-based `YYYY-MM-DD.md`
- Artifacts: `{type}_{topic}_{date}.{ext}` (e.g., `report_q1-revenue_2026-04-22.md`)

### Auto-Creation Protocol
Khi PRO-W04 nhận yêu cầu tạo project:
1. Hỏi user: "Project này thuộc epic nào?" (suggest existing hoặc tạo mới)
2. Tạo folder structure
3. Generate brief.md từ template
4. Return: "Đã tạo project tại `projects/{epic}/{project}/`. Brief sẵn sàng để review."
