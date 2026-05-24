# Mandatory Agent Anatomy Checklist (REQ-02)

Để đảm bảo Agent SI (System Instruction/Profile) đạt chuẩn MAS 4.0 và qua cửa Audit, khi sinh file Profile Agent hãy soi chiếu lại:

## Tier 2 & Tier 3 Agents (Điều Phối / Directors)
Tối thiểu 15 hạng mục (Phải có đủ 100%):
1. [ ] **Name & ID:** Định danh duy nhất (VD: `GOV-W01`).
2. [ ] **Description:** Meta ngắn gọn 1 câu dùng cho routing.
3. [ ] **Role Mission:** Tuyên ngôn sứ mệnh 2 dòng.
4. [ ] **Capabilities:** Liệt kê năng lực cốt lõi (Gạch đầu dòng).
5. [ ] **Assigned Workflows:** Nêu đích danh file `.md` flow.
6. [ ] **Assigned Meta-Skills:** Tên Skill được trỏ vào từ `.agents/skills/`.
7. [ ] **KB Connectivity (Quan trọng Nhất):** Dạy Agent móc tool `view_file` đọc `.context/domain/[Thư mục tương ứng].md`.
8. [ ] **Input Constraints:** Giới hạn nhận dữ liệu (VD: Nhận JSON, không nhận Audio).
9. [ ] **Output Constraints:** Giới hạn xả dữ liệu (VD: Max 300 từ, format Markdown).
10. [ ] **Context Overload Mngt:** Dạy LLM xử trí khi token đầy (Summarize and flush).
11. [ ] **Quality Definition (DoD):** Tiêu chuẩn hoàn thành nhiệm vụ. Nếu thiếu, làm lại.
12. [ ] **Restrictions / Boundaries (Cực Nhạy Cảm):** Nêu cái KHÔNG ĐƯỢC LÀM (VD: Không đụng Code, Không xoá Database).
13. [ ] **Failure Patterns:** Các lối mòn hay sai, dặn né đi.
14. [ ] **Handoff Rules:** Ném output qua QUEUE chờ ai duyệt?
15. [ ] **Tier Prioritization:** `> [!IMPORTANT] Override Priority: Tier 2` nằm rành rọt ở trên cùng (Dòng 3).

## Tier 4 Agents (Specialists / Công Nhân Vạch đích)
Rút gọn bằng 7 lõi trọng điểm:
1. [ ] Mission (Làm gì 1 câu chốt).
2. [ ] Mandatory Output Format (Trả ra kiểu bảng, kiểu JSON, hay Text?).
3. [ ] Input Expected (Trông chờ input gì từ cấp trên?).
4. [ ] KB Connectivity (Đọc tài liệu nào lấy sample).
5. [ ] Assigned Skills (Có Cần Không?).
6. [ ] Restriction (Dặn không làm lấn vạch).
7. [ ] Error Route (Lỗi thì báo lỗi ai?).
