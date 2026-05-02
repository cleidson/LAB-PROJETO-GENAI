import os
from functools import lru_cache
from typing import Generator

from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()

DEFAULT_DATABASE_URL = "sqlite:///./prompthub.db"


def _resolve_database_url() -> str:
    return os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)


@lru_cache(maxsize=1)
def get_engine():
    database_url = _resolve_database_url()
    connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
    return create_engine(database_url, echo=False, connect_args=connect_args)


def get_session() -> Generator[Session, None, None]:
    with Session(get_engine()) as session:
        yield session


def create_db_and_tables() -> None:
    from app.infrastructure.models.prompt_model import PromptModel  # noqa: F401

    SQLModel.metadata.create_all(get_engine())
