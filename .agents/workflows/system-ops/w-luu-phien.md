---
description: "System component: w-luu-phien.md"
semantic_triggers: ['w-luu-phien']
---

﻿---
description: Auto-save trạng thái session tại các milestone ngữ nghĩa cho mindx-agent_v1.
semantic_triggers: ['checkpoint', 'save session', 'lưu trạng thái', 'chốt sổ tạm', 'mindx-agent_v1 checkpoint', 'luu phien']
version: 3.0.0
lifecycle: ACTIVE
---

# Quy trình: Checkpoint Session — mindx-agent_v1
// turbo-all

- **👤 Owner:** `[@Cố vấn AI MindX]`
- **🛠 Skill Target:** `[quan-ly-phien]`

---

## Trigger Conditions

### Milestone Triggers (Auto-fire on ANY of these):
1. **Major Artifact Delivery:** Agent finalizes a primary tracking file (e.g., `Bang-Dieu-Khien/BANG-DIEU-KHIEN.md`, báo cáo cuối cùng).
2. **Workflow Handoff/Transition:** Task transfers across Swarm tiers.
3. **Manual Command:** Human types `/w-luu-phien`.
4. **Turn Threshold:** Session exceeds 15 turns without save.

### Evaluation Logic
```
IF (Semantic Milestone reached OR Handoff initiated OR Turn > 15) → FIRE checkpoint
ELSE → Continue normally
```

> **Key Principle:** Checkpoint is a SIDE-EFFECT of existing work, not a standalone action.

---

### Execute Atomic Checkpoint

- **👤 Owner:** `[@Cố vấn AI MindX]`
- **📥 Input:** Trigger reason string + optional insight extraction payload
- **🛠 Skill Target:** `[quan-ly-phien]`
- **⚙️ Action:** Execute atomic wrapper script via Terminal (nếu có kịch bản PowerShell chuẩn):
  ```powershell
  .\.agents\skills\quan-ly-phien\scripts\trigger_checkpoint.ps1 `
    -WorkspaceRoot "managed_workspaces/mindx-agent_v1" `
    -TriggerReason "[trigger reason]" `
    -InsightPayload "[extracted insights if any]"
  ```
  Nếu chạy manual mode (FILE_MODE do kịch bản chưa có):
  1. Snapshot current `managed_workspaces/mindx-agent_v1/Bang-Dieu-Khien/TIEN-DO.md` state.
  2. Log checkpoint entry to `managed_workspaces/mindx-agent_v1/.agents/memory_bus/ledger.md`:
     `| [timestamp] | Session-Checkpoint | Cố vấn AI MindX | [trigger reason] |`
  3. Update `state.json` or `BANG-DIEU-KHIEN.md` with `last_updated` timestamp.

- **📦 Output Required:** Script console confirmation. No manual JSON parsing needed.

---

## Audit & Quality Gates

- **Gate 1 (Trigger Respect):** Agent MUST NOT hallucinate checkpoint triggers outside predefined semantic events.
- **Gate 2 (Non-blocking):** Checkpoint operations must complete transparently without disrupting primary operation.
- **Gate 3 (Path Validation):** MUST use `-WorkspaceRoot "managed_workspaces/mindx-agent_v1"` parameter for DB guards and script execution.
- **Verification:** `.agents/memory_bus/ledger.md` logs `Session-Checkpoint` entry successfully.
