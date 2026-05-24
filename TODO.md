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

- [ ] Define risk limits
- [ ] Block stale candidates
- [ ] Block duplicates
- [ ] Block missing target/invalidation
- [ ] Block unsupported symbols
- [ ] Block non-paper-review candidates

## Phase 4 — Alpaca paper adapter

- [ ] Design adapter interface
- [ ] Add paper-only config checks
- [ ] Implement dry-run broker adapter first
- [ ] Add Alpaca paper adapter only after approval

## Phase 5 — Manual approval execution

- [ ] Require explicit approval flag
- [ ] Submit paper orders only
- [ ] Record broker response

## Phase 6 — Journal reconciliation

- [ ] Record fills
- [ ] Record target/invalidation outcome
- [ ] Reconcile open/closed paper positions

## Phase 7 — Reporting

- [ ] CLI summary
- [ ] Paper outcome report
- [ ] Blocked order report
