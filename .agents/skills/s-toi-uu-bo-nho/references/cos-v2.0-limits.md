# COS v2.0 Absolute Boundary Constraints

Tài liệu này xác định các giới hạn Token Vận hành Cứng theo tiêu chuẩn Tier của **Context Operating System v2.0**. Hệ thống Context Surgeon phải kiểm toán dựa trên các đường cơ sở (baselines) sau:

## Ngưỡng Phì Đại Tệp Tin (File Bloat Thresholds)
1. **Agent SI Tối Đa**: $15 \text{ KB}$ (Khoảng $3.5K-4K \text{ Tokens}$).
2. **Skill Payload Tối Đa**: $20 \text{ KB}$.
3. **Workflow Length Tối Đa**: $10 \text{ KB}$ (Cổ xúy tinh giản theo Zero-Native Law).

Bất kỳ giá trị nào chạm ngưỡng Max Limit trên đều phải bị đánh cờ `CRITICAL_BLOAT` và tiến hành phẫu thuật bóc tách ngay lập tức.

## Ngân Sách Phân Cấp (Tiered Budget Engine)
Khi đánh giá toàn bộ Hệ Hành Trang (Backpack) của một Agent, tổng số Tokens mang vác không được phép đâm thủng hạn mức ngân sách:

- **Lean Budget (Cấp 1):** $\leq 8,000 \text{ Tokens}$. An toàn tuyệt đối, hiệu năng suy nghĩ > 95%.
- **Standard Budget (Cấp 2):** $12,000 \text{ Tokens}$ (Hard Max cho mọi quy trình Tự Động). 
- **Rich Budget (Cấp 3):** $\leq 16,000 \text{ Tokens}$. Chỉ dành cho Quá trình Bootstrapping, Yêu cầu Human Request. Nguy cơ Lost in the Middle ~ 25%.

> [!CAUTION] Hệ quả sập đổ (The Cascade Collapse)
> Việc thả rông Payload Skill nặng đến $107\text{ KB}$ (như trường hợp Payload của `ws-course-factory`) sẽ lập tức bóp nát khả năng ghi nhớ ngắn hạn của LLM, gây hiện tượng Ảo Giác Quyết Định (Hallucinated Assertions).
