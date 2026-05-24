# Context Splice Pattern Mechanics

**Giai đoạn:** Áp dụng khi Agent SI hoặc Skill Payload vượt quá 15KB (Token Bloat).
**Mục tiêu:** Di chuyển kiến thức thô cồng kềnh (Raw Domain Knowledge) ra khỏi thân Agent (Inline) và chuyển thành mô hình Gọi Cục Bộ (RAG Pointer).

## Kỹ Thuật Bóc Tách (Factorization)

Khi đối mặt với File $>15KB$:
1. Phân loại khối nào là **Logic Động** (If X then Y) $\rightarrow$ Giữ nguyên ở thân gốc.
2. Khối nào là **Dữ liệu Tĩnh** (Templates, Frameworks, Tables, Reference Text) $\rightarrow$ Tuyệt đối phải cắt.

> [!IMPORTANT] NGUYÊN TẮC BẢO TOÀN KHÔNG PHÁ HỦY (NON-DESTRUCTIVE SPLICE)
> TRƯỚC KHI tiến hành gọt, cắt hay tóm tắt một file lõi (như README, Rules, Pipeline), BẮT BUỘC phải Dump/Copy chính xác 100% nguyên bản toàn bộ file đó ra một file lưu trữ tĩnh (Ví dụ: `KB/README_Legacy_Full_V4.md`). 
> Tuyệt đối KHÔNG được nén hay tóm tắt dữ liệu trong quá trình tách ghép mà không có bản lưu trữ gốc. Điều này đảm bảo 0% mất mát Tri thức lịch sử (Institutional Knowledge) của Workspace.

## Phẫu Thuật RAG (Retrieval Augmented Generation Pointer)

**BẢN CŨ LỖI (BÉO PHÌ):**
```markdown
# ## Sứ Mệnh
# Bạn là Chuyên gia Khảo sát.
# 
# ## Khung khảo sát (Payload nặng 20KB)
# [Toàn bộ nội dung thô 20KB...]
```

**BẢN ĐƯỢC PHẪU THUẬT RAG (TỐI ƯU COS):**
```markdown
# ## Sứ Mệnh
# Bạn là Chuyên gia Khảo sát.
# 
# ## Khung Khảo Sát
# BẮT BUỘC SỬ DỤNG TOOL `view_file` ĐỂ ĐỌC TEMPLATE CHI TIẾT DƯỚI ĐÂY:
# [LOAD-KNOWLEDGE: file:///absolute/path/to/KB/domain/khung_khao_sat.md]
```
> [!CAUTION] Cấu trúc Tiêm (Pointer):
> Luôn sử dụng từ khóa `BẮT BUỘC SỬ DỤNG TOOL view_file` ngay liền kề với đường dẫn để ép GPT/LLM Models không thể đoán bừa (hallucinate) nội dung. Cánh cổng Token sẽ không mở cho tới khi nó thực thụ kích hoạt Tool.
