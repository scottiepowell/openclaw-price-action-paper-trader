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

- [ ] Define Strategy Lab queue input contract
- [ ] Define Strategy Lab journal input contract
- [ ] Implement read-only loader
- [ ] Validate required fields
- [ ] Reject non-ready candidates
- [ ] Add fixtures from sanitized Strategy Lab outputs

## Phase 2 — Order-plan generation

- [ ] Define order plan schema
- [ ] Convert approved candidates into order plans
- [ ] Add blocked-order reasons
- [ ] Keep broker action disabled

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
