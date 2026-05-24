# Phase 7 — Manual Approval Command Layer

Done.

- Pulled the latest changes first.
- Added manual approval and simulated submission domain models.
- Added offline-only approval artifact generation, validation, and simulated submission services.
- Added safe CLI commands: `approvals list`, `approvals validate`, and `approvals submit-simulated`.
- Generated the approval and simulated-submission queue artifacts under `runs/`.
- Verified with `PYTHONPATH=src pytest -q` (`46 passed`).

Safety stayed intact: `broker_action_allowed` remains false everywhere, and no live broker/network path was added.
