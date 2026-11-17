# Architecture and data contract

## Data flow
User tap -> Android MediaProjection consent -> user-selected screen capture -> local OCR -> user review/edit -> API -> schema validation -> SQLite.

## Observation contract
sport; competition; event_name; event_start_utc; market_name; selection_name; decimal_odds; captured_at_utc; source; OCR confidence; review status.

## Rules
1. Append observations; never overwrite odds history.
2. Store timestamps in UTC and require timezone-aware input.
3. Separate event, market, and selection identity.
4. OCR confidence is not prediction confidence.
5. Never invent missing scores, odds, teams, or times.
6. Bookmaker implied probability is not a calibrated model prediction.
7. Future models require chronological holdouts and baseline comparisons.

## Phases
P1 schema, ingestion, storage, Android permission shell.
P2 one-frame capture, local OCR, user review, secure synchronization.
P3 event matching and permitted historical data enrichment.
P4 statistical analytics, calibration, dashboard, alerts.
P5 shadow-mode evaluation and safety review. No wagering automation.
