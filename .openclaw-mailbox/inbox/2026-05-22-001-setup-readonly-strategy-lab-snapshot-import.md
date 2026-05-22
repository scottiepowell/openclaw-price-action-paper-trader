# OpenClaw Inbox Prompt: Setup Read-Only Strategy Lab Snapshot Import

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

Use the dedicated apps channel:

```text
#openclaw-apps
channel id: 1507382627651555480
```

Do not use the Strategy Lab channel for this task.

## Boundary

Do not add Alpaca integration.
Do not add broker submission.
Do not create live trading logic.
Do not submit orders.
Do not create autonomous execution.
Do not enable paper trading.

This task is Phase 0 / Phase 1 scaffolding only.

## Context

The Strategy Lab repo now contains:

- replay evidence matrix
- paper readiness matrix
- paper review queue
- paper watch journal
- validated replay evidence
- full 11-symbol 1Day + 5Min historical artifact handoff

The paper-trader repo should consume these outputs as:

```text
read-only imported snapshots
```

Strategy Lab remains the source of truth.

The paper-trader repo must NOT modify Strategy Lab outputs.

## Task

Create the initial read-only snapshot import structure.

Create:

```text
data_refs/
  strategy_lab/
    snapshots/
      strategy_lab_snapshot_v1/
```

Inside the snapshot directory create:

```text
README.md
MANIFEST.yaml
```

The README should explain:

- snapshot purpose
- read-only contract
- source Strategy Lab repo
- snapshot import philosophy
- Strategy Lab remains source of truth
- no broker execution
- no Alpaca execution

The MANIFEST should document expected imported artifact types:

```text
replay_evidence_matrix
paper_readiness_matrix
paper_review_queue
paper_watch_journal
artifact_index
selected_review_plans
selected_replay_cases
```

## Add scaffolding utilities

Create:

```text
src/paper_trader/adapters/strategy_lab_reader.py
```

This should be:

- read-only
- placeholder/scaffold only
- no broker logic
- no Alpaca logic
- no execution logic

Include placeholder functions like:

```python
load_replay_evidence_matrix()
load_paper_readiness_matrix()
load_paper_review_queue()
load_paper_watch_journal()
```

Functions may return empty lists/placeholders for now.

## Documentation

Update:

```text
README.md
PROJECT_BRIEF.md
TODO.md
```

Add:

- snapshot import architecture
- Strategy Lab dependency flow
- separation of concerns
- future paper-trader phases

Document the intended pipeline:

```text
Strategy Lab
  ↓
Replay evidence
  ↓
Paper readiness
  ↓
Paper review queue
  ↓
Paper Trader app
  ↓
Future paper broker adapter
  ↓
Execution journal
```

## Tests

Add lightweight tests only if appropriate.

No network calls.
No Alpaca.
No broker dependencies.

Run:

```text
pytest -q
```

## Deliverable

Write the response under:

```text
.openclaw-mailbox/outbox/2026-05-22-001-setup-readonly-strategy-lab-snapshot-import-response.md
```

Include:

1. Files created/changed.
2. Snapshot directory created.
3. Strategy Lab snapshot contract summary.
4. Adapter scaffolding summary.
5. Documentation updates.
6. Test results.

After committing, run:

```text
git push
```

Also reply in Discord with only:

```text
Mailbox response written and pushed: .openclaw-mailbox/outbox/2026-05-22-001-setup-readonly-strategy-lab-snapshot-import-response.md
```
