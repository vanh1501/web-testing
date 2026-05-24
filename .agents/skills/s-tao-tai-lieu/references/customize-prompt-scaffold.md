# Customize business-artifact-builder — Prompt scaffold

## Template chat với Agent

```text
@business-artifact-builder Tôi muốn customize skill này cho phòng ban/doanh nghiệp [TÊN].

1. HOOK_DOCUMENT_TYPE — Loại tài liệu tôi dùng nhiều:
   [report / proposal / SOP / meeting_minutes / memo / business_letter / training_handout / project_handoff]

2. HOOK_OUTPUT_CHANNEL — Đầu ra mặc định:
   [docx_ready_markdown / docx_file / google_docs_ready / marp_slide / google_slides_ready / package]

3. HOOK_STYLE_PROFILE — Tone mặc định:
   [executive / formal / operational / training / internal / client_facing]

4. HOOK_BRAND_PROFILE — Brand guideline:
   [có BO-NHAN-DIEN.md / có template Word / chưa có]

5. HOOK_TEMPLATE_LIBRARY — Mẫu riêng nếu có:
   [paste path hoặc mô tả template]
```

## Agent hành xử

1. Đọc `SKILL.md` hiện tại.
2. Cập nhật 5 HOOK markers theo context.
3. Không thay đổi hard quan-ly-quy-tac về dữ liệu nhạy cảm, citation, human review, không ghi đè file gốc.
4. Bump version v1.0 → v1.1 nếu customize.
5. Tạo `LICH-SU-THAY-DOI.md` nếu workspace yêu cầu.

## Standardize Test

1. Test DOCX: chuyển 1 draft báo cáo thành DOCX-ready.
2. Test Slide: chuyển cùng nội dung thành deck 5-8 slide.
3. Test Package: tạo báo cáo + slide tóm tắt.
4. Test sensitivity: input có tên/email cá nhân → skill phải cảnh báo/mask.
5. Test brand: nếu có brand kit, output không được bịa màu/logo/font.

## Không customize được

- Không bỏ human review với tài liệu gửi ngoài.
- Không bỏ cảnh báo dữ liệu nhạy cảm.
- Không bỏ yêu cầu source/citation khi dùng số liệu.
- Không nâng slide bullet limit vượt 3 bullet cấp 1.
- Không claim đã export file thật nếu chỉ tạo markdown.
