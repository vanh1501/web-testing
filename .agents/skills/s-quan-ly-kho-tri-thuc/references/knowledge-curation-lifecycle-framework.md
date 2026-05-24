# Knowledge Curation Lifecycle Framework
> **Phiên bản:** v1.0 | **Áp dụng cho:** Vận hành & duy trì kho tri thức nội bộ liên tục
> **Loại:** Operational Framework — Content Lifecycle Management

---

## 1. Vấn đề cốt lõi: Knowledge Decay

Knowledge Base không phải "build một lần rồi xong" — nó **decay theo thời gian** nếu không có lifecycle management. Triệu chứng:

- Người dùng không tin KB → tự hỏi đồng nghiệp thay vì tra KB
- Article outdated nhưng không có ai cập nhật
- Nội dung duplicate — cùng thông tin ở 3 nơi khác nhau
- "Tôi thêm bài vào rồi mà không ai đọc"

Framework này giải quyết **toàn bộ vòng đời** của 1 knowledge article — từ khi ý tưởng xuất hiện đến khi deprecate.

---

## 2. Knowledge Article Lifecycle — 6 Stage

```
Stage 1: CAPTURE     → Ghi nhận knowledge cần được document
Stage 2: DRAFT       → Viết nội dung
Stage 3: REVIEW      → Kiểm tra chất lượng trước publish
Stage 4: PUBLISH     → Đưa vào KB chính thức
Stage 5: MAINTAIN    → Cập nhật theo chu kỳ + event trigger
Stage 6: RETIRE      → Archive hoặc delete khi không còn cần
```

**Trạng thái hợp lệ cho metadata `status`:**
```
Draft → Review → Active → Outdated → Deprecated
                    ↑          |
                    └──────────┘ (update xong → Active lại)
```

---

## 3. Stage 1 — CAPTURE

### 3.1 Nguồn capture knowledge

Không phải chỉ chủ động viết — phần lớn knowledge nằm ở:

| Nguồn | Cách khai thác | Tần suất |
|-------|---------------|----------|
| **Câu hỏi lặp lại** | Khi ai đó hỏi câu đã trả lời ≥2 lần → document ngay | Liên tục |
| **Onboarding confusion** | Ghi lại điều nhân viên mới hay bị nhầm | Mỗi lần onboard |
| **Post-mortem / Lessons learned** | Trích knowledge từ báo cáo sau sự cố | Mỗi sự cố/dự án |
| **Chuyên gia rời tổ chức** | Exit interview có focus vào knowledge transfer | Mỗi lần offboard |
| **Quy trình vừa chuẩn hóa** | Mỗi quy trình ESOAR hoàn thành → viết SOP vào KB | Sau mỗi cải tiến |

### 3.2 Capture Trigger Protocol

Áp dụng **"3-Strike Rule":**
```
Lần 1 ai đó hỏi câu X → Trả lời bình thường
Lần 2 ai đó hỏi câu X → Trả lời + ghi chú "cần document"
Lần 3 ai đó hỏi câu X → Document trước khi trả lời
```

**Capture format tối thiểu** (ghi vào backlog, không cần perfect):
```markdown
## Knowledge Capture Note
- Câu hỏi / vấn đề: [Mô tả ngắn]
- Người có knowledge: [Tên]
- Deadline document: [Ngày]
- Article Type đề xuất: SOP / How-to / Policy / FAQ / ...
- Domain/Category đề xuất: [Từ taxonomy]
```

---

## 4. Stage 2 — DRAFT

### 4.1 Writing Principle — Pyramid First

Mọi article viết theo nguyên tắc **Pyramid (đảo ngược)**:

```
Câu 1-2: Kết luận / Câu trả lời trực tiếp
↓
Phần giữa: Bước thực hiện / Logic chi tiết
↓
Cuối: Background / Context / Lý do tại sao
```

**Lý do:** Người đọc KB cần trả lời nhanh — không đọc từ đầu đến cuối như sách.

### 4.2 Writing Quality Criteria (6 tiêu chí)

| # | Tiêu chí | Test | Pass / Fail |
|---|---------|------|-------------|
| 1 | **Actionable** | Người đọc biết làm gì ngay sau khi đọc? | Mỗi bước có động từ hành động cụ thể |
| 2 | **Specific** | Không có từ mơ hồ? | Không có "thường", "đôi khi", "có thể" không có context |
| 3 | **Complete** | Đã có exception handling? | Có ≥1 trường hợp đặc biệt được xử lý |
| 4 | **Findable** | Tiêu đề + tags đủ để search ra? | Test search với 3 từ khóa khác nhau |
| 5 | **Maintainable** | Ai cần update khi nào? | Metadata `owner` + `review_due` đã điền |
| 6 | **Linked** | Có link đến article liên quan? | ≥1 "Xem thêm" link (nếu có article liên quan) |

### 4.3 Article Length Budget

| Type | Length Target | Ghi chú |
|------|--------------|---------|
| SOP | 400-800 từ | Không kể header/metadata |
| How-to | 150-400 từ | Ngắn và scannable |
| Policy | 200-500 từ | Focus on quan-ly-quy-tac, không giải thích nhiều |
| FAQ | 50-150 từ/câu hỏi | Mỗi Q&A độc lập, không cần đọc theo thứ tự |
| Reference | Không giới hạn | Bảng biểu, danh sách — không cần readable flow |
| Case Study | 500-1.000 từ | Narrative + Lesson learned bắt buộc |

---

## 5. Stage 3 — REVIEW

### 5.1 Review Protocol 2-Pass

