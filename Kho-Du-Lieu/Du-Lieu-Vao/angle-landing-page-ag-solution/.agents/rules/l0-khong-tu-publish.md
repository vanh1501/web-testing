# Rule L0 — Không tự publish

Agent không được tự merge, publish hoặc đưa landing page live nếu chưa có người có quyền repo xác nhận.

Agent chỉ được:
- Chuẩn bị file
- Chuẩn bị branch name
- Chuẩn bị commit message
- Chuẩn bị PR description
- Viết lệnh Git mẫu

Bắt buộc dừng ở Publish Gate nếu:
- HTML QA chưa pass
- Form/tracking chưa rõ
- Claim chưa duyệt
- Người có quyền repo chưa xác nhận
