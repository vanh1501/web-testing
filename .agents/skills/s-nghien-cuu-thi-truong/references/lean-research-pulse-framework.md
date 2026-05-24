# Lean Research Pulse Framework
> **Phiên bản:** v1.0 | **Áp dụng cho:** Nghiên cứu thị trường — Chiến lược / Giải pháp / Đối thủ
> **Loại:** Operational Framework — Pragmatic Intelligence Cycle

---

## 1. Mục đích & Phạm vi áp dụng

Framework này điều hành quá trình nghiên cứu thị trường theo nguyên tắc **tối thiểu thời gian — tối đa tín hiệu có thể hành động được**. Áp dụng khi:

- Cần ra quyết định trong ≤5 ngày làm việc
- Ngân sách data tối thiểu (không có Nielsen / Euromonitor)
- Mục tiêu đầu ra là **Business Decision** (không phải báo cáo hàn lâm)

**Không dùng** framework này khi: nghiên cứu cần độ chính xác thống kê ≥95% (dùng full survey design) hoặc nghiên cứu pháp lý / regulatory compliance.

---

## 2. Kiến trúc 4 Phase

```
Phase 1: SIGNAL SCAN      (4h)  → Xác định nguồn + trọng số
Phase 2: RAPID SYNTHESIS  (8h)  → Thu thập + filter + nhóm
Phase 3: GAP FILL         (4h)  → Lấp lỗ hổng + triangulate
Phase 4: INSIGHT LOCK     (2h)  → Đúc insight + confidence score
────────────────────────────────
Tổng time-box tối đa: 18h làm việc = ~2.5 ngày
```

---

## 3. Phase 1 — SIGNAL SCAN (Time-box: 4h)

### 3.1 Xác định Research Question duy nhất

Công thức: `[Đối tượng] + [Hành vi/Trạng thái] + [Điều kiện/Bối cảnh]`

Ví dụ tốt: "SME ngành F&B tại TP.HCM đang dùng giải pháp quản lý kho nào và lý do chưa chuyển sang phần mềm chuyên dụng?"
Ví dụ xấu: "Thị trường phần mềm quản lý kho như thế nào?" → Quá rộng, không hành động được.

### 3.2 Phân loại nguồn và gán trọng số

Thực thi bảng sau **ngay khi nhận Research Question**:

| Tier | Loại nguồn | Trọng số tín hiệu (W) | Công cụ thu thập |
|------|-----------|----------------------|-----------------|
| T1 — Primary Direct | Phỏng vấn sâu người dùng cuối / buyer | W = 0.40 | Lịch hẹn 20 phút / form async |
| T2 — Primary Proxy | Review platforms (Google, App Store, Trustpilot, Cốc Cốc) | W = 0.25 | Scrape / đọc thủ công ≥30 reviews |
| T3 — Secondary Reported | Báo cáo ngành, industry blog, press release đối thủ | W = 0.20 | Google Scholar, VietnamBiz, VIRAC |
| T4 — Secondary Derived | LinkedIn, forum, group Facebook, Reddit | W = 0.15 | LinkedIn Sales Navigator / manual |

**Quy tắc bắt buộc:**
- Tổng Σ(W) = 1.00
- Phải có ≥1 nguồn T1 (primary direct). Thiếu T1 → ghi nhận "Low-Confidence Research" trong output.
- T3+T4 không được chiếm >50% tổng evidence.

### 3.3 Signal Register (bảng thu thập)

Tạo bảng với cột: `Signal_ID | Tier | Nguồn | URL/Ref | Tóm tắt nội dung | Tag chủ đề | Trọng số`

Mục tiêu: thu thập **tối thiểu 25 signals**, phân bố theo Tier ≥ [5 T1, 7 T2, 8 T3, 5 T4].

---

## 4. Phase 2 — RAPID SYNTHESIS (Time-box: 8h)

### 4.1 Affinity Grouping — 3 Pass

**Pass 1 — Raw dump (2h):** Đọc toàn bộ 25+ signals. Ghi note ngắn cho mỗi signal. Không phân tích.

**Pass 2 — Tag & nhóm (3h):** Gán mỗi signal vào ≥1 trong 5 bucket sau (MECE):

| Bucket | Định nghĩa | Câu hỏi kiểm tra |
|--------|-----------|-----------------|
| **PAIN** | Vấn đề / nỗi đau hiện tại của đối tượng | "Người dùng đang khó chịu điều gì?" |
| **GAIN** | Kết quả mong muốn / kỳ vọng | "Họ muốn đạt được gì?" |
| **JOB** | Công việc cần hoàn thành | "Họ thuê giải pháp để làm gì?" |
| **BARRIER** | Lý do chưa chuyển đổi / mua | "Điều gì cản trở hành động?" |
| **SIGNAL_WEAK** | Dữ liệu mâu thuẫn, chưa đủ bằng chứng | "Cần kiểm chứng thêm" |

