import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "observations.sqlite3"

def connect():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    with connect() as con:
        con.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sport TEXT NOT NULL,
            competition TEXT,
            event_name TEXT NOT NULL,
            event_start_utc TEXT,
            market_name TEXT NOT NULL,
            selection_name TEXT NOT NULL,
            decimal_odds REAL NOT NULL CHECK(decimal_odds > 1),
            captured_at_utc TEXT NOT NULL,
            source TEXT NOT NULL,
            ocr_confidence REAL NOT NULL CHECK(ocr_confidence >= 0 AND ocr_confidence <= 1),
            review_status TEXT NOT NULL CHECK(review_status IN ('pending','verified','rejected')),
            created_at_utc TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """)
        con.execute("CREATE INDEX IF NOT EXISTS idx_obs_event_time ON observations(event_name, captured_at_utc)")
        con.execute("CREATE INDEX IF NOT EXISTS idx_obs_sport_time ON observations(sport, captured_at_utc)")
