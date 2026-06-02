from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.entity import Entity


class EntityRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, entity: Entity) -> Entity:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def get_by_id(self, entity_id: UUID) -> Entity | None:
        stmt = select(Entity).where(Entity.id == entity_id)
        return self.db.scalar(stmt)

    def get_by_name(self, name: str) -> Entity | None:
        stmt = select(Entity).where(Entity.name == name)
        return self.db.scalar(stmt)

    def get_by_ticker(self, ticker: str) -> Entity | None:
        stmt = select(Entity).where(Entity.ticker == ticker)
        return self.db.scalar(stmt)

    def list(self, offset: int = 0, limit: int = 100) -> list[Entity]:
        stmt = (
            select(Entity)
            .offset(offset)
            .limit(limit)
            .order_by(Entity.name)
        )
        return list(self.db.scalars(stmt).all())

    def delete(self, entity: Entity) -> None:
        self.db.delete(entity)
        self.db.commit()
