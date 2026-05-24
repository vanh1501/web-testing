# Hard Baseline File Checklist (Gate 4 Execution Blocker)

> **[MANDATORY — GATE 4 EXECUTION BLOCKER]** 
> Every governed workspace MUST internally possess ALL the files listed below. 
> Missing ANY singular component = automatic Gate 4 execution fail. No exceptions allowed.

## `.agents/quan-ly-quy-tac/` — Governance Core (min 7 physical files)
- [ ] `memory-contract.yml` — enforcing `security_gate.write_lock: true`
- [ ] `swarm-protocol.md` — enforcing HPRF Tier 1 definition block
- [ ] `orchestration-quan-ly-quy-tac.md` — enforcing HPRF Tier 2 definition block
- [ ] `safety-guardrails.md` — copied + tailored from core baseline
- [ ] `handoff-protocol.md` — copied + safely customized from core baseline
- [ ] `worker-roles.md` — strict agent role boundaries and forbidden scopes mapped
- [ ] `CHANGELOG.md` — cleanly initialized displaying v1.0.0 genesis entry

## `.context/` — Metadata Maps (min 4 physical files)
- [ ] `PROJECT.md` — master workspace identity verification card
- [ ] `GLOSSARY.md` — localized domain terminology glossary (targeting ≥10 complex terms)
- [ ] `SCOPE.md` — definitive in/out explicit scope definitions carrying boundary tabular matrix
- [ ] `domain/INDEX.md` — central KB manifest structurally mapped against dynamic agent routing

## Root — Operational Identity (min 3 physical files)
- [ ] `.agents/agents.md` — comprehensive MAS vertical hierarchy, strict roster, horizontal interaction matrix
- [ ] `QUALITY-LOG.md` — baseline audit tracking trail fully initialized
- [ ] `README.md` — accessible functional setup guide coupled with 5-Zone physical file index

**Self-check:** System executes `ls` terminal string targeting each path mapping. All endpoints must physically exist on disk. If ANY endpoint reads missing → formally create prior to Gate 4 clearance.
