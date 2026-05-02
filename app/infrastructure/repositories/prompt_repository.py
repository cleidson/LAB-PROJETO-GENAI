from sqlmodel import Session, select

from app.domain.entities.prompt_template import PromptTemplate


class PromptRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, prompt: PromptTemplate) -> PromptTemplate:
        self.session.add(prompt)
        self.session.commit()
        self.session.refresh(prompt)
        return prompt

    def get_all(self) -> list[PromptTemplate]:
        statement = select(PromptTemplate).order_by(PromptTemplate.created_at.desc())
        return list(self.session.exec(statement).all())

    def get_by_id(self, prompt_id: str) -> PromptTemplate | None:
        statement = select(PromptTemplate).where(PromptTemplate.id == prompt_id)
        return self.session.exec(statement).first()

    def update(self, prompt: PromptTemplate) -> PromptTemplate:
        self.session.add(prompt)
        self.session.commit()
        self.session.refresh(prompt)
        return prompt

    def delete(self, prompt: PromptTemplate) -> None:
        self.session.delete(prompt)
        self.session.commit()
