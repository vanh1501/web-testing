---
description: "System component: WORKFLOW_INDEX.md"
semantic_triggers: ['WORKFLOW_INDEX']
---

---
title: "Workflow Registry"
domain_tags: ["workflows", "registry", "index", "orchestration"]
summary: "Index 7 workflow trong workspace MindX BOM Library v2.0 — check trước khi route"
applicable_agents: ["ALL"]
version: v2.0
last_updated: 2026-05-15
audit_score: 7/7 production-ready (post-rebuild)
---

# 00_WORKFLOW_INDEX — MindX BOM Workflow Registry (v2.0)

## 1. Phân hệ Nghiệp vụ Cốt lõi (core-business/)

| # | Workflow ID | Name | Skill Target | Status |
|---|-------------|------|--------------|--------|
| 1 | WF-PRJ-INIT-01 | [khoi-tao-du-an-moi](core-business/w-khoi-tao-du-an-moi.md) | `quan-ly-du-an` | v2.0 Production |
| 2 | WF-TASK-INTAKE-01 | [phan-tich-nhiem-vu](core-business/w-phan-tich-nhiem-vu.md) | `phan-tich-yeu-cau, quan-ly-du-an` | v2.0 Production |
| 3 | WF-DATA-REPORT-01 | [phan-tich-va-bao-cao](core-business/w-phan-tich-va-bao-cao.md) | `phan-tich-du-lieu, quan-ly-du-an, tao-tai-lieu` | v2.0 Production |
| 4 | WF-PM-COMPREHENSIVE-01 | [quan-tri-du-an](core-business/w-quan-tri-du-an.md) | `quan-ly-du-an, tao-tai-lieu` | v2.0 Production |
| 5 | WF-DOC-PRODUCTION-01 | [san-xuat-tai-lieu](core-business/w-san-xuat-tai-lieu.md) | `tao-tai-lieu, chuan-hoa-tai-lieu` | v2.0 Production |
| 6 | WF-BPM-LIFECYCLE-01 | [s-xay-dung-quy-trinh](core-business/w-xay-dung-quy-trinh.md) | `xay-dung-quy-trinh, tao-tai-lieu, chuan-hoa-tai-lieu` | v2.0 Production |
| 7 ⭐ | WF-META-AUDIT-01 | [audit-va-toi-uu-luong-cong-viec](core-business/w-audit-va-toi-uu-luong-cong-viec.md) | `phan-tich-yeu-cau, tao-tai-lieu, chuan-hoa-tai-lieu` | v2.0 Production (NEW) |

⭐ = Meta-workflow Layer 2 — audit/optimize chính workflow library (replicate pattern Luồng 2+3 của WF6)

## 2. Phân hệ Vận hành Hệ thống (system-ops/)

| # | Workflow ID | Name | Target |
|---|-------------|------|--------|
| 8 | WF-SYS-START | [khoi-dong-phien](system-ops/w-khoi-w-dong-phien.md) | Khởi tạo phiên, load state |
| 9 | WF-SYS-END | [dong-phien](system-ops/w-dong-phien.md) | Đóng phiên, cập nhật KI |
| 10 | WF-SYS-SAVE | [luu-phien](system-ops/w-luu-phien.md) | Checkpoint giữa chừng |
| 11 | WF-SYS-HEALTH | [kiem-tra-suc-khoe](system-ops/w-kiem-tra-suc-khoe.md) | Đồng bộ index và audit sức khỏe nhẹ |
| 12 | WF-SYS-AUDIT | [s-kiem-dinh-workspace](system-ops/w-kiem-dinh-workspace.md) | Phân tích và kiểm định cấu trúc hệ thống 5-Zone (v3.0) |
| 13 | WF-SYS-OPTIMIZE | [s-toi-uu-workspace](system-ops/w-toi-uu-workspace.md) | Tự động vá lỗi (Self-healing) dựa trên Audit Report (v2.0) |
| 14 | WF-SYS-CLEAN | [ve-sinh-workspace](system-ops/w-ve-sinh-workspace.md) | Archive rác, dọn dẹp dự án |
| 15 | WF-SYS-SKILL | [s-tao-ky-nang-moi](system-ops/w-tao-ky-nang-moi.md) | Scaffold skill mới |
| 16 | WF-SYS-HELP | [tro-giup](system-ops/w-tro-giup.md) | Hướng dẫn sử dụng BOM |
| 17 | WF-SYS-DEPLOY | [cai-dat-giai-phap](system-ops/w-cai-dat-giai-phap.md) | Tiếp nhận ZIP Spec Pack, kiểm định 3 Lớp, cài đặt components |

