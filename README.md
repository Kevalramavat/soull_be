# Soull Backend

FastAPI backend for the Soull application.

## Prerequisites

- [uv](https://github.com/astral-sh/uv)
- PostgreSQL

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Configuration:
   Create a `.env` file in the `soull_be` directory and set your `DATABASE_URL`:
   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/soull_db
   ```

3. Run Database Migrations:
   ```bash
   uv run alembic upgrade head
   ```

4. Run the development server:
   ```bash
   uv run uvicorn app.main:app --reload
   ```

## API Documentation

Once the server is running, you can access the interactive documentation at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Database Structure

- `app/core/config.py`: Settings and environment variables management.
- `app/core/database.py`: SQLAlchemy async engine and sessionmaker.
- `app/api/deps.py`: Dependency injection for database sessions.
- `app/models/base.py`: Declarative base class for all models.
- `app/models/user.py`: Sample User model.
- `migrations/`: Alembic migration scripts and configuration.
- `migrations/env.py`: Asynchronous migration runner.
