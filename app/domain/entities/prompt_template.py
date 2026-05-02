from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4

from app.domain.enums.prompt_status import PromptStatus


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class PromptTemplate:
    title: str
    instructions: str
    expected_output: str
    description: str | None = None
    persona: str | None = None
    context: str | None = None
    tags: list[str] = field(default_factory=list)
    status: PromptStatus = PromptStatus.DRAFT
    id: str = field(default_factory=lambda: str(uuid4()))
    version: int = 1
    created_at: datetime = field(default_factory=utcnow)
    updated_at: datetime = field(default_factory=utcnow)
