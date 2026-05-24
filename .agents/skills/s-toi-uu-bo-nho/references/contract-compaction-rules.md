# Giao thức Compaction & Dual-Write (Xả nén và Ghi kép)

Để duy trì khả năng hoạt động không giới hạn (Zero-Bloat) của Context Window trong phiên chạy dài, Memory Bus Contract buộc phải kích hoạt cơ chế Xả Nén định kỳ. Kỹ sư Memory Bus (Bạn) BẮT BUỘC tuân thủ các quy tắc sau khi khởi tạo File hoặc Optimize Hợp đồng chưa đạt yêu cầu.

## 1. Trigger Turn Count Law
- Khối `compaction_protocol` PHẢI ấn định số `trigger_turn_count`. Giá trị chuẩn là `20`.
- Cơ chế Action phải là `summarize_and_flush`. Tuyệt đối không xóa trắng mà không rút tủy nội dung (summarize).

## 2. Telemetry Dual-Write Law
- Tính năng Ghi kép (Dual-Write) giúp gửi tín hiệu đo lường từ Workspace lên Hồ chứa cục bộ của Hạm Đội (Cục Giám Sát).
- `telemetry_dual_write` LUÔN LUÔN phải được trỏ tới địa chỉ `"CENTRAL_REGISTRY"`. Cấm ghi đè địa chi ảo.

## 3. Quá trình Can thiệp (Optimize Mechanism)
- Khi bạn được gọi để Vá (Fix) file `memory-contract.yml`, đừng làm hỏng quyền RBAC đang có (mảng Keys). CHỈ TÌM VÀ CẤY Thêm Khối Dữ Liệu sau đây vào đầu File nếu chúng vắng mặt:

```yaml
# ==========================================
# [Round 2 Artisan] Dual-Write & Compaction
# ==========================================
compaction_protocol:
  trigger_turn_count: 20
  action: "summarize_and_flush"
telemetry_dual_write: "CENTRAL_REGISTRY"
```

## Kiểm Tra Trải Nghiệm Lỗ Hổng 
Mọi Hợp đồng không chứa khối `compaction_protocol` ĐỀU BỊ COI LÀ RỖNG/KẸT. Tiến hành cảnh cáo và xuất tệp Delta Report sửa đổi.
