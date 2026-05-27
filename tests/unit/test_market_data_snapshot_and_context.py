from pathlib import Path
import inspect

from price_action_paper_trader.adapters.market_data_provider import FakeMarketDataProvider, UnavailableMarketDataProvider
from price_action_paper_trader.cli import main as cli_main
from price_action_paper_trader.domain.market_data import MarketDataBar, MarketDataSnapshot
from price_action_paper_trader.services.market_context_assessment_service import (
    build_market_context_assessments,
    generate_market_context_assessment_report,
)
from price_action_paper_trader.services.market_data_snapshot_service import (
    generate_market_data_snapshot_artifacts,
    generate_unavailable_snapshot_artifacts,
)
from price_action_paper_trader.services.order_plan_builder import build_order_plans


def test_fake_provider_produces_deterministic_bars():
    provider = FakeMarketDataProvider()
    first = provider.fetch_snapshot(["NVDA"], ["5Min"], 15)
    second = provider.fetch_snapshot(["NVDA"], ["5Min"], 15)

    assert first.status == "pass"
    assert first.snapshot.snapshot_id == second.snapshot.snapshot_id
    assert first.snapshot.broker_action_allowed is False
    assert first.snapshot.is_live_execution_allowed is False
    assert first.snapshot.bars == second.snapshot.bars
    assert len(first.snapshot.bars) == 5


def test_snapshot_artifacts_are_generated_and_safe(tmp_path):
    report = generate_market_data_snapshot_artifacts(
        symbols=["NVDA", "SPY"],
        timeframes=["5Min", "1Day"],
        delay_minutes=15,
        provider=FakeMarketDataProvider(),
        output_root=tmp_path,
    )

    assert report["provider_status"] == "pass"
    assert report["count"] == 20
    assert report["snapshot"].broker_action_allowed is False
    assert report["snapshot"].is_live_execution_allowed is False
    assert report["queue_markdown"].is_file()
    assert report["queue_csv"].is_file()
    assert report["queue_json"].is_file()

    md_text = report["queue_markdown"].read_text(encoding="utf-8")
    csv_text = report["queue_csv"].read_text(encoding="utf-8")
    assert "Provider source: fake" in md_text
    assert "Broker action allowed: false" in md_text
    assert "not an order signal" in md_text
    assert "snapshot_id,symbol,timeframe,timestamp" in csv_text
    assert ",false," in csv_text


def test_unavailable_provider_emits_safe_status(tmp_path):
    report = generate_unavailable_snapshot_artifacts(
        symbols=["NVDA"],
        timeframes=["5Min"],
        delay_minutes=15,
        output_root=tmp_path,
    )

    assert report["provider_status"] == "market_data_unavailable"
    assert report["count"] == 0
    assert report["snapshot"].snapshot_status == "market_data_unavailable"
    assert report["snapshot"].broker_action_allowed is False
    assert report["snapshot"].is_live_execution_allowed is False
    assert "market data credentials unavailable" in report["queue_markdown"].read_text(encoding="utf-8")


def test_market_context_assessment_uses_phase9_10_chain_and_marks_human_review_required(tmp_path, monkeypatch):
    # keep report outputs local for the test
    import price_action_paper_trader.services.market_context_assessment_service as context_module
    import price_action_paper_trader.services.market_data_snapshot_service as snapshot_module

    monkeypatch.setattr(context_module, "DEFAULT_OUTPUT_ROOT", tmp_path / "reports")
    monkeypatch.setattr(context_module, "MARKET_DATA_OUTPUT_ROOT", tmp_path / "market_data")
    monkeypatch.setattr(snapshot_module, "DEFAULT_OUTPUT_ROOT", tmp_path / "market_data")

    report = generate_market_context_assessment_report()

    assert report["report"].overall_status == "warning"
    assert report["report"].total_complete_traces == 1
    assert report["report"].incomplete_traces == 10
    assert len(report["report"].assessment_rows) == 11
    assert report["queue_markdown"].is_file()
    assert report["queue_csv"].is_file()

    row = next(item for item in report["report"].assessment_rows if item.candidate_id == "PTC-004")
    assert row.human_review_required is True
    assert row.broker_action_allowed is False
    assert row.plan_context_status in {"aligned", "mixed", "invalidated", "stale", "insufficient_data"}

    md_text = report["queue_markdown"].read_text(encoding="utf-8")
    csv_text = report["queue_csv"].read_text(encoding="utf-8")
    assert "Overall manifest status: warning" in md_text
    assert "human_review_required" in csv_text
    assert ",false," in csv_text


