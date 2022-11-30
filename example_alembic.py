alembic init alembic
alembic revision -m "revision database"
alembic upgrade {revision value located in alembic file}
alembic current  --> shows current revision table
alembic heads --> refers to latest revision
alembic upgrade head --> upgrades to newest revision
alembic upgrade +1 --> upgrade one level
alembic downgrade -1 OR {revision number}--> rollback / downgrade
alembic history
alembic revision --autogenerate -m "auto-vote" --> looks into models because we imported the models via from app.models import Base
and we passed it into the target_metadata
