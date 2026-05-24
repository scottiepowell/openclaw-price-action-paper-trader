# TODO — On The Levels

## Phase 0 — Scaffold

- [x] Create repo skeleton
- [x] Add safety-first README
- [x] Add AGENTS.md
- [x] Add project brief
- [x] Add configs
- [x] Add package skeleton
- [x] Add initial tests

## Phase 1 — Read-only Strategy Lab import

- [x] Define Strategy Lab queue input contract
- [x] Define Strategy Lab journal input contract
- [x] Implement read-only loader
- [ ] Validate required fields
- [ ] Reject non-ready candidates
- [x] Add fixtures from sanitized Strategy Lab outputs
- [x] Add read-only snapshot import structure

## Phase 2 — Order-plan generation

- [x] Define order plan schema
- [x] Convert approved candidates into order plans
- [x] Add blocked-order reasons
- [x] Keep broker action disabled
- [x] Generate offline order-plan artifacts

## Phase 3 — Risk gate

- [x] Define risk limits
- [x] Block stale candidates
- [x] Block duplicates
- [x] Block missing target/invalidation
- [x] Block unsupported symbols
- [x] Block non-paper-review candidates

## Phase 4 — Simulated broker adapter

- [x] Design adapter interface
- [x] Add paper-only config checks
- [x] Implement dry-run broker adapter first
- [x] Keep Alpaca adapter isolated for a future phase

## Phase 5 — Manual approval execution

- [x] Require explicit approval flag
- [x] Submit paper-order intent only
- [x] Record broker response locally without network calls

## Phase 6 — Alpaca paper adapter scaffold

- [x] Define broker interface
- [x] Add manual approval model
- [x] Add disabled-by-default Alpaca scaffold
- [x] Add broker safety gate
- [x] Add paper-only config defaults
- [x] Keep `broker_action_allowed` false by default

## Phase 7 — Journal reconciliation

- [x] Record execution lineage
- [x] Detect duplicate execution records
- [x] Detect malformed execution records
- [x] Record fills
- [x] Record target/invalidation outcome
- [x] Reconcile open/closed paper positions
- [x] Generate audit/reconciliation artifacts

## Phase 8 — Reporting

- [ ] CLI summary
- [ ] Paper outcome report
- [ ] Blocked order report
