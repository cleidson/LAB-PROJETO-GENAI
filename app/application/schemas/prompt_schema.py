from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.domain.enums.prompt_status import PromptStatus


def _normalize_tags(tags: list[str] | None) -> list[str]:
    if not tags:
        return []
    return [tag.strip() for tag in tags if tag and tag.strip()]


class PromptCreateRequest(BaseModel):
    title: str = Field(min_length=1, description="Titulo do prompt")
    description: str | None = None
    persona: str | None = None
    context: str | None = None
    instructions: str = Field(min_length=1)
    expected_output: str = Field(min_length=1)
    tags: list[str] = Field(default_factory=list)
    status: PromptStatus = PromptStatus.DRAFT

    @field_validator("title", "instructions", "expected_output")
    @classmethod
    def validate_required_text(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Este campo e obrigatorio.")
        return cleaned

    @field_validator("description", "persona", "context")
    @classmethod
    def normalize_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        cleaned = value.strip()
        return cleaned or None

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, value: list[str]) -> list[str]:
        return _normalize_tags(value)


class PromptUpdateRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    persona: str | None = None
    context: str | None = None
    instructions: str | None = None
    expected_output: str | None = None
    tags: list[str] | None = None
    status: PromptStatus | None = None

    @field_validator("title", "instructions", "expected_output")
    @classmethod
    def validate_optional_required_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Este campo nao pode ser vazio.")
        return cleaned

    @field_validator("description", "persona", "context")
    @classmethod
    def normalize_optional_update_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        cleaned = value.strip()
        return cleaned or None

    @field_validator("tags")
    @classmethod
    def validate_optional_tags(cls, value: list[str] | None) -> list[str] | None:
        if value is None:
            return None
        return _normalize_tags(value)


class PromptResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    description: str | None = None
    persona: str | None = None
    context: str | None = None
    instructions: str
    expected_output: str
    tags: list[str]
    status: PromptStatus
    version: int
    created_at: str
    updated_at: str


class AnalyzePromptResponse(BaseModel):
    score: int
    classification: str
    suggestions: list[str]


class PriorityAdvisorResponse(BaseModel):
    priority: str
    reason: str
    recommended_action: str


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None
