# SOP Template Enterprise-Grade — 19 Sections

Reference file cho CREATE mode khi target audience L3+ / Enterprise client.
Bar reference: KD-11 Elmich SOP (multi-warehouse, multi-channel, 11 roles).

## When to Load This File

Load khi:
- CREATE mode + maturity = L3+
- User explicit request: "tôi cần SOP enterprise grade", "đầy đủ chuẩn"
- Client là enterprise (>200 nhân viên, multi-department, formal governance)

KHÔNG load cho L0-L1 (over-engineering). KHÔNG load cho L2 (use 12-section template).

---

## 19-Section Structure (theo thứ tự bắt buộc)

```
I. Thông tin chung
II. Căn cứ ban hành / Văn bản liên quan
III. Mục đích
IV. Phạm vi và đối tượng áp dụng
V. Định nghĩa thuật ngữ và mã *** [bắt buộc nếu ≥5 domain terms]
VI. Nguyên tắc quản trị chung
VII. Thông tin bắt buộc theo nguồn phát sinh
VIII. Thẩm quyền phê duyệt *** [TÁCH BIỆT khỏi RACI]
IX. Vai trò và trách nhiệm
X. Quy ước RACI
XI. Bảng RACI tổng hợp theo quy trình con *** [cross-tab nếu ≥3 sub-processes]
XII. Danh mục quy trình con
XIII. Tiến độ thực hiện (SLA tổng quan)
XIV. Diễn giải các quy trình con chính
XV. Mối quan hệ quy trình và KPI
XVI. Hồ sơ/biểu mẫu áp dụng *** [auto-generate mã BM-XX-NN]
XVII. Kiểm soát tuân thủ
XVIII. Xử lý vi phạm *** [enterprise required, SMB optional]
XIX. Hiệu lực thi hành
```

`***` = sections hay bị skip nhất → bắt buộc check.

---

## Section-by-Section Spec

### I. Thông tin chung

**Mục đích**: Process metadata at-a-glance.

**Required content** (table format):

| Nội dung | Chi tiết |
|----------|----------|
| Mã quy trình | [Auto-generate: 2-letter prefix theo nhóm + số thứ tự, vd: KD-11, HR-03] |
| Tên quy trình | [Full descriptive name, không viết tắt] |
| Đơn vị chủ trì | [Department primary owner] |
| Đơn vị phối hợp chính | [Departments phối hợp, comma-separated] |
| Cấp phê duyệt | [Approval authority — link đến Section VIII] |
| Đối tượng áp dụng | [Scope: products/services/regions/teams] |
| Tần suất thực hiện | [Daily/Weekly/Monthly/Ad-hoc + frequency estimate] |

### II. Căn cứ ban hành / Văn bản liên quan

**Mục đích**: Legal/operational authority basis. Skip = giảm credibility với enterprise audit.

**Required content**:
- "Căn cứ vào Nội quy, Quy chế làm việc Công ty [Tên]"
- "Căn cứ vào chức năng quyền hạn của [Cấp có authority]"
- "Căn cứ vào thực tế công việc, xét đề nghị của [Cấp đề xuất]"
- (Optional) Tham chiếu regulations/standards áp dụng (ISO, ngành, pháp luật)

### III. Mục đích

**Required content** (table format, 3-5 mục đích):

| Mục đích | Diễn giải |
|----------|-----------|
| [Mục đích 1 — 1 cụm từ ngắn] | [Diễn giải cụ thể 1-2 câu] |

Mẫu mục đích:
- "Đảm bảo đồng bộ và minh bạch khi [hoạt động]"
- "Phân định rõ trách nhiệm các bộ phận, cá nhân"
- "Giảm thời gian xử lý, tối ưu nguồn lực"
- "Đảm bảo tuân thủ regulation/policy"

### IV. Phạm vi và đối tượng áp dụng

**Required content** (table format):

| Đối tượng | Nội dung áp dụng |
|-----------|------------------|
| Bộ phận áp dụng chính | [Primary department + danh mục activities] |
| Đối tượng liên đới | [Cá nhân/bộ phận liên quan theo sơ đồ tổ chức] |

Explicit exclusions (nếu có): "Quy trình này KHÔNG áp dụng cho [X] — xem [link tới quy trình khác]"

### V. Định nghĩa thuật ngữ và mã *** CRITICAL

**Bắt buộc** nếu có ≥5 domain-specific terms hoặc codes.

**Required content** (table format):

| Khái niệm / Mã | Diễn giải |
|----------------|-----------|
| [Term hoặc Code] | [Definition rõ ràng cho người mới] |

Ví dụ KD-11 dùng warehouse codes:
- HN98 — Kho hàng chờ phân loại
- HN97 — Kho hàng lỗi, hàng chờ hủy
- HCM 14_D/C/B/A — Kho hàng lỗi phân loại D/C/B/A

Critical rule: Mọi viết tắt/abbreviation lần đầu xuất hiện PHẢI ở Section V. Section khác chỉ dùng abbreviation sau khi đã định nghĩa.

### VI. Nguyên tắc quản trị chung

**Required content** (table format, 3-5 nguyên tắc):

