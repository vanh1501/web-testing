---
name: 00-trich-claim-tu-landing-page
description: |
  Trích và phân loại claim từ landing page gốc, claim library, sale kit và nguồn dự án.
---

# Skill: 00-trich-claim-tu-landing-page

## Khi nào dùng

Dùng trong workflow `00-tao-landing-page-theo-angle` khi cần: Trích và phân loại claim từ landing page gốc, claim library, sale kit và nguồn dự án.

## Đầu vào bắt buộc

- Input angle hoặc output của skill trước đó.
- CTA chính.
- Section giữ nguyên.
- Claim library nếu có liên quan.
- Nguồn dự án tương ứng.

## Mini workflow

1. Kiểm tra input đủ/chưa đủ.
2. Đọc nguồn dự án liên quan.
3. Thực hiện nhiệm vụ chính của skill.
4. Tạo deliverable chuẩn.
5. Gắn cờ claim/rủi ro nếu có.
6. Bàn giao sang skill tiếp theo hoặc dừng ở gate phù hợp.

## Deliverables

- File markdown/output theo tên skill.
- Ghi chú rủi ro.
- Handoff note.

## Tiêu chí đạt

- Output rõ ràng, có cấu trúc.
- Không bịa claim.
- Không vượt quyền.
- Có điểm dừng nếu thiếu dữ liệu hoặc cần người duyệt.
- Có handoff rule.

## Handoff

- Nếu đạt: chuyển sang skill tiếp theo trong workflow.
- Nếu chưa đạt: quay lại skill trước hoặc dừng ở gate.
- Nếu có claim/HTML/publish risk: dừng chờ người duyệt.
