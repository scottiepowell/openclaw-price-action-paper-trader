"""Read-only market data providers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from hashlib import sha256
from pathlib import Path
from typing import Protocol, Sequence

from price_action_paper_trader.domain.market_data import MarketDataBar, MarketDataSnapshot


FAKE_MARKET_ANCHOR_UTC = datetime(2026, 5, 27, 13, 0, 0, tzinfo=timezone.utc)


@dataclass(frozen=True)
class MarketDataProviderResult:
    snapshot: MarketDataSnapshot
    status: str
    notes: str = ""


class MarketDataProvider(Protocol):
    def fetch_snapshot(self, symbols: Sequence[str], timeframes: Sequence[str], delay_minutes: int) -> MarketDataProviderResult:
        ...


def _timeframe_minutes(timeframe: str) -> int:
    normalized = timeframe.strip().lower()
    return {
        "1min": 1,
        "5min": 5,
        "15min": 15,
        "1day": 60 * 24,
    }.get(normalized, 5)


def _stable_price_seed(symbol: str, timeframe: str) -> int:
    digest = sha256(f"{symbol.upper()}|{timeframe.lower()}".encode("utf-8")).hexdigest()[:8]
    return int(digest, 16)


def _trend_sign(symbol: str, timeframe: str) -> int:
    return 1 if _stable_price_seed(symbol, timeframe) % 2 == 0 else -1


def _bar_series(symbol: str, timeframe: str, delay_minutes: int, fetched_at: datetime) -> list[MarketDataBar]:
    interval = _timeframe_minutes(timeframe)
    trend = _trend_sign(symbol, timeframe)
    seed = _stable_price_seed(symbol, timeframe)
    base_price = 80.0 + (seed % 70)
    latest_ts = fetched_at - timedelta(minutes=delay_minutes)
    bars: list[MarketDataBar] = []
    for idx in range(5):
        offset = 4 - idx
        ts = latest_ts - timedelta(minutes=interval * offset)
        close = round(base_price + trend * (idx + 1) * (0.6 if interval < 60 * 24 else 1.5), 2)
        open_price = round(close - trend * 0.35, 2)
        high = round(max(open_price, close) + 0.22, 2)
        low = round(min(open_price, close) - 0.22, 2)
        volume = 1_000_000 + (seed % 250_000) + idx * 7_500
        bars.append(
            MarketDataBar(
                symbol=symbol.upper(),
                timeframe=timeframe,
                timestamp=ts.isoformat(),
                open=open_price,
                high=high,
                low=low,
                close=close,
                volume=volume,
                source="fake",
                feed="delayed_historical",
                fetched_at=fetched_at.isoformat(),
                data_delay_minutes=delay_minutes,
                is_delayed=delay_minutes >= 15,
            )
        )
    return bars


@dataclass(frozen=True)
class FakeMarketDataProvider:
    source: str = "fake"
    feed: str = "delayed_historical"

    def fetch_snapshot(self, symbols: Sequence[str], timeframes: Sequence[str], delay_minutes: int) -> MarketDataProviderResult:
        cleaned_symbols = tuple(dict.fromkeys(symbol.strip().upper() for symbol in symbols if symbol.strip()))
        cleaned_timeframes = tuple(dict.fromkeys(timeframe.strip() for timeframe in timeframes if timeframe.strip())) or ("5Min",)
        fetched_at = FAKE_MARKET_ANCHOR_UTC
        bars: list[MarketDataBar] = []
        for symbol in cleaned_symbols:
            for timeframe in cleaned_timeframes:
                bars.extend(_bar_series(symbol, timeframe, delay_minutes, fetched_at))
        window_start = min((bar.timestamp for bar in bars), default=fetched_at.isoformat())
        window_end = max((bar.timestamp for bar in bars), default=fetched_at.isoformat())
        snapshot = MarketDataSnapshot(
            snapshot_id=f"MDS-{sha256('|'.join(cleaned_symbols + cleaned_timeframes).encode('utf-8')).hexdigest()[:16].upper()}",
            symbols=cleaned_symbols,
            timeframes=cleaned_timeframes,
            window_start=window_start,
            window_end=window_end,
            fetched_at=fetched_at.isoformat(),
            source=self.source,
            feed=self.feed,
            data_delay_minutes=delay_minutes,
            is_live_execution_allowed=False,
            broker_action_allowed=False,
            bars=tuple(bars),
            snapshot_status="pass",
            notes="fake delayed historical market data for offline review only",
        )
        return MarketDataProviderResult(snapshot=snapshot, status="pass", notes="fake provider used")


@dataclass(frozen=True)
class UnavailableMarketDataProvider:
    source: str = "unavailable"
    feed: str = "none"
    reason: str = "market data credentials unavailable"

    def fetch_snapshot(self, symbols: Sequence[str], timeframes: Sequence[str], delay_minutes: int) -> MarketDataProviderResult:
        cleaned_symbols = tuple(dict.fromkeys(symbol.strip().upper() for symbol in symbols if symbol.strip()))
        cleaned_timeframes = tuple(dict.fromkeys(timeframe.strip() for timeframe in timeframes if timeframe.strip())) or ("5Min",)
        fetched_at = FAKE_MARKET_ANCHOR_UTC
        snapshot = MarketDataSnapshot(
            snapshot_id=f"MDS-UNAVAILABLE-{sha256('|'.join(cleaned_symbols + cleaned_timeframes).encode('utf-8')).hexdigest()[:12].upper()}",
            symbols=cleaned_symbols,
            timeframes=cleaned_timeframes,
            window_start=fetched_at.isoformat(),
            window_end=fetched_at.isoformat(),
            fetched_at=fetched_at.isoformat(),
            source=self.source,
            feed=self.feed,
            data_delay_minutes=delay_minutes,
            is_live_execution_allowed=False,
            broker_action_allowed=False,
            bars=tuple(),
            snapshot_status="market_data_unavailable",
            notes=self.reason,
        )
        return MarketDataProviderResult(snapshot=snapshot, status="market_data_unavailable", notes=self.reason)