| STT | Nguyên tắc | Nội dung áp dụng |
|-----|-----------|------------------|
| 1 | [Nguyên tắc tên ngắn] | [Enforcement rule cụ thể, có số nếu được] |

Mẫu nguyên tắc:
- "Bắt buộc lập phiếu nhập kho" — toàn bộ hàng phải có chứng từ
- "SLA xử lý X ngày" — timing hard limit
- "Đồng bộ hệ thống và lưu trữ" — data + document policy
- "Lưu trữ vật lý tách biệt" — segregation rule

### VII. Thông tin bắt buộc theo nguồn phát sinh

**Required content** (table format):

| Nguồn phát sinh | Thông tin bắt buộc ghi nhận |
|-----------------|----------------------------|
| [Source type 1] | [Required data points] |

Mục đích: data quality requirement per scenario. Phòng phòng "tôi không biết cần ghi gì" khi handle case mới.

### VIII. Thẩm quyền phê duyệt *** CRITICAL — TÁCH BIỆT KHỎI RACI

**Required content** (table format):

| Đối tượng / Case | Thẩm quyền phê duyệt |
|------------------|---------------------|
| [Case 1] | [Position có authority] |

**Critical distinction**:
- RACI = ai LÀM, ai được tham vấn, ai được informed
- Approval matrix = ai có AUTHORITY ra quyết định cuối cùng

Common mistake: gộp 2 cái vào RACI Accountable column. KHÔNG đủ — cần explicit matrix cho phép decision-making rules.

Ví dụ KD-11:
- Nhóm hàng BHĐT → Trưởng bộ phận BH & CSKH duyệt
- Tại kho Hà Nội → Giám đốc Kinh doanh duyệt
- Hủy hàng Loại A có điện → Giám đốc Điều hành duyệt

### IX. Vai trò và trách nhiệm

**Required content** (table format, per role narrative):

| Vị trí | Vai trò / Trách nhiệm |
|--------|----------------------|
| [Role title] | [Detailed narrative 2-3 câu — không chỉ RACI letter, mà context] |

Differentiates từ Section X RACI: Section IX là **narrative** (mô tả vai trò), Section X-XI là **structured matrix** (R/A/C/I letters).

### X. Quy ước RACI

**Required content** (legend table — luôn standard):

| Ký hiệu | Ý nghĩa |
|---------|---------|
| R | Responsible – Bộ phận trực tiếp thực hiện |
| A | Accountable – Bộ phận/cấp chịu trách nhiệm cuối cùng |
| C | Consulted – Bộ phận được tham vấn/cho ý kiến |
| I | Informed – Bộ phận được thông tin |

Section này luôn giống nhau across SOPs. Include cho mỗi SOP để audience không cần lookup external.

### XI. Bảng RACI tổng hợp theo quy trình con *** CRITICAL

**Required content** (cross-tab matrix nếu ≥3 sub-processes):

| Mã | Quy trình con | Role 1 | Role 2 | Role 3 | ... | Role N |
|----|---------------|--------|--------|--------|-----|--------|
| [Sub-process ID] | [Sub-process name] | R/A/C/I | R/A/C/I | R/A/C/I | ... | R/A/C/I |

**Critical rules**:
- Exactly 1 A per row (sub-process). Multiple A = governance ambiguity.
- Max 3 C per row. ≥5 C = "hoa hồng RACI" anti-pattern.
- Mỗi role/column tối thiểu 1 R hoặc 1 A trong toàn bảng. Role có toàn I = không cần trong matrix.

**Note for special cases**: dual accountability (e.g., A* footnote) cho phép khi specific carve-out:
> "Tại bước X, [Role A] là người chịu trách nhiệm chính (A) về [aspect]. [Role B] đóng vai trò (C), nhưng sẽ chịu trách nhiệm phụ (A*) riêng với [carve-out scope]."

### XII. Danh mục quy trình con

**Required content** (table):

| STT | Mã quy trình con | Tên quy trình con |
|-----|------------------|-------------------|
| 1 | [PARENT-ID.01] | [Sub-process name] |

Auto-generation: parent SOP có mã KD-11 → sub-processes là KD-11.01, KD-11.02, ...

### XIII. Tiến độ thực hiện (SLA tổng quan)

**Required content** (table, end-to-end timeline view):

| Mốc thời gian | Quy trình con | Nội dung công việc | Chủ trì | Đầu ra |
|---------------|---------------|--------------------|---------|--------|
| [Time mark, vd: "Tối đa 02 giờ", "Trong 5 ngày"] | [Sub-process ID] | [What happens] | [Role responsible] | [Deliverable] |

Skill PHẢI: pull SLA values từ Section XIV details + reconcile no conflict.

### XIV. Diễn giải các quy trình con chính

**Per sub-process** (table format, ~3-5 rows):

```
### KD-11.0X – [Sub-process name]
| Nội dung | Chi tiết |
|----------|----------|
| Yêu cầu thực thi | [Mandatory rules] |
| Thời hạn | [SLA — match Section XIII] |
| Vị trí nhập liệu | [System/location where data goes] |
| SLA chéo | [Cross-role timing rules] |
| Lưu trữ | [Document retention] |
```

