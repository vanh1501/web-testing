# Mẫu yêu cầu tùy chỉnh Process Builder cho từng phòng ban

Tài liệu này giúp quản lý phòng ban cung cấp thông tin đủ rõ để Agent tùy chỉnh skill `process-builder` theo quy trình thực tế.

## 1. Mẫu prompt dùng ngay

```text
@process-builder
Tôi là quản lý phòng ban [TÊN PHÒNG BAN].
Tôi muốn chuẩn hóa quy trình [TÊN QUY TRÌNH].

1. Loại quy trình:
- A. Quy trình tiếp xúc khách hàng
- B. Quy trình nội bộ liên phòng ban
- C. Quy trình kiểm soát chất lượng
- D. Quy trình cá nhân/nhóm nhỏ
- E. Khác: [...]

2. Các giai đoạn chính hiện tại:
[Liệt kê 4-6 giai đoạn chính, ví dụ: nhận yêu cầu → xử lý → kiểm tra → gửi kết quả → theo dõi]

3. Quy trình này nên chạy thử trong bao lâu?
- A. 1 tuần, nếu quy trình đơn giản
- B. 2 tuần, mặc định
- C. 4 tuần, nếu nhiều bước hoặc nhiều người tham gia
- D. 1 quý, nếu quy trình theo chu kỳ quý

4. SOP cần thêm phần đặc thù nào?
- A. Kịch bản/tone trao đổi với khách hàng
- B. Kiểm tra tuân thủ/dữ liệu nhạy cảm
- C. Tiêu chuẩn chất lượng/rubric
- D. Khác: [...]
```

## 2. Những phần được phép tùy chỉnh

- Tên phòng ban và tên quy trình.
- Các giai đoạn của quy trình.
- Thời gian chạy thử.
- Phần bổ sung trong SOP, ví dụ: kịch bản khách hàng, kiểm tra tuân thủ, tiêu chuẩn chất lượng.
- Tiêu chí đo thành công trong giai đoạn chạy thử.

## 3. Những phần không được tùy chỉnh tùy tiện

3 nguyên tắc dưới đây là bắt buộc để giữ chất lượng phương pháp:

1. **Giữ nguyên ESOAR**: mỗi bước quy trình chỉ nên được xử lý theo 1 trong 5 hướng: bỏ, chuẩn hóa, tối ưu, tự động hóa hoặc thiết kế lại.
2. **Ưu tiên bỏ - chuẩn hóa - tối ưu trước**: tổng số bước thuộc 3 nhóm này nên đạt ít nhất 60%.
3. **Chuẩn hóa trước khi tự động hóa**: không tự động hóa bước chưa rõ đầu vào, đầu ra, người phụ trách và tiêu chí đạt.

## 4. Kiểm tra sau khi tùy chỉnh

Sau khi Agent tạo bộ quy trình, kiểm tra nhanh 5 điểm:

- [ ] Có đủ 5 tài liệu đầu ra.
- [ ] Quy trình hiện tại được mô tả rõ trước khi đề xuất quy trình mới.
- [ ] Mỗi bước có một người phụ trách chính.
- [ ] SOP có checklist rõ cho từng bước.
- [ ] Kế hoạch chạy thử có 3-5 tiêu chí đo được.
