---
description: Cơ chế Maker-Checker bắt buộc kiểm tra chéo trước khi ghi đè file hệ thống hoặc xóa dữ liệu.
activation: Always On
---

# L2 Maker-Checker Protocol

> [!IMPORTANT] Override Priority: High
> Enforced by Harness Layer.

## Scope

Maker-Checker áp dụng cho các thao tác HIGH-RISK:
1. Xóa file/thư mục.
2. Ghi đè file đã tồn tại (không qua version pattern).
3. Sửa đổi file trong `.agents/quan-ly-quy-tac/` hoặc `.agents/workflows/`.
4. Thay đổi cấu trúc thư mục (tạo/xóa/đổi tên thư mục hệ thống).

## Protocol

### Maker (Agent thực thi):
1. Mô tả rõ hành động sẽ thực hiện.
2. Liệt kê file/thư mục bị ảnh hưởng.
3. Đánh giá rủi ro: LOW / MEDIUM / HIGH.

### Checker (Operator xác nhận):
1. Review đề xuất từ Maker.
2. Approve / Reject / Request modification.

### Execution:
- `Approve` → Agent thực thi, ghi log vào `Quan-Tri/AGENT-LOG.md`.
- `Reject` → Agent hủy thao tác, ghi log lý do reject.
- `Request modification` → Agent điều chỉnh, quay lại Maker step.

## 3-Strike Escalation Rule

- Strike 1: Rework → Agent sửa và đề xuất lại.
- Strike 2: Rework → Agent sửa lần cuối.
- Strike 3: HALT → Ngừng thao tác hoàn toàn. Ghi vào `AGENT-LOG.md` flag "maker-checker-escalation". Bàn giao cho đặc vụ `Cố vấn AI MindX` hoặc chờ Sếp quyết định hướng xử lý.

## Exemptions

Các thao tác KHÔNG cần Maker-Checker:
- Tạo file mới (chưa tồn tại trước đó).
- Đọc/phân tích file (read-only).
- Cập nhật `Quan-Tri/AGENT-LOG.md` (log operation).
- Cập nhật index files trong `Bang-Dieu-Khien/` (auto-sync).