Section dài nhất của SOP. Mỗi sub-process expand 4-8 rows tùy complexity.

### XV. Mối quan hệ quy trình và KPI

**Required content** (table format):

| Hạng mục | Chi tiết |
|----------|----------|
| Mối quan hệ với quy trình khác | [Upstream/downstream relationships, vd: "Lệnh thu hồi phát sinh từ KD-07"] |
| Process owner ↔ business outcome link | [Trace lineage] |
| Đề xuất KPI [1] | [Metric definition + target] |
| Đề xuất KPI [2] | [Metric definition + target] |

Mục đích: prevent process silo. Mọi SOP phải biết quan hệ với portfolio.

### XVI. Hồ sơ/biểu mẫu áp dụng *** CRITICAL

**Required content** (table format):

| STT | Mã biểu mẫu | Tên hồ sơ / biểu mẫu |
|-----|-------------|---------------------|
| 1 | BM-[PROCESS-CODE]-01 | [Form name] |
| 2 | BM-[PROCESS-CODE]-02 | [Form name] |

**Auto-generation rule**: mã = "BM-" + process code + "-" + 2-digit sequential number.
- SOP KD-11 → forms BM-KD11-01, BM-KD11-02, ...
- SOP HR-03 → forms BM-HR03-01, BM-HR03-02, ...

Mọi form referenced trong Section XIV PHẢI có entry trong Section XVI.

### XVII. Kiểm soát tuân thủ

**Required content** (table format):

| Đơn vị giám sát | Trách nhiệm |
|-----------------|-------------|
| [Compliance body 1 — vd: Internal Audit] | [Specific oversight role] |
| [Compliance body 2 — vd: BI/Analytics] | [Monitoring role] |
| [Compliance body 3 — vd: Finance/Tax] | [Financial compliance check] |

Best practice: ≥2 oversight bodies cho enterprise SOPs. Single oversight = SPOF risk.

### XVIII. Xử lý vi phạm *** ENTERPRISE REQUIRED

**Required content** (table format):

| Tình huống vi phạm | Hình thức xử lý kỷ luật |
|--------------------|------------------------|
| [Violation type 1 — minor] | [Sanction 1 — quantified, vd: "Trừ 10% trọng số KPI per lỗi"] |
| [Violation type 2 — repeated] | [Sanction 2 — nhắc nhở/cảnh cáo bằng văn bản] |
| [Violation type 3 — serious] | [Sanction 3 — xem xét lại công việc, chấm dứt HĐLĐ] |
| Gây thiệt hại tài sản | [Compensation per VN labor law] |

Skip cho SMB (L0-L1). Required cho enterprise (L3+). Mọi sanction phải có evidence trail (audit log) — nếu chưa có monitoring → flag.

### XIX. Hiệu lực thi hành

**Required content** (table format):

| Nội dung | Chi tiết |
|----------|----------|
| Hiệu lực | "Quy trình này có hiệu lực kể từ ngày [date], bổ sung và thay thế cho các quy định khác trái với nội dung tại quy định này." |
| Phê duyệt | [Approver name + position + date signed] |
| Phiên bản | [Version number, vd: v1.0, v2.1] |
| Nơi nhận | [Distribution list — departments + storage locations] |

---

## Maturity Downgrade Rules

Nếu maturity != L3+, dùng simplified template:

### L0-L1 → 8-section simplified
Keep: I (Thông tin chung), III (Mục đích), IV (Phạm vi), IX (Vai trò), XIII (SLA), XIV (Sub-process details), XVI (Forms), XIX (Hiệu lực)
Skip: II, V, VI, VII, VIII, X, XI, XII, XV, XVII, XVIII

### L2 → 12-section standard
Add to L0-L1 baseline: V (Glossary if needed), VI (Nguyên tắc), X (RACI legend), XI (RACI matrix), XVII (Kiểm soát)
Still skip: II, VII, VIII, XV, XVIII

### L3+ → Full 19-section (đây là template default)

---

## Common Pitfalls When Generating SOP

1. **Skip Section V** vì "team biết hết rồi" → nhân viên mới onboard không hiểu codes/abbreviations. Fix: nếu có ≥5 terms, MUST include.

2. **Gộp Section VIII vào Section XI (RACI)** → mất explicit decision authority. Fix: keep separate matrices.

3. **Section XI có multiple A** trên 1 row → governance ambiguity. Fix: dual accountability dùng footnote A* convention, không 2 A.

4. **Section XVI thiếu forms** mà Section XIV reference → broken pointers. Fix: cross-reference check trước output.

5. **Section XVIII vague** ("xử lý theo quy định") → unenforceable. Fix: quantify (vd: "trừ 10% KPI").

6. **Section XIX thiếu version + nơi nhận** → SOP không formal. Fix: required cho enterprise.

---

## Output Example Header (skill generates đầu output)

```
# QUY TRÌNH [MÃ]: [TÊN]

## I. Thông tin chung
[table]

## II. Căn cứ ban hành / Văn bản liên quan
[table]
...
```

Match format KD-11 exactly. Enterprise client expects familiar structure.
