from enum import Enum
from uuid import uuid4

from sqlalchemy import (
    String,
    Text,
    Date,
    DateTime,
    ForeignKey,
    Enum as SqlEnum,
    JSON,
    Index,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.db.base import Base


class SentimentEnum(str, Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"


class News(Base):
    __tablename__ = "news"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    entity_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("entities.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    title: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    url: Mapped[str] = mapped_column(
        String(2048),
        nullable=False,
        unique=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    source_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    author: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    published_date: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        index=True,
    )

    sentiment: Mapped[SentimentEnum] = mapped_column(
        SqlEnum(
            SentimentEnum,
            name="sentiment_enum",
        ),
        nullable=False,
        default=SentimentEnum.NEUTRAL,
        index=True,
    )

    news_metadata: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    language: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True,
        default="en",
    )

    article_hash: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
        unique=True,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    entity = relationship(
        "Entity",
        back_populates="news",
    )

    __table_args__ = (
        Index("idx_news_entity_date", "entity_id", "published_date"),
        Index("idx_news_sentiment_date", "sentiment", "published_date"),
        Index("idx_news_source_date", "source_name", "published_date"),
    )

    def __repr__(self):
        return (
            f"<News(id={self.id}, "
            f"title='{self.title[:50]}', "
            f"sentiment='{self.sentiment}')>"
        )
