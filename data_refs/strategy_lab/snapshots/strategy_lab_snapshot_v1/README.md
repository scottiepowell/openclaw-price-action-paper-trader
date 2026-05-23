# strategy_lab_snapshot_v1

This directory is a read-only imported snapshot of Strategy Lab outputs.
It now contains the first imported v1 artifact set.

## Purpose

It provides a stable import boundary for the paper trader app so it can consume
validated Strategy Lab artifacts without modifying Strategy Lab itself.

## Read-only contract

- Strategy Lab remains the source of truth.
- This repo may read imported snapshot artifacts only.
- This repo must not write back to Strategy Lab outputs.
- No broker execution lives here.
- No Alpaca execution lives here.
- No autonomous trading logic lives here.

## Source

Upstream repository:

- `scottiepowell/openclaw-monster-academy-strategy-lab`

## Snapshot import philosophy

Treat Strategy Lab outputs as immutable handoff artifacts. The paper trader may
index, validate, and summarize them, but it does not own their lifecycle.

Imported artifact groups in this snapshot:

- replay evidence matrix
- paper readiness matrix
- paper review queue
- paper watch journal
- replay packets and decision summaries
- per-PTC readiness/review/journal artifacts

## Expected imported artifact types

See `MANIFEST.yaml` for the expected artifact set.
