# Hướng dẫn nhân sự dùng @business-artifact-builder

## Skill này dùng để làm gì?

Dùng để biến nội dung đã có thành tài liệu dễ gửi, dễ đọc, đúng format hơn. Người dùng chỉ cần đưa nội dung thô và nói rõ muốn đầu ra là báo cáo, đề xuất, SOP, biên bản, slide hoặc cả bộ tài liệu.

## 3 prompt mẫu dùng nhanh

### Mẫu 1 — Làm báo cáo DOCX-ready

```text
@business-artifact-builder Chuyển nội dung sau thành báo cáo DOCX-ready cho [người đọc].
Yêu cầu: kết luận trước, có bảng action plan, có appendix nguồn.
[paste nội dung]
```

### Mẫu 2 — Làm proposal

```text
@business-artifact-builder Format nội dung sau thành proposal gửi [người đọc].
Yêu cầu: bối cảnh, vấn đề, 2 phương án, trade-off, khuyến nghị, kế hoạch và rủi ro.
[paste nội dung]
```

### Mẫu 3 — Làm slide tóm tắt

```text
@business-artifact-builder Chuyển báo cáo sau thành slide deck 6 slide.
Yêu cầu: mỗi slide 1 ý chính, tối đa 3 bullet, slide cuối có next steps.
[paste nội dung]
```

## Khi nào cần báo manager/BOM duyệt?

- Tài liệu gửi khách hàng, BOD, đối tác hoặc public.
- Nội dung có dữ liệu nhạy cảm.
- Output có đề xuất ngân sách, nhân sự, pháp lý, tài chính.
- Agent cảnh báo `Source needed`, `Sensitive data`, hoặc `Human review required`.

## Lưu ý cho người vận hành

- Skill này format và trình bày, không thay thế phán đoán quản lý.
- Nếu nội dung đầu vào sai, skill không được phép làm nó thành “đúng” bằng ngôn từ đẹp.
- Nếu cần phân tích dữ liệu, dùng skill phân tích trước rồi mới dùng skill này để trình bày.
