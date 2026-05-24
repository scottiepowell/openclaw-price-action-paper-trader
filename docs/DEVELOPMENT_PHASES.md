# Development Phases

## Phase 0 — Scaffold only

Create repo, docs, configs, package skeleton, and tests.

## Phase 1 — Read-only Strategy Lab import

Read paper-review queue and paper-watch journal from Strategy Lab. Validate schema. No broker.

## Phase 2 — Order-plan generation

Convert approved candidates into local order plans. Still no broker.

## Phase 3 — Risk gate

Block unsafe or incomplete plans before any paper execution layer exists.

## Phase 4 — Simulated broker adapter

Implement an offline-only simulated execution adapter. Live trading remains unsupported and Alpaca stays out of scope.

## Phase 5 — Journal reconciliation

Record execution lineage, duplicate/malformed execution records, fills, target/invalidation outcome, and audit trail.

## Phase 6 — Alpaca paper adapter scaffold

Add a disabled-by-default, paper-only broker interface and safety gate. No submissions yet.

## Phase 7 — Reporting dashboard/CLI

Summarize active watches, paper outcomes, blocked plans, and execution history.
