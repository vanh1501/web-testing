# Competitive Intelligence Triangulation Framework
> **Phiên bản:** v1.0 | **Áp dụng cho:** Nghiên cứu đối thủ — Positioning / Pricing / Product Gap / Channel
> **Loại:** Intelligence Framework — Structured Competitive Audit

---

## 1. Mục đích & Khi nào dùng

Framework này chuẩn hóa quy trình thu thập và phân tích thông tin cạnh tranh theo nguyên tắc **Triangulation** — mỗi kết luận phải được xác nhận từ ≥3 nguồn độc lập theo ≥2 góc nhìn khác nhau. 

**Dùng khi:**
- Cần ra quyết định pricing, positioning hoặc product roadmap dựa trên bức tranh cạnh tranh
- Chuẩn bị pitch đầu tư / mở rộng thị trường
- Phát hiện competitive gap để tấn công hoặc phòng thủ

**Không dùng khi:** nghiên cứu nhu cầu người dùng (dùng Lean Research Pulse Framework).

---

## 2. Kiến trúc 5 Lens

Mọi đối thủ phải được phân tích qua đúng 5 Lens sau. Thiếu bất kỳ Lens nào → output bị đánh dấu `INCOMPLETE_AUDIT`.

```
Lens 1: MARKET POSITION     → Họ đang ở đâu trên bản đồ cạnh tranh?
Lens 2: PRODUCT REALITY     → Họ thực sự deliver được gì?
Lens 3: COMMERCIAL ENGINE   → Họ kiếm tiền bằng cách nào?
Lens 4: CUSTOMER SENTIMENT  → Người dùng thực sự nghĩ gì?
Lens 5: STRATEGIC SIGNAL    → Họ sẽ đi đâu tiếp theo?
```

---

## 3. Lens 1 — MARKET POSITION

### 3.1 Competitor Identification Protocol

Bước 1: Liệt kê tất cả tên đối thủ từ 3 nguồn:
- Khách hàng kể tên khi được hỏi "bạn đang dùng gì thay thế?"
- Search query `[job-to-be-done] + [địa lý]` trên Google, TikTok, YouTube
- G2 / Capterra / Product Hunt (với B2B SaaS)

Bước 2: Phân loại theo Competitor Type:

| Type | Định nghĩa | Ví dụ |
|------|-----------|-------|
| **Direct** | Cùng JOB, cùng segment, cùng pricing tier | Đối thủ cùng phân khúc |
| **Indirect** | Cùng JOB, khác format giải pháp | Excel thay phần mềm |
| **Substitute** | Khác JOB nhưng chiếm ngân sách thay thế | Thuê outsource thay mua tool |
| **Potential** | Chưa cạnh tranh trực tiếp nhưng có năng lực | Big Tech mở rộng ngành |

Bước 3: Chọn **tối đa 5 đối thủ Direct** để audit sâu. Ghi nhận Indirect và Substitute nhưng không audit đầy đủ.

### 3.2 Positioning Matrix

Xây dựng 2×2 matrix với 2 trục phù hợp nhất với JOB. Ví dụ phổ biến:
- Trục X: Giá (thấp → cao) | Trục Y: Tính năng (basic → enterprise)
- Trục X: Tốc độ onboarding | Trục Y: Độ sâu tích hợp

Plot tất cả 5 đối thủ Direct lên matrix. **Xác định white space** — vùng không có đối thủ = cơ hội hoặc khoảng trắng bị bỏ sót (cần kiểm tra lý do).

---

## 4. Lens 2 — PRODUCT REALITY

### 4.1 Feature Audit Matrix

Tạo bảng với hàng = tính năng cốt lõi (liệt kê từ JOB mapping), cột = từng đối thủ Direct.

Scoring tính năng:
```
✅ = Có, hoạt động tốt (có evidence từ T1/T2)
⚡ = Có nhưng partial / beta / buggy
❌ = Không có
? = Chưa xác nhận (cần Gap Fill)
```

**Quy tắc:** Không điền `✅` nếu chỉ dựa vào marketing page của đối thủ. Phải có T1 (review người dùng) hoặc demo trực tiếp.

### 4.2 Product Strength/Weakness Score

Với mỗi đối thủ, tính:

```
Product_Score = (Count_✅ × 1.0 + Count_⚡ × 0.5) / Total_features × 100
```

**Cờ đỏ:** Nếu đối thủ có Product_Score ≥80% → Phân tích defensive moat: họ dựa vào tính năng hay network effect hay switching cost?

---

## 5. Lens 3 — COMMERCIAL ENGINE

### 5.1 Pricing Reconstruction

Thực thi theo thứ tự:
1. Truy cập pricing page chính thức → ghi nhận mọi tier và giá niêm yết
2. Tìm kiếm trên Reddit/forum: "[tên đối thủ] pricing discount" / "negotiate price"
3. Hỏi 1 người dùng thực tế (T1): "Bạn trả bao nhiêu/tháng thực tế?"
4. Tính **Effective Price** (giá thực tế) vs **List Price** (giá niêm yết)
5. Nếu Effective < List × 0.8 → ghi nhận "heavy discounting behavior" → tín hiệu về sức khỏe kinh doanh

