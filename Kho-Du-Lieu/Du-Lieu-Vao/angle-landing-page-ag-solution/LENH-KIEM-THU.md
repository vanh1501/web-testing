# Lệnh kiểm thử mẫu

## Happy path
```text
/tao-landing-page-theo-angle dau-vao/input-demo-3-thang-he.md
```

## Test thiếu CTA
```text
Chạy workflow nhưng input không có CTA chính.
```
Expected: dừng ở Input Gate.

## Test claim rủi ro
```text
Thêm claim: đảm bảo con có sản phẩm hoàn chỉnh sau khóa học.
```
Expected: dừng ở Claim Gate.

## Test CTA sai
```text
Input CTA là test miễn phí nhưng HTML dùng Nhận ưu đãi ngay.
```
Expected: HTML QA fail.
