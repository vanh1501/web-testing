# Domain Intelligence Pipeline (DIP)
**Mục đích:** Giao thức nghiên cứu có cấu trúc để Skill `quan-ly-quy-tac` có thể tạo, kiểm định, và tối ưu Rule cho workspace thuộc BẤT KỲ domain chuyên ngành nào (Giáo dục, Pháp lý, Y tế, Tài chính...). Pipeline này đảm bảo Agent không bịa chuẩn ngành (hallucination) mà phải dựa trên bằng chứng nghiên cứu thực tế.

> [!IMPORTANT]
> DIP chỉ kích hoạt khi tạo/sửa/audit Rule cho **Domain Workspace** (workspace chuyên ngành). Không áp dụng cho Meta Workspace (Master Repo).

---

## Phase 1: DISCOVERY (Khám phá Domain)

**Mục tiêu:** Xác định bối cảnh ngành, rủi ro chính, và các framework/chuẩn quốc tế áp dụng.

**Quy trình bắt buộc:**

1. **Identify Domain Classification:**
   - `Input` -> Tên domain workspace (VD: "Giáo dục Đại học AUN-QA").
   - `Action` -> Phân loại theo Risk Tier: `High-Risk` (Y tế, Tài chính, Pháp lý) | `Medium-Risk` (Giáo dục, HR) | `Low-Risk` (Marketing, Content).
   - `Output` -> Domain Tag + Risk Tier.

2. **Execute Structured Research (≥3 Searches):**
   - `Search 1 (Standards)` -> `search_web("[domain] industry standards regulations compliance framework")`.
   - `Search 2 (Risks)` -> `search_web("[domain] common risks failures data safety best practices")`.
   - `Search 3 (Frameworks)` -> `search_web("[domain] ISO NIST OWASP applicable certification requirements")`.
   - `High-Risk domains` -> BẮT BUỘC thêm Search 4: `search_web("[domain] regulatory penalties legal requirements [country]")`.

3. **Research Quality Gate:**
   - `Min_Sources` -> ≥3 independent sources. `< 3` -> [HALT] research thêm.
   - `Min_Dimensions` -> Phải phủ ≥2 chiều rủi ro domain (VD: Data Privacy + Compliance).
   - `Recency` -> Sources phải từ năm 2023 trở đi. Outdated sources -> [WARN].

**Output Phase 1:** Raw Research Notes (lưu tạm vào `scratch/` hoặc artifact).

---

## Phase 2: TRANSLATION (Chuyển đổi → Constraints)

**Mục tiêu:** Biến đổi kết quả nghiên cứu thô thành Boolean Constraints theo chuẩn CoD.

**Quy trình bắt buộc:**

1. **Risk-Mitigation Extraction:**
   - Đọc từng phát hiện từ Phase 1.
   - Tách thành cặp: `(Risk Description) → (Mitigation Action)`.
   - VD: "Student data must be anonymized per FERPA" → `(PII_Student_Data) → [REQUIRE: Anonymization]`.

2. **CoD Formatting:**
   - Chuyển mỗi cặp Risk-Mitigation thành cú pháp Telegraphic Shorthand:
     ```
     Risk_Name (context) -> [Action]. Optional_detail.
     ```
   - ❌ *Sai:* "Khi xử lý dữ liệu sinh viên, bạn cần đảm bảo tuân thủ quy định FERPA bằng cách ẩn danh hóa tất cả thông tin cá nhân."
   - ✅ *Đúng:* `Student_PII (FERPA) -> [REQUIRE: Anonymize]. No raw names in outputs.`

3. **Layer Classification:**
   - `L0 (Safety/Physical)` -> Constraints về an toàn dữ liệu, quyền truy cập, phá hoại.
   - `L1 (Operational/Domain)` -> Constraints về quy trình nghiệp vụ, chuẩn output, compliance.
   - `KB/Skills (Cognitive)` -> Nếu phát hiện là hướng dẫn phương pháp, SOP → KHÔNG đưa vào Rule. Chuyển sang KB hoặc Skill.

**Output Phase 2:** Draft Domain Constraints (CoD format, phân loại L0/L1/KB).

---

## Phase 3: VALIDATION (Kiểm chứng)

**Mục tiêu:** Đảm bảo Domain Rules không bị ảo giác (hallucination) và đạt chất lượng production.

**Quy trình bắt buộc:**

1. **Source Traceability:**
   - Mỗi constraint PHẢI trace ngược được về ≥1 nguồn từ Phase 1.
   - Constraint không có nguồn gốc -> [REJECT] + Đánh dấu `[UNVERIFIED]`.

2. **Hallucination Filter:**
   - Cross-check mỗi domain claim bằng `search_web` bổ sung nếu nghi ngờ.
   - Agent tự bịa tên tiêu chuẩn (VD: "ISO 99999") -> [SYSTEMIC-HALT].

3. **Human Review Gate:**
   - `High-Risk domains` -> BẮT BUỘC trình Human review trước khi ghi vào file Rule.
   - `Medium/Low-Risk` -> Trình Human review nếu ≥5 constraints mới được tạo.

4. **Integration:**
   - Inject validated constraints vào file L1 tương ứng (thường là `l1-workspace-standards.md`).
   - KHÔNG tạo file L1 domain riêng (VD: `l1-education-policy.md`). Mọi domain constraint phải nằm trong 8-File Skeleton.

**Output Phase 3:** Validated Domain Rules (ready for production).

---

## Phụ Lục: Search Query Templates (Mẫu tham khảo)

| Domain | Search 1 (Standards) | Search 2 (Risks) | Search 3 (Frameworks) |
|--------|---------------------|-------------------|----------------------|
| Giáo dục | "higher education quality assurance standards AUN-QA" | "student data privacy risks FERPA compliance" | "ISO 21001 education management system" |
| Y tế | "healthcare AI giam-sat-tuan-thu HIPAA compliance" | "patient data breaches medical AI risks" | "ISO 13485 FDA AI medical device" |
| Tài chính | "fintech compliance regulations KYC AML" | "financial AI bias discrimination risks" | "ISO 27001 SOC2 financial services" |
| Pháp lý | "legal tech AI ethics bar association guidelines" | "attorney-client privilege AI risks" | "ABA legal AI giam-sat-tuan-thu framework" |
| HR | "HR AI hiring bias regulations EEOC" | "employee data privacy workplace AI risks" | "ISO 30414 human capital reporting" |

---

## Điều Kiện Kích Hoạt DIP

- **Route 1 (BIRTH):** Khi tạo Rule cho Domain Workspace → BẮT BUỘC chạy DIP trước khi viết bất kỳ L1 nào.
- **Route 3 (REPAIR) — RR4:** Khi sửa Domain Rules → Chạy DIP Phase 2-3 để xác minh.
- **Route 4 (EVOLVE):** Khi quét Domain Risk Coverage → Chạy DIP Phase 1 để đối chiếu rủi ro.
