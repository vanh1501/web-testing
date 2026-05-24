---
description: "System component: w-deploy-appendix.md"
semantic_triggers: ['w-deploy-appendix']
---

# Phụ lục: /w-cai-dat-giai-phap — Circuit Breaker, Edge Cases, Output Contract

> **Parent Workflow:** `01-w-cai-dat-giai-phap.md` (WF-SYS-DEPLOY-01 v2.0)
> Agent BẮT BUỘC đọc file này khi gặp lỗi hoặc cần tham chiếu Output Contract.

## Circuit Breaker Policy

| Failure mode | Detection | Retry | Fallback |
|---|---|---|---|
| ZIP corrupt | Unzip exception | 0 (immediate) | HALT + báo Operator |
| Skill build fail | `01-tao-ky-nang-moi` error | 2 lần | Skip skill + log delta |
| Workflow build fail | `01-tao-quy-trinh-moi` error | 2 lần | Skip workflow + log delta |
| Write permission denied | OS error | 1 lần | HALT + ask permission |
| >3 component failures | Accumulative count | 0 | **SYSTEMIC-HALT** — Dừng deploy, rollback staging, báo Operator |

## Edge Cases & Recovery

1. **ZIP double-wrapped** (folder con lồng nhau) → Auto-detect root folder (tìm `.agents/` hoặc `README.md`).
2. **ZIP không có `business_sources/`** → WARN "Skill/Workflow có thể thiếu ngữ cảnh nguồn." + vẫn deploy.
3. **Skill tham chiếu skill chưa có** → WARN liệt kê broken dependency. Không HALT (có thể fix ở PDCA).
4. **Operator muốn deploy 1 phần** → Dùng `--only skills` hoặc `--only workflows`. Skip component ngoài scope.
5. **Deploy giữa chừng crash** → Staging vẫn còn. Chạy lại workflow → Idempotent (skip đã deploy, tiếp phần còn lại).
6. **ZIP v1.1 đè lên v1.0** (Patch) → Step 6 Conflict Detection xử lý: backup v1.0 → deploy v1.1.
7. **Component domain không khớp workspace** → WARN "Skill [X] có thể không phù hợp domain." + vẫn deploy.
8. **Tên file chứa ký tự đặc biệt** → Auto-sanitize (slugify kebab-case) + WARN.
9. **2 ZIP riêng biệt (Route 2)** → Chạy workflow 2 lần: lần 1 với Skill Library, lần 2 với Workflow Library. Idempotent đảm bảo an toàn.

## Output Contract (Idempotent JSON)

```json
{
  "workflow_id": "WF-SYS-DEPLOY-01",
  "route": "1_spec_pack | 2_library_upgrade",
  "run_status": "success | partial_success | halt",
  "spec_pack_name": "...",
  "qa_gate_results": {
    "layer_1_manifest": "A | B | C",
    "layer_2_format": "PASS | WARN | FAIL",
    "layer_3_safety": "PASS | FAIL"
  },
  "deployed": {
    "s-quan-ly-quy-tac": [{"name": "...", "path": "...", "status": "new | overwrite"}],
    "skills": [{"name": "...", "path": "...", "status": "new | overwrite | upgrade"}],
    "workflows": [{"name": "...", "path": "...", "slash_command": "...", "status": "new | overwrite | same_skip"}],
    "sources": [{"name": "...", "path": "..."}],
    "docs": [{"name": "...", "path": "..."}]
  },
  "conflicts_resolved": [{"name": "...", "action": "overwrite | rename | skip"}],
  "skipped": [{"name": "...", "reason": "already_exists | same_version"}],
  "backup_path": "_archive/{timestamp}/",
  "index_sync": true,
  "delta_report_path": "Kho-Du-Lieu/Ket-Qua/{du-an}/BAO-CAO-TRIEN-KHAI-SPEC.md",
  "next_action": "Chạy TEST_PROMPTS.md hoặc Slash Command mới để kiểm thử"
}
```

## Cross-Workflow Chaining

- **Receives from:** Operator upload ZIP (Day 2 Cụm 2) hoặc `/w-00-phan-tich-nhiem-vu` (khi classify là DEPLOY task).
- **Hands off to:**
  - `/slash-command-moi` → Test thực tế (Day 2 Cụm 2 bước chạy thử).
  - Cụm 3 PDCA Loop → Nếu test có lỗi, gửi báo cáo cho ChatGPT.
  - `/01-kiem-dinh-workspace` → Audit toàn workspace post-deploy.

```
Operator upload ZIP vào Kho-Du-Lieu/Du-Lieu-Vao/
    ↓
/w-cai-dat-giai-phap (THIS WORKFLOW)
    ↓ Auto-Router
    ├── Route 1 (Spec Pack) → QA 3 Lớp nghiêm ngặt → Deploy
    └── Route 2 (Library)   → QA nhẹ → Path Mapping → Deploy
        ↓ Deploy thành công
        ├── Operator chạy /slash-command-moi → Test thực tế
        │   ↓ Có lỗi
        │   ├── BAO-CAO-PHAN-TICH-CHAY-THU.md (Cụm 2)
        │   └── Gửi ChatGPT → PDCA Loop (Cụm 3)
        │
        └── /01-kiem-dinh-workspace → Audit post-deploy
```
