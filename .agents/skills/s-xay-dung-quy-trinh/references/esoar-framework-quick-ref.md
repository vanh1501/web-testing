# Giải thích nhanh ESOAR cho Process Builder

ESOAR là khung giúp đánh giá từng bước trong một quy trình. Mục tiêu là tránh kiểu “cứ thấy rối là tự động hóa”, một thói quen nghe hiện đại nhưng thường chỉ giúp lỗi chạy nhanh hơn.

## 1. ESOAR gồm 5 hướng xử lý

| Ký hiệu | Tên tiếng Anh | Cách hiểu tiếng Việt | Dùng khi nào? |
|---|---|---|---|
| E | Eliminate | Bỏ bớt | Bước không tạo giá trị, bị lặp, không ai dùng đầu ra |
| S | Standardize | Chuẩn hóa | Nhiều người làm mỗi người một kiểu, đầu ra không đồng đều |
| O | Optimize | Tối ưu | Bước vẫn cần giữ nhưng có thể làm nhanh hơn, ít lỗi hơn |
| A | Automate | Tự động hóa | Bước có luật rõ, đầu vào/đầu ra rõ, đã được chuẩn hóa trước |
| R | Re-engineer | Thiết kế lại | Quy trình sai từ gốc, vá từng bước không còn hiệu quả |

## 2. Ba nguyên tắc bắt buộc

1. **Không đổi nghĩa ESOAR.**  
   5 nhóm trên phải giữ nguyên để mọi phòng ban dùng cùng một cách hiểu.

2. **Quy tắc 60/40.**  
   Nên có ít nhất 60% số bước thuộc nhóm Bỏ bớt + Chuẩn hóa + Tối ưu. Nếu quá nhiều bước nhảy thẳng sang Tự động hóa hoặc Thiết kế lại, cần giải thích lý do.

3. **Chuẩn hóa trước khi tự động hóa.**  
   Không tự động hóa bước chưa rõ đầu vào, đầu ra, người phụ trách, tiêu chí đạt. Nếu không, Agent chỉ giúp phòng ban tạo lỗi nhanh hơn, rất văn minh và cũng rất tai hại.

## 3. Khi nào được ngoại lệ?

Có thể xin ngoại lệ nếu quy trình thuộc nhóm:

- Pháp chế/tuân thủ.
- Bảo mật hoặc kiến trúc kỹ thuật nhạy cảm.
- Tổng hợp dữ liệu nội bộ có luật xử lý rất rõ.
- Quy trình cần nhiều đánh giá chuyên môn của con người.

Mỗi ngoại lệ cần ghi rõ:

```yaml
meta.exception:
  rule: "60/40"
  original_ratio: "Tỷ lệ ban đầu"
  proposed_ratio: "Tỷ lệ đề xuất"
  rationale: "Lý do ngoại lệ"
  signoff_required: true
  signoff_owner: "Người cần phê duyệt"
```

## 4. Dấu hiệu đạt/chưa đạt

| Mức | Dấu hiệu |
|---|---|
| ĐẠT | E+S+O đạt ít nhất 60%, mọi bước tự động hóa đều đã được chuẩn hóa trước |
| CẢNH BÁO | E+S+O dưới 60% nhưng có lý do ngoại lệ rõ |
| TẠM DỪNG | Muốn tự động hóa bước chưa có đầu vào/đầu ra rõ, thiếu người phụ trách hoặc SOP không có checklist |
