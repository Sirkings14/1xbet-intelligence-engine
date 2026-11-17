from datetime import datetime, timezone
from typing import Literal
from pydantic import BaseModel, Field, field_validator

Sport = Literal["football", "basketball", "tennis", "volleyball", "hockey", "baseball", "esports", "other"]
ReviewStatus = Literal["pending", "verified", "rejected"]

class ObservationIn(BaseModel):
    sport: Sport
    competition: str | None = Field(default=None, max_length=160)
    event_name: str = Field(min_length=2, max_length=240)
    event_start_utc: datetime | None = None
    market_name: str = Field(min_length=1, max_length=160)
    selection_name: str = Field(min_length=1, max_length=160)
    decimal_odds: float = Field(gt=1.0, le=10000)
    captured_at_utc: datetime
    source: Literal["android_screen_user_capture", "manual_entry"] = "manual_entry"
    ocr_confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    review_status: ReviewStatus = "pending"

    @field_validator("captured_at_utc", "event_start_utc")
    @classmethod
    def require_timezone(cls, value):
        if value is not None and value.tzinfo is None:
            raise ValueError("Datetime must include a timezone")
        return value.astimezone(timezone.utc) if value else value
