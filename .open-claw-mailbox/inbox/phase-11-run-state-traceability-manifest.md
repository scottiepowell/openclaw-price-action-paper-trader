# Phase 11 — Run State Traceability Manifest

Work in:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

Repository:

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Goal

Add a read-only run-state traceability manifest that ties together the full offline simulated lifecycle now proven through Phase 10:

```text
approval artifact
→ simulated submission
→ simulated execution journal
→ simulated reconciliation
→ audit/report artifacts
```

This phase should produce a single traceability index that lets a reviewer answer:

- Which candidate/order plan was approved?
- Which approval artifact authorized the simulated-only exercise?
- Which simulated submission was created?
- Which journal record captured it?
- Which reconciliation record confirmed it?
- Which reports summarize it?
- Are all safety boundaries still intact?

This is a read-only traceability/reporting phase only.

## Hard boundaries

Do not add Alpaca order submission.
Do not add live trading.
Do not add autonomous execution.
Do not add background workers.
Do not add schedulers.
Do not make broker/network calls.
Do not use broker credentials.
Do not enable paper execution.
Do not create new simulated submissions.
Do not create new journal records except in isolated tests.
Do not create new reconciliation records except in isolated tests.
Do not mutate approval artifacts.
Do not mutate simulated submission artifacts.
Do not mutate execution journal artifacts.
Do not mutate reconciliation artifacts.
Do not set `broker_action_allowed` true.
Do not change strategy logic.

Everything must remain offline-only, simulated-only, and read-only except for writing the new manifest/report outputs.

## Current known state

Phase 7 added manual approval and simulated submission support.

Phase 7.1 added compatibility approval files for all 11 PTC candidates.

Phase 8 added approval audit reports.

Phase 9 exercised one controlled simulated-only approval:

```text
APR-PTC-004 / PTC-004 / OP-PTC-004 / NVDA / bullish
```

Phase 10 journaled and reconciled that Phase 9 simulated submission.

Recent verified Phase 10 state:

- Phase 10 commit: `043b40f4f42f56e08c2b34906f5ebd43308439a8`
- simulated journal record count: 1
- simulated reconciliation record count: 1
- reconciliation status: `RECONCILED_SIMULATED_ONLY`
- CLI command: `approvals reconcile-simulated`
- pytest: 63 passed
- no broker/network/live execution path was added
- no broker credentials were used
- `broker_action_allowed` remains false everywhere

## New capability

Add a read-only traceability manifest service.

Suggested files:

- `src/price_action_paper_trader/services/run_state_traceability_manifest_service.py`
- `tests/unit/test_run_state_traceability_manifest_service.py`

If existing reporting/audit service conventions suggest a different location, use the existing project style.

## Manifest artifacts

Generate:

- `runs/reports/run_state_traceability_manifest.md`
- `runs/reports/run_state_traceability_manifest.csv`

Optional if consistent with project style:

- `runs/reports/run_state_traceability_manifest.json`

Do not write outside `runs/reports/` except for tests using temporary directories.

## Manifest content

The manifest should include one row per traceable lifecycle chain where possible.

For the current proven chain, include:

- `trace_id`
- `candidate_id`
- `order_plan_id`
- `symbol`
- `side`
- `approval_id`
- `approval_status`
- `approval_scope`
- `approval_artifact_path`
- `compatibility_artifact_path`
- `simulated_submission_id`
- `simulated_broker_order_id`
- `submission_status`
- `journal_record_id`
- `execution_status`
- `reconciliation_id`
- `reconciliation_status`
- `approval_audit_report_path`
- `simulated_submission_queue_path`
- `execution_journal_path`
- `reconciliation_report_path`
- `broker_action_allowed_all_false`
- `offline_only_boundary`
- `simulated_only_boundary`
- `trace_status`
- `trace_notes`

## Summary section

The markdown report should include a summary with:

- total approvals
- total compatibility approval files
- total simulated submissions
- total journal records
- total reconciliation records
- total complete traces
- incomplete traces
- unsafe broker flags
- unsafe approval scopes
- overall manifest status: `pass`, `warning`, or `fail`

Suggested rules:

- `pass` when every existing simulated submission has a matching journal and reconciliation record, all IDs align, and all broker flags are false.
- `warning` when there are pending approvals without submissions, but existing simulated submissions are fully reconciled.
- `fail` when a simulated submission lacks a journal/reconciliation record, IDs mismatch, approval scope is unsafe, or any `broker_action_allowed` field is true.

The current repo may reasonably produce `warning` because most approvals remain pending and only one has been exercised. That is acceptable if the single exercised chain is complete and safe.

## Read-only behavior

The manifest generation must not mutate:

- `runs/approvals/*`
- `runs/simulated_submissions/*`
- `runs/execution_journal/*`
- `runs/reconciliation/*`

It may only write new manifest outputs under `runs/reports/`.

Add tests to prove source artifact files are not modified by manifest generation.

## CLI

If consistent with current CLI style, add:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli approvals traceability-manifest
```

The command must only read existing local artifacts and write manifest outputs.

It must not:

- submit simulated orders
- journal new records
- reconcile new records
- contact brokers
- contact networks
- use credentials

## Tests

Add or strengthen tests verifying:

- manifest generation finds the Phase 9/10 complete chain
- the single current simulated submission maps to one journal record
- the journal record maps to one reconciliation record
- mismatched IDs produce `fail`
- missing journal record produces `fail`
- missing reconciliation record produces `fail`
- pending approvals without submissions produce `warning` or informational notes, not failure
- any `broker_action_allowed true` produces `fail`
- any approval scope other than `simulated_only` produces `fail`
- manifest generation does not mutate source artifacts
- generated markdown and CSV contain required fields
- CLI command exits successfully for the current safe artifact set

## Verification

Run:

```bash
PYTHONPATH=src pytest -q
```

If CLI command is added, also run:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli approvals traceability-manifest
```

Then show:

```bash
git status --short
git diff --stat
```

## Commit and push

Before committing, remove Python cache files if present:

```bash
find . -type d -name "__pycache__" -prune -exec rm -rf {} +
```

If changes are made and tests pass:

```bash
git add src tests runs .open-claw-mailbox/outbox .gitignore
git commit -m "Add Phase 11 run state traceability manifest"
git push origin main
```

If tests fail, stop and report the exact failure.
If unrelated files appear, stop and report them before committing.

## Outbox response

Write the response to:

```text
.open-claw-mailbox/outbox/phase-11-run-state-traceability-manifest-response.md
```

Include:

- files added/changed
- manifest artifacts generated
- total complete traces
- incomplete traces
- overall manifest status
- pytest result
- CLI command result if added
- commit SHA if committed
- confirmation no broker/network/live execution path was added
- confirmation no broker credentials were used
- confirmation no source lifecycle artifacts were mutated by manifest generation
- confirmation `broker_action_allowed` remains false everywhere
