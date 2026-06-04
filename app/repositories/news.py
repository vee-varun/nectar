from datetime import date
from uuid import UUID

from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.models.news import News


class NewsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, news: News) -> News:
        self.db.add(news)
        self.db.commit()
        self.db.refresh(news)
        return news

    def get_by_id(self, news_id: UUID) -> News | None:
        stmt = select(News).where(News.id == news_id)
        return self.db.scalar(stmt)

    def get_by_url(self, url: str) -> News | None:
        stmt = select(News).where(News.url == url)
        return self.db.scalar(stmt)

    def get_by_entity(
        self,
        entity_id: UUID,
        offset: int = 0,
        limit: int = 100,
    ) -> list[News]:
        stmt = (
            select(News)
            .where(News.entity_id == entity_id)
            .order_by(News.published_date.desc())
            .offset(offset)
            .limit(limit)
        )

        return list(self.db.scalars(stmt).all())

    def get_by_sentiment(
        self,
        sentiment: str,
        offset: int = 0,
        limit: int = 100,
    ) -> list[News]:
        stmt = (
            select(News)
            .where(News.sentiment == sentiment)
            .order_by(News.published_date.desc())
            .offset(offset)
            .limit(limit)
        )

        return list(self.db.scalars(stmt).all())

    def get_by_date_range(
        self,
        start_date: date,
        end_date: date,
    ) -> list[News]:
        stmt = (
            select(News)
            .where(
                News.published_date >= start_date,
                News.published_date <= end_date,
            )
            .order_by(News.published_date.desc())
        )

        return list(self.db.scalars(stmt).all())

    def list(
        self,
        company_name: str | None = None,
        offset: int = 0,
        limit: int = 100,
    ) -> list[News]:
        stmt = select(News)
        print(f"repo company_name={company_name}")
        if company_name:
            search_term = f"%{company_name}%"

            stmt = stmt.where(
                or_(
                    News.title.ilike(search_term),
                    News.description.ilike(search_term),
                    News.url.ilike(search_term),
                )
            )

        stmt = (
            stmt
            .order_by(News.published_date.desc())
            .offset(offset)
            .limit(limit)
        )

        return list(self.db.scalars(stmt).all())

    def delete(self, news: News) -> None:
        self.db.delete(news)
        self.db.commit()
