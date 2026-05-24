# Mẫu: Báo cáo Pyramid

## 1. Mục đích
Mẫu này dùng để viết báo cáo ngắn gọn cho BOM hoặc quản lý cấp cao, bắt đầu bằng kết luận chính rồi mới trình bày bằng chứng. Đây là cách tránh biến báo cáo thành bãi đỗ xe của số liệu.

## 2. Khi nào dùng
- Khi cần báo cáo tuần/tháng/quý.
- Khi cần trình bày performance vs target.
- Khi cần đưa ra quyết định dựa trên KPI.

## 3. Thông tin cần điền
| Trường | Mô tả | Ví dụ |
|---|---|---|
| Kỳ báo cáo | Tuần/tháng/quý cần phân tích | Tháng 4/2026 |
| Người đọc | Ai sẽ duyệt hoặc ra quyết định | CEO, BOM Marketing |
| Kết luận chính | Một câu trả lời câu hỏi “so what?” | ROAS miss target do Facebook Ads và Influencer kéo tụt |
| 3 phát hiện chính | 3 luận điểm nâng đỡ kết luận | ROAS, channel, brand line |
| Bằng chứng | Số liệu cụ thể cho từng phát hiện | ROAS 3.45x vs target 4.0x |
| Quyết định cần có | Việc cần người quản lý chốt | Reallocate budget |

## 4. Nội dung mẫu
```markdown
# Báo cáo [Tên/Kỳ]

## 1. Kết Luận Điểm
> [!IMPORTANT]
> **[1 câu kết luận chính, có số liệu hoặc nguyên nhân chính]**

## 2. Bức Tranh Tổng Quan (Descriptive Statistics)
> **Mục tiêu:** Trình bày "What happened?" (cái gì đang diễn ra) để người đọc nắm được baseline trước khi đi sâu. BẮT BUỘC dùng biểu đồ Unicode thanh ngang (Progress Bar) cho tỷ trọng.

| Chỉ số / Phân bổ | Biểu đồ (Unicode) | Tỷ trọng |
|---|---|---|
| **[Nhóm 1]** | `████████░░` | [XX]% |
| **[Nhóm 2]** | `████░░░░░░` | [YY]% |

## 3. Phân Tích Chẩn Đoán (Diagnostic Findings)
> **Mục tiêu:** Trả lời "Why did it happen?" (tại sao lại như vậy). Rút ra các kết luận sâu dựa trên tương quan.

### 3.1. [Emoji 🟢/🟡/🔴] Phát hiện 1 — [Tên phát hiện/Nguyên nhân]
- **Số liệu chứng minh:** [Trích xuất từ Bức tranh tổng quan]
- **Phân tích tương quan:** [Tại sao lại có con số này?]

### 3.2. [Emoji 🟢/🟡/🔴] Phát hiện 2 — [Tên phát hiện/Nguyên nhân]
- ...

## 4. Gợi Ý Hướng Đào Sâu (Deep-Dive Areas)
> [!WARNING]
> **Mục tiêu:** Gợi mở các hướng phân tích tiếp theo từ Vĩ mô đến Vi mô. Sử dụng ngôn ngữ tư vấn (Consultative), khơi gợi sự tò mò (Be Curious), KHÔNG dùng câu hỏi chất vấn.
> 1. **[Vĩ mô / Chiến lược]:** [Gợi ý phân tích...]
> 2. **[Trung mô / Quy trình]:** [Gợi ý phân tích...]
> 3. **[Vi mô / Thực thi]:** [Gợi ý phân tích...]

## 5. Hành Động Đề Xuất
| Hành động | Người phụ trách | Hạn hoàn thành | Kết quả đo được |
|---|---|---|---|
| ... | ... | ... | ... |
```

## 5. Checklist kiểm tra
- [ ] Kết luận nằm ở đầu báo cáo.
- [ ] Có phần Bức tranh tổng quan (Descriptive) thiết lập baseline trước khi Phân tích chẩn đoán (Diagnostic).
- [ ] Có 3-5 phát hiện chính, không spam 20 chỉ số.
- [ ] Có mục Gợi Ý Hướng Đào Sâu sử dụng văn phong tư vấn, đi từ Vĩ mô đến Vi mô.
- [ ] Mỗi phát hiện có số liệu cụ thể làm bằng chứng.
- [ ] Có hành động đề xuất với người phụ trách và deadline.
- [ ] Sử dụng Emoji (🟢🟡🔴) chỉ báo trạng thái cho các Phát hiện chính.
- [ ] Sử dụng khối `> [!IMPORTANT]` và `> [!WARNING]` cho Kết luận và Câu hỏi.
- [ ] Sử dụng Bảng (Table) và biểu đồ thanh ngang Unicode `████░░` cho Bức tranh tổng quan.
