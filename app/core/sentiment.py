from app.services.sentiment import SentimentService

_sentiment_service = None


def get_sentiment_service() -> SentimentService:
    global _sentiment_service

    if _sentiment_service is None:
        _sentiment_service = SentimentService()

    return _sentiment_service
