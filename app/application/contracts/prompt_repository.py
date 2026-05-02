from abc import ABC, abstractmethod

from app.domain.entities.prompt_template import PromptTemplate


class PromptRepositoryPort(ABC):
    @abstractmethod
    def create(self, prompt: PromptTemplate) -> PromptTemplate:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[PromptTemplate]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, prompt_id: str) -> PromptTemplate | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, prompt: PromptTemplate) -> PromptTemplate:
        raise NotImplementedError

    @abstractmethod
    def delete(self, prompt: PromptTemplate) -> None:
        raise NotImplementedError
