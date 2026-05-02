from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel

from app.domain.enums.prompt_status import PromptStatus


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class PromptTemplate(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    title: str
    description: str | None = None
    persona: str | None = None
    context: str | None = None
    instructions: str
    expected_output: str
    tags: list[str] = Field(default_factory=list, sa_column=Column(JSON, nullable=False))
    status: PromptStatus = Field(default=PromptStatus.DRAFT)
    version: int = Field(default=1, nullable=False)
    created_at: datetime = Field(default_factory=utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=utcnow, nullable=False)
