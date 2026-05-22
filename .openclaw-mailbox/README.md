# OpenClaw Mailbox

This directory is a GitHub-backed handoff point for prompts and responses.

## Folders

- `inbox/` contains prompts for OpenClaw to read.
- `outbox/` contains responses written by OpenClaw.
- `archive/` contains completed or superseded prompts.

## Normal use

1. Add a prompt under `inbox/`.
2. Commit and push.
3. Tell OpenClaw through Discord to pull latest and read the newest inbox prompt.
4. OpenClaw writes its response under `outbox/` and commits it.
5. Pull and review the response.

## Phone prompt

```text
In openclaw-price-action-paper-trader, pull latest, read the newest .openclaw-mailbox/inbox prompt, do the requested work, then write and commit a response under .openclaw-mailbox/outbox.
```
