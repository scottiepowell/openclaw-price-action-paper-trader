# Targeted Gap-Fill Plan

## Goal
Fill the weakest evidence buckets without broad relaxation of replay discovery constraints.

## Current evidence shape
- Strongest coverage: bullish/bearish `candidate_for_manual_review` drafts.
- Confirmed examples exist for:
  - bullish `confirmed_breakout`
  - bullish `confirmed_breakout_no_target_hit`
  - bearish `confirmed_breakdown`
  - bearish `confirmed_breakdown_no_target_hit`
  - bearish `failed_breakdown_reclaim`
  - bullish `watch_no_trigger`
- Weak or missing buckets:
  - bullish failed breakout reclaim
  - bullish target-not-hit outside the existing May cluster
  - bullish target already hit before confirmation
  - bearish no-target-hit beyond META-heavy coverage
  - bearish support-touch / no-trigger
  - bearish target already hit before confirmation
  - bearish ambiguous
  - additional confirmed examples across symbols not already overrepresented

## Proposed gap-fill targets

### 1) Bullish failed breakout reclaim
- Why it matters: proves a breakout can fail after closing above resistance.
- Candidate selection rule: bullish close above resistance where the next 6 bars reclaim below the resistance level.
- Suggested loosened constraint: none; keep strict date spacing and symbol caps.
- Expected source: audit near-miss symbols with repeated high-score AVGO/NVDA breakouts.
- Status: remain `NOT_VERIFIED`, `manual_review_status: pending`.

### 2) Bullish target-not-hit outside the May cluster
- Why it matters: separates valid breakout structure from full target completion.
- Candidate selection rule: bullish breakout with no target hit inside the confirmation window, but clean structure.
- Suggested loosened constraint: allow targeted symbol reuse if the date is outside the occupied window.
- Expected source: MSFT / AAPL / GOOGL near-misses and existing HR-006 style structure.
- Status: remain `NOT_VERIFIED`, `manual_review_status: pending`.

### 3) Bullish target already hit before confirmation
- Why it matters: catches look-ahead / invalid replay setup risk.
- Candidate selection rule: breakout-looking bar where target is already satisfied before the entry-confirmation bar.
- Suggested loosened constraint: targeted exception only, not broader discovery relaxation.
- Expected source: candidate review of AVGO / NVDA sequences around the May cluster.
- Status: remain `NOT_VERIFIED`, `manual_review_status: pending`.

### 4) Bearish no-target-hit on non-SPY/IWM symbols
- Why it matters: broadens bearish coverage beyond the current index-heavy examples.
- Candidate selection rule: close below support with follow-through that never reaches the downside target.
- Suggested loosened constraint: none; keep current caps.
- Expected source: QQQ / AAPL / NVDA / AMZN bearish discovery rows.
- Status: remain `NOT_VERIFIED`, `manual_review_status: pending`.

### 5) Bearish support-touch / no-trigger
- Why it matters: records a clean no-trigger case instead of forcing a breakdown label.
- Candidate selection rule: support is tested, but the close never confirms a breakdown.
- Suggested loosened constraint: allow selection of a non-breakdown candidate from nearby near-miss windows.
- Expected source: bearish near-miss candidates with low follow-through but no close-through.
- Status: remain `NOT_VERIFIED`, `manual_review_status: pending`.

### 6) Bearish target already hit before confirmation
- Why it matters: prevents over-crediting bearish confirmation when the target is pre-filled.
- Candidate selection rule: downside target is reached before the candidate bar is confirmed.
- Suggested loosened constraint: none; this is a targeted gap-fill / validation case.
- Expected source: META / AVGO bearish near-miss clusters.
- Status: remain `NOT_VERIFIED`, `manual_review_status: pending`.

### 7) Bearish ambiguous
- Why it matters: documents noisy structure and reduces forced binary labeling.
- Candidate selection rule: support break is weak, oscillatory, or mixed after confirmation.
- Suggested loosened constraint: none; pick from lower-ranked bearish near-misses.
- Expected source: mixed bearish rows in the audit near-miss set.
- Status: remain `NOT_VERIFIED`, `manual_review_status: pending`.

### 8) Additional confirmed examples across symbols
- Why it matters: keeps the matrix from overfitting to META / SPY / NVDA / AVGO.
- Candidate selection rule: one confirmed example per underrepresented symbol and side.
- Suggested loosened constraint: relax only symbol reuse pressure, not window spacing.
- Expected source: GOOGL, AMZN, TSLA, MSFT, AAPL, QQQ.
- Status: remain `NOT_VERIFIED`, `manual_review_status: pending`.

## Recommended selection policy
- Keep `broker_action_allowed: false` everywhere.
- Keep the core avoid-existing-window rule intact.
- Create only targeted cases that fill a named bucket.
- Prefer one case per missing bucket before adding more symbol diversity.
- Do not create broad replay batches until the gap buckets are clearly represented.

## Suggested next batch
1. one bullish failed breakout reclaim
2. one bullish target-not-hit outside May
3. one bearish no-target-hit on a non-index symbol
4. one bearish support-touch / no-trigger
5. one bearish ambiguous case

## Boundary
- Discovery / manual review planning only
- No promotion
- No broker action allowed
