from uuid import UUID

from sqlalchemy.orm import Session

from app.models.entity import Entity
from app.repositories.entity import EntityRepository
from app.schemas.entity import EntityCreate, EntityUpdate


class EntityService:
    def __init__(self, db: Session):
        self.repository = EntityRepository(db)

    def create_entity(
        self,
        entity_data: EntityCreate,
    ) -> Entity:
        existing = self.repository.get_by_name(
            entity_data.name
        )

        if existing:
            raise ValueError(
                f"Entity '{entity_data.name}' already exists"
            )

        entity = Entity(
            name=entity_data.name,
            ticker=entity_data.ticker,
            aliases=entity_data.aliases,
        )

        return self.repository.create(entity)

    def get_entity(
        self,
        entity_id: UUID,
    ) -> Entity | None:
        return self.repository.get_by_id(entity_id)

    def list_entities(
        self,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Entity]:
        return self.repository.list(
            offset=offset,
            limit=limit,
        )

    def update_entity(
        self,
        entity_id: UUID,
        data: EntityUpdate,
    ) -> Entity | None:
        entity = self.repository.get_by_id(entity_id)

        if not entity:
            return None

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(entity, field, value)

        self.repository.db.commit()
        self.repository.db.refresh(entity)

        return entity

    def delete_entity(
        self,
        entity_id: UUID,
    ) -> bool:
        entity = self.repository.get_by_id(entity_id)

        if not entity:
            return False

        self.repository.delete(entity)

        return True
