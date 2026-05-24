# Operational CRUD Guardrails (Child Workspace)
> [!IMPORTANT]
> TIER 1 - PROTOCOL.

## 1. ACCESS & I/O AUTHORIZATION
- `Scope` -> Write ONLY to: `Du-An/{epic}/{project}/artifacts/`, `Du-An/`, `Quan-Tri/AGENT-LOG.md`.
- `Read-Only Zones` -> `Kho-Du-Lieu/Du-Lieu-Vao/`, `.agents/quan-ly-quy-tac/`.

## 2. I/O PATTERNS
- `Read_Before_Write` -> [REQUIRE] Check file exists before overwriting.
- `Parallel_Write` -> [DENY]. Sequential atomic writes only.

## 3. PAYLOAD & ENVIRONMENT
- `Max_File_Size` -> 15KB per file.
- `Chunking` -> If > 15KB: Split into sections with cross-references.
- `Root_Dump` -> [DENY] test/scratch files at workspace root. CẤM tạo bất kỳ file `.py`, `.ps1`, `.sh`, `.json` tạm thời ngoài sandbox.
- `Script_Sandboxing` -> [DENY] creating `.py`, `.ps1`, `.sh` scripts at workspace root `/`, `.agents/`, `.agents/skills/`, or `.agents/workflows/`. **CANONICAL SANDBOX: `tmp/`** (thư mục `tmp/` tại gốc workspace). MUST store and execute ALL ad-hoc scripts exclusively in `tmp/`. Đây là quy tắc BẤT KHẢ XÂM PHẠM — vi phạm = Audit Failure tự động.
- `Auto-Cleanup` -> Agent MUST delete or move scripts to `tmp/_archive/` after task completion. Scripts ngâm > 7 ngày trong `tmp/` bị flag STALE.

## 4. ASSET MANAGEMENT
- `Output_Categorization` -> MUST route to `Du-An/{epic}/{project}/artifacts/`.
- `Naming_Convention` -> Per `Quan-Tri/CHINH-SACH.md` Section 1.
- `Archive` -> Older project artifacts -> `Du-An/_archive/`.

## 5. OUTPUT VALIDATION
- `Pre_Write_Check` -> Validate structure before write.
- `Post_Write_Check` -> Verify index sync after write.
- `Fail_Loud` -> [DENY] silently skipping errors. Report to operator.

> [!IMPORTANT] Override Priority: High
> Bắt buộc tuân thủ cho hệ thống MAS V8.


