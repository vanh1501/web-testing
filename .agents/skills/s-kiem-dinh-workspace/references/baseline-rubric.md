# MAS 4.0 Baseline Compliance Rubric

Bảng tính điểm phục vụ cho Bước 2 của Workspace Auditor.

## 11-Point Checkpoint
1. **.agents/agents.md**: Có Sứ mệnh Domain-specific, Có Function Boundaries, Có Ràng Buộc Cấm (Restrictions).
2. **.agents/quan-ly-quy-tac/**: Đạt >= 3 files. Không được thiếu 3 file thần chú: `core-standards.md`, `safety-guardrails.md`, `handoff-protocol.md`.
3. **.agents/workflows/**: Đạt >= 2 files. Workflows dập từ Value Chain, không phải dummy file.
4. **.context/PROJECT.md**: Sống động, Có sứ mệnh Stakeholders, Có Phạm Vi Cụ Thể (In/Out Scope). Không dùng Placeholder.
5. **.context/GLOSSARY.md**: Bộ từ điển tối thiểu 10 Thuật Ngữ Của Ngành (Không viết kiểu "Agent là gì").
6. **QUEUE.md**: Nằm gọn trong `artifacts/handoffs/` và giữ nguyên bảng Template Chờ (Kanban).
7. **golden-tests.md**: >= 3 Cases Nhập vai Vàng (Happy Path, Edge Case Dữ Liệu Thiếu, Violation Cấm Kỵ).
8. **QUALITY-LOG.md**: Timeline nhật ký sức khỏe, cách entry cuối < 14 Ngày.
9. **IMPROVEMENT-BACKLOG.md**: Bể phốt chứa các Bug, Issue, Hoặc Món Đồ Đợi Fix.
10. **Baseline Drift**: Nhận diện phiên bản Version Khởi Tạo. Nếu File Cốt lõi bị xoá, gạch bỏ, giảm nhẹ hình phạt (Tamper) => Tước Quyền 🔴.
11. **Memory Bus Keys**: `keys.yaml` có định tuyến được State Sync Variables hay không?
