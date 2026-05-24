# Variant — Executive Report DOCX

## Mục đích

Dùng khi cần chuyển nội dung thô thành báo cáo điều hành gửi CEO/BOD/manager.

## Khi nào dùng

- Báo cáo tuần/tháng/quý.
- Báo cáo kết quả dự án.
- Báo cáo phân tích từ output của `bi-report-builder`.
- Báo cáo đánh giá hiện trạng/quy trình.

## Prompt mẫu

```text
@business-artifact-builder Chuyển nội dung sau thành báo cáo DOCX-ready cho CEO. 
Mục tiêu: đọc trong 5 phút, thấy kết luận, bằng chứng, rủi ro và đề xuất hành động.
Output: docx-ready markdown, có bảng action plan và appendix nguồn.
[paste nội dung]
```

## Cấu trúc đầu ra

1. Trang bìa ngắn.
2. Executive Summary.
3. Kết luận chính.
4. 3-5 insight/bằng chứng.
5. Rủi ro/vấn đề cần chú ý.
6. Đề xuất hành động.
7. Action plan.
8. Appendix số liệu/nguồn.

## Checklist

- [ ] Kết luận nằm đầu báo cáo.
- [ ] Mỗi insight có evidence.
- [ ] Có owner + deadline cho action.
- [ ] Có nguồn/citation cho số liệu.
- [ ] Không dài quá mức cần thiết.
