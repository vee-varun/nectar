from uuid import uuid4

from sqlalchemy import String, DateTime, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Entity(Base):
    __tablename__ = "entities"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    ticker: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        index=True,
    )

    exchange: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    sector: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    industry: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    website: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
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

    news = relationship(
        "News",
        back_populates="entity",
        cascade="all, delete-orphan",
    )

    aliases: Mapped[list[str] | None] = mapped_column(
        ARRAY(String),
        nullable=True,
    )

    def __repr__(self):
        return f"<Entity(id={self.id}, name='{self.name}')>"
