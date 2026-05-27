"""Read-only market data snapshot generation."""

from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, Sequence

from price_action_paper_trader.adapters.market_data_provider import (
    FakeMarketDataProvider,
    MarketDataProvider,
    UnavailableMarketDataProvider,
)
from price_action_paper_trader.domain.market_data import MarketDataBar, MarketDataSnapshot


DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "market_data"


def _serialize_bar(bar: MarketDataBar) -> dict[str, Any]:
    data = asdict(bar)
    data["is_delayed"] = str(bar.is_delayed).lower()
    return data


def _write_markdown(snapshot: MarketDataSnapshot, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "latest_market_snapshot.md"
    lines = [
        "# Latest Market Data Snapshot",
        "",
        "Read-only delayed market data for human review only.",
        "",
        f"- Snapshot ID: {snapshot.snapshot_id}",
        f"- Provider source: {snapshot.source}",
        f"- Feed: {snapshot.feed}",
        f"- Snapshot status: {snapshot.snapshot_status}",
        f"- Symbols: {', '.join(snapshot.symbols) if snapshot.symbols else 'none'}",
        f"- Timeframes: {', '.join(snapshot.timeframes) if snapshot.timeframes else 'none'}",
        f"- Requested / actual window: {snapshot.window_start} → {snapshot.window_end}",
        f"- Fetched at: {snapshot.fetched_at}",
        f"- Data delay minutes: {snapshot.data_delay_minutes}",
        f"- Broker action allowed: {str(snapshot.broker_action_allowed).lower()}",
        f"- Live execution allowed: {str(snapshot.is_live_execution_allowed).lower()}",
        f"- Notes: {snapshot.notes}",
        "- Note: this is not an order signal and not trade authorization.",
        "",
        "| symbol | timeframe | timestamp | open | high | low | close | volume | source | feed | fetched_at | data_delay_minutes | is_delayed |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | --- |",
    ]
    for bar in snapshot.bars:
        lines.append(
            f"| {bar.symbol} | {bar.timeframe} | {bar.timestamp} | {bar.open:.2f} | {bar.high:.2f} | {bar.low:.2f} | {bar.close:.2f} | {bar.volume} | {bar.source} | {bar.feed} | {bar.fetched_at} | {bar.data_delay_minutes} | {str(bar.is_delayed).lower()} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _write_csv(snapshot: MarketDataSnapshot, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "latest_market_snapshot.csv"
    fieldnames = [
        "snapshot_id",
        "symbol",
        "timeframe",
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "source",
        "feed",
        "fetched_at",
        "data_delay_minutes",
        "is_delayed",
        "window_start",
        "window_end",
        "snapshot_status",
        "broker_action_allowed",
        "is_live_execution_allowed",
        "notes",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for bar in snapshot.bars:
            row = _serialize_bar(bar)
            row.update(
                {
                    "snapshot_id": snapshot.snapshot_id,
                    "window_start": snapshot.window_start,
                    "window_end": snapshot.window_end,
                    "snapshot_status": snapshot.snapshot_status,
                    "broker_action_allowed": str(snapshot.broker_action_allowed).lower(),
                    "is_live_execution_allowed": str(snapshot.is_live_execution_allowed).lower(),
                    "notes": snapshot.notes,
                }
            )
            writer.writerow(row)
        if not snapshot.bars:
            writer.writerow(
                {
                    "snapshot_id": snapshot.snapshot_id,
                    "symbol": "",
                    "timeframe": "",
                    "timestamp": snapshot.fetched_at,
                    "open": "",
                    "high": "",
                    "low": "",
                    "close": "",
                    "volume": "",
                    "source": snapshot.source,
                    "feed": snapshot.feed,
                    "fetched_at": snapshot.fetched_at,
                    "data_delay_minutes": snapshot.data_delay_minutes,
                    "is_delayed": "false",
                    "window_start": snapshot.window_start,
                    "window_end": snapshot.window_end,
                    "snapshot_status": snapshot.snapshot_status,
                    "broker_action_allowed": str(snapshot.broker_action_allowed).lower(),
                    "is_live_execution_allowed": str(snapshot.is_live_execution_allowed).lower(),
                    "notes": snapshot.notes,
                }
            )
    return path


def _write_json(snapshot: MarketDataSnapshot, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "latest_market_snapshot.json"
    payload = asdict(snapshot)
    payload["broker_action_allowed"] = str(snapshot.broker_action_allowed).lower()
    payload["is_live_execution_allowed"] = str(snapshot.is_live_execution_allowed).lower()
    payload["bars"] = [asdict(bar) | {"is_delayed": str(bar.is_delayed).lower()} for bar in snapshot.bars]
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def generate_market_data_snapshot_artifacts(
    symbols: Sequence[str],
    timeframes: Sequence[str],
    delay_minutes: int = 15,
    provider: MarketDataProvider | None = None,
    output_root: str | Path | None = None,
) -> dict[str, Any]:
    provider = provider or FakeMarketDataProvider()
    result = provider.fetch_snapshot(symbols, timeframes, delay_minutes)
    snapshot = result.snapshot
    output_root_path = Path(output_root) if output_root is not None else DEFAULT_OUTPUT_ROOT
    md_path = _write_markdown(snapshot, output_root_path)
    csv_path = _write_csv(snapshot, output_root_path)
    json_path = _write_json(snapshot, output_root_path)
    return {
        "count": len(snapshot.bars),
        "snapshot": snapshot,
        "provider_status": result.status,
        "provider_notes": result.notes,
        "queue_markdown": md_path,
        "queue_csv": csv_path,
        "queue_json": json_path,
    }


def generate_unavailable_snapshot_artifacts(
    symbols: Sequence[str],
    timeframes: Sequence[str],
    delay_minutes: int = 15,
    output_root: str | Path | None = None,
) -> dict[str, Any]:
    return generate_market_data_snapshot_artifacts(
        symbols=symbols,
        timeframes=timeframes,
        delay_minutes=delay_minutes,
        provider=UnavailableMarketDataProvider(),
        output_root=output_root,
    )
