# Workspace Optimization Protocols

> [!IMPORTANT]
> Tài liệu này chứa các giao thức thi công chi tiết cho 2 vòng gọt đẽo (Automation & Artisan) của skill `workspace-optimizer`. Được trích xuất từ workflow để đảm bảo chuẩn Zero-Native.

## ⚙️ ROUND 1: AUTOMATION (Chế độ Nhả Lệnh Kịch Bản)

> **Luật Lõi Vòng 1:** CẤM tuyệt đối việc LLM xuất nội dung File Markdown dài. Nhiệm vụ của bạn là sinh ra các khối Mã Python chạy lệnh HƯ HỎNG (Destructive/Structural) để dọn dẹp và đi lại dây diện rộng.

### 1A. Sửa chữa Cấu trúc Vật Lý (ROOT, 5-Zone & Antigravity Harness)
- Quét danh sách Thư mục bị thiếu từ Báo cáo Audit (Đặc biệt: `.agents/`, `artifacts/handoffs/`, `artifacts/session-reports/`, `artifacts/ki-drafts/`).
- Khởi tạo File Cột Mốc `progress.md` tại Root nếu bị bay màu.
- Xuất script Python chạy hàng loạt lệnh mkdir tạo đủ phần xương sống. Di dời `AGENTS.md` gốc vào rễ `.agents/agents.md` nếu còn nằm lạc loài.
- Chạy script thuyên chuyển tài nguyên từ lõi Root bị bẩn vào thư mục outputs/ hoặc KB/ theo luật Zero-Floating Law.

### 1B. Mass Purge (Thanh Trừng Hồn Ma)
- Dựa trên danh sách Agent V5 từ .agents/agents.md. Tìm tất cả những file Monolithic .md (Nhóm W0X, SXX cũ) đang trôi nổi trong .agents/agents/.
- Xuất lệnh Remove-Item hoặc thư viện Python os.remove trảm hàng loạt các Hồn Ma này mà không cần đọc nội dung của chúng. Mục đích: Cắt đứt nguồn gây nhiễu RAG.