def test_market_context_assessment_handles_stale_and_missing_data():
    plan = next(plan for plan in build_order_plans() if plan.candidate_id == "PTC-004")
    bar = MarketDataBar(
        symbol="NVDA",
        timeframe="5Min",
        timestamp="2026-05-27T12:30:00+00:00",
        open=100.0,
        high=101.0,
        low=99.0,
        close=100.5,
        volume=1000,
        source="fake",
        feed="delayed_historical",
        fetched_at="2026-05-27T13:00:00+00:00",
        data_delay_minutes=30,
        is_delayed=True,
    )
    stale_snapshot = MarketDataSnapshot(
        snapshot_id="MDS-STALE",
        symbols=("NVDA",),
        timeframes=("5Min",),
        window_start=bar.timestamp,
        window_end=bar.timestamp,
        fetched_at=bar.fetched_at,
        source="fake",
        feed="delayed_historical",
        data_delay_minutes=30,
        is_live_execution_allowed=False,
        broker_action_allowed=False,
        bars=(bar,),
        snapshot_status="pass",
        notes="stale snapshot for test",
    )
    missing_snapshot = MarketDataSnapshot(
        snapshot_id="MDS-MISSING",
        symbols=("NVDA",),
        timeframes=("5Min",),
        window_start="2026-05-27T13:00:00+00:00",
        window_end="2026-05-27T13:00:00+00:00",
        fetched_at="2026-05-27T13:00:00+00:00",
        source="fake",
        feed="delayed_historical",
        data_delay_minutes=15,
        is_live_execution_allowed=False,
        broker_action_allowed=False,
        bars=tuple(),
        snapshot_status="market_data_unavailable",
        notes="missing bars",
    )

    stale_row = build_market_context_assessments(stale_snapshot, [plan])[0]
    missing_row = build_market_context_assessments(missing_snapshot, [plan])[0]

    assert stale_row.plan_context_status == "stale"
    assert stale_row.human_review_required is True
    assert stale_row.broker_action_allowed is False
    assert missing_row.plan_context_status == "insufficient_data"
    assert missing_row.human_review_required is True
    assert missing_row.broker_action_allowed is False


def test_market_data_services_have_no_trading_or_network_dependency():
    import price_action_paper_trader.adapters.market_data_provider as provider_module
    import price_action_paper_trader.services.market_data_snapshot_service as snapshot_module
    import price_action_paper_trader.services.market_context_assessment_service as context_module

    for source in (
        inspect.getsource(provider_module).lower(),
        inspect.getsource(snapshot_module).lower(),
        inspect.getsource(context_module).lower(),
    ):
        assert "alpaca" not in source
        assert "requests" not in source
        assert "http.client" not in source
        assert "urllib" not in source
        assert "submit order" not in source
        assert "broker_action_allowed = true" not in source


def test_cli_market_data_commands_work_offline(tmp_path, monkeypatch):
    import price_action_paper_trader.services.market_data_snapshot_service as snapshot_module
    import price_action_paper_trader.services.market_context_assessment_service as context_module

    monkeypatch.setattr(snapshot_module, "DEFAULT_OUTPUT_ROOT", tmp_path / "market_data")
    monkeypatch.setattr(context_module, "DEFAULT_OUTPUT_ROOT", tmp_path / "reports")
    monkeypatch.setattr(context_module, "MARKET_DATA_OUTPUT_ROOT", tmp_path / "market_data")

    assert cli_main(["market-data", "snapshot", "--symbols", "NVDA", "--timeframes", "5Min", "--delay-minutes", "15", "--provider", "fake"]) == 0
    assert cli_main(["market-data", "assess-context"]) == 0

    assert (tmp_path / "market_data" / "latest_market_snapshot.md").is_file()
    assert (tmp_path / "market_data" / "latest_market_snapshot.csv").is_file()
    assert (tmp_path / "reports" / "market_context_assessment_report.md").is_file()
    assert (tmp_path / "reports" / "market_context_assessment_report.csv").is_file()


def test_market_context_generation_does_not_mutate_source_lifecycle_artifacts(tmp_path, monkeypatch):
    import price_action_paper_trader.services.market_context_assessment_service as context_module
    import price_action_paper_trader.services.market_data_snapshot_service as snapshot_module

    source_paths = [
        Path("runs/approvals/PTC-004-approval.md"),
        Path("runs/simulated_submissions/simulated_submission_queue.csv"),
        Path("runs/execution_journal/simulated_execution_journal.csv"),
        Path("runs/reconciliation/simulated_reconciliation_report.csv"),
    ]
    before = {path: path.read_text(encoding="utf-8") for path in source_paths}

    monkeypatch.setattr(context_module, "DEFAULT_OUTPUT_ROOT", tmp_path / "reports")
    monkeypatch.setattr(context_module, "MARKET_DATA_OUTPUT_ROOT", tmp_path / "market_data")
    monkeypatch.setattr(snapshot_module, "DEFAULT_OUTPUT_ROOT", tmp_path / "market_data")

    generate_market_context_assessment_report()

    after = {path: path.read_text(encoding="utf-8") for path in source_paths}
    assert before == after
