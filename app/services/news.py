from datetime import date
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.news import News
from app.repositories.news import NewsRepository
from app.schemas.news import NewsCreate, NewsUpdate


class NewsService:
    def __init__(self, db: Session):
        self.repository = NewsRepository(db)

    def create_news(
        self,
        news_data: NewsCreate,
    ) -> News:
        existing = self.repository.get_by_url(
            news_data.url
        )

        if existing:
            return existing

        news = News(
            entity_id=news_data.entity_id,
            title=news_data.title,
            url=news_data.url,
            description=news_data.description,
            published_date=news_data.published_date,
            sentiment=news_data.sentiment,
            source_name=news_data.source_name,
            news_metadata=news_data.news_metadata,
        )

        return self.repository.create(news)

    def get_news(
        self,
        news_id: UUID,
    ) -> News | None:
        return self.repository.get_by_id(news_id)

    def get_news_by_entity(
        self,
        entity_id: UUID,
        offset: int = 0,
        limit: int = 100,
    ) -> list[News]:
        return self.repository.get_by_entity(
            entity_id=entity_id,
            offset=offset,
            limit=limit,
        )

    def get_news_by_sentiment(
        self,
        sentiment: str,
        offset: int = 0,
        limit: int = 100,
    ) -> list[News]:
        return self.repository.get_by_sentiment(
            sentiment=sentiment,
            offset=offset,
            limit=limit,
        )

    def get_news_by_date_range(
        self,
        start_date: date,
        end_date: date,
    ) -> list[News]:
        return self.repository.get_by_date_range(
            start_date=start_date,
            end_date=end_date,
        )

    def list_news(
        self,
        offset: int = 0,
        limit: int = 100,
    ) -> list[News]:
        return self.repository.list(
            offset=offset,
            limit=limit,
        )

    def update_news(
        self,
        news_id: UUID,
        data: NewsUpdate,
    ) -> News | None:
        news = self.repository.get_by_id(news_id)

        if not news:
            return None

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(news, field, value)

        self.repository.db.commit()
        self.repository.db.refresh(news)

        return news

    def delete_news(
        self,
        news_id: UUID,
    ) -> bool:
        news = self.repository.get_by_id(news_id)

        if not news:
            return False

        self.repository.delete(news)

        return True
