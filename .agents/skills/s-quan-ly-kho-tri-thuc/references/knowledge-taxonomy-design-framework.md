# Knowledge Taxonomy Design Framework
> **Phiên bản:** v1.0 | **Áp dụng cho:** Thiết kế kiến trúc kho tri thức nội bộ — Ontology-first approach
> **Loại:** Architecture Framework — Knowledge Organization & Retrieval Design

---

## 1. Tại sao Ontology-first

Sai lầm phổ biến nhất khi xây kho tri thức: **bắt đầu bằng việc viết nội dung** mà không có kiến trúc phân loại. Kết quả: sau 3 tháng, kho tri thức trở thành "đống file" — không ai tìm được gì.

**Ontology-first** nghĩa là: thiết kế **cây phân loại và quan hệ giữa các khái niệm trước** — sau đó mới viết nội dung vào.

---

## 2. Kiến trúc 4 Layer của Knowledge Taxonomy

```
Layer 1: DOMAIN        → Lĩnh vực kiến thức lớn nhất (VD: "Bán hàng", "Vận hành")
Layer 2: CATEGORY      → Nhóm chủ đề trong Domain (VD: "Quy trình bán hàng", "KPI")
Layer 3: TOPIC         → Chủ đề cụ thể (VD: "Quy trình xử lý leads", "Cách tính ARR")
Layer 4: ARTICLE/NOTE  → Bài viết / note thực tế
```

**Quy tắc layer:**
- Layer 1: Tối đa 8 Domain cho 1 tổ chức (nếu >8 → đang over-categorize)
- Layer 2: Tối đa 6 Category / Domain
- Layer 3: Tối đa 10 Topic / Category
- Layer 4: Không giới hạn, nhưng mỗi Article gắn đúng 1 Topic

---

## 3. Phase 1 — Domain Discovery (2h)

### 3.1 Jobs-to-be-Done Knowledge Audit

Hỏi ≥5 người dùng tiềm năng của kho tri thức: "Lần cuối bạn không biết làm gì và phải hỏi đồng nghiệp / Google là việc gì?"

Thu thập ≥20 câu trả lời. Phân nhóm bằng Affinity Grouping thành các cluster. Mỗi cluster lớn = 1 Domain candidate.

### 3.2 Domain Selection Matrix

Đánh giá mỗi Domain candidate theo 3 tiêu chí:

| Domain candidate | Frequency (lần/tháng người cần) | Business Impact (H/M/L) | Knowledge Gap (H/M/L) | Priority Score |
|-----------------|--------------------------------|------------------------|----------------------|----------------|
| {{DOMAIN_1}} | {{FREQ_1}} | H/M/L | H/M/L | {{SCORE_1}} |

```
Priority_Score = Frequency × 0.4 + Impact_score × 0.35 + Gap_score × 0.25
Impact_score: H=3, M=2, L=1
Gap_score: H=3 (nhiều người không biết), M=2, L=1
```

Chọn **top 5-8 Domain** có Priority_Score cao nhất. Loại Domain có Score thấp — không ưu tiên xây trước.

---

## 4. Phase 2 — Taxonomy Tree Design (4h)

### 4.1 MECE Check cho Taxonomy

Taxonomy đạt chuẩn khi thỏa mãn **2 điều kiện MECE**:

**Mutually Exclusive (không trùng lặp):**
- Test: Lấy 1 article bất kỳ → có thể đặt vào ≥2 Topic khác nhau không?
- Nếu có → 2 Topic đó đang overlap → merge hoặc tách rõ ranh giới

**Collectively Exhaustive (không bỏ sót):**
- Test: Liệt kê top 20 câu hỏi phổ biến nhất → tất cả đều rơi vào đúng 1 Topic?
- Nếu có câu hỏi không thuộc Topic nào → thiếu Topic → thêm vào taxonomy

### 4.2 Taxonomy Validation — 3-Question Test

Với mỗi Category và Topic, trả lời 3 câu hỏi:

1. **Stable?** — Tên Category/Topic có thể dùng trong ≥1 năm mà không lỗi thời?
2. **Actionable?** — Người dùng biết ngay đây chứa gì khi đọc tên?
3. **Findable?** — Khi search từ khóa liên quan, người dùng sẽ nghĩ đến tên này?

Nếu bất kỳ câu nào "Không" → rename hoặc restructure Category/Topic đó.

### 4.3 Naming Convention

**Quy tắc đặt tên bắt buộc:**

| Layer | Quy tắc | Ví dụ tốt | Ví dụ xấu |
|-------|---------|-----------|-----------|
| Domain | Danh từ ngắn, ≤3 từ | "Bán hàng", "Vận hành HR" | "Các vấn đề liên quan đến bán hàng" |
| Category | Danh từ + phạm vi | "Quy trình bán hàng", "Công cụ & Template" | "Thứ linh tinh", "Misc" |
| Topic | Câu hỏi dạng "Cách làm X" hoặc "Khái niệm X" | "Cách xử lý khiếu nại", "Chính sách hoa hồng" | "Khiếu nại", "Hoa hồng" |
| Article | Tiêu đề rõ, có động từ hoặc danh từ cụ thể | "Quy trình xử lý khiếu nại Level 2 — Step-by-step" | "Khiếu nại 2024" |

