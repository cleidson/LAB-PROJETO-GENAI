from sqlmodel import Session, select

from app.application.contracts.prompt_repository import PromptRepositoryPort
from app.domain.entities.prompt_template import PromptTemplate
from app.infrastructure.models.prompt_model import PromptModel


def _to_domain(model: PromptModel) -> PromptTemplate:
    return PromptTemplate(
        id=model.id,
        title=model.title,
        description=model.description,
        persona=model.persona,
        context=model.context,
        instructions=model.instructions,
        expected_output=model.expected_output,
        tags=list(model.tags),
        status=model.status,
        version=model.version,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def _to_model(prompt: PromptTemplate) -> PromptModel:
    return PromptModel(
        id=prompt.id,
        title=prompt.title,
        description=prompt.description,
        persona=prompt.persona,
        context=prompt.context,
        instructions=prompt.instructions,
        expected_output=prompt.expected_output,
        tags=list(prompt.tags),
        status=prompt.status,
        version=prompt.version,
        created_at=prompt.created_at,
        updated_at=prompt.updated_at,
    )


class PromptRepository(PromptRepositoryPort):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, prompt: PromptTemplate) -> PromptTemplate:
        model = _to_model(prompt)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return _to_domain(model)

    def get_all(self) -> list[PromptTemplate]:
        statement = select(PromptModel).order_by(PromptModel.created_at.desc())
        return [_to_domain(model) for model in self.session.exec(statement).all()]

    def get_by_id(self, prompt_id: str) -> PromptTemplate | None:
        statement = select(PromptModel).where(PromptModel.id == prompt_id)
        model = self.session.exec(statement).first()
        if model is None:
            return None
        return _to_domain(model)

    def update(self, prompt: PromptTemplate) -> PromptTemplate:
        model = self.session.get(PromptModel, prompt.id)
        if model is None:
            model = _to_model(prompt)
        else:
            model.title = prompt.title
            model.description = prompt.description
            model.persona = prompt.persona
            model.context = prompt.context
            model.instructions = prompt.instructions
            model.expected_output = prompt.expected_output
            model.tags = list(prompt.tags)
            model.status = prompt.status
            model.version = prompt.version
            model.created_at = prompt.created_at
            model.updated_at = prompt.updated_at

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return _to_domain(model)

    def delete(self, prompt: PromptTemplate) -> None:
        model = self.session.get(PromptModel, prompt.id)
        if model is not None:
            self.session.delete(model)
        self.session.commit()