**Pass 1 — Subject Matter Expert Review:**
- Người review: Domain Expert (không phải người viết)
- Checklist:
  - [ ] Nội dung chính xác về mặt kỹ thuật / nghiệp vụ?
  - [ ] Không có thông tin lỗi thời?
  - [ ] Exception handling có đủ không?

**Pass 2 — Usability Review:**
- Người review: 1 người không quen với chủ đề (simulates new user)
- Test: Họ có thể làm theo hướng dẫn mà không cần hỏi thêm không?
- Nếu có ≥2 điểm cần clarify → Draft chưa đủ rõ

### 5.2 Review SLA

| Article Type | SLA Review | Escalate khi quá SLA |
|-------------|-----------|---------------------|
| SOP / Policy quan trọng | 3 ngày làm việc | Notify KB Owner |
| How-to / FAQ | 1 ngày làm việc | Auto-publish nếu không có feedback trong 1 ngày |
| Template | 2 ngày làm việc | Notify Domain Expert |

---

## 6. Stage 4 — PUBLISH

### 6.1 Publish Checklist bắt buộc

- [ ] Metadata đầy đủ (id, title, domain, category, topic, type, owner, dates, status)?
- [ ] Pass cả 2 Review?
- [ ] Taxonomy placement đúng (không đặt sai layer)?
- [ ] Tags ≤5, không trùng với Topic name (tags bổ sung, không duplicate)?
- [ ] Internal links đến articles liên quan (nếu có)?
- [ ] Đã thông báo đến team liên quan?

### 6.2 Launch Communication Template

```
[New KB Article] {{TIEU_DE_ARTICLE}} — {{DOMAIN}} / {{CATEGORY}}

📝 Nội dung: [1-2 câu mô tả article giải quyết vấn đề gì]
🔗 Link: {{LINK}}
👤 Owner: {{OWNER}}
📅 Review tiếp: {{REVIEW_DATE}}

Phản hồi / góp ý → tag @{{OWNER}}
```

---

## 7. Stage 5 — MAINTAIN

### 7.1 Trigger-based Update (ưu tiên hơn schedule)

Cập nhật **ngay lập tức** khi có 1 trong các trigger:

| Trigger | Action | SLA |
|---------|--------|-----|
| Quy trình liên quan thay đổi | Update SOP | Trong ngày |
| Tool / System thay đổi | Update How-to | Trong 2 ngày |
| Policy thay đổi | Update Policy + notify tất cả readers | Trong ngày |
| Nhận ≥2 phản hồi "sai rồi" | Review ngay | Trong ngày |
| Nhận ≥3 phản hồi "không rõ" | Rewrite section bị phàn nàn | Trong 3 ngày |

### 7.2 Scheduled Review — Decay Matrix

```
Decay_Rate mỗi loại article (% outdated per year):
- Policy:    30-50% (thay đổi theo quy định, pháp luật)
- SOP:       20-35% (thay đổi theo process improvement)
- How-to:    15-25% (thay đổi theo tool update)
- Reference: 40-60% (pricing, danh sách thay đổi liên tục)
- FAQ:       10-15% (ổn định nếu taxonomy đúng)
- Case Study: <5% (historical record)
```

Review cycle **phải** ngắn hơn Decay_Rate threshold:
- Policy, Reference → 6 tháng/lần
- SOP, How-to → 12 tháng/lần
- FAQ → 18 tháng/lần

### 7.3 KB Health Dashboard — 5 Metrics

Đo hàng tháng:

```
1. Freshness_Rate = Count(Active) / Count(Active + Outdated) × 100%
   Target: ≥85%

2. Coverage_Rate = Count(documented JTBDs) / Count(all identified JTBDs) × 100%
   Target: ≥70% (không cần 100% — ưu tiên high-impact trước)

3. Findability_Score = % câu hỏi test tìm được đúng article ≤3 click
   Target: ≥80%

4. Usage_Rate = Unique articles viewed / Total articles × 100% (monthly)
   Target: ≥50% (nếu <50% → đang xây content không ai cần)

5. Orphan_Rate = Count(articles không được link đến bởi article nào) / Total
   Target: <20% (orphan quá nhiều = taxonomy không kết nối)
```

---

## 8. Stage 6 — RETIRE

### 8.1 Retire Criteria

Article được Retire khi ≥1 trong các điều kiện:

- **Outdated không thể update:** Quy trình / tool không còn dùng và không có replacement
- **Merged:** Nội dung đã được merge vào article khác đầy đủ hơn
- **Superseded:** Có article mới chính xác hơn thay thế hoàn toàn

### 8.2 Retire Protocol

```
Bước 1: Đổi status → Deprecated
Bước 2: Thêm banner đầu article: "⚠️ Article này đã Deprecated. 
         Xem thay thế tại: [Link article mới]"
Bước 3: Giữ nguyên 90 ngày (không delete) để redirects không vỡ
Bước 4: Sau 90 ngày → Archive (không delete hẳn — giá trị historical)
```

**Cấm hard delete** article đã có ≥10 unique views — có thể đang được link ở nơi khác.

---

## 9. Anti-Patterns trong Knowledge Curation

| Anti-pattern | Hệ quả | Fix |
|---|---|---|
| "Publish và quên" | KB decay nhanh, mất trust | Stage 5 bắt buộc với SLA rõ |
| Viết cho author, không cho reader | Chỉ người viết hiểu | Pass 2 (Usability Review) bắt buộc |
| Duplicate articles vô tình | Người dùng không biết dùng cái nào | Search trước khi create — duplicate = merge cũ |
| Over-document | 500 articles nhưng chỉ 50 có giá trị | Coverage_Rate threshold + prune khi Usage_Rate thấp |
| Knowledge hoarding | "Tôi giữ knowledge trong email" | 3-Strike Rule tự động push capture |
