---
file: .agents/skills/s-chuan-hoa-tai-lieu/references/gamma-to-marp-mapping.md
purpose: Bản hướng dẫn chi tiết quy đổi 12 cấu trúc layout trực quan từ tư duy Gamma sang cú pháp mã lệnh Marp Markdown của MindX.
trigger: Kích hoạt đồng thời khi SKILL.md thực thi Bước 3 và Bước 4.
---

# Từ điển ánh xạ 12 cấu trúc Layout B2B (Gamma to Marp Mapping)

Tài liệu này ép quy tắc biên dịch cấu trúc hiển thị cho AI. Khi phân tích nội dung text thô, AI phải đối chiếu bảng dưới đây để chọn mô hình trực quan tối ưu nhất, không được tự bịa ra cấu trúc layout nằm ngoài danh mục chuẩn của tổ chức.

---

### 1. Slide Bìa Chủ Đề (Cover Layout)

* **Ngữ cảnh sử dụng:** Bắt đầu bài học, mở đầu module lớn.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
# TÊN CHUYÊN ĐỀ ĐÀO TẠO VIẾT HOA
*Subtitle: Giải pháp tối ưu hiệu suất toàn diện cho doanh nghiệp*

<!-- _class: slide-cover -->
<!-- _layout_cue: Gamma - Cover Layout -->
<!-- 
_speaker_notes:
Chào mừng các học viên đến với chuyên đề đào tạo hôm nay.
-->
```

---

### 2. Slide Chuyển Phần / Ngăn Phân Tách (Section Divider Layout)

* **Ngữ cảnh sử dụng:** Kết thúc một chương, chuyển sang một phần lớn tiếp theo của bài giảng để điều hòa nhịp học viên.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# PHẦN 1: THỰC TRẠNG VÀ PHƯƠNG PHÁP LUẬN
*Khoảng nghỉ nhìn nhận trước khi đi vào giải pháp thực chiến*

<!-- _class: slide-divider -->
<!-- _layout_cue: Gamma - Section Divider Layout -->
<!-- 
_speaker_notes:
Chúng ta vừa hoàn thành phần tổng quan. Bây giờ, hãy cùng bước sang Phần 1.
-->
```

---

### 3. Split Layout (Mô hình Chia đôi 50/50 Văn bản & Hình ảnh)

* **Ngữ cảnh sử dụng:** Giải thích một khái niệm mới, một định nghĩa cần hình ảnh thực tế hỗ trợ minh họa ngay lập tức để tăng khả năng hấp thụ thông tin.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# Mô Hình Vận Hành Trợ Lý AI Thế Thế Hệ Mới
*Tư duy cộng tác tối ưu giữa Người và Máy*

