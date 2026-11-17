# 1xBet Intelligence Engine

Read-only sports information monitoring and analysis. Phase 1 establishes a user-authorized Android capture shell and a Python observation API.

## Safety
- No automated bets, deposits, withdrawals, or account actions.
- No credentials or private account data are collected.
- Capture is user-initiated and requires Android system consent.
- Only use information visible to you and permitted by the app terms and local law.
- OCR output remains unverified until reviewed by the user.

## Architecture
Android (Kotlin, MediaProjection, on-device OCR) -> reviewed observation -> FastAPI -> SQLite immutable timestamped ledger -> later analytics/dashboard/alerts.

## Backend quick start
```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs

## Android
Open `android/` in Android Studio, install on a physical device, and test the explicit capture-permission flow. The current app is a permission scaffold; OCR, frame capture, and secure sync are next-phase work.

## Phase 1 acceptance
See docs/PHASE_1_CHECKLIST.md. Do not enable continuous capture until the app terms, Android permission flow, and local legal requirements are reviewed.
