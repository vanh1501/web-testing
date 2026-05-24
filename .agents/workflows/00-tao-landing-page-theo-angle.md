# Quy Trình: /w-00-tao-landing-page-theo-angle

## Trigger

`/w-00-tao-landing-page-theo-angle dau-vao/input-angle-moi.md`

## Mục tiêu

Biến content angle thành landing page HTML hoàn chỉnh, có kiểm claim, message match, HTML QA và GitHub handoff.

## Role map

| Bước | Agent | Con người |
|---|---|---|
| Input check | Kiểm đủ dữ liệu | Marketer bổ sung |
| Angle brief | Phân tích angle | Marketer duyệt |
| Claim check | Phân loại claim | Marketing/Product Owner duyệt |
| Copy | Viết landing page | Marketer duyệt |
| Message match | Chấm và tạo revision brief | Marketer quyết |
| HTML | Tạo file HTML | Người kiểm HTML review |
| GitHub handoff | Chuẩn bị PR/lệnh Git | Người có quyền repo publish |

## Skill chain

1. `00-phan-tich-angle`
2. `00-trich-claim-tu-landing-page`
3. `00-viet-lai-copy-landing-page`
4. `00-kiem-tra-message-match`
5. `00-tao-html-landing-page`
6. `00-kiem-tra-html`
7. `00-tao-github-handoff`

## Decision gates

| Gate | Điều kiện dừng | Người duyệt |
|---|---|---|
| Input Gate | Thiếu angle/CTA/audience/section giữ nguyên | Performance Marketer |
| Claim Gate | Claim nhạy cảm | Marketing/Product Owner |
| Content Gate | Copy final | Performance Marketer |
| HTML Gate | HTML chưa pass QA | Người kiểm HTML |
| Publish Gate | Chuẩn bị merge/live | Người có quyền repo |

## Output

Tạo folder `dau-ra/<ten-angle>/` gồm:
- `angle-brief.md`
- `claim-check.md`
- `landing-page-copy.md`
- `message-match-check.md`
- `landing-page.html`
- `html-qa-checklist.md`
- `github-handoff.md`
- `experiment-log.md`

## Feedback loop

Sau khi chạy test CR:
- Ghi baseline CR
- Ghi test CR
- Ghi traffic source
- Ghi insight học được
- Cập nhật backlog cải tiến angle/copy/html
