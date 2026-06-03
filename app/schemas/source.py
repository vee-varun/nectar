from datetime import datetime

from app.enums.source import SourceStatus

from pydantic import BaseModel, ConfigDict, HttpUrl


class SourceBase(BaseModel):
    name: str
    rss_url: HttpUrl

    website_url: HttpUrl | None = None

    source_type: str = "rss"

    is_active: bool = True

    fetch_interval_minutes: int = 60

    archive_day_range: int = 30

    metadata_json: dict | None = None


class SourceCreate(SourceBase):
    pass


class SourceUpdate(BaseModel):
    name: str | None = None

    rss_url: HttpUrl | None = None

    website_url: HttpUrl | None = None

    source_type: str | None = None

    is_active: bool | None = None

    fetch_interval_minutes: int | None = None

    archive_day_range: int | None = None

    status: SourceStatus | None = None

    metadata_json: dict | None = None


class SourceResponse(SourceBase):
    id: int

    status: SourceStatus

    last_fetched_at: datetime | None = None

    last_attempted_at: datetime | None = None

    last_error: str | None = None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
