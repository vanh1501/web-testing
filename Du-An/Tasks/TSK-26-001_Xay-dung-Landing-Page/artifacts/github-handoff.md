# Tài Liệu Bàn Giao Mã Nguồn GitHub (GitHub Handoff) — TSK-26-001

**Mã Tác vụ:** TSK-26-001  
**Ngày thực hiện:** 2026-05-23  
**Tập tin bàn giao:** `landing-page.html`  
**Nhà phát triển:** Trợ lý Kỹ thuật `00-tao-github-handoff` (PRO-W03)  

Tài liệu này hướng dẫn chi tiết các bước đưa mã nguồn trang đích lên kho lưu trữ GitHub và thiết lập đẩy tự động lên Vercel để trang web hoạt động trực tuyến chỉ trong 3 phút.

---

## 📦 1. Thông Tin Đóng Gói Mã Nguồn (Deployment Specifications)

* **Tên nhánh đề xuất (Branch Name):** `feat/game-angle-landing-page-tsk-26-001`
* **Commit Message mẫu:** `feat(marketing): add mobile-optimized dark mode landing page for game creative angle`
* **Tệp tin bàn giao chính:** [landing-page.html](file:///Users/vanh1501/Downloads/mindx-agent_v1%20%282%29/Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page.html)

---

## 💻 2. Gói Lệnh Git Mẫu (Git Terminal Commands)

Bạn chỉ cần mở Terminal (cửa sổ dòng lệnh) của máy tính, di chuyển vào thư mục dự án và chạy các lệnh đơn giản sau:

```bash
# 1. Tạo một nhánh làm việc mới từ nhánh chính (main)
git checkout -b feat/game-angle-landing-page-tsk-26-001

# 2. Thêm file HTML trang đích vào danh sách chuẩn bị đẩy
git add "Du-An/Tasks/TSK-26-001_Xay-dung-Landing-Page/artifacts/landing-page.html"

# 3. Ghi nhận thay đổi với thông điệp rõ ràng
git commit -m "feat(marketing): add mobile-optimized dark mode landing page for game creative angle"

# 4. Đẩy nhánh này lên kho lưu trữ GitHub của bạn
git push origin feat/game-angle-landing-page-tsk-26-001
```

---

## 🚀 3. Hướng dẫn Triển khai Live lên Vercel cực nhanh

Sau khi đã đẩy mã nguồn lên GitHub thành công, bạn làm theo 3 bước cực kỳ đơn giản sau để đưa trang đích chạy thực tế:

1. **Đăng nhập Vercel:** Truy cập [Vercel.com](https://vercel.com) và đăng nhập bằng tài khoản GitHub của bạn.
2. **Tạo Project mới:** Click vào nút **"Add New"** ➔ chọn **"Project"** ➔ Chọn kho lưu trữ GitHub của dự án này.
3. **Thiết lập & Deploy:**
   * Tại mục **Root Directory**, bạn có thể chọn thư mục chứa file HTML hoặc để mặc định.
   * Click nút **"Deploy"**. Vercel sẽ tự động phân tích và cấp cho bạn một đường dẫn (URL) trực tuyến miễn phí (dạng `project-name.vercel.app`) chỉ sau 10 giây!

---

## 📝 4. Bản Mô Tả Pull Request (PR Description Template)

Khi gửi yêu cầu gộp nhánh (Pull Request) trên GitHub, bạn hãy sử dụng mẫu mô tả chuyên nghiệp sau để đội kỹ thuật duyệt nhanh:

```markdown
## Yêu Cầu Thay Đổi: Bổ sung Landing Page theo Góc Tiếp Cận "Biến Đam Mê Game thành Lập Trình"

### 🎯 Mục tiêu:
- Tăng trưởng tỷ lệ chuyển đổi (CR) nhóm phụ huynh có con thích chơi game (9-17 tuổi) bằng cách định hướng tích cực sở thích của trẻ sang tư duy lập trình khoa học.
- Đã được kiểm định chất lượng hiển thị trên thiết bị di động (Mobile-First) và rà soát an toàn từ ngữ quảng cáo (no claims risk).

### 🛠️ Các thay đổi chính:
- Bổ sung file `landing-page.html` chứa mã nguồn tối ưu chuẩn Sleek Dark Mode cao cấp.
- Đầy đủ hệ thống form đăng ký test năng lực và định hướng công nghệ miễn phí.
- Hiển thị lộ trình học trực quan theo độ tuổi của trẻ.

### 🧪 Trạng thái kiểm định kỹ thuật (QA):
- [x] Đạt chuẩn SEO Meta & cấu trúc ngữ nghĩa HTML5.
- [x] Tối ưu hóa hiển thị responsive hoàn hảo trên di động.
- [x] Đã loại bỏ các tuyên bố quảng cáo quá đà (claim check passed).
```
