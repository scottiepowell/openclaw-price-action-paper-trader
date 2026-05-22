# Development Phases

## Phase 0 — Scaffold only

Create repo, docs, configs, package skeleton, and tests.

## Phase 1 — Read-only Strategy Lab import

Read paper-review queue and paper-watch journal from Strategy Lab. Validate schema. No broker.

## Phase 2 — Order-plan generation

Convert approved candidates into local order plans. Still no broker.

## Phase 3 — Risk gate

Block unsafe or incomplete plans before any paper execution layer exists.

## Phase 4 — Paper broker adapter

Implement Alpaca paper account adapter only. Live trading remains unsupported.

## Phase 5 — Manual approval execution

Submit paper orders only when explicitly approved.

## Phase 6 — Journal reconciliation

Record broker response, fills, target/invalidation outcome, and audit trail.

## Phase 7 — Reporting dashboard/CLI

Summarize active watches, paper outcomes, blocked plans, and execution history.
