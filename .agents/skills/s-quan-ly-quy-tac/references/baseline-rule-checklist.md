# Baseline Rule Checklist (SOP Tiêu Chuẩn Cho Hệ Thống Rule)
**Mục Đích:** Tài liệu này là "Sách giáo khoa" (SOP Standard) bắt buộc mà Kỹ năng `quan-ly-quy-tac` phải tham chiếu khi thực hiện Khởi tạo (BIRTH) hoặc Kiểm định MECE (EVOLVE) cho bất kỳ Workspace nào. Nó đóng gói tiêu chuẩn MECE 5 Chiều và nguyên tắc viết luật nén (Chain of Draft).

---

## 1. Nguyên Tắc Viết Luật (Chain of Draft & Semantic Compression)
Để tối ưu Token cho bộ nhớ Agent, MỌI FILE RULE (L0, L1) phải được viết theo nguyên tắc sau:
- **Telegraphic Shorthand (Mã giả điện tín):** Xóa bỏ đại từ nhân xưng, từ nối, văn xuôi giải thích ("Tại sao phải làm vậy"). 
- **Boolean Constraints:** Sử dụng cấu trúc `IF -> THEN -> HALT`.
- **Domain Grounding:** Với Workspace chuyên ngành (Domain Workspace), mọi L1 Rule phải đi qua Domain Intelligence Pipeline (DIP) để lấy minh chứng từ `search_web`. Cấm ảo giác (hallucination).
- **Ví dụ Tiêu Chuẩn:**
  - ❌ *Sai (Văn xuôi):* "Mỗi khi bạn chuẩn bị thực thi lệnh xóa file, bạn bắt buộc phải dừng lại hỏi người dùng."
  - ✅ *Đúng (CoD):* `Destructive_Cmds (rm, drop) -> HALT -> Require Human Approval.`

---

## 2. Tiêu Chuẩn MECE 5 Chiều (5-Dimension MECE Gap Analysis)
Một hệ thống MAS Agentic Workspace chỉ được coi là Đạt Chuẩn (Collectively Exhaustive) nếu bao phủ đủ 5 trụ cột rủi ro sau. Các file luật phải Độc lập (Mutually Exclusive) và không dẫm chân lên nhau.

### Chiều 1: Governance & Identity (Chiến lược & Định danh)
- **Mục tiêu:** Xác định Đặc vụ là ai, được phép làm gì ở tầm vĩ mô.
- **Files Bắt Buộc:**
  - `l0-giam-sat-tuan-thu-constitution.md`: Hiến pháp cốt lõi (Cấm sửa đổi cấu hình Master). Trigger: `always_on`.
  - `l0-identity-and-scope.md`: Nhận diện vai trò Agent. Trigger: `always_on`.

### Chiều 2: Risk & Safety (Rủi ro & An toàn)
- **Mục tiêu:** Các rào cản ngăn chặn phá hoại dữ liệu, lộ lọt PII, vòng lặp vô hạn.
- **Files Bắt Buộc:**
  - `l0-safety-and-escalation.md`: Giới hạn thực thi, bảo mật dữ liệu, quy trình leo thang. Trigger: `always_on`.

### Chiều 3: Memory & Routing (Điều hướng & Bộ nhớ)
- **Mục tiêu:** Quản lý cách hệ thống tải ngữ cảnh và phân mảnh bộ nhớ.
- **Files Bắt Buộc:**
  - `l0-cos-routing-protocol.md`: Giao thức định tuyến Context OS. Trigger: `always_on`.
  - `l1-core-cheatsheet-fallback.md`: Phao cứu sinh khi hệ thống sụp đổ. Trigger: `Semantic (On-Demand)`.

### Chiều 4: Workspace Operations (Vận hành & Tiêu chuẩn Output)
- **Mục tiêu:** Đảm bảo chất lượng I/O, cấu trúc thư mục, chuẩn Code.
- **Files Bắt Buộc:**
  - `l1-workspace-standards.md`: Chuẩn I/O, phong cách Code. Trigger: `glob: managed_workspaces/**/*` (hoặc cấu hình tương đương tùy Workspace).
  - `l1-operational-crud.md`: Quy chuẩn đọc/ghi file. Trigger: `Semantic (On-Demand)`.

### Chiều 5: Swarm Coordination (Phối hợp Bầy đàn)
- **Mục tiêu:** Quy định giao tiếp giữa các Đặc vụ, bàn giao (Handoff), hàng đợi.
- **Files Bắt Buộc:**
  - `l1-swarm-operations.md`: Giao thức Handoff. Trigger: `glob: artifacts/handoffs/**/*`.
  - `l2-changelog.md`: Ghi nhận lịch sử thay đổi kiến trúc. Trigger: `Semantic (On-Demand)`.

---

## 3. Khung Xương 8-File (The 8-File Guardrail Skeleton)
Khi thực thi `Route 1: BIRTH` hoặc kiểm tra thiếu hụt, danh sách **8 TỆP TỐI THIỂU** sau đây phải có mặt tại `.agents/quan-ly-quy-tac/` của mọi Workspace (có thể tùy chỉnh theo nghiệp vụ nhưng KHÔNG được làm mất 5 Chiều MECE):

1. `l0-giam-sat-tuan-thu-constitution.md` (Chiều 1)
2. `l0-identity-and-scope.md` (Chiều 1)
3. `l0-safety-and-escalation.md` (Chiều 2)
4. `l0-cos-routing-protocol.md` (Chiều 3)
5. `l1-workspace-standards.md` (Chiều 4)
6. `l1-swarm-operations.md` (Chiều 5)
7. `l1-core-cheatsheet-fallback.md` (Chiều 3 - Fallback)
8. `l2-changelog.md` (Chiều 5 - History)

> [!WARNING]
> Mọi file nghiệp vụ chuyên ngành (Ví dụ: `l1-hr-recruitment-policy.md`) KHÔNG ĐƯỢC PHÉP nằm trong thư mục `quan-ly-quy-tac/`. Phải được bứt ra và chuyển về `.agents/skills/` hoặc `KB/standards/`. Thư mục `quan-ly-quy-tac/` chỉ chứa 5 chiều không gian vật lý của MAS.