![bg right:45% Phác thảo quy trình vận hành 3D](https://images.mindx.edu.vn/assets/ai-bot-3d.png)
- **Cốt lõi xử lý:** AI đóng vai trò xử lý các tác vụ lặp lại khối lượng lớn.
- **Điểm kiểm soát:** Con người nắm giữ quyền xét duyệt và ra quyết định cuối cùng.
- **Luồng dữ liệu:** Di chuyển liên tục, có cơ chế lưu trữ snapshot trạng thái.

<!-- _class: slide-simple -->
<!-- _layout_cue: Gamma - Split Text/Image Layout -->
<!-- 
_speaker_notes:
Như các anh chị có thể thấy trên màn hình, mô hình này chia làm hai phần...
-->
```

---

### 4. 3-Column Cards (Mô hình Ba thẻ Nội dung Đối xứng)

* **Ngữ cảnh sử dụng:** Trình bày 3 khía cạnh song song, 3 giải pháp cùng cấp, hoặc 3 trụ cột chiến lược của một dự án.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# 3 Trụ Cột Chuyển Đổi Số Cho Phòng HR
*Hành trình dịch chuyển năng lực vận hành*

- **Số hóa SOP:** Chuyển đổi toàn bộ quy trình giấy sang checklist tương tác.
- **Đào tạo Agent:** Đóng gói năng lực chuyên gia thành các trợ lý ảo hỗ trợ.
- **Chuẩn hóa QA:** Thiết lập hệ thống kiểm định chất lượng đầu ra tự động.

<!-- _class: slide-simple -->
<!-- _layout_cue: Gamma - 3-Column Cards Layout -->
<!-- 
_speaker_notes:
Chúng ta có 3 trụ cột chính cần lưu ý ở đây...
-->
```

---

### 5. Vertical Timeline (Mô hình Dòng thời gian / Quy trình Tuyến tính)

* **Ngữ cảnh sử dụng:** Mô tả các bước của một quy trình vận hành tiêu chuẩn (SOP), lịch trình triển khai dự án qua các giai đoạn.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# Lộ Trình Triển Khai Không Gian Làm Việc AI
*Dây chuyền 4 bước đưa giải pháp vào thực tế vận hành*

1. **Bước 1 (Tuần 1):** Thu thập toàn bộ tài liệu nguồn (SOP thô, biểu mẫu).
2. **Bước 2 (Tuần 2):** Xây dựng kiến trúc Blueprint và định nghĩa Component.
3. **Bước 3 (Tuần 3):** Chạy thử nghiệm có kiểm soát (Pilot) trên tệp user nhỏ.
4. **Bước 4 (Tuần 4):** Đóng gói Spec Pack và bàn giao toàn diện cho phòng ban.

<!-- _class: slide-simple -->
<!-- _layout_cue: Gamma - Vertical Timeline Layout -->
<!-- 
_speaker_notes:
Lộ trình của chúng ta sẽ kéo dài trong vòng 4 tuần...
-->
```

---

### 6. Ma Trận 2x2 (Strategic Matrix Layout)

* **Ngữ cảnh sử dụng:** Phân loại dữ liệu, mô hình SWOT, ma trận Eisenhower (Quan trọng - Khẩn cấp), phân định các nhóm chiến lược.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# Ma Trận Phân Loại Tác Vụ Đào Tạo B2B
*Chiến lược phân bổ nguồn lực tối ưu*

| | **Tác động Cao (High Impact)** | **Tác động Thấp (Low Impact)** |
|---|---|---|
| **Dễ làm (Easy)** | **Nhóm 1: Thắng nhanh (Quick Wins)**<br>• Báo cáo định kỳ<br>• Soạn thảo slide thô | **Nhóm 2: Tác vụ nền (Fill-ins)**<br>• Định dạng văn bản<br>• Gắn nhãn lưu trữ |
| **Khó làm (Hard)** | **Nhóm 3: Chiến lược (Major Projects)**<br>• Tự động hóa SOP<br>• Xây dựng Core Skill | **Nhóm 4: Điểm nghẽn (Thankless Tasks)**<br>• Sửa code thủ công<br>• Tích hợp API sâu |

<!-- _class: slide-simple -->
<!-- _layout_cue: Gamma - Strategic 2x2 Matrix Layout -->
<!-- 
_speaker_notes:
Nhìn vào ma trận này, chúng ta sẽ tập trung vào nhóm Thắng nhanh trước...
-->
```

---

### 7. Bảng Đối Chiếu / So Sánh (Comparison Matrix Layout)

* **Ngữ cảnh sử dụng:** So sánh ưu - nhược điểm giữa các giải pháp, so sánh năng lực của ta với đối thủ, hoặc so sánh kịch bản trước và sau cải tiến.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# Bảng So Sánh Năng Lực Vận Hành
*Sự dịch chuyển hiệu suất giữa hai phương thức làm việc*

| Tiêu chí phân tích | Cách làm thủ công (AS-IS) | Hệ thống Antigravity (TO-BE) |
|---|---|---|
| **Thời gian xử lý** | Kéo dài từ 2 - 3 ngày làm việc | Tối giản còn 15 - 30 phút |
| **Tỷ lệ sai sót số liệu** | Khoảng 15% do nhập liệu thủ công | Giảm thiểu về mức dưới 1% |
| **Phụ thuộc chuyên gia** | Rất cao (Người giỏi nghỉ là vỡ quy trình) | Thấp (Năng lực đã đóng gói thành Skill) |

<!-- _class: slide-simple -->
<!-- _layout_cue: Gamma - Comparison Table Layout -->
<!-- 
_speaker_notes:
Bảng đối chiếu này cho thấy sự khác biệt rõ rệt...
-->
```

---

### 8. Phễu Chuyển Đổi (Funnel Conversion Layout)

* **Ngữ cảnh sử dụng:** Mô tả hành trình khách hàng B2B, tỷ lệ rơi rụng qua các vòng tuyển dụng nhân sự, hoặc các bước lọc dữ liệu thô.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# Phễu Chuyển Đổi Lead Khách Hàng B2B
*Tối ưu hóa điểm chạm để giảm thiểu tỷ lệ rơi rụng khách hàng*

- **Tầng 1: Tiếp cận (Awareness):** 1,000 Doanh nghiệp nhận diện thương hiệu.
- **Tầng 2: Quan tâm (Interest):** 300 Doanh nghiệp để lại thông tin nhu cầu.
- **Tầng 3: Giải pháp (Proposal):** 50 Doanh nghiệp tham gia nhận demo giải pháp.
- **Tầng 4: Chốt deal (Conversion):** 10 Khách hàng chính thức ký kết hợp đồng.

<!-- _class: slide-simple -->
<!-- _layout_cue: Gamma - Funnel Conversion Layout -->
<!-- 
_speaker_notes:
Hành trình chuyển đổi này gồm 4 tầng...
-->
```

---

### 9. Trích Dẫn Lãnh Đạo (Executive Quote Layout)

* **Ngữ cảnh sử dụng:** Đưa ra thông điệp truyền cảm hứng, trích dẫn câu nói của CEO/Chuyên gia đầu ngành để bảo chứng cho luận điểm bài học.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# Triết Lý Vận Hành Trong Kỷ Nguyên Trí Tuệ Nhân Tạo
*Góc nhìn chiến lược từ Ban Điều Hành*

> "AI không thay thế con người. Nhưng những người biết điều phối AI sẽ thay thế và loại bỏ những người không biết dùng AI."
> 
> **— Ban Giám Đốc Công Nghệ MindX Tech School**

<!-- _class: slide-simple -->
<!-- _layout_cue: Gamma - Executive Quote Layout -->
<!-- 
_speaker_notes:
Thông điệp từ Ban Giám Đốc muốn nhấn mạnh tầm quan trọng của việc làm chủ công cụ mới...
-->
```

---

### 10. Số Liệu Trọng Yếu (Big Stats / Data Callout Layout)

* **Ngữ cảnh sử dụng:** Nhấn mạnh một con số tăng trưởng ấn tượng, kết quả KPI vượt bậc, hoặc một cột mốc tài chính quan trọng.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# Cột Mốc Tối Ưu Hóa Chi Phí Vận Hành Năm 2026
*Kết quả minh chứng cho sức mạnh chuyển đổi số quy trình*

# 45%
### Cắt giảm chi phí nhân sự thô trên toàn hệ thống đào tạo B2B

<!-- _class: slide-simple -->
<!-- _layout_cue: Gamma - Big Stats Layout -->
<!-- 
_speaker_notes:
Con số 45% này chính là kết quả nổi bật nhất của dự án...
-->
```

---

### 11. Câu Hỏi Thường Gặp (FAQ / Accordion Layout)

* **Ngữ cảnh sử dụng:** Giải đáp thắc mắc cuối giờ học, liệt kê các tình huống phản bác của khách hàng (Handling Objections) cho team Sales.
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# Câu Hỏi Thường Gặp Về Quy Trình Bảo Mật Dữ Liệu
*Giải đáp lo ngại phổ biến của các đối tác doanh nghiệp B2B*

- **Q1: Dữ liệu của doanh nghiệp có bị leak ra ngoài không?**
  *Trả lời:* Tuyệt đối không. Hệ thống kích hoạt Rule ẩn danh PII cứng ở tầng lõi.
- **Q2: Giảng viên không thạo công nghệ có sử dụng được Marp không?**
  *Trả lời:* Khâu sinh mã đã có AI lo. Giảng viên chỉ cần đọc bản preview trực quan.

<!-- _class: slide-simple -->
<!-- _layout_cue: Gamma - FAQ Layout -->
<!-- 
_speaker_notes:
Dưới đây là một số câu hỏi phổ biến mà chúng tôi nhận được...
-->
```

---

### 12. Quy Trình Vòng Lặp (Flywheel / Cycle Process Layout)

* **Ngữ cảnh sử dụng:** Mô tả quy trình cải tiến liên tục (PDCA), vòng đời phát triển sản phẩm, hoặc chiến lược giữ chân khách hàng (Retention Wheel).
* **Cấu trúc mã Marp Ép buộc:**

```markdown
---
# Vòng Lặp Cải Tiến Chất Lượng Nội Dung Đào Tạo
*Cơ chế tự tiến hóa dựa trên phản hồi thực tế*

- **Trạm 1 - Thu thập (Collect):** Ghi nhận feedback của học viên cuối mỗi phiên.
- **Trạm 2 - Phân tích (Analyze):** AI rà soát lỗ hổng kiến thức và lỗi layout slide.
- **Trạm 3 - Tinh chỉnh (Refine):** Cập nhật lại kho tài liệu tham chiếu (References).
- **Trạm 4 - Tái triển khai (Deploy):** Xuất bản phiên bản slide đào tạo mới V2.

<!-- _class: slide-simple -->
<!-- _layout_cue: Gamma - Flywheel Layout -->
<!-- 
_speaker_notes:
Quy trình cải tiến này vận hành theo một vòng lặp khép kín...
-->
```
