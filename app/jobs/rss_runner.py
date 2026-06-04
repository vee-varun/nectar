from app.db.session import SessionLocal
from app.jobs.rss_ingestion import RSSIngestionJob
import logging

logger = logging.getLogger(__name__)

def run_rss_ingestion():
    logger.info("=== RSS JOB STARTED ===")
    db = SessionLocal()
    try:
        job = RSSIngestionJob(db)
        job.run()
        db.commit()
        logger.info("=== RSS JOB COMPLETED ===")
    except Exception as e:
        db.rollback()
        logger.info(f"=== RSS JOB FAILED: {e} ===")
        raise
    finally:
        db.close()
