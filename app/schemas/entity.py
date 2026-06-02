from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class EntityBase(BaseModel):
    name: str
    ticker: str | None = None
    aliases: list[str] = []


class EntityCreate(EntityBase):
    pass


class EntityUpdate(BaseModel):
    name: str | None = None
    ticker: str | None = None
    aliases: list[str] | None = None


class EntityResponse(EntityBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
