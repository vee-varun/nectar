#!/bin/sh

set -e

echo "Generating migrations..."
alembic revision --autogenerate -m "auto_migration" || true

echo "Running migrations..."
alembic upgrade head

echo "Starting API..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
