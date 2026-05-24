# Scripts — business-artifact-builder

Thư mục này chứa script tham khảo để xuất DOCX từ markdown.

## Trạng thái

- Script chỉ là reference cho bước hardening.
- Chưa claim đã test trong Google Antigravity.
- Chỉ dùng khi môi trường có Python và thư viện `python-docx`.

## Cách dùng dự kiến

```bash
python export_docx_from_markdown.py input.md output.docx
```

## Lưu ý

- Không ghi đè file gốc nếu chưa được duyệt.
- Nếu export fail, giữ `docx-ready.md` làm output an toàn.
- Với template Word công ty phức tạp, cần hardening thêm.