### 1C. Vá Cáp Epistemic Wiring (Regex Mass Replace)
- Nếu Audit phát hiện Orphaned Routing (Cáp đứt) trong workflows/.
- Xuất khối mã Python tự động tìm và thay thế (Regex Replace) các Alias hỏng thành ID CF-XX mới trên TOÀN BỘ file workflows/*.md cùng một lúc.
- Lệnh Python này đồng thời nhét ép Header Metadata (- **👤 Owner:**) vào các file nếu thiếu.

### 1D. DNA Injection & Queue Schema Fix (V2.0 Core)
- Nếu Kính hiển vi báo lỗi `🔴 [LOCAL-FIX] Missing Auto-Boot DNA`, xuất mã Python để đọc Regex chèn ngầm lõi `## WORKER AUTO-BOOT` và `## FLUSH PROTOCOL` tại đáy file Agent SI.
- Script Python sẽ tự động dò tìm cấu trúc `QUEUE.md` và tái format bảng lưới thành V2.0 Header (Chèn cột `Deadline` và chỉnh sửa format).

### 1E. Archive Compression (Đóng băng Context Bloat)
- Khi đọc cờ `🔴 [LOCAL-FIX] Context Bloat` từ Audit, xuất shell script/Python gom gốc toàn bộ thư mục `_archive/`, `legacy/` dưới dạng text trong `.agents/`.
- Tiến hành nén chúng thành định dạng `.zip` và quăng xuống Kho `local_datawarehouse/legacy_vault/` kèm thẻ `INDEX.json`. Sau đó xóa tàn dư folder Text gốc.

---

## 🎨 ROUND 2: ARTISAN (Chế độ Gọt Đẽo Nghệ Nhân)

> **Luật Lõi Vòng 2:** 
> 1. **SLOW-MODE:** Sửa **TỪNG FILE MỘT**. Cấm batch-refactor (vd: "Viết lại 5 SIs cùng lúc").
> 2. **Anti-GIGO (ReRAG Gateway):** Đối với Agent/Skill dính cờ `[Hollow Shell]` (Rỗng tuếch) hoặc thiếu `[Domain Specificity Index]` từ Audit. Thợ Gọt Đẽo (Là Bạn) BẮT BUỘC phải dùng lệnh tìm kiếm (`search_web`) hoặc moi kho (`view_file` vào `KB/domain_architectures/`) để tìm Công thức nghiệp vụ lõi (Domain Payload). Phải nạp Payload đó vào đầu TRƯỚC KHI sửa File. Tự biên tự diễn bằng Template Cũ = Vi phạm Rule Vận hành.
> 3. **Circuit Breaker (Chống Lặp Vô Cực):** Nếu 1 File (Agent/Skill) thất bại trong nỗ lực gọt đẽo và bị Kính hiển vi đánh Rớt Lần 2 (Oscillation Loop) -> NGẮT ĐIỆN. Không cố sửa mù. Ném ngay File đó vào `Failed_Optimization_Log.md` và cắm cờ 🔴 Đợi Human Review.

### 2A. Rèn Agent SI (High-Fidelity V5 Molding)
- **Phương pháp:** Nhắm tới từng Agent bị báo lỗi CQ-08 hoặc thiếu Context.
- Tự động gọi mas5-agent-factory (hoặc viết Config YAML) với Mật độ cao (≥ 2 Steps Vận hành, Ràng buộc chéo gắt gao). Không tái sử dụng rule nông cạn.
- Nếu Bloat > 15KB: Cắt bỏ các ví dụ, tống xưng vào KB/templates và thay thành 1 câu Prompt gọi RAG.

### 2B. Gọt Giũa Skill & Cấu trúc HPRF (Antigravity CE/HE Standard)
- Đối với các bộ SKILL.md bị đánh Cờ Vàng/Đỏ: Tiêu chuẩn hóa theo nguyên lý Nén Ngữ Cảnh (Progressive Disclosure). File `SKILL.md` BẮT BUỘC phải xén mỏng dưới 50 dòng (chỉ chứa YAML Intent và Trigger).
- Toàn bộ Logic tĩnh, Quy trình, Handoff phải mổ ruột ném vào `resources/methodology.md`. CẤM NHỒI NHÉT Markdown hàng trăm dòng lềnh bềnh vào SKILL.md để bảo vệ 12K Token Budget.
- Tìm các File Luật trong .agents/quan-ly-quy-tac/: Bổ sung Khối Tag Prioriry HPRF (Tier 1, 2, 3) để chống cãi lệnh.

### 2C. Rule Enforcement (HPRF Tier Injection, Constraint logic)
- Sửa đổi mượt mà các điểm giao tiếp T3 -> T3 (Phải bẻ cong qua COORD Orchestrator). 
- **[Quy tắc Độc quyền Memory]:** Khi nhận yêu cầu sửa chữa lỗi tại `memory-contract.yml` (VD: thiếu RBAC, thiếu write_quan-ly-quy-tac, hoặc Dual Write), **BẠN KHÔNG ĐƯỢC TỰ Ý CHỈNH SỬA FILE**. Mà BẮT BUỘC gọi/ủy quyền cho Kỹ năng chuyên trách `@memory-bus-engineer` thao tác gọt đẽo để tránh LLM Hallucinated Code.
- **[Zero-Overwrite Law]:** Khi nhận yêu cầu vá Luật Quản trị (Governance/Rules), LLM CẤM được phép Xóa Đè hoặc tự viết lại toàn bộ nguyên lý L1. YÊU CẦU dùng chiến thuật Append/Insert (Bơm thêm khối Metadata/Rule mới nối tiếp sau phiên bản cũ) để chống bóp méo bản quyền.
- **[Rule Compression Protocol]:** Nếu File Luật Hành chính (Governance/Protocols) vượt quá 10KB, BẮT BUỘC chẻ nhỏ 50% dung lượng phần logic phụ sang tệp Layer-2 đặt tại `.agents/quan-ly-quy-tac/components/`. File gốc chỉ giữ lại Header Tier và chèn `> [!IMPORTANT] RAG POINTER MANDATE` yêu cầu Agent gọi Tool `view_file` tới bản Layer-2 khi cần đọc sâu.
- **[Rule Factory Red-Zone Protocol]:** Nếu Kính Hiển Vi bắt lỗi cấu trúc MECE chồng chéo hoặc Context Bloat tại nhóm `L1`, BẮT BUỘC tống cổ File L1 đó sang cho Skill chuyên trách `[s-quan-ly-quy-tac]` (Route 7). Yêu cầu Skill đó gọt ép xung và đè phần ruột quan trọng vào `L1-core-cheatsheet-fallback.md` để giải phóng RAM.

### 2D. Post-Molding Sync (Bảo vệ Răng Cưa Bầy Đàn)
- Cảnh báo: Việc nhét thêm Công thức/Matrix chuyên gia sâu vào Agent X (ở 2A) có thể khiến Định dạng Output của nó trở nên lạ lẫm với Agent Y tuyến dưới.
- Sau khi gọt xong 1 Agent/Workflow, BẮT BUỘC nhúng mắt (Scan) qua Input của Agent Downstream để đảm bảo Đầu Ra-Đầu Vào vẫn khớp ngàm (Epistemic Coupling). Hạ gục hiệu ứng Domino đứt gãy.
