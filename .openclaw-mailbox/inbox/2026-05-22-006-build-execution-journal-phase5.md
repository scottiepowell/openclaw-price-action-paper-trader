# OpenClaw Inbox Prompt: Build Execution Journal & Reconciliation Layer (Phase 5)

## Repo

Work in this repo only:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

GitHub repo:

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Discord channel

Use:

```text
#openclaw-apps
channel id: 1507382627651555480
```

## Boundary

Do not add Alpaca integration.
Do not add real broker submission.
Do not create live trading logic.
Do not submit orders.
Do not use real credentials.
Do not create autonomous execution.
Do not enable live trading.
Do not write back to Strategy Lab.

This phase must remain:

```text
offline-only
simulated-only
non-networked
```

`broker_action_allowed` must remain `false` everywhere.

## Context

The repo currently supports:

```text
Strategy Lab snapshot import
→ readiness filtering
→ offline order plans
→ risk gate
→ simulated broker adapter
→ simulated execution records
```

The next architectural layer is:

```text
execution journal + reconciliation
```

The purpose is to validate execution lifecycle tracking and future auditability before any real broker integration exists.

## Goal

Implement:

```text
simulated execution records
  ↓
execution journal
  ↓
reconciliation reports
```

## Create domain model

Create:

```text
src/price_action_paper_trader/domain/journal_entry.py
```

Suggested fields:

```python
candidate_id
symbol
side
simulated_order_id
execution_status
journal_status
journal_timestamp_utc
risk_gate_status
snapshot_source
notes
broker_action_allowed
```

Use lightweight dataclass/object structure only.

## Create service

Create:

```text
src/price_action_paper_trader/services/execution_journal.py
```

Suggested functions:

```python
build_journal_entry(execution_record)
build_execution_journal(records)
serialize_journal_entry(entry)
reconcile_execution_records(records)
```

## Journal behavior

The execution journal should:

- accept simulated execution records only
- preserve execution lineage
- link execution records back to PTC candidates
- preserve snapshot source references
- produce deterministic reconciliation summaries
- remain fully offline-only

Do not add fills.
Do not add live pricing.
Do not add async workers.
Do not add schedulers.
Do not add polling loops.

## Reconciliation behavior

Create reconciliation summaries that detect:

```text
missing execution records
missing order plans
duplicate simulated order IDs
invalid execution status
missing candidate linkage
```

Warnings only are acceptable for some categories.

## Generated artifacts

Create:

```text
runs/execution_journal/
```

Generate:

```text
runs/execution_journal/execution_journal.md
runs/execution_journal/execution_journal.csv
runs/execution_journal/reconciliation_report.md
runs/execution_journal/reconciliation_report.csv
```

Optionally create:

```text
runs/execution_journal/entries/PTC-*-journal-entry.md
```

Each generated journal entry should include:

- candidate ID
- symbol
- side
- simulated order ID
- execution status
- risk gate status
- snapshot source
- explicit offline-only boundary
- explicit simulated-only boundary

## Documentation

Update:

```text
README.md
PROJECT_BRIEF.md
TODO.md
docs/ARCHITECTURE.md
docs/DEVELOPMENT_PHASES.md
```

Add:

- Phase 5 architecture
- execution journal role
- reconciliation lifecycle
- future broker reconciliation separation
- auditability goals

Document intended future flow:

```text
Strategy Lab snapshot
  ↓
readiness filter
  ↓
order plans
  ↓
risk gate
  ↓
simulated broker adapter
  ↓
execution journal
  ↓
reconciliation
```

## Tests

Add/update tests:

- journal entries generate from simulated execution records
- reconciliation reports generate correctly
- duplicate simulated order IDs are detected
- malformed execution records are rejected
- execution lineage is preserved
- broker_action_allowed remains false
- no network calls introduced
- no Alpaca dependency introduced

Run:

```text
PYTHONPATH=src pytest -q
```

## Deliverable

Write the response under:

```text
.openclaw-mailbox/outbox/2026-05-22-006-build-execution-journal-phase5-response.md
```

Include:

1. Files created/changed.
2. Execution journal architecture summary.
3. Execution journal artifact paths.
4. Reconciliation artifact paths.
5. Count of journal entries.
6. Count of reconciliation warnings/errors.
7. Which reconciliation categories were implemented.
8. Confirmation everything remains offline-only.
9. Confirmation no Alpaca dependency exists.
10. Confirmation `broker_action_allowed: false` everywhere.
11. Test results.

After committing, run:

```text
git push
```

Also reply in Discord with only:

```text
Mailbox response written and pushed: .openclaw-mailbox/outbox/2026-05-22-006-build-execution-journal-phase5-response.md
```
