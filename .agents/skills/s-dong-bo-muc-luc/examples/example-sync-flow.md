# Ví Dụ — Luồng Đồng Bộ Index Sau Khi Sinh Báo Cáo

**Vai trò:** Minh họa luồng `dong-bo-muc-luc` được trigger sau khi skill chuyên gia sinh artifact. Dùng làm reference khi audit hành vi sync hoặc onboard quy tắc 5.

---

## Kịch bản

Pipeline phân tích đối thủ vừa hoàn thành Bước 1 — `nghien-cuu-thi-truong-strategist` sinh evidence pack. Quy tắc 5 trigger `dong-bo-muc-luc` cập nhật index.

**Trạng thái trước sync:**

| Tệp/Index | Trạng thái |
|-----------|-----------|
| Tệp mới: `Kho-Du-Lieu/Ket-Qua/phan-tich-doi-thu/01-evidence-pack.md` | Vừa sinh |
| `DANH-SACH-BAO-CAO.md` | Chưa có entry mới |
| `DANH-SACH-DU-AN.md` | Đã có entry "phan-tich-doi-thu" trạng thái `Đang làm` |
| `BANG-DIEU-KHIEN.md` | Cập nhật lần cuối: 2 ngày trước |

---

## Step 1 — Quét thực tế

Index-syncer quét 4 thư mục nguồn. Diff phát hiện:

| Thư mục | Tệp mới | Diff với index |
|---------|---------|----------------|
| `Kho-Du-Lieu/Ket-Qua/phan-tich-doi-thu/` | `01-evidence-pack.md` | Thiếu entry trong `DANH-SACH-BAO-CAO` |
| `Du-An/phan-tich-doi-thu/` | (không thay đổi) | Không diff |
| `.agents/` | (không thay đổi) | Không diff |

→ 1 diff loại "thiếu". Áp Step 3 nhánh tự động.

---

## Step 2 — So sánh

Validate entry mới đề xuất:

```
Tên báo cáo: 01-evidence-pack
Dự án: phan-tich-doi-thu  ← FK resolve OK (khớp DANH-SACH-DU-AN)
Đường dẫn: Kho-Du-Lieu/Ket-Qua/phan-tich-doi-thu/01-evidence-pack.md
Ngày tạo: 2026-05-01  ← lấy timestamp file
Loại: phân tích  ← infer từ pattern tên + nội dung
```

4 check pass.

---

## Step 3 — Áp dụng

**Cập nhật `DANH-SACH-BAO-CAO.md`:**

```markdown
# Danh Sách Báo Cáo

Cập nhật lần cuối: 2026-05-01 14:32

| Tên báo cáo | Dự án | Đường dẫn | Ngày tạo | Loại |
|-------------|-------|-----------|----------|------|
| ... (entries cũ) | ... | ... | ... | ... |
| 01-evidence-pack | phan-tich-doi-thu | Kho-Du-Lieu/Ket-Qua/phan-tich-doi-thu/01-evidence-pack.md | 2026-05-01 | phân tích |
```

**Cập nhật `Du-An/phan-tich-doi-thu/TIEN-DO.md`:**

Phát hiện task "Thu thập + đánh giá data 3 đối thủ" trong `TIEN-DO.md` đang ở trạng thái `Đang làm`. Sau khi sinh evidence pack → đề xuất operator chuyển sang `Chờ` (chờ operator review). KHÔNG tự đánh dấu `Đã xong` (theo Phần 3 `kb-workspace-templates.md` — agent không tự xác nhận hoàn thành).

```
Em vừa cập nhật DANH-SACH-BAO-CAO. Task "Thu thập + đánh giá data 3
đối thủ" trong TIEN-DO em đề xuất chuyển sang trạng thái `Chờ` để
anh review evidence pack. Anh xác nhận chuyển trạng thái không?
```

---

## Step 4 — Cập nhật master dashboard

Sau khi 2 thay đổi áp dụng → tổng hợp `BANG-DIEU-KHIEN.md`:

```markdown
# Bảng Điều Khiển — Workspace Quản Lý Cấp Trung

Cập nhật lần cuối: 2026-05-01 14:32

## Tổng quan

- Dự án đang chạy: 1 → xem DANH-SACH-DU-AN.md
- Báo cáo gần nhất: 01-evidence-pack (2026-05-01) → xem DANH-SACH-BAO-CAO.md
- Kỹ năng đang hoạt động: 10 → xem DANH-SACH-KY-NANG.md
- Sức khỏe workspace: Tốt

## Hoạt động gần đây

| Ngày | Hoạt động | Dự án | Trạng thái |
|------|-----------|-------|------------|
| 2026-05-01 | Sinh evidence pack 3 đối thủ | phan-tich-doi-thu | Chờ review |
| ... |
```

Đánh giá sức khỏe: 0 entry "thừa" + audit gần nhất không có issue → `Tốt`.

---

## Step 5 — Validation cuối

Ghi log `Quan-Tri/AGENT-LOG.md`:

```
2026-05-01 14:32 | s-dong-bo-muc-luc | trigger: nghien-cuu-thi-truong-strategist sinh artifact
  - Cập nhật DANH-SACH-BAO-CAO: thêm 1 entry
  - Cập nhật BANG-DIEU-KHIEN: master refresh
  - Đề xuất chuyển trạng thái TIEN-DO task #1 → Chờ (đợi operator phản hồi)
  - 0 diff loại "thừa"
  - 0 diff loại "sai metadata"
```

Verify "Cập nhật lần cuối" của 2 tệp đã đổi đều `2026-05-01 14:32`.

→ Sync xong, return về orchestrator.

---

## Bài học rút ra (cho Sổ Tay Quyết Định)

**Một là chuyển trạng thái task không tự động.** Index-syncer đề xuất chuyển sang `Chờ` nhưng KHÔNG tự ghi — chờ operator xác nhận. Driver: tránh agent tự ý đánh dấu task xong (vi phạm Phần 3 quy ước phân quyền), giữ operator có quyền cuối cùng.

**Hai là sức khỏe workspace tính realtime.** Mỗi lần sync xong, master dashboard refresh đánh giá sức khỏe. Pattern này cho phép operator nhìn 1 chỗ biết trạng thái — adoption lever quan trọng cho persona quản lý cấp trung không có thời gian audit thủ công.

**Ba là log granular giúp debug drift.** Mỗi sync ghi rõ trigger source + số diff từng loại. Khi audit phát hiện "high drift", có dữ liệu cụ thể trace ngược tới skill nào ghi tệp không tuân quy tắc 5.

---

## Reference KB

- `kb-workspace-baseline.md` Phần 3.2 (vai trò dong-bo-muc-luc)
- `kb-index-format.md` Phần 3 (bảng trigger cập nhật tự động)
- `kb-workspace-templates.md` Phần 3 (quy ước phân quyền agent ↔ operator)
