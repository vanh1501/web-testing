# Prompt mẫu để chạy demo giải pháp

Copy prompt này vào Project/ChatGPT sau khi đã upload workspace hoặc thêm các file nguồn cần thiết.

```text
Hãy chạy end-to-end giải pháp Angle Landing Page Builder cho dự án sau.

## Input

1. Tên angle:
[Điền tên angle]

2. Content angle:
[Paste angle muốn test]

3. Landing page mẫu:
[URL hoặc file landing-page-goc-copy.md]

4. Đối tượng khách hàng:
[Ví dụ: Ba mẹ có con từ 9–17 tuổi]

5. CTA chính:
[Ví dụ: Đăng ký 1 buổi test công nghệ miễn phí]

6. Section giữ nguyên:
- Lộ trình khóa học
- Sản phẩm đầu ra
- Học viên tiêu biểu
- Phụ huynh nói gì về MindX
- Báo chí nói gì về MindX
- Q&A nếu có
- Form đăng ký gốc/tracking
- Đối tác / proof lớn nếu chưa duyệt

7. USP sản phẩm muốn ưu tiên:
[Liệt kê USP nếu có. Nếu không có, hãy lấy từ nguồn dự án.]

8. Yêu cầu output:
- angle-brief.md
- claim-check.md
- landing-page-copy.md
- message-match-check.md
- landing-page.html
- html-qa-checklist.md
- github-handoff.md

## Yêu cầu vận hành

- Không dùng claim cần duyệt nếu chưa flag.
- CTA phải đúng input.
- Hero có form + CTA.
- Problem/Why/USP phải show, don’t tell.
- Why không dùng educate chung chung.
- USP phải map với problem đã nêu.
- Không publish thật, chỉ tạo GitHub handoff.
```
```

## Prompt mẫu với angle đã test

```text
Hãy chạy end-to-end giải pháp Angle Landing Page Builder.

## Input

1. Tên angle:
3 tháng hè — sản phẩm công nghệ

2. Content angle:
Cùng là 3 tháng hè, có bạn thì chỉ nhớ mình đã xem gì trên điện thoại, có bạn lại nhớ cảm giác lần đầu tự tạo ra một sản phẩm công nghệ của riêng mình như thế nào.

3. Landing page mẫu:
Dùng nguồn `nguon-du-an/landing-page-mau/landing-page-goc-copy.md`.

4. Đối tượng khách hàng:
Ba mẹ có con từ 9–17 tuổi.

5. CTA chính:
Đăng ký 1 buổi test công nghệ miễn phí

6. Section giữ nguyên:
- Lộ trình khóa học
- Học viên tiêu biểu
- Q&A
- Form đăng ký gốc/tracking
- Đối tác
- Về MindX

7. USP sản phẩm muốn ưu tiên:
- Học qua dự án thật
- Lộ trình theo độ tuổi
- Mentor hướng dẫn
- Dùng AI đúng cách
- Buổi test công nghệ miễn phí

8. Output mong muốn:
Tạo đủ bộ file output và file HTML landing page.

## Yêu cầu:
- Không tự thêm số học viên, số cơ sở, đối tác, học bổng hoặc mức lương nếu chưa duyệt.
- Nếu section giữ nguyên chưa có HTML gốc, chỉ dựng placeholder và ghi rõ cần thay trước publish.
- Tạo GitHub handoff nhưng không claim đã publish.
```
```
