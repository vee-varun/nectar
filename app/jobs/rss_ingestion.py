import feedparser
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.repositories.source import SourceRepository
from app.services.source import SourceService
from app.models.news import News
from app.models.news import SentimentEnum
from app.services.sentiment import SentimentService
import logging
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)

class RSSIngestionJob:
    def __init__(self, db: Session):
        self.db = db
        self.source_repo = SourceRepository(db)
        self.source_service = SourceService(self.source_repo)
        self.sentiment_service = SentimentService()
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
        if description:
            description = BeautifulSoup(description, "html.parser").get_text(separator=" ", strip=True)

        if not title or not url:
            return  # skip bad entries
       
        sentiment = None
        if title or description:
            try:
                sentiment = self.sentiment_service.analyze(title, description,)
                if sentiment:
                    try:
                        sentiment = SentimentEnum[sentiment.upper()]
                    except KeyError:
                        sentiment = None
            except Exception as err:
                logger.error(f'Error while analysing the sentiment for the news with URL: {url} | Error: {err}')

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
            description=description,
            published_date=published_at,
            source_id=source.id,
            entity_id='11111111-1111-1111-1111-111111111111',
            created_at=datetime.now(timezone.utc),
            sentiment=sentiment,
        )

        self.db.add(news)

    # -------------------------
    # Date parsing helper
    # -------------------------
    def _parse_date(self, entry):
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            return datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)

        return datetime.now(timezone.utc)
