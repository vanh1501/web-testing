# Component Builder — Troubleshooting & Diagnostics

Bảng chẩn đoán lỗi chuyên biệt dành cho quá trình Build Component (Phase 3) của System Architecture.

## Phân Tích Dấu Hiệu (Diagnostics)

| Root Issue | Diagnostic Cause | Suggested Remediation Fix |
|-------|-------|-----|
| Systemic Architecture mapped too complex | Destructive Scope creep propagating from Phase 1 Intake | Force Revisit A-ESOAR analytical filter, aggressively reduce active R-steps |
| Component Builder agent heavily utilizing unpopulated placeholder tags | Structurally insufficient or vague Intake brief | Mandate return to S01 parameters requesting increased situational detail resolution |
| Functional Golden tests critically fail during evaluation | Inherited execution quan-ly-quy-tac structurally conflict or are completely missing | Exhaustively review all CLEAR baseline scores, force fix universally lowest-scoring quan-ly-quy-tac hierarchy first |
| Target Memory Bus contract logically missing `security_gate` enforcement | Flawed or careless structural Template stripping extraction | Command immediate re-copy injection mechanism from original master baseline template parameters |
| Agent KB paths reference `.context/knowledge/` | Build sequence created agents before KB existed (legacy v1.x bug) | Run binding test (Step 14), bulk-replace all `.context/knowledge/` → `KB/domain/` |
| Agent references Skill ID not in `00_SKILL_INDEX.md` | Skill naming mismatch between agent and registry | Canonicalize: use exact folder name from `.agents/skills/` in both Index and Agent SI |
| Duplicate `## KB Connectivity` sections in Agent SI | Builder ran in multiple passes without merge | Deduplicate: keep ONLY the section with verified `KB/domain/` paths |
