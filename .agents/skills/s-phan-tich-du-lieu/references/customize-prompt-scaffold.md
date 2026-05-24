# Customize bi-report-builder — Prompt scaffold cho học viên Day 2

## Template chat với agent

Copy template, fill [...] với thông tin phòng ban anh/chị:

@bi-report-builder Tôi là BOM phòng ban [TÊN], bàn [KD/BACK/Tech].
Tôi muốn customize skill này:

1. **HOOK_INPUT_SCHEMA — data thô tôi thường nhận:**
   - Required columns: [liệt kê 5-10 cột bắt buộc]
   - Format: [Excel .xlsx / CSV / Google Sheets / sao kê PDF]
   - Sample row: [paste 1 dòng dữ liệu mẫu]
   - Date format thường gặp: [DD/MM/YYYY / YYYY-MM-DD]

2. **HOOK_METRIC_CATALOG — KPI phòng ban tôi:**
   Liệt kê 5-10 metric primary + 3-5 metric secondary, mỗi metric có:
   - Tên: [vd ROAS, CAC, MTTR, time-to-hire]
   - Công thức: [vd ROAS = revenue / spend]
   - Target: [vd 4.0x]
   - Warning threshold: [vd <3.5x]
   - Source columns: [vd revenue, spend từ schema]

3. **HOOK_PYRAMID_ANGLE — Góc nhìn chính báo cáo tôi cần:**
   [vd: "performance vs target + channel decomposition" — KD MKT
    hoặc "funnel drop-off + source effectiveness" — BACK HR
    hoặc "trend + severity mix + SLA" — Tech support]

4. **HOOK_OUTPUT_FORMAT — Format báo cáo tôi thích:**
   - Length: [ngắn 8 dòng executive / vừa 12-15 dòng / dài 25 dòng]
   - Chart inline: [có / không, nếu có loại nào: bar/line/funnel]
   - Dashboard link: [Looker Studio link / Google Sheets / không]
   - Appendix: [KPI table raw / cleaning log / source comparison]

5. **Constraint riêng phòng ban tôi:**
   [vd: không show số tuyệt đối tài chính, chỉ ratio
    hoặc: PII candidate phải redact CMND
    hoặc: compare luôn với cùng kỳ năm trước]

## Agent hành xử sau khi nhận prompt

1. Read SKILL.md bi-report-builder hiện tại
2. Edit 4 HOOK markers theo prompt
3. Bump version v1.0 → v1.1
4. Tạo entry `LICH-SU-THAY-DOI.md` (date, who, what, why)
5. Confirm: "Skill customize xong cho phòng ban [TÊN] v1.1.
   Anh/chị test với 1 báo cáo thật?"

## Standardize Test (BẮT BUỘC sau customize)

1. **Test cá nhân:** Paste 1 data thật → run full pipeline 3 step
   → check output đạt expectation
2. **Test 2 người:** 1 đồng nghiệp test cùng data → output gần
   đồng đều không? (>80% match)
3. **Test edge case:** Cố tình thêm 1 outlier + 1 missing row →
   skill có warn không?
4. PASS gate: 3 test trên đều PASS → handoff operator

## Tinh chỉnh khi test FAIL

- Output không Pyramid (conclusion ở cuối) → check Step 3 anti-pattern
- Metric sai formula → check HOOK_METRIC_CATALOG, không phải logic skill
- Output dài/ngắn quá → tinh HOOK_OUTPUT_FORMAT, không edit body
- Generic insight → tinh anti-pattern list trong HOOK (specific hơn)

KHÔNG re-customize toàn bộ — chỉ chỉnh HOOK marker liên quan.

## Version bump rule

- v1.0 → v1.X: chỉ thay HOOK markers (minor — Day 2 customize)
- v1.X → v2.0: thay đổi pipeline 3-step (vd thêm Step 4 forecasting,
  hoặc split Step 3 thành slide + dashboard) — major bump, cần
  Tech Lead review

## Anti-pattern customize

- ❌ Copy HOOK_METRIC_CATALOG từ phòng ban khác (MKT copy của HR)
- ❌ Bỏ Step 1 Cleaning để chạy nhanh (sẽ fail outlier/missing)
- ❌ Override anti-pattern list (cứng cho 12/12 BOM)
- ❌ Thêm Step mới (Step 5/6) → cần v2.0 major bump
- ❌ Disable r-sensitivity-check (PII rule là Always On)
