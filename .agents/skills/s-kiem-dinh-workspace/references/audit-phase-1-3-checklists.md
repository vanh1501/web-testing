# Audit Workspace — Phase 1-3 Checklists

> **Purpose:** Reference checklists for executing Phase 1 (Value Stream), Phase 2 (Skills), and Phase 3 (Phantom Agents).

## Phase 1: Workflow Quality & Routing Logic (VALUE STREAM)

**1a. CQS Compliance & Zero-Native Law:**
- Every workflow in `.agents/workflows/`:
  - **Size Gate:** < 0.8KB = 🔴 Skeleton. > 15KB = 🟡 Bloat Warning (unless justified).
  - YAML frontmatter with `description:` ≥ 10 words? 🔴 if missing.
  - **Metadata Gate:** MUST have explicit `- **👤 Owner:**` and `- **🛠 Skill Target:**`. 🔴 [LOCAL-FIX] Auto-Fail if missing.
  - **Zero-Native Law:** The `Skill Target` MUST NOT be `[Native]`. 🔴 [SYSTEMIC-HALT] Auto-Fail if explicitly defined as native.
  - **Execution Constraint:** Workflows MUST NOT contain >10 lines of step-by-step domain logic. 🔴 [SYSTEMIC-HALT] Zero-Native Violation if execution logic is embedded.

**1b. Binding Density & Call Graph (Epistemic Lock):**
- Every workflow SHOULD be backlinked from ≥ 1 Agent SI OR be classified as `<!-- [WORKFLOW TYPE: human-trigger] -->`. 🟡 Warning if orphaned.
- Identify **orphan workflows**: 0 internal refs AND 0 agent backlinks AND NOT classified as human-trigger. 🟡 Warning.
- **Action Target Mandate:** Workflows MUST explicitly specify the executing Agent ID (e.g., `[AMY-WXX]`) in all action steps. Ambiguous routing = 🔴 [SYSTEMIC-HALT].
- **[ORPHANED ROUTING MANDATE]:** The Audit LLM MUST cross-verify every Agent ID executed inside Workflows against the authoritative roster in `.agents/agents.md`. If a workflow invokes an obsolete, disconnected, or ghost Agent ID, emit: 🔴 [SYSTEMIC-HALT] Orphaned Routing!.
- **[CIRCULAR DEPENDENCY DEADLOCK]:** Phát hiện vòng lặp = 🔴 [SYSTEMIC-HALT] Circular Deadlock!.

## Phase 2: Skill Coverage & Rigor (ARSENAL)

**2a. Skill Supply/Demand Ratio:**
- Ratio = `domain_skills` / `productive_agents`
- Ratio < 0.3 → 🔴 [SYSTEMIC-HALT] Auto-Fail.
- Ratio < 0.5 → 🟡 Warning.

**2b. Skill Quality & Ghost Check:**
- Every skill demanded by a workflow MUST exist. 🔴 [LOCAL-FIX] if missing.
- **[MANDATORY GHOST CHECK]:** Cross-reference every folder name inside `.agents/skills/` against all Agent SIs and Workflows. If unwired: 🔴 [LOCAL-FIX].
- Skills are strictly for **tool execution**. They MUST NOT contain `## Voice` or `## Persona`. 🔴 [LOCAL-FIX] if polluted.
- **[EPISTEMIC WIRING LOCK]:** Agent SIs MUST explicitly define `[[Linked Skills]]: [...]`. Calling a skill outside of this list is a Role Breach. 🔴 [SYSTEMIC-HALT].

**2c. Domain Expert Payload (Rigor) & Anti-Hollow Shell:**
- Evaluate Canonical Trifecta Check (missing frameworks -> 🔴 [LOCAL-FIX]).
- Evaluate Quantification Test (missing formulas/matrices -> 🔴 [LOCAL-FIX]).
- **[GENERIC TEMPLATE TRAP]:** Quét mật độ lời khuyên sáo rỗng > 20% → 🔴 [SYSTEMIC-HALT] Hollow Skill.
- **[DOMAIN SPECIFICITY INDEX - DSI]:** Nếu không tìm ra nổi 1 thực thể chuyên biệt nào (ma trận, công thức lõi) → 🔴 [SYSTEMIC-HALT] Generic Template.

**2d. Deep Content & 4-Tier Structural Analysis:**
1. **Skill Size Gate (Pre-Check):**
   - SKILL.md < 1 KB → 🔴 [SYSTEMIC-HALT] Empty shell. Rebuild via skill-writer Route 3.
   - SKILL.md < 10 KB → 🔴 [LOCAL-FIX] Under-developed. Needs enrichment via skill-writer Route 3 (ADDIE).
   - SKILL.md ≥ 10 KB → PASS. Proceed to 4-Tier Compliance Audit.
2. **Run 4-Tier Compliance Audit** (10-point scoring):
   - Physical Structure (4 pts): `references/`, `assets/`, `evals/`, `scripts/` existence.
   - Body Compliance (4 pts): `## RESOURCES`, `## QA`, `## WHEN TO CLARIFY`, `## OUTPUT FORMAT`.
   - Content Purity (2 pts): Line count ≤ 50.
   - **A2A Prompt Injection Resilience:** Rào cản Input Validation.
3. **If COMPLIANCE_SCORE < 7**: Execute Extractability Analysis.
4. **Classify each skill**: FULL_COMPLIANT, AUTO_FIXABLE, MANUAL_REVIEW, SKELETON.
5. **Evals Quality Gate**: Generic test cases → 🟡 WARNING.

## Phase 3: Phantom Agent Architecture Check (WORKERS)

**3a. Context Efficiency & Phantom Agent Compliance:**
- Ensure `.agents/agents/` DOES NOT EXIST (Phantom model). If found, emit 🔴 [SYSTEMIC-HALT] V5 Folder Bloat Detected.
- Verify `L1-swarm-registry.md` exists and explicitly lists ID, Tier, Role, Linked Skills.

**3b. CQS Validation & Anti-Hollow Shell:**
- Validate against 7-Section Check at the Registry level.
- Check `Linked Skills`. Missing = 🔴 [LOCAL-FIX].
- **[GROUNDING TEST]:** So sánh chéo role với hệ thống `KB/`.

**3c. Cấy Gen V2.0 (Auto-Boot & Flush):**
- Quy tắc Auto-Boot/Flush phải có trong `L1-swarm-registry.md`. Nếu thiếu = 🔴 [LOCAL-FIX] Missing Auto-Boot DNA.
