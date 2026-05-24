# Research — Evaluation Test Cases

## TC-01: Happy Path — Market Research
**Prompt**: "Nghiên cứu thị trường e-commerce VN 2026, quy mô + xu hướng + top players"
**Expected Pipeline**: RECEIVE → SCOPE (decompose 3 sub-Qs) → SOURCE → COLLECT → EVALUATE → SYNTHESIZE → DELIVER
**Pass Criteria**:
- [x] Show decomposition: "Tôi sẽ tìm: (1) Market size, (2) Growth rate, (3) Top 5 players"
- [x] ≥2 Grade B+ sources per finding
- [x] Confidence levels stated (High/Medium/Low)
- [x] Gaps section present
- [x] Sources listed with grades
- [x] Pyramid structure (answer first)
**Fail**: Single source conclusions, no confidence, no gaps

## TC-02: Happy Path — Competitor Quick Scan
**Prompt**: "So sánh nhanh Notion vs Monday vs ClickUp cho team 10 người"
**Expected**: COMPETITIVE pattern → comparison matrix → recommendation
**Pass**: Matrix (features × options), scoring, recommendation with trade-offs, source grades
**Fail**: Just lists features without scoring, no recommendation, or strong bias without evidence

## TC-03: Edge — Conflicting Sources
**Prompt**: "Thị trường AI Việt Nam đang bao nhiêu tỷ USD?"
**Expected**: Tìm nhiều sources → nếu conflict → report CẢ HAI figures → explain difference
**Pass**: "Theo [Source A, Grade A]: $X tỷ. Theo [Source B, Grade B]: $Y tỷ. Khác biệt do [methodology]. Estimate range: $X-Y tỷ (Medium confidence)."
**Fail**: Pick one number arbitrarily, or average without explanation

## TC-04: Edge — No Good Data Available
**Prompt**: "Market size ngành coaching Việt Nam"
**Expected**: Search → not enough Grade A-B data → flag clearly
**Pass**: "Không có report đáng tin cậy về market size coaching VN. Proxy approach: [estimate from adjacent data]. Confidence: LOW. Recommend: primary nghien-cuu-thi-truong (survey) needed."
**Fail**: Makes up number, or refuses to help at all

## TC-05: Violation — Opinion Presented as Fact
**Prompt**: "AI sẽ thay thế 50% việc làm trong 5 năm tới — đúng không?"
**Expected**: Trace claim → evaluate → separate fact from opinion
**Pass**: "Claim này xuất phát từ [source, year]. Methodology: [description]. Counter-evidence: [other studies]. Verdict: Đây là prediction (not fact), confidence MEDIUM, range [X-Y%] tùy ngành."
**Fail**: Simply confirms or denies without evidence, presents prediction as fact

## TC-06: Happy Path — Fact-Check
**Prompt**: "'73% doanh nghiệp VN đã dùng AI năm 2025' — nguồn nào? Đúng không?"
**Expected**: FACT-CHECK pattern → trace original source → evaluate methodology → verdict
**Pass**: Identifies original source + methodology + sample size + limitations + verdict (Confirmed/Partially/Unconfirmed) + confidence
**Fail**: Just Googles the number and repeats it
