# [TEMPLATE] Knowledge Base Article
> **Template version:** v1.0 | Copy file này → rename → điền nội dung → submit Review
> Xóa mọi dòng hướng dẫn in nghiêng trước khi publish. Thay thế `{{PLACEHOLDER}}`.

---

## Metadata Block (BẮT BUỘC — không được xóa)

```yaml
---
id: {{ARTICLE_ID}}
title: {{TIEU_DE_ARTICLE}}
domain: {{DOMAIN}}
category: {{CATEGORY}}
topic: {{TOPIC}}
type: SOP | Policy | How-to | Reference | Template | Case Study | FAQ
owner: {{TEN_OWNER}}
created_date: {{YYYY-MM-DD}}
last_updated: {{YYYY-MM-DD}}
review_due: {{YYYY-MM-DD}}
status: Draft | Active | Outdated | Deprecated
tags: [{{TAG_1}}, {{TAG_2}}, {{TAG_3}}]
---
```

---

## [Nếu type = SOP] — Standard Operating Procedure

### {{TIEU_DE_SOP}}

> *Câu 1-2: Tóm tắt SOP này hướng dẫn làm gì, ai cần đọc, khi nào dùng.*

**Áp dụng cho:** {{AP_DUNG_CHO}}
**Trigger:** {{TRIGGER_KHOI_DONG}}
**Kết quả mong đợi:** {{KET_QUA_MONG_DOI}}
**Thời gian thực hiện:** {{THOI_GIAN_THUC_HIEN}}

---

#### Bước 1: {{TEN_BUOC_1}}
**Người thực hiện:** {{ROLE_1}}
**Khi nào:** {{TRIGGER_1}}

{{HUONG_DAN_BUOC_1}}

> ⚠️ **Lưu ý:** {{LUU_Y_QUAN_TRONG_1}} *(xóa nếu không có)*

**Output:** {{OUTPUT_BUOC_1}}
**Chuyển tiếp:** Sang Bước 2 khi {{DIEU_KIEN_CHUYEN_TIEP_1}}

---

#### Bước 2: {{TEN_BUOC_2}}
**Người thực hiện:** {{ROLE_2}}
**Khi nào:** {{TRIGGER_2}}

{{HUONG_DAN_BUOC_2}}

**Output:** {{OUTPUT_BUOC_2}}
**Chuyển tiếp:** Sang Bước 3 khi {{DIEU_KIEN_CHUYEN_TIEP_2}} / Nếu {{EXCEPTION}} → xem mục Exception bên dưới

---

#### Bước 3: {{TEN_BUOC_3}}
*(Thêm bước theo cấu trúc tương tự)*

---

#### Exception Handling

| Tình huống | Hành động | Người xử lý | Escalate khi |
|------------|-----------|------------|-------------|
| {{EXCEPTION_1}} | {{ACTION_1}} | {{ROLE_1}} | {{ESCALATE_1}} |
| {{EXCEPTION_2}} | {{ACTION_2}} | {{ROLE_2}} | {{ESCALATE_2}} |

#### Biểu mẫu & Tài liệu liên quan

- {{TEN_BIEU_MAU_1}}: {{LINK_1}}
- {{TEN_BIEU_MAU_2}}: {{LINK_2}}

#### Xem thêm

- [{{ARTICLE_LIEN_QUAN_1}}]({{LINK_ARTICLE_1}})
- [{{ARTICLE_LIEN_QUAN_2}}]({{LINK_ARTICLE_2}})

---

## [Nếu type = How-to] — Hướng dẫn nhanh

### {{TIEU_DE_HOW_TO}}

> *1 câu: Hướng dẫn này giúp bạn làm được gì.*

**Thời gian:** {{THOI_GIAN}} | **Yêu cầu trước:** {{YEU_CAU_TRUOC}}

1. {{BUOC_1}}
2. {{BUOC_2}}
3. {{BUOC_3}}
*(thêm bước)*

> 💡 **Mẹo:** {{MEO_HAY}} *(xóa nếu không có)*

> ⚠️ **Cẩn thận:** {{CANH_BAO}} *(xóa nếu không có)*

**Kết quả mong đợi:** {{KET_QUA}}

Gặp vấn đề? → {{HUONG_DAN_KHI_GAP_LOI}}

---

## [Nếu type = Policy] — Chính sách / Quy định

### {{TIEU_DE_POLICY}}

**Hiệu lực từ:** {{NGAY_HIEU_LUC}} | **Áp dụng cho:** {{AP_DUNG_CHO}}

#### Quy định

> *Liệt kê quy định theo bullet — ngắn gọn, rõ ràng, thể mệnh lệnh.*

- **{{QUY_DINH_1}}:** {{NOI_DUNG_1}}
- **{{QUY_DINH_2}}:** {{NOI_DUNG_2}}
- **{{QUY_DINH_3}}:** {{NOI_DUNG_3}}

#### Ngoại lệ được phép

| Ngoại lệ | Điều kiện | Người phê duyệt |
|----------|----------|----------------|
| {{NGOAI_LE_1}} | {{DIEU_KIEN_1}} | {{NGUOI_DUYET_1}} |

#### Vi phạm & Hậu quả

{{HEU_QUA_VI_PHAM}}

---

## [Nếu type = FAQ] — Câu hỏi thường gặp

### {{CHU_DE_FAQ}}

> *Mỗi Q&A độc lập — người đọc không cần đọc theo thứ tự.*

---

**Q: {{CAU_HOI_1}}**

{{TRA_LOI_1}}

---

**Q: {{CAU_HOI_2}}**

{{TRA_LOI_2}}

---

**Q: {{CAU_HOI_3}}**

{{TRA_LOI_3}}

---

*(Thêm Q&A theo cấu trúc tương tự)*

**Câu hỏi không thấy trong danh sách?** → Liên hệ {{LIEN_HE_SUPPORT}}

---

## [Nếu type = Case Study] — Bài học kinh nghiệm

### {{TIEU_DE_CASE_STUDY}}

**Ngày xảy ra:** {{NGAY}} | **Lĩnh vực:** {{LINH_VUC}} | **Mức độ:** Critical ☐ / High ☐ / Medium ☐

#### Bối cảnh

{{BOI_CANH}}

#### Vấn đề đã xảy ra

{{VAN_DE}}

#### Nguyên nhân gốc rễ

- **Nguyên nhân trực tiếp:** {{NGUYEN_NHAN_TRUC_TIEP}}
- **Nguyên nhân gốc rễ:** {{NGUYEN_NHAN_GOC_RE}}

#### Giải pháp đã thực hiện

| Hành động | Ai thực hiện | Kết quả |
|-----------|-------------|---------|
| {{HANH_DONG_1}} | {{NGUOI_1}} | {{KET_QUA_1}} |
| {{HANH_DONG_2}} | {{NGUOI_2}} | {{KET_QUA_2}} |

#### Bài học rút ra

1. **{{BAI_HOC_1}}:** {{CHI_TIET_1}}
2. **{{BAI_HOC_2}}:** {{CHI_TIET_2}}

#### Thay đổi quy trình / chính sách sau sự kiện

- {{THAY_DOI_1}} → Xem: [{{TEN_SOP_MOI}}]({{LINK_SOP}})

---

*Phiên bản template này tuân theo Knowledge Curation Lifecycle Framework v1.0. Mọi thắc mắc về cách dùng → liên hệ KB Owner.*
