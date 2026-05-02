from datetime import datetime

from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel

from app.domain.enums.prompt_status import PromptStatus


class PromptModel(SQLModel, table=True):
    id: str = Field(primary_key=True)
    title: str
    description: str | None = None
    persona: str | None = None
    context: str | None = None
    instructions: str
    expected_output: str
    tags: list[str] = Field(default_factory=list, sa_column=Column(JSON, nullable=False))
    status: PromptStatus = Field(default=PromptStatus.DRAFT)
    version: int = Field(default=1, nullable=False)
    created_at: datetime
    updated_at: datetime
