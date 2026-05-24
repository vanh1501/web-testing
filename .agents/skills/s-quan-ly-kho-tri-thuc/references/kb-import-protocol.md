# references/kb-import-protocol.md — BULK IMPORT & CONVERT Protocol

## Purpose
Detailed protocol for Route 1 (BULK IMPORT). Dùng khi tiếp nhận các tài liệu legacy (DOCX, PDF, Confluence Export) cần được bóc tách và chuyển đổi thành Markdown thô để chuẩn bị cho quá trình ép chuẩn Diátaxis (Route 2).

## Quy trình Handoff (DIP Pipeline)

Route 1 đóng vai trò như một **Trạm Trung Chuyển (Dispatcher)**. Bạn KHÔNG tự tay bóc tách PDF hoặc DOCX phức tạp, mà ủy quyền cho kỹ năng chuyên trách `doc-formatting` (Document-to-MD Intelligence Pipeline).

### Phase 1 — Phân tích nguồn (Triage)
1. Xác định định dạng file nguồn (PDF, DOCX, TXT, HTML, Confluence Export).
2. Xác định dung lượng và độ phức tạp (Có nhiều bảng biểu không? Có sơ đồ kiến trúc không?).
3. Nếu file quá lớn (> 20 trang) hoặc chứa nội dung của nhiều hệ thống khác nhau, đề xuất người dùng cắt nhỏ file (split) trước khi import.

### Phase 2 — Delegate cho `doc-formatting`
1. Gọi `doc-formatting` (DIP Pipeline) để xử lý file.
2. Cung cấp chỉ thị rõ ràng cho `doc-formatting`:
   - "Chỉ bóc tách text, bảng biểu, và code block."
   - "Giữ nguyên cấu trúc Heading gốc."
   - "Không tự ý format hay rút gọn nội dung, cần giữ độ trung thực (fidelity) cao nhất."

### Phase 3 — Tiếp nhận & Làm sạch Markdown thô (Pre-processing)
Sau khi `doc-formatting` trả về Markdown thô, thực hiện các bước dọn dẹp cơ bản trước khi chuyển sang Route 2:
1. **Remove Artifacts:** Xóa bỏ header/footer, số trang thừa bị dính vào trong quá trình OCR/Export.
2. **Fix Encoding:** Xử lý các ký tự Unicode lỗi, khoảng trắng thừa.
3. **Heading Normalize:** Đảm bảo sử dụng `#`, `##`, `###` thay vì bôi đậm `**Text**`.
4. **Code Block Sanity Check:** Đảm bảo các đoạn code/JSON/XML được bọc trong ` ``` ` đúng cách.

---

## Các Trường hợp Đặc biệt (Edge Cases)

### 1. File chứa Sơ đồ (Architecture Diagrams / Flowcharts)
- Markdown không thể hiển thị ảnh thô nhúng bên trong Word.
- **Hành động:** Đặt Placeholder `[TODO: Insert Diagram - Tên sơ đồ]` tại vị trí tương ứng. Yêu cầu user cung cấp file ảnh riêng lẻ hoặc source Mermaid/PlantUML nếu có.

### 2. File Confluence Export (HTML / ZIP)
- Confluence thường sinh ra các Macro thừa (Jira ticket links, Table of Contents macro).
- **Hành động:** Xóa các macro tự động của Confluence (`{toc}`, `{children}`). Chuyển đổi Jira link thành format Markdown link tĩnh.

### 3. File Excel / Bảng Biểu Phức Tạp
- Các bảng ma trận (matrix) hoặc bảng gộp ô (merged cells) sẽ bị vỡ khi chuyển sang Markdown table.
- **Hành động:** Chuyển bảng phức tạp thành danh sách (List) hoặc yêu cầu giữ nguyên file Excel làm đính kèm thay vì cố ép thành Markdown.

---

## Output Validation (Trước khi sang Route 2)
Checklist hoàn thành Route 1:
- [ ] Dữ liệu đã là text thuần (Markdown).
- [ ] Không còn rác OCR (số trang, header lặp).
- [ ] Bảng biểu (nếu có) không bị vỡ cột.
- [ ] Code block hiển thị rõ ràng.
- [ ] Các ảnh/sơ đồ bị thiếu đã được đánh dấu `[TODO: Insert ...]`.

**Tiếp theo:** Sau khi file đạt chuẩn Markdown thô, tự động trigger **Route 2: STANDARDIZE & CLASSIFY** để ép vào khung Diátaxis và YAML Frontmatter.
