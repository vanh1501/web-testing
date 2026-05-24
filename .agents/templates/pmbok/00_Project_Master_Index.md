# 00_PROJECT_MASTER_INDEX (BẢN ĐỒ VẬN HÀNH DỰ ÁN)

**Dự án:** {{PROJECT_CODE}} ({{PROJECT_NAME}})
**Cập nhật lần cuối:** {{DATE}}

Tài liệu này là "Bản đồ Định tuyến" (Routing Map) DÀNH CHO TRỢ LÝ AI. Bất kỳ Đặc vụ nào (Agent) khi được gọi vào dự án này đều PHẢI đọc file này để biết lấy dữ liệu ở đâu, ghi kết quả vào chỗ nào, và gọi lệnh nào cho đúng.

---

## 1. BẢN ĐỒ DỮ LIỆU ĐẦU VÀO (INPUT DATA SOURCES)

Nơi hệ thống nạp nhiên liệu để tính toán. Các Đặc vụ **KHÔNG ĐƯỢC PHÉP** ghi đè hoặc xóa các file trong khu vực này.

| Loại Dữ liệu | Đường dẫn (Path) | Mục đích | Agent Phụ trách Đọc |
|--------------|------------------|----------|----------------------|
| **(Nguồn 1)** | `Kho-Du-Lieu/Du-Lieu-Vao/{{PROJECT_FOLDER}}/` | (Mô tả) | (Agent) |

---

## 2. BẢN ĐỒ DỮ LIỆU ĐẦU RA (OUTPUT DESTINATIONS)

Nơi hệ thống xả báo cáo sau khi tính toán xong. Các Đặc vụ **BẮT BUỘC** phải ghi file vào đúng thư mục tương ứng. CẤM xuất báo cáo lung tung.

| Loại Báo Cáo / Kết Quả | Workflow Kích hoạt | Đường dẫn Lưu trữ (Output Path) | Định dạng |
|------------------------|--------------------|---------------------------------|-----------|
| **(Báo cáo 1)** | `@[/workflow-name]` | `Kho-Du-Lieu/Ket-Qua/{{PROJECT_FOLDER}}/` | `.md` |

---

## 3. KHU VỰC TÀI SẢN CHIẾN LƯỢC (PROJECT KNOWLEDGE BASE)

Khu vực này chứa các chất xám cốt lõi của dự án. Agent chỉ dùng để làm form mẫu chiếu theo, KHÔNG làm nơi lưu file sinh ra hàng ngày.

| Cụm Nghiệp Vụ | Đường Dẫn Thư Mục/Tệp | Chứa Tài Liệu Gì? |
|---------------|-----------------------|-------------------|
| **Quản trị Dự án (PMBOK)** | `Du-An/{{PROJECT_FOLDER}}/00_*` | Project Charter, RACI, Risk/Change Log. |

---

## 4. QUY TẮC ĐỊNH TUYẾN DÀNH CHO ORCHESTRATOR

Khi Đặc vụ Điều phối (`tro-ly-dieu-phoi`) nhận lệnh từ Operator liên quan đến dự án này, hãy áp dụng quy tắc quét sau:
1. (Yêu cầu 1) ➔ Rút data từ (nguồn), xả vào (đích).
2. (Yêu cầu 2) ➔ Rút data từ (nguồn), xả vào (đích).

*(File này phải được dùng làm bối cảnh - Context - mỗi khi bất kỳ quy trình nào trong {{PROJECT_CODE}} khởi chạy)*
