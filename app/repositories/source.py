from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.source import Source


class SourceRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, source_id: int) -> Source | None:
        stmt = select(Source).where(Source.id == source_id)
        return self.db.scalar(stmt)

    def get_by_name(self, name: str) -> Source | None:
        stmt = select(Source).where(Source.name == name)
        return self.db.scalar(stmt)

    def get_by_rss_url(self, rss_url: str) -> Source | None:
        stmt = select(Source).where(Source.rss_url == rss_url)
        return self.db.scalar(stmt)

    def get_all(
        self,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Source]:
        stmt = (
            select(Source)
            .offset(offset)
            .limit(limit)
            .order_by(Source.id)
        )

        return list(self.db.scalars(stmt).all())

    def list_active(self) -> list[Source]:
        stmt = (
            select(Source)
            .where(Source.is_active.is_(True))
            .order_by(Source.id)
        )

        return list(self.db.scalars(stmt).all())

    def create(self, source: Source) -> Source:
        self.db.add(source)
        self.db.commit()
        self.db.refresh(source)
        return source

    def update(self, source: Source) -> Source:
        self.db.commit()
        self.db.refresh(source)
        return source

    def delete(self, source: Source) -> None:
        self.db.delete(source)
        self.db.commit()
