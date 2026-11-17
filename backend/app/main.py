from fastapi import FastAPI, Query
from .db import connect, init_db
from .schemas import ObservationIn

app = FastAPI(title="1xBet Intelligence Engine API", version="0.1.0",
              description="Read-only observation ingestion and audit API. No betting execution.")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok", "service": "observation-api"}

@app.post("/observations", status_code=201)
def create_observation(item: ObservationIn):
    p = item.model_dump()
    with connect() as con:
        cur = con.execute("""
            INSERT INTO observations (
                sport, competition, event_name, event_start_utc, market_name,
                selection_name, decimal_odds, captured_at_utc, source,
                ocr_confidence, review_status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["sport"], p["competition"], p["event_name"],
            p["event_start_utc"].isoformat() if p["event_start_utc"] else None,
            p["market_name"], p["selection_name"], p["decimal_odds"],
            p["captured_at_utc"].isoformat(), p["source"],
            p["ocr_confidence"], p["review_status"]
        ))
        return {"id": cur.lastrowid, "stored": True, "review_status": p["review_status"]}

@app.get("/observations")
def list_observations(limit: int = Query(default=100, ge=1, le=500), sport: str | None = None):
    sql, params = "SELECT * FROM observations", []
    if sport:
        sql += " WHERE sport = ?"
        params.append(sport)
    sql += " ORDER BY captured_at_utc DESC LIMIT ?"
    params.append(limit)
    with connect() as con:
        rows = con.execute(sql, params).fetchall()
        return {"count": len(rows), "items": [dict(row) for row in rows]}
