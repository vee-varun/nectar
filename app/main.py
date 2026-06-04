from fastapi import FastAPI

from app.api.v1.entities import router as entities_router
from app.api.v1.news import router as news_router
from app.api.v1.sources import router as sources_router

from app.core.scheduler import scheduler
from app.jobs.rss_runner import run_rss_ingestion
import app.core.logging

app = FastAPI(
    title="News as a Service Lite",
)

@app.on_event("startup")
def startup_event():
    print("=== STARTUP EVENT FIRED ===")
    scheduler.add_job(
        run_rss_ingestion,
        trigger="interval",
        seconds=10,          # adjust frequency
        id="rss_ingestion",
        replace_existing=True,
        max_instances=1      # prevents overlap
    )

    scheduler.start()
    print("=== SCHEDULER STARTED ===")

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown(wait=False)


app.include_router(entities_router)
app.include_router(news_router)
app.include_router(sources_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