---

## 5. Phase 3 — Metadata Schema Design

### 5.1 Bắt buộc Metadata cho mọi Article

```yaml
---
id: [UUID hoặc slug duy nhất]
title: [Tiêu đề rõ]
domain: [1 trong 5-8 Domain đã chốt]
category: [1 Category thuộc Domain]
topic: [1 Topic thuộc Category]
type: [SOP | Policy | How-to | Reference | Template | Case Study | FAQ]
owner: [Tên người / team chịu trách nhiệm nội dung]
created_date: [YYYY-MM-DD]
last_updated: [YYYY-MM-DD]
review_due: [YYYY-MM-DD]
status: [Draft | Active | Outdated | Deprecated]
tags: [tối đa 5 từ khóa phụ]
---
```

### 5.2 Article Type Definitions (MECE)

| Type | Định nghĩa | Ví dụ |
|------|-----------|-------|
| **SOP** | Hướng dẫn từng bước thực hiện quy trình cụ thể | "SOP: Onboard nhân viên mới" |
| **Policy** | Quy định / chính sách phải tuân theo | "Chính sách hoàn tiền" |
| **How-to** | Hướng dẫn ngắn cho 1 task cụ thể | "Cách export báo cáo từ HubSpot" |
| **Reference** | Tài liệu tra cứu / bảng biểu / danh sách | "Bảng giá sản phẩm 2025" |
| **Template** | Biểu mẫu / file mẫu có thể dùng ngay | "Template email cold outreach" |
| **Case Study** | Bài học từ tình huống thực tế | "Case study: Xử lý khủng hoảng KH tháng 3" |
| **FAQ** | Câu hỏi thường gặp + trả lời | "FAQ: Chính sách nghỉ phép" |

---

## 6. Phase 4 — Retrieval Architecture

### 6.1 2 Mode tìm kiếm cần thiết kế song song

**Mode 1 — Browse (duyệt theo cây):**
```
Domain → Category → Topic → Article list
```
Dùng khi: người dùng biết mình cần loại thông tin gì nhưng không biết từ khóa chính xác.

**Mode 2 — Search (tìm kiếm từ khóa):**
Yêu cầu:
- Full-text search trên Title + Tags + Content
- Alias mapping: từ đồng nghĩa dẫn đến cùng article (VD: "nghỉ phép" = "leave" = "vacation")

### 6.2 Findability Score

Đánh giá khả năng tìm kiếm của Knowledge Base sau khi build:

```
Test: Lấy 10 câu hỏi thực tế của người dùng
      → Tìm kiếm trong KB
      → Đếm số câu tìm thấy đúng article trong ≤3 click / ≤10 giây

Findability_Score = Tìm thấy / 10 × 100%
Target: ≥80%
```

---

## 7. Phase 5 — Governance Structure

### 7.1 Role phân quyền

| Role | Quyền | Trách nhiệm |
|------|-------|------------|
| **KB Owner** | Full access — create / edit / delete / approve | Duy trì taxonomy, phê duyệt article quan trọng |
| **Domain Expert** | Create + edit trong Domain của mình | Viết và cập nhật nội dung chuyên môn |
| **Contributor** | Create draft (cần approve) | Đóng góp nội dung, không publish trực tiếp |
| **Reader** | Read-only | Tìm kiếm và đọc |

### 7.2 Review Cadence

| Article Type | Review Frequency | Trigger tự động review |
|-------------|-----------------|----------------------|
| Policy / SOP | 6 tháng / lần | Ngày effective + 180 ngày |
| How-to / Reference | 12 tháng / lần | Ngày last_updated + 365 ngày |
| Template | Khi có version mới | Event-based |
| Case Study / FAQ | Không review định kỳ | Khi có phản hồi outdated |

**Tự động trigger:** Khi `review_due` đã qua → gán status = `Outdated` + notify KB Owner.

---

## 8. Anti-Patterns khi thiết kế Taxonomy

| Anti-pattern | Hệ quả | Fix |
|---|---|---|
| Taxonomy theo org chart | Khi restructure tổ chức, KB vỡ | Taxonomy theo JOB (người cần biết để làm gì) |
| Too granular — 20+ Domain | Không ai biết tìm ở đâu | Giới hạn cứng ≤8 Domain |
| Flat structure — chỉ 1 layer | Tìm không ra, scroll mãi | Bắt buộc 4-Layer hierarchy |
| No owner per article | Article outdated không ai hay | Metadata `owner` bắt buộc, notify owner khi review_due |
| Tag abuse — 20 tags/article | Tags vô nghĩa | Hard limit: ≤5 tags/article |
