# OpenClaw Inbox Prompt: Import Real Strategy Lab Snapshot v1

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
Do not add broker submission.
Do not create live trading logic.
Do not submit orders.
Do not create autonomous execution.
Do not enable paper trading.
Do not write back to Strategy Lab.

This is still Phase 1: read-only Strategy Lab import.

## Context

The previous task created the read-only snapshot scaffold:

```text
data_refs/strategy_lab/snapshots/strategy_lab_snapshot_v1/
```

and added the placeholder reader:

```text
src/price_action_paper_trader/adapters/strategy_lab_reader.py
```

Now import the actual Strategy Lab contract artifacts into the snapshot directory and make the reader load real files.

Strategy Lab source repo path:

```text
/home/scott/projects/openclaw-monster-academy-strategy-lab
```

Strategy Lab remains source of truth. The paper-trader repo should contain a copied, read-only snapshot.

## Source artifacts to import

Copy these from the Strategy Lab repo if they exist:

```text
runs/replay/replay_evidence_matrix.md
runs/replay/replay_evidence_matrix.csv
runs/paper_readiness/paper_readiness_matrix.md
runs/paper_readiness/paper_readiness_matrix.csv
runs/paper_review/paper_review_queue.md
runs/paper_review/paper_review_queue.csv
runs/paper_journal/paper_watch_journal.md
runs/paper_journal/paper_watch_journal.csv
data_refs/historical_market_data/artifact_index.yaml
configs/replay_discovery.yaml
docs/STRATEGY_LAB_MILESTONE_REPLAY_TO_PAPER_REVIEW.md
```

Also copy selected generated per-candidate artifacts for candidates currently in the Strategy Lab paper-review queue, if present:

```text
runs/paper_review/PTC-*-paper-review-plan.md
runs/paper_journal/PTC-*-journal.md
```

Place copied files under:

```text
data_refs/strategy_lab/snapshots/strategy_lab_snapshot_v1/
```

Suggested layout:

```text
data_refs/strategy_lab/snapshots/strategy_lab_snapshot_v1/
  README.md
  MANIFEST.yaml
  replay/
    replay_evidence_matrix.md
    replay_evidence_matrix.csv
  paper_readiness/
    paper_readiness_matrix.md
    paper_readiness_matrix.csv
  paper_review/
    paper_review_queue.md
    paper_review_queue.csv
    plans/
      PTC-*-paper-review-plan.md
  paper_journal/
    paper_watch_journal.md
    paper_watch_journal.csv
    journals/
      PTC-*-journal.md
  configs/
    artifact_index.yaml
    replay_discovery.yaml
  docs/
    STRATEGY_LAB_MILESTONE_REPLAY_TO_PAPER_REVIEW.md
```

## Manifest update

Update:

```text
data_refs/strategy_lab/snapshots/strategy_lab_snapshot_v1/MANIFEST.yaml
```

Include:

- snapshot_id: strategy_lab_snapshot_v1
- source_repo_path
- source_repo_git_commit, if available
- import_timestamp_utc
- imported artifacts and relative paths
- paper_review_queue_count
- paper_watch_journal_count
- ready_for_paper_review_count
- broker_action_allowed_expected: false
- read_only: true
- notes that Strategy Lab remains source of truth

## Reader implementation

Update:

```text
src/price_action_paper_trader/adapters/strategy_lab_reader.py
```

Implement read-only loaders for the snapshot files:

```python
load_replay_evidence_matrix(snapshot_dir)
load_paper_readiness_matrix(snapshot_dir)
load_paper_review_queue(snapshot_dir)
load_paper_watch_journal(snapshot_dir)
load_manifest(snapshot_dir)
```

Use CSV parsing for `.csv` matrix/queue/journal files.
Use YAML parsing for `MANIFEST.yaml` if PyYAML is already available. If not, either add `pyyaml` to `requirements.txt` or implement a small safe fallback, whichever is cleaner for this repo.

The loaders must not write files.
The loaders must not mutate Strategy Lab.
The loaders must not call broker or Alpaca code.

## Tests

Add/update tests:

- snapshot directory contains imported matrix/queue/journal files
- manifest loads successfully
- paper-review queue loads and has at least one row
- paper-watch journal loads and has at least one row
- readiness matrix loads and includes READY_FOR_PAPER_REVIEW rows
- all loaded rows either have `broker_action_allowed` false or do not attempt broker action
- loaders are read-only
- no Alpaca/broker dependency is introduced

Run:

```text
pytest -q
```

## Deliverable

Write the response under:

```text
.openclaw-mailbox/outbox/2026-05-22-002-import-real-strategy-lab-snapshot-v1-response.md
```

Include:

1. Files created/changed.
2. Snapshot import path.
3. Source Strategy Lab commit/path used.
4. Imported artifact list.
5. Paper-review queue count.
6. Paper-watch journal count.
7. READY_FOR_PAPER_REVIEW count.
8. Reader implementation summary.
9. Test results.
10. Any missing source artifacts.

After committing, run:

```text
git push
```

Also reply in Discord with only:

```text
Mailbox response written and pushed: .openclaw-mailbox/outbox/2026-05-22-002-import-real-strategy-lab-snapshot-v1-response.md
```
