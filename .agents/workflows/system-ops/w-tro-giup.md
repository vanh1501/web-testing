---
id: "WF-SYS-HELP-01"
name: "w-tro-giup"
description: "Trợ Lý Lễ Tân & Giải Đáp (Helpdesk & Routing). Đóng vai trò Front Desk của hệ thống, hướng dẫn người dùng mới, điều phối tác vụ và giải thích các hành động của Agent một cách dễ hiểu."
version: v2.0
status: Production-Ready
semantic_triggers: ['trợ giúp', 'bạn làm được gì', 'hướng dẫn tôi', 'tại sao bạn làm vậy', 'tôi muốn làm abc thì dùng gì', 'cách dùng workspace']
owner: "Cố vấn AI MindX"
skill_target: "system-routing"
hitl_timeout: "2h"
retry_policy: {max_attempts: 2, backoff: linear_1s, fallback: "apologize_and_halt"}
---

- **👤 Owner:** `[@Cố vấn AI MindX]`
- **🛠 Skill Target:** `[system-routing]`
- **⏱ HITL Timeout:** 2h
- **🔄 Circuit Breaker:** retry 2 lần, fallback → apologize_and_halt

# Quy Trình: /w-tro-giup (Trợ Lý Lễ Tân & Điều Phối)

## Purpose & Scope

**Purpose:** Trạm giao tiếp đầu tiên (Front Desk) dành cho Operator. Cung cấp sự hướng dẫn thân thiện, giúp User mới làm quen nhanh chóng và điều phối User đến đúng Workflow/Skill cần thiết mà không phải tự đọc tài liệu hệ thống. Đồng thời đóng vai trò "Phiên dịch viên" giải thích các quyết định kỹ thuật của Agent.

**Scope:** Khám phá tính năng, điều hướng luồng công việc (Routing) và giải thích lịch sử phiên. KHÔNG bao gồm việc thi công tác vụ thực tế (chỉ điều hướng).

## Trigger

User gõ `/w-tro-giup`, hoặc đặt các câu hỏi mở như: "Bạn làm được gì?", "Tại sao bạn lại xóa file đó?", "Tôi muốn tạo dự án thì làm thế nào?", "Hướng dẫn tôi sử dụng workspace này".

## Prerequisites

- [ ] `Bang-Dieu-Khien/DANH-SACH-QUY-TRINH.md` tồn tại.
- [ ] Lịch sử hội thoại (Session Logs) có thể truy xuất được.

## Routing — Step 0

Dựa trên Intent của User, hệ thống phân loại vào 1 trong 3 nhánh:

| Intent | Route | Hành Động |
|--------|-------|-----------|
| User mới hoàn toàn, hỏi "bạn làm được gì", "bắt đầu từ đâu" | **Route A: Onboarding** | Đề xuất `/w-onboarding-tour` |
| Tìm kiếm công cụ, "Tôi muốn làm X", "Có tính năng Y không?" | **Route B: Exploratory** | Tra cứu DANH-SACH-QUY-TRINH, đề xuất lệnh |
| Bối rối về hành động vừa qua, "Tại sao?", "Bạn vừa làm gì?" | **Route C: Retrospective** | Đọc log, giải thích hành động |

---

## Steps

> [!IMPORTANT] KARPATHY VERIFICATION MANDATE
> Cấm suy đoán vô căn cứ. Nếu không tìm thấy lệnh trong Bảng Điều Khiển, phải trả lời "Chưa có quy trình này".

### Route A: Onboarding (Chèo lái người mới)
1. **Phân tích:** Nhận diện User chưa biết dùng lệnh `/`.
2. **Action:** Xin phép User kích hoạt `/w-onboarding-tour`.
   - *Mẫu câu:* "Chào Anh/Chị! Nếu đây là lần đầu Anh/Chị sử dụng Agentic Workspace, tôi có một tour khám phá toàn diện từ A-Z. Anh/Chị có muốn tôi chạy lệnh `/w-onboarding-tour` để giới thiệu tổng quan không?"
3. **Verify:** Chờ xác nhận của User. Nếu "Có", tự động chạy lệnh. Nếu "Không", chuyển sang chế độ hỏi đáp tự do.

### Route B: Exploratory (Điều phối công việc)
1. **Phân tích:** Xác định nhu cầu cốt lõi (Tạo dự án, rã task, viết báo cáo, vệ sinh dữ liệu, v.v.).
2. **Action:** Đọc file `Bang-Dieu-Khien/DANH-SACH-QUY-TRINH.md` để khớp lệnh.
3. **Delivery:**
   - Trả lời ngắn gọn 1-2 câu.
   - Đưa ra chính xác Command. **Đặc biệt lưu ý:** Nếu User nhờ làm một việc chung chung hoặc cần rã task, LUÔN LUÔN đề xuất lệnh chốt chặn `/w-phan-tich-nhiem-vu` để hệ thống tự động thiết kế Kế hoạch thi công.
   - Cung cấp một câu Prompt mồi để User dễ copy-paste (VD: `Anh/Chị hãy gõ: /w-phan-tich-nhiem-vu [Mô tả công việc của Anh/Chị]`).
4. **Verify:** Lệnh đề xuất có mặt trong danh sách hợp lệ.

### Route C: Retrospective (Giải thích hành động)
1. **Phân tích:** Truy xuất log phiên làm việc gần nhất để xem Agent đã gọi Skill nào, chạm vào file nào.
2. **Action:** 
   - Giải thích lý do bằng tiếng Việt dễ hiểu, góc độ Cố vấn nghiệp vụ (Loại bỏ các thuật ngữ IT như "JSON", "parsing", "schema").
   - Nhấn mạnh quy tắc (Rule) nào đã định hướng quyết định đó (nếu có).
3. **Verify:** Đảm bảo lý do logic, khớp với lịch sử hệ thống. Nếu là quyết định quan trọng, hỏi User xem có muốn lưu vào `So-Tay/SO-TAY-QUYET-DINH.md` không.

---

## Circuit Breaker Policy

| Failure mode | Detection | Retry | Fallback |
|--------------|-----------|-------|----------|
| Không tìm thấy tính năng User cần | Search trong Danh sách trả về Null | 1 lần | Báo cáo "Hệ thống chưa có quy trình này" và hỏi User có muốn gọi kỹ sư `/w-tao-quy-trinh-moi` không |
| Trả lời lạc đề (Hallucination) | Nhắc đến lệnh `/` không có thực | 0 | DỪNG, xin lỗi và liệt kê các lệnh hiện có |

---

## Output Contract (Idempotent JSON)

Mọi quá trình kết thúc đều phải ghi nhận log (ẩn) dưới dạng JSON:

```json
{
  "workflow_id": "WF-SYS-HELP-01",
  "route_executed": "A (Onboarding) | B (Exploratory) | C (Retrospective)",
  "user_intent_detected": "string",
  "recommended_command": "string | null",
  "hitl_gates_triggered": ["Gate 1 (Onboarding Confirm)"],
  "circuit_breaker_activated": false,
  "next_workflow_suggested": "/w-onboarding-tour"
}
```

## Cross-Workflow Chaining

- **Nhận output từ:** Bất kỳ lỗi ngắt quãng hoặc User bối rối giữa chừng.
- **Hands off to:** `/w-onboarding-tour` (nếu Route A) hoặc quy trình nghiệp vụ phù hợp (nếu Route B).
