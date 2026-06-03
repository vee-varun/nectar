from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.repositories.source import SourceRepository
from app.schemas.source import (
    SourceCreate,
    SourceResponse,
    SourceUpdate,
)
from app.services.source import SourceService

router = APIRouter(
    prefix="/sources",
    tags=["Sources"],
)

DBSession = Annotated[Session, Depends(get_db)]

def get_source_service(
    db: DBSession,
) -> SourceService:
    repo = SourceRepository(db)
    return SourceService(repo)

@router.get(
    "",
    response_model=list[SourceResponse],
)
def list_sources(
    db: DBSession,
):
    service = get_source_service(db)
    return service.list_sources()


@router.get(
    "/{source_id}",
    response_model=SourceResponse,
)
def get_source(
    source_id: int,
    db: DBSession,
):
    service = get_source_service(db)

    source = service.get_source(source_id)

    if not source:
        raise HTTPException(
            status_code=404,
            detail="Source not found",
        )

    return source

@router.post(
    "",
    response_model=SourceResponse,
    status_code=201,
)
def create_source(
    payload: SourceCreate,
    db: DBSession,
):
    service = get_source_service(db)

    return service.create_source(payload)



@router.put(
    "/{source_id}",
    response_model=SourceResponse,
)
def update_source(
    source_id: int,
    payload: SourceUpdate,
    db: DBSession,
):
    service = get_source_service(db)

    try:
        return service.update_source(
            source_id,
            payload,
        )

    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Source not found",
        )

@router.delete(
    "/{source_id}",
    status_code=204,
)
def delete_source(
    source_id: int,
    db: DBSession,
):
    service = get_source_service(db)

    try:
        service.delete_source(source_id)

    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Source not found",
        )

@router.post(
    "/{source_id}/pause",
    response_model=SourceResponse,
)
def pause_source(
    source_id: int,
    db: DBSession,
):
    service = get_source_service(db)

    try:
        return service.pause_source(source_id)

    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Source not found",
        )


