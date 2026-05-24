# Tiêu chuẩn Thẩm định RBAC (Role-Based Access Control) cho Hợp đồng Bộ nhớ

Khi Audit hoặc Cấu hình một file `memory-contract.yml`, BẮT BUỘC rà soát chặt chẽ các luật dưới đây. Vi phạm bất cứ Rule nào = Bắn Cờ Đỏ (Red Flag) và yêu cầu Optimize.

## 1. Domain Data Law (Thánh địa Bất khả xâm phạm)
Bất kỳ đường dẫn nào chứa chuỗi `.context/domain` BẮT BUỘC phải thoả mãn:
- `access.write` **BẮT BUỘC RỖNG** `[]`. Cấm tuyệt đối cấu hình Agent Tier 3/4 được quyền Ghi trừ Data Warehouse/Knowledge-Forge Agent được cấp Pass đục ngầm cụ thể.
- `note` PHẢI đi kèm cảnh báo: `"READ ONLY — NEVER write to context files"`.
*(Nếu Hợp đồng cấp quyền Write cho một Worker ở mảng này => Tội rò rỉ bộ nhớ, phạt điểm ngay).*

## 2. Telemetry Write-Lock (Kiểm soát Ống xả)
- Mảng `trace_config.enabled` PHẢI là `true`.
- Các file `state.json`, `session-log.json`, `ledger.md` (thuộc phân mảng State) PHẢI giới hạn quyền `write:` DUY NHẤT cho Điều phối viên (Coordinator/Session-Manager) hoặc Orchestrator Agent của phòng ban (Ví dụ OAC-COORD, CF-01-CPM).
- Worker cấp thấp không được phép tự chốt Sổ Cái.

## 3. Conflict Resolution
Phải khai báo rõ ràng cơ chế giải quyết xung đột khi nhiều luồng Ghi diễn ra cùng lúc.
- `conflict_resolution.default` phải là `last-writer-wins-with-log`.
- Phải có cơ chế `escalate_to: "Human Orchestrator"`.

## 4. Xung Vận Hành Memory
Hợp đồng V2 yêu cầu BẮT BUỘC phải quy định Ống Xả Telemetry (đưa siêu trí nhớ lên Cục tổng) qua trường:
- `compaction_protocol.trigger_turn_count`
- `telemetry_dual_write: "CENTRAL_REGISTRY"`

## 5. Dual-Context & Knowledge Strict Check
Dựa theo `MEMORY-BUS-CONTRACT` lõi, Hệ Sinh Thái bắt buộc phải có mô hình trí nhớ kép:
- `write_quan-ly-quy-tac` và `read_quan-ly-quy-tac` PHẢI khả dụng trong file memory-contract.
- Đặc quyền đọc phải thiết lập Thứ tự ưu tiên (Priority Index) ở mức cao nhất dành cho `knowledge_items` (KI Mandatory Check), trước khi Agent lục lọi vào `conversation_logs` gây phình Token.
- Hộp Lưu Trữ KIs bắt buộc phải có 5 trường Metadata `[title, domain_tag, key_insight, source_conversation_id, confidence_level]`. Thiếu 1 trong 5 = 🔴 [LOCAL-FIX].

## Chẩn Đoán Khi Audit
Nếu nhận cờ Gợi ý Audit (Audit Trigger):
1. **Quét mảng `keys`**: Tìm các thư mục `.context/domain`.
2. **Kiểm tra `write` array**: Nếu != `[]` -> Báo cáo Lỗi Ngữ nghĩa Xâm phạm RBAC.
3. **Quét Telemetry**: Thiếu trường Central Registry -> Báo cáo Mù Thông tin.
4. **Quét Dual-Context**: Thiếu bộ `read_quan-ly-quy-tac.ki_check_mandatory: true` -> Cảnh cáo Ngốn Token.
