from uuid import UUID

from fastapi import APIRouter, HTTPException, Query

from app.db.dependencies import DBSession
from app.schemas.entity import EntityResponse
from app.schemas.news import (
    NewsApiResponse,
    NewsResponse,
    PressNewsResponse,
)
from app.services.entity import EntityService
from app.services.news import NewsService

router = APIRouter(
    prefix="/entities",
    tags=["Entities"],
)


@router.get(
    "",
    response_model=list[EntityResponse],
)
def list_entities(
    db: DBSession,
):
    service = EntityService(db)

    return service.list_entities()


@router.get(
    "/{entity_id}",
    response_model=EntityResponse,
)
def get_entity(
    entity_id: UUID,
    db: DBSession,
):
    service = EntityService(db)

    entity = service.get_entity(entity_id)

    if not entity:
        raise HTTPException(
            status_code=404,
            detail="Entity not found",
        )

    return entity


@router.get(
    "/{entity_id}/news",
    response_model=NewsApiResponse,
)
def get_entity_news(
    entity_id: UUID,
    db: DBSession,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=1000),
):
    entity_service = EntityService(db)
    news_service = NewsService(db)

    entity = entity_service.get_entity(entity_id)

    if not entity:
        raise HTTPException(
            status_code=404,
            detail="Entity not found",
        )

    news_items = news_service.get_news_by_entity(
        entity_id=entity_id,
        offset=offset,
        limit=limit,
    )

    return NewsApiResponse(
        response_data=PressNewsResponse(
            press_news=[
                NewsResponse.model_validate(news)
                for news in news_items
            ]
        )
    )
