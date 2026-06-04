from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class NewsBase(BaseModel):
    title: str
    url: str
    description: str | None = None
    published_date: datetime

    sentiment: str | None = None

    source_id: int

    news_metadata: dict | None = None


class NewsCreate(NewsBase):
    entity_id: UUID


class NewsUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    sentiment: str | None = None
    news_metadata: dict | None = None


class NewsResponse(NewsBase):
    id: UUID
    entity_id: UUID

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PressNewsResponse(BaseModel):
    press_news: list[NewsResponse]


class NewsApiResponse(BaseModel):
    response_data: PressNewsResponse
