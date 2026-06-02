# app/db/dependencies.py

from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from fastapi import Depends
from typing import Annotated

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

DBSession = Annotated[
    Session,
    Depends(get_db)
]
