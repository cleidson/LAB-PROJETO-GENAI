from app.application.contracts.prompt_repository import PromptRepositoryPort
from app.application.schemas.prompt_schema import PromptCreateRequest, PromptUpdateRequest
from app.domain.entities.prompt_template import PromptTemplate, utcnow


class PromptNotFoundError(Exception):
    pass


class PromptValidationError(Exception):
    pass


class PromptUseCases:
    def __init__(self, repository: PromptRepositoryPort) -> None:
        self.repository = repository

    def create_prompt(self, payload: PromptCreateRequest) -> PromptTemplate:
        if not payload.title or not payload.instructions or not payload.expected_output:
            raise PromptValidationError("Title, instructions e expected_output sao obrigatorios.")

        prompt = PromptTemplate(
            title=payload.title,
            description=payload.description,
            persona=payload.persona,
            context=payload.context,
            instructions=payload.instructions,
            expected_output=payload.expected_output,
            tags=payload.tags,
            status=payload.status,
        )
        return self.repository.create(prompt)

    def list_prompts(self) -> list[PromptTemplate]:
        return self.repository.get_all()

    def get_prompt(self, prompt_id: str) -> PromptTemplate:
        prompt = self.repository.get_by_id(prompt_id)
        if prompt is None:
            raise PromptNotFoundError("Prompt nao encontrado.")
        return prompt

    def update_prompt(self, prompt_id: str, payload: PromptUpdateRequest) -> PromptTemplate:
        prompt = self.get_prompt(prompt_id)
        updates = payload.model_dump(exclude_unset=True)

        if not updates:
            raise PromptValidationError("Informe ao menos um campo para atualizar.")

        for field_name, value in updates.items():
            setattr(prompt, field_name, value)

        prompt.version += 1
        prompt.updated_at = utcnow()
        return self.repository.update(prompt)

    def delete_prompt(self, prompt_id: str) -> None:
        prompt = self.get_prompt(prompt_id)
        self.repository.delete(prompt)
