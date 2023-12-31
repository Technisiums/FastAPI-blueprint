""""
env file for alembic migrations
"""
from logging.config import fileConfig

from alembic import context
from app.database.models import Base
import alembic
from sqlalchemy import engine_from_config, create_engine, pool


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

from app.config.settings import settings

config.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URI)


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    create_engine(settings.SQLALCHEMY_DATABASE_URI, isolation_level="AUTOCOMMIT")
    # drop testing db if it exists and create a fresh one
    # with default_engine.connect() as default_conn:
    #     default_conn.execute(f"DROP DATABASE IF EXISTS {DATABASE_CREFO_DB}_test")
    #     default_conn.execute(f"CREATE DATABASE {DATABASE_CREFO_DB}_test")
    connectable = config.attributes.get("connection", None)
    config.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URI)

    if connectable is None:
        connectable = engine_from_config(
            config.get_section(config.config_ini_section),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

    with connectable.connect() as connection:
        alembic.context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with alembic.context.begin_transaction():
            alembic.context.run_migrations()


run_migrations_offline()
