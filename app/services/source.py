from datetime import datetime, timedelta, timezone

from app.enums.source import SourceStatus
from app.models.source import Source
from app.repositories.source import SourceRepository
from app.schemas.source import SourceCreate, SourceUpdate


class SourceService:
    def __init__(self, repo: SourceRepository):
        self.repo = repo

    # -------------------------
    # CRUD
    # -------------------------

    def create_source(self, data: SourceCreate) -> Source:
        source = Source(**data.model_dump(mode="json"))
        return self.repo.create(source)

    def get_source(self, source_id: int) -> Source | None:
        return self.repo.get(source_id)

    def list_sources(self, offset: int = 0, limit: int = 100) -> list[Source]:
        return self.repo.get_all(offset=offset, limit=limit)

    def update_source(self, source_id: int, data: SourceUpdate) -> Source:
        source = self.repo.get(source_id)
        if not source:
            raise ValueError("Source not found")

        update_data = data.model_dump(mode="json", exclude_unset=True)

        for key, value in update_data.items():
            setattr(source, key, value)

        return self.repo.update(source)

    def delete_source(self, source_id: int) -> None:
        source = self.repo.get(source_id)
        if not source:
            raise ValueError("Source not found")

        self.repo.delete(source)

    # -------------------------
    # Status management
    # -------------------------

    def pause_source(self, source_id: int) -> Source:
        source = self.repo.get(source_id)
        if not source:
            raise ValueError("Source not found")

        source.status = SourceStatus.PAUSED
        source.is_active = False

        return self.repo.update(source)

    def activate_source(self, source_id: int) -> Source:
        source = self.repo.get(source_id)
        if not source:
            raise ValueError("Source not found")

        source.status = SourceStatus.ACTIVE
        source.is_active = True

        return self.repo.update(source)

    def mark_failed(self, source: Source, error: str) -> Source:
        source.status = SourceStatus.FAILED
        source.last_error = error
        source.last_attempted_at = datetime.now(timezone.utc)

        return self.repo.update(source)

    def mark_success(self, source: Source) -> Source:
        source.status = SourceStatus.ACTIVE
        source.last_error = None
        source.last_fetched_at = datetime.now(timezone.utc)
        source.last_attempted_at = datetime.now(timezone.utc)

        return self.repo.update(source)

    # -------------------------
    # Scheduler helpers
    # -------------------------

    def get_active_sources(self) -> list[Source]:
        return self.repo.list_active()

    def get_due_sources(self) -> list[Source]:
        """
        Returns sources that should be fetched based on:
        - is_active
        - fetch_interval_minutes
        """
        sources = self.repo.list_active()

        now = datetime.now(timezone.utc)
        due_sources = []

        for source in sources:
            if not source.last_fetched_at:
                due_sources.append(source)
                continue

            next_fetch_time = source.last_fetched_at + timedelta(
                minutes=source.fetch_interval_minutes
            )

            if next_fetch_time <= now:
                due_sources.append(source)

        return due_sources
