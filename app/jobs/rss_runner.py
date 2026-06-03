from app.db.session import SessionLocal
from app.jobs.rss_ingestion import RSSIngestionJob


def run_rss_ingestion():
    db = SessionLocal()
    try:
        job = RSSIngestionJob(db)
        job.run()
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
