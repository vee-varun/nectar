# News as a Service Lite

A lightweight FastAPI service for storing, managing, and serving news articles associated with entities (companies, organizations, brands, etc.).

## Tech Stack

* Python 3.10+
* FastAPI
* PostgreSQL
* SQLAlchemy 2.x
* Alembic
* Pydantic Settings
* Docker & Docker Compose

---

# Project Structure

```text
app/
├── api/
├── core/
│   └── config.py
├── db/
│   ├── base.py
│   ├── dependencies.py
│   └── session.py
├── models/
│   ├── entity.py
│   └── news.py
├── repositories/
├── schemas/
├── services/
└── main.py

alembic/
docker-compose.yml
Dockerfile
requirements.txt
.env
```

---

# Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@postgres:5432/newsdb
```

For local development without Docker:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/newsdb
```

---

# Running with Docker

## Build Containers

```bash
docker compose build
```

## Start Services

```bash
docker compose up -d
```

Verify containers:

```bash
docker ps
```

---

# Database Migrations

## Create Migration

```bash
docker compose exec api alembic revision --autogenerate -m "initial schema"
```

## Apply Migration

```bash
docker compose exec api alembic upgrade head
```

## Migration History

```bash
docker compose exec api alembic history
```

## Current Version

```bash
docker compose exec api alembic current
```

---

# Access PostgreSQL

Connect to PostgreSQL container:

```bash
docker compose exec postgres psql -U postgres -d newsdb
```

List tables:

```sql
\dt
```

Describe table:

```sql
\d entities
\d news
```

Exit:

```sql
\q
```

---

# Running FastAPI Locally

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# Common Commands

## Stop Containers

```bash
docker compose down
```

## Restart Containers

```bash
docker compose restart
```

## Rebuild After Dependency Changes

```bash
docker compose up --build -d
```

## View Logs

```bash
docker compose logs -f api
```

## Open Shell in API Container

```bash
docker compose exec api bash
```

---

# Development Workflow

1. Modify SQLAlchemy models.
2. Generate Alembic migration.
3. Review migration file.
4. Apply migration.
5. Implement repository layer.
6. Implement service layer.
7. Expose API endpoints.
8. Write tests.
9. Build Docker image.
10. Deploy.

---

# Initial Setup Checklist

* [ ] Create `.env`
* [ ] Build Docker image
* [ ] Start containers
* [ ] Generate migration
* [ ] Apply migration
* [ ] Verify tables in PostgreSQL
* [ ] Run FastAPI
* [ ] Open Swagger UI
* [ ] Start API development

```
```