## 3. Phân hệ Báo cáo Định kỳ (02-reporting/)

| # | Workflow ID | Name | Target |
|---|-------------|------|--------|
| 18 | WF-RPT-MONTHLY | [monthly-kpi-report](02-reporting/w-monthly-kpi-report.md) | Báo cáo KPI tháng tự động |

## Cross-Workflow Chaining Map

```
Operator yêu cầu thô
    ↓ phan-tich-nhiem-vu (WF2: Task Intake Gateway)
    │   ↓ Classify Task vs Project
    │
    ├── PROJECT → khoi-tao-du-an-moi (WF1: Scaffold)
    │              ↓
    │              quan-tri-du-an (WF4: PM End-to-End)
    │                  ↓ project running
    │                  phan-tich-va-bao-cao Route 2 (WF3: RAG Status)
    │
    ├── DATA TASK → phan-tich-va-bao-cao (WF3: Mega Data Pipeline)
    │                ↓ Route 1/3/4 → render báo cáo
    │                san-xuat-tai-lieu (WF5: Doc Production)
    │                    ↓ Mandatory chain
    │                    chuan-hoa-tai-lieu → DOCX/PPTX
    │
    ├── PROCESS TASK → xay-dung-quy-trinh (WF6: BPM Lifecycle)
    │                   ↓ Luồng 1/2/3 CREATE/AUDIT/OPTIMIZE
    │                   san-xuat-tai-lieu (WF5: SOP Package format)
    │
    └── DOC TASK → san-xuat-tai-lieu (WF5: Doc Production)

META-LAYER:
  audit-va-toi-uu-luong-cong-viec (WF7) → audit any of WF1-6 + chính nó
```

## Skill Target Coverage (workflow → skill mapping)

| Skill v2.0 | Workflows dùng |
|------------|---------------|
| `chuan-hoa-tai-lieu` | WF3 (R3, R4), WF5 (mandatory chain), WF6, WF7 |
| `nghien-cuu-thi-truong` | (chưa workflow dùng — gap, có thể tạo workflow research-pipeline sau) |
| `phan-tich-du-lieu` | WF3 (Route 1, 4), WF6 (data step) |
| `phan-tich-yeu-cau` | WF2 (intake + breakdown), WF7 (file intake) |
| `quan-ly-du-an` | WF1, WF2, WF3 (Route 2), WF4 |
| `tao-tai-lieu` | WF3 (R3, R4), WF4 (Step 7), WF5 (chính), WF6, WF7 |
| `xay-dung-quy-trinh` | WF6 (chính) |

## Deployment Notes cho Google Antigravity

1. **Unzip vào `.agents/workflows/` folder** của workspace Antigravity
2. **Verify skill library v2.0 đã deploy trước** (skill names trong workflow PHẢI khớp library)
3. **Add `kb-mas-v8-gold-criteria.md` vào project knowledge** (cần cho WF7 audit)
4. **Test routing 7 workflow** trong Brain — gõ semantic trigger cho mỗi workflow
5. **Test HITL timeout** — trigger 1 workflow, không response 24h, verify auto-action fire
6. **Test Circuit Breaker** — force skill timeout, verify retry 3 + fallback
7. **Monitor Output Contract** — mọi workflow xuất JSON theo schema declared

## Known Gaps (cần build sau)

| Gap | Mô tả | Priority |
|-----|-------|----------|
| `workflow-research-pipeline` | Workflow dedicated cho `nghien-cuu-thi-truong` (currently không có WF chính chuyên cho research) | P1 |
| `workflow-onboarding-bom` | Quick-start guide thành workflow tự động cho BOM mới | P2 |
| `workflow-skill-library-audit` | Tương tự WF7 nhưng cho SKILL library (audit skill thay vì workflow) | P2 |

## Audit & Maintenance Schedule

- **Định kỳ 30 ngày:** Chạy WF7 Luồng C META-AUDIT trên toàn library, catch drift sớm
- **Định kỳ 60 ngày:** Chạy WF7 Luồng A trên 2-3 workflow critical (WF2 Task Intake, WF3 Mega Data)
- **Khi skill library update:** Chạy WF7 Luồng A trên các workflow có Skill Target affected
- **Khi BOM report bug workflow:** Chạy WF7 Luồng A + B trên workflow đó

## References

- Audit baseline: `audit-report-mindx-workflow-library-v1.md`
- Skill library: `mindx-skill-library-v2.0.zip` (skill v2.0 dependencies)
- KB rubric: `kb-mas-v8-gold-criteria.md` v1.0.1
- Quick-start BOM: `cam-nang-bom-7-skill-mindx-v1.md`