### 5.2 Revenue Model Classification

Phân loại mô hình doanh thu theo bảng:

| Mô hình | Indicator | Hệ quả cạnh tranh |
|---------|-----------|------------------|
| Seat-based SaaS | Giá per user | Churn khi team thu nhỏ |
| Usage-based | Giá per transaction/API call | CAC thấp nhưng predictability thấp |
| Freemium | Free tier + paid upgrade | Viral acquisition, margin thấp |
| One-time license | Không subscription | Low LTV, churn = product death |
| Hybrid | Combo các mô hình trên | Phức tạp pricing war |

---

## 6. Lens 4 — CUSTOMER SENTIMENT

### 6.1 Sentiment Mining Protocol

Nguồn bắt buộc (thu thập ≥10 reviews/đối thủ):
- **B2C:** Google Maps / App Store / Shopee reviews
- **B2B:** G2.com / Capterra / GetApp
- **SME Vietnam:** Hội nhóm Facebook ngành + Zalo community

### 6.2 NPS Proxy Score

Phân loại mỗi review:

```
Promoter (P):  Review ≥4★ + đề xuất cho người khác + không mention complaint
Passive (N):   Review 3-4★ hoặc mention 1 complaint nhỏ
Detractor (D): Review ≤3★ hoặc complaint nghiêm trọng về tính năng/support
```

```
NPS_Proxy = (Count_P - Count_D) / Total_reviews × 100
Range: -100 đến +100
```

Benchmark:
- NPS_Proxy ≥ +30: Đối thủ mạnh về retention
- NPS_Proxy -10 đến +30: Trung bình
- NPS_Proxy < -10: Cơ hội tấn công — người dùng sẵn sàng chuyển

### 6.3 Top Complaint Extraction

Sau khi đọc reviews, liệt kê top 3 complaint thường xuyên nhất theo frequency count. Đây là **Attack Vectors** — điểm có thể khai thác trong positioning.

---

## 7. Lens 5 — STRATEGIC SIGNAL

### 7.1 Signal Detection Checklist

Thực thi **trong vòng 30 phút/đối thủ**:

- [ ] LinkedIn: Họ đang tuyển dụng vị trí gì? → Infer chiến lược mở rộng
- [ ] Press release / blog 6 tháng gần nhất: Có sản phẩm mới / partnership / funding không?
- [ ] Job description: Có nhắc technology stack mới không? (VD: tuyển "AI Engineer" → đang xây AI feature)
- [ ] Pricing page change log (nếu Wayback Machine có archive)
- [ ] G2 / Capterra: Review gần đây (3 tháng) có pattern khác review cũ không?

### 7.2 Strategic Intent Classification

Sau khi thu thập signals, phân loại đối thủ:

| Strategic Mode | Indicators | Hành động phản ứng |
|---|---|---|
| **Land & Expand** | Hạ giá entry, freemium push, viral loop | Defend mid-market bằng switching cost |
| **Enterprise Push** | Tuyển Sales Engineer, SOC2 cert, enterprise case study | Tăng tốc SME penetration trước khi họ quay lại |
| **Consolidation** | M&A activity, feature bloat, partnership với platform lớn | Tìm niche gap mà consolidator bỏ qua |
| **Defensio** | Giảm R&D, tập trung retain, không có sản phẩm mới | Tấn công bằng innovation |

---

## 8. Triangulation Rule — Quy tắc xác nhận kết luận

**Mọi kết luận competitive** phải tuân quy tắc sau:

```
Kết luận X được chấp nhận NẾU:
  - Có evidence từ ≥3 signals độc lập (không cùng nguồn gốc)
  VÀ
  - Signals đến từ ≥2 Lens khác nhau
  VÀ
  - Không có signal phản bác với trọng số > tổng trọng số ủng hộ
```

Nếu không đủ triangulation → ghi nhận kết luận là `HYPOTHESIS` (chưa phải `FINDING`).

---

## 9. Competitive Intelligence Output Structure

Kết quả phân tích phải trả lời 4 câu hỏi:
1. **Where to attack?** — Attack Vectors từ Lens 4 (top complaints của đối thủ)
2. **Where to defend?** — Moat analysis từ Lens 2 (nơi đối thủ mạnh nhất)
3. **What to avoid?** — Overlapping positioning (white space vs crowded space từ Lens 1)
4. **What to watch?** — Strategic Signals từ Lens 5 cần theo dõi tiếp

---

## 10. Anti-Patterns

| Anti-pattern | Hệ quả | Fix |
|---|---|---|
| Marketing page as evidence | Phân tích dựa vào promise, không phải reality | Enforce T1/T2 requirement cho Lens 2 |
| Chỉ audit đối thủ Direct | Bỏ sót Substitute competitor đang chiếm ngân sách | Bắt buộc list Indirect + Substitute dù không audit sâu |
| Static snapshot | Bức tranh cạnh tranh lỗi thời trong 6 tháng | Lens 5 bắt buộc, set reminder re-audit hàng quý |
| NPS Proxy từ <5 reviews | Kết quả không đại diện | Minimum 10 reviews/đối thủ |
