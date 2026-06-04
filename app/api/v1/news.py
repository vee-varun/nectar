from uuid import UUID

from fastapi import APIRouter, Query, HTTPException

from app.db.dependencies import DBSession
from app.schemas.news import NewsResponse
from app.services.news import NewsService

router = APIRouter(
    prefix="/news",
    tags=["News"],
)


@router.get(
    "",
    response_model=list[NewsResponse],
)
def list_news(
    db: DBSession,
    company_name: str | None = Query(
        default=None,
        description="Search in title, description and url",
    ),
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=1000),
):
    service = NewsService(db)

    return service.list_news(
        company_name=company_name,
        offset=offset,
        limit=limit,
    )


@router.get(
    "/{news_id}",
    response_model=NewsResponse,
)
def get_news(
    news_id: UUID,
    db: DBSession,
):
    service = NewsService(db)

    news = service.get_news(news_id)

    if not news:
        raise HTTPException(
            status_code=404,
            detail="News not found",
        )

    return news
