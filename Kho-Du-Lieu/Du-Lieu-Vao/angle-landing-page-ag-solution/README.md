# Angle Landing Page AG Solution

Gói này là workspace vận hành giải pháp **Content Angle → Landing Page HTML** trên Google Antigravity hoặc một Project trong ChatGPT.

## Mục tiêu

Performance Marketer nhập một content angle mới. Agent sẽ:

1. Phân tích angle.
2. Kiểm tra claim.
3. Viết lại landing page theo angle.
4. Giữ nguyên các section cố định.
5. Kiểm tra message match.
6. Tạo HTML landing page.
7. Kiểm tra HTML.
8. Chuẩn bị GitHub handoff.

## Người dùng chính

- Performance Marketer: nhập angle, duyệt nội dung, đo CR.
- Marketing/Product Owner: duyệt claim.
- Người kiểm tra HTML: duyệt layout, form, CTA, responsive.
- Người có quyền repo: merge/publish.
- Agent: tạo bản nháp, kiểm tra, tạo HTML, chuẩn bị handoff.

## Cách chạy nhanh

1. Điền file `dau-vao/input-angle-moi.md`.
2. Gọi workflow: `/tao-landing-page-theo-angle dau-vao/input-angle-moi.md`
3. Agent tạo output trong `dau-ra/<ten-angle>/`.
4. Người phụ trách duyệt theo các gate.
5. Nếu HTML QA pass, dùng `github-handoff.md` để đưa file lên repo.

## Output chuẩn

Mỗi angle sẽ sinh:

- `angle-brief.md`
- `claim-check.md`
- `landing-page-copy.md`
- `message-match-check.md`
- `landing-page.html`
- `html-qa-checklist.md`
- `github-handoff.md`
- `experiment-log.md`
