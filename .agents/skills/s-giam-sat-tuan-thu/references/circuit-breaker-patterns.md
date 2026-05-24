# Circuit Breaker Patterns (Phase 6.5)

This document outlines the 3-state machine spec for Circuit Breakers in a MAS Workspace.
When auditing `giam-sat-tuan-thu` Gate 5, verify that workflows/skills have explicit handling for these states.

## The 3-State Spec

1. **CLOSED (Normal Operation)**
   - The system executes tasks normally.
   - Failure thresholds are monitored.

2. **OPEN (Halt Operation)**
   - Triggered when cascade failures > N times.
   - Must define a timeout (e.g., pause execution for X minutes or require human intervention).
   - *Requirement:* Workflows must explicitly state what happens when failures exceed the threshold.

3. **HALF-OPEN (Probe Retry)**
   - After timeout, allow 1 test execution to probe system health.
   - If success -> CLOSED.
   - If fail -> OPEN.

## Human-in-the-Loop (HITL) Escalation

Workflows must define an explicit `HITL` trigger when the Circuit Breaker is OPEN and the system cannot self-heal.

## Context Saturation Index (CSI) Check

Context Load per Value Stream MUST be < 40KB. If it exceeds 40KB, the Circuit Breaker should trip to prevent token collapse.

## Audit Violation Triggers

1. **Missing States**: If a core workflow lacks definitions for OPEN/HALF-OPEN states, it is a `🔴 [LOCAL-FIX]`.
2. **No HITL**: If there is no human escalation path defined for infinite loops, it is a `🔴 [LOCAL-FIX]`.