**Pass 3 — Frequency count (3h):**

Tính `Frequency Score (FS)` cho mỗi nhóm:

```
FS(bucket_i) = Σ [W(signal_j) × Mention_weight(signal_j)]
Mention_weight = 1.0 (trực tiếp đề cập) | 0.5 (ngụ ý) | 0.2 (suy luận)
```

Rank top 5 insights theo FS. Đây là **Insight Candidates**.

### 4.2 Contradiction Check

Với mỗi Insight Candidate, thực thi:
1. Tìm ít nhất 1 signal mâu thuẫn với insight đó
2. Nếu có ≥3 signals mâu thuẫn → downgrade insight xuống `SIGNAL_WEAK`
3. Document mâu thuẫn trong section "Contradictions & Caveats" của output

---

## 5. Phase 3 — GAP FILL (Time-box: 4h)

### 5.1 Gap Detection Matrix

Sau Phase 2, điền bảng Gap Detection:

| Câu hỏi nghiên cứu gốc | Đã có evidence? | Tier cao nhất có | Confidence hiện tại | Action |
|------------------------|-----------------|-----------------|--------------------|----|
| [Q1] | Có / Không | T1/T2/T3/T4 | High/Med/Low | Đủ / Cần thêm |

**Ngưỡng hành động:**
- Confidence = High: ≥3 signals từ T1+T2 đồng thuận
- Confidence = Med: ≥2 signals T2+T3 hoặc 1 T1
- Confidence = Low: chỉ T4 hoặc <2 signals

### 5.2 Rapid Gap Fill Protocol

Với mỗi gap "Cần thêm": thực thi đúng 1 trong 3 action sau (không kết hợp):

- **Action A — Quick Interview:** Gửi 3 câu hỏi qua Zalo/email cho ≥2 người T1. Time-box: 2h.
- **Action B — Review Mining:** Đọc thêm 15 reviews trên platform phù hợp. Time-box: 1h.
- **Action C — Accept Low-Confidence:** Ghi nhận gap trong output, không fill — khi gap không critical.

---

## 6. Phase 4 — INSIGHT LOCK (Time-box: 2h)

### 6.1 Insight Statement Formula

Mỗi insight viết theo cấu trúc bắt buộc:

```
"[Đối tượng cụ thể] + [Hành vi/Trạng thái quan sát được] + [lý do suy luận] 
 vì [underlying driver], dẫn đến [hệ quả kinh doanh]."
```

Ví dụ: "Chủ cửa hàng F&B quy mô 1-3 chi nhánh không triển khai phần mềm kho vì chi phí onboarding vượt ROI nhận thức trong ≤6 tháng, dẫn đến churn cao ở giai đoạn trial."

### 6.2 Confidence Score chuẩn hóa

```
Confidence_Score = (FS_normalized × 0.6) + (Source_diversity × 0.4)

Source_diversity = số Tier khác nhau có evidence / 4
FS_normalized = FS(insight) / FS(max_insight)
```

| Score range | Label | Hành động cho người dùng |
|-------------|-------|--------------------------|
| 0.75 – 1.00 | HIGH | Đủ để quyết định chiến lược |
| 0.50 – 0.74 | MED | Cần validate thêm trước khi đầu tư lớn |
| 0.00 – 0.49 | LOW | Chỉ dùng định hướng, không làm căn cứ ngân sách |

### 6.3 Output Lock Checklist

Trước khi xuất báo cáo, kiểm tra bắt buộc:

- [ ] Research Question gốc đã được trả lời trực tiếp?
- [ ] ≥3 insights có Confidence ≥ MED?
- [ ] Tất cả SIGNAL_WEAK đã được document?
- [ ] Contradictions & Caveats có ≥1 mục?
- [ ] Không có insight nào dựa 100% vào T4?

---

## 7. Anti-Patterns — Cấm tuyệt đối

| Anti-pattern | Hệ quả | Cách phòng |
|---|---|---|
| Confirmation bias sourcing — chỉ tìm nguồn ủng hộ giả thuyết sẵn có | Insight sai, ra quyết định sai | Pass 1 cấm đặt giả thuyết trước |
| Report hoarding — thu thập 50+ nguồn không filter | Phân tích tê liệt, vượt time-box | Cứng 25 signals, Gap Fill cho phần còn thiếu |
| Single source dominance — 1 báo cáo T3 chiếm >40% citation | Sai lệch hệ thống | Enforce trọng số Tier |
| Vague insight — "Khách hàng muốn sản phẩm tốt hơn" | Không hành động được | Áp dụng cứng Insight Statement Formula |
