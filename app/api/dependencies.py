from fastapi import Depends
from sqlmodel import Session

from app.application.services.priority_advisor import PriorityAdvisor
from app.application.services.prompt_analyzer import PromptAnalyzer
from app.application.services.prompt_service import PromptService
from app.application.use_cases.prompt_use_cases import PromptUseCases
from app.infrastructure.database import get_session
from app.infrastructure.repositories.prompt_repository import PromptRepository


def get_prompt_service(session: Session = Depends(get_session)) -> PromptService:
    """Centraliza a composicao do servico principal da API."""
    repository = PromptRepository(session)
    use_cases = PromptUseCases(repository)
    analyzer = PromptAnalyzer()
    priority_advisor = PriorityAdvisor()
    return PromptService(use_cases, analyzer, priority_advisor)
