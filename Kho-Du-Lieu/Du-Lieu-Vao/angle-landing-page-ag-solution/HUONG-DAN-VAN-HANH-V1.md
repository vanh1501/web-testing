# Hướng dẫn vận hành v1

## Bước 1 — Chuẩn bị input

Điền `dau-vao/input-angle-moi.md` với:
- Tên angle
- Content angle
- Audience
- CTA chính
- Section giữ nguyên
- USP ưu tiên nếu có
- Ghi chú claim cần tránh

## Bước 2 — Chạy workflow

Gọi:

```text
/tao-landing-page-theo-angle dau-vao/input-angle-moi.md
```

## Bước 3 — Duyệt angle và claim

Người duyệt:
- Performance Marketer duyệt angle brief.
- Marketing/Product Owner duyệt claim.

Dừng nếu có claim chưa duyệt.

## Bước 4 — Duyệt copy

Kiểm tra:
- Hero có đúng Big Promise không.
- Problem có cảnh đời thật không.
- Why có thông tin cụ thể không.
- USP có map với problem không.
- CTA đúng input không.

## Bước 5 — Tạo HTML và kiểm HTML

HTML phải:
- Có form ở hero nếu CTA là đăng ký/test/tư vấn.
- CTA đúng wording.
- Responsive cơ bản.
- Không tự bịa proof.
- Ghi rõ form demo nếu chưa có tracking.

## Bước 6 — GitHub handoff

Chỉ chạy khi HTML QA pass. Agent chỉ tạo:
- Tên file
- Branch name
- Commit message
- PR description
- Lệnh Git mẫu

Người có quyền repo tự merge/publish.

## Bước 7 — Đo kết quả

Sau khi publish thật:
- Ghi URL
- Baseline CR
- Test CR
- Traffic source
- Nhận xét
- Quyết định giữ/tắt/sửa/scale
