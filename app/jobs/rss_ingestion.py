import feedparser
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.repositories.source import SourceRepository
from app.services.source import SourceService
from app.models.news import News

class RSSIngestionJob:
    def __init__(self, db: Session):
        self.db = db
        self.source_repo = SourceRepository(db)
        self.source_service = SourceService(self.source_repo)

    # -------------------------
    # Public entry point
    # -------------------------
    def run(self):
        sources = self.source_service.get_due_sources()

        for source in sources:
            try:
                self._process_source(source)
                self.source_service.mark_success(source)

            except Exception as e:
                self.source_service.mark_failed(source, str(e))

    # -------------------------
    # Process single RSS source
    # -------------------------
    def _process_source(self, source):
        feed = feedparser.parse(source.rss_url)

        if not feed or not hasattr(feed, "entries"):
            raise ValueError(f"Invalid RSS feed: {source.rss_url}")

        for entry in feed.entries:
            self._process_entry(source, entry)

    # -------------------------
    # Process single RSS entry
    # -------------------------
    def _process_entry(self, source, entry):
        title = getattr(entry, "title", None)
        url = getattr(entry, "link", None)
        description = getattr(entry, "description", None)

        if not title or not url:
            return  # skip bad entries

        # simple dedup (VERY important)
        existing = (
            self.db.query(News)
            .filter(News.url == url)
            .first()
        )

        if existing:
            return

        published_at = self._parse_date(entry)

        news = News(
            title=title,
            url=url,
            content=description,
            published_date=published_at,
            source_id=source.id,
            source_name=source.name,  # optional denormalized field
            created_at=datetime.now(timezone.utc),
        )

        self.db.add(news)

    # -------------------------
    # Date parsing helper
    # -------------------------
    def _parse_date(self, entry):
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            return datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)

        return datetime.now(timezone.utc)
