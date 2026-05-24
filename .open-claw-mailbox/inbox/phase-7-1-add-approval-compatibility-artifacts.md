# Phase 7.1 Corrective Follow-up — Add Approval Compatibility Artifacts

Work in:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

Repository:

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Problem

The Phase 7.1 audit found path/filename drift, but did not add the original requested compatibility approval files.

GitHub still does not have:

```text
runs/approvals/PTC-004-approval.md
```

The original Phase 7 mailbox task requested individual approval templates at these exact paths:

- `runs/approvals/PTC-004-approval.md`
- `runs/approvals/PTC-005-approval.md`
- `runs/approvals/PTC-009-approval.md`
- `runs/approvals/PTC-017-approval.md`
- `runs/approvals/PTC-019-approval.md`
- `runs/approvals/PTC-021-approval.md`
- `runs/approvals/PTC-022-approval.md`
- `runs/approvals/PTC-024-approval.md`
- `runs/approvals/PTC-032-approval.md`
- `runs/approvals/PTC-034-approval.md`
- `runs/approvals/PTC-035-approval.md`

## Goal

Add compatibility approval files at those exact paths.

Keep the existing `runs/approvals/templates/` directory if it exists. Do not remove it.

Each compatibility file must default to:

```yaml
approval_status: pending
approval_scope: simulated_only
broker_action_allowed: false
```

## Hard boundaries

Do not add Alpaca order submission.
Do not add live trading.
Do not add autonomous execution.
Do not add background workers.
Do not add schedulers.
Do not make network calls except git fetch/pull/push.
Do not use broker credentials.
Do not enable paper execution.
Do not set `broker_action_allowed` true.
Do not redesign the implementation.
Do not change strategy logic.

Everything must remain simulated-only and offline-only.

## Required steps

1. Change into the repo:

```bash
cd /home/scott/projects/openclaw-price-action-paper-trader
```

2. Pull latest safely:

```bash
git fetch origin main
git rebase origin/main
```

If there are conflicts, stop and report the conflicting files. Do not guess.

3. Remove Python cache files if present:

```bash
find . -type d -name "__pycache__" -prune -exec rm -rf {} +
```

4. Add or update artifact generation so it creates the original compatibility files at:

```text
runs/approvals/PTC-004-approval.md
runs/approvals/PTC-005-approval.md
runs/approvals/PTC-009-approval.md
runs/approvals/PTC-017-approval.md
runs/approvals/PTC-019-approval.md
runs/approvals/PTC-021-approval.md
runs/approvals/PTC-022-approval.md
runs/approvals/PTC-024-approval.md
runs/approvals/PTC-032-approval.md
runs/approvals/PTC-034-approval.md
runs/approvals/PTC-035-approval.md
```

5. Regenerate approval artifacts if the project has a command/service for that.

6. Add or update tests to verify those exact files exist after generation.

7. Run:

```bash
PYTHONPATH=src pytest -q
```

8. If tests pass, commit and push:

```bash
git add src tests runs .open-claw-mailbox/outbox
git commit -m "Add Phase 7 approval compatibility artifacts"
git push origin main
```

9. Write or update the outbox response at:

```text
.open-claw-mailbox/outbox/phase-7-1-approval-compatibility-artifacts-response.md
```

Include:

- compatibility approval files added: yes/no
- exact compatibility file count
- pytest result
- commit SHA
- confirmation no broker/network/live execution path was added
- confirmation `broker_action_allowed` remains false everywhere

## Expected result

The repo should contain both:

- the existing `runs/approvals/templates/` artifacts, if already present
- compatibility files directly under `runs/approvals/` using the original Phase 7 filenames

## Stop conditions

Stop and report instead of pushing if:

- rebase conflicts occur
- pytest fails
- any change would require real broker behavior
- any change would set `broker_action_allowed` true
- unrelated files appear in `git diff --stat`
