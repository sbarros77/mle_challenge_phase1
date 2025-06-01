from sqlalchemy import Engine, create_engine


def get_engine() -> Engine:
    """
    Create and return a SQLAlchemy engine for the PostgreSQL database.
    """
    return create_engine(
        url="postgresql://dba:F3rr4r1!2025@fiap-pb-db.postgres.database.azure.com:5432/embrapa_wine", echo=True
    )
