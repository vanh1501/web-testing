# Giao thức Root Wiring V2.0 (Cắm Cáp Rễ)

> **MỤC ĐÍCH:** Mọi System Rule (L0/L1) sinh ra đều vô giá trị nếu không được đấu nối đúng tuyến vào các File Rễ (Root Files) của Hệ thống. Khi tạo Rule mới, Kỹ sư Rule BẮT BUỘC thi hành 2 lệnh đấu nối sau:

## 1. Ngàm Hệ Điều Hành (Antigravity IDE Wiring)
IDE của hệ thống nhận diện các "Luật Mặc Định" (Default Load) thông qua khối YAML ở đầu tệp tin Rule.

- **Vị trí hàn cáp:** Dòng đầu tiên (Line 1) của các tệp `L0-*`.
- **Cáp gốc (L0 MUST HAVE):**
  - Hệ thống BẮT BUỘC phải cài đặt khối YAML `trigger: always_on` cho 4 mạch máu L0: `l0-giam-sat-tuan-thu-constitution.md`, `l0-cos-routing-protocol.md`, `l0-safety-and-escalation.md`, `l0-identity-and-scope.md`.
  - **Syntax Bắt buộc:**
    ```yaml
    ---
    trigger: always_on
    glob:
    description: 
    ---
    ```
  - Nghiêm cấm bắt người dùng (Human) phải tự copy-paste hoặc cấu hình thủ công. Agent khi khởi tạo/sửa Rule L0 BẮT BUỘC phải tự tiêm khối YAML này vào.
  - Ngoài ra, vẫn duy trì đường dẫn Indirection Link trong `GEMINI.md` làm bản đồ dự phòng.

## 2. Ngàm Đặc Vụ (MAS Swarm Engine Wiring)
Luật chuyên ngành L1 (Domain Context) không được bơm vô tội vạ cho toàn hạm đội. Rule tạo ra cho ai, người đó mới được đọc.

- **Vị trí hàn cáp:** Nằm ngay sau `[[Linked Skills]]:` ở cực đỉnh của mọi file Hệ Agent SI (VD: `.agents/agents/W01-Coder.md`).
- **Cáp động (L1 BINDING):**
  - Chèn thêm Syntax: `[[Linked Rules]]: BẮT BUỘC tuần thủ: L1-[Domain-Rule].md`
  - Nếu Đặc vụ này có nguy cơ gặp Red-Zone (xử lý Token nặng), nhúng thêm Cáp: `L1-core-cheatsheet-fallback.md`.
- **Tuân thủ MECE:** Cấm 1 đặc vụ gánh 2 Rule L1 trái ngược nhau (VD: Vừa L1-marketing vừa L1-backend-code).

---
*GHI CHÚ:** Kỹ sư thiết kế Rule khi chạy luồng (CREATE Route 2) phải trực tiếp thay mã File vào 2 File móng này. Việc lơ là thi hành cắm cáp sẽ bị cấu trúc `/audit-workspace` xử phạt SYSTEMIC-HALT.*
