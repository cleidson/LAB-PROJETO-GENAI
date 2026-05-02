from dataclasses import asdict

from fastapi import APIRouter, Depends, HTTPException, status

from app.application.schemas.prompt_schema import (
    AnalyzePromptResponse,
    ApiResponse,
    PriorityAdvisorResponse,
    PromptCreateRequest,
    PromptResponse,
    PromptUpdateRequest,
)
from app.api.dependencies import get_prompt_service
from app.application.services.prompt_service import PromptService
from app.application.use_cases.prompt_use_cases import PromptNotFoundError, PromptValidationError
from app.domain.entities.prompt_template import PromptTemplate

router = APIRouter(prefix="/api/prompts", tags=["prompts"])


def _to_prompt_response(prompt: PromptTemplate) -> PromptResponse:
    """Mapeia a entidade de dominio para o contrato HTTP de resposta."""
    data = asdict(prompt)
    data["created_at"] = prompt.created_at.isoformat()
    data["updated_at"] = prompt.updated_at.isoformat()
    return PromptResponse(**data)


@router.post("", response_model=PromptResponse, status_code=status.HTTP_201_CREATED)
def create_prompt(payload: PromptCreateRequest, service: PromptService = Depends(get_prompt_service)) -> PromptResponse:
    """Cria um novo prompt e retorna sua representacao completa."""
    try:
        prompt = service.create_prompt(payload)
        return _to_prompt_response(prompt)
    except PromptValidationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("", response_model=list[PromptResponse])
def list_prompts(service: PromptService = Depends(get_prompt_service)) -> list[PromptResponse]:
    """Lista os prompts cadastrados em ordem de criacao mais recente."""
    return [_to_prompt_response(prompt) for prompt in service.list_prompts()]


@router.get("/{prompt_id}", response_model=PromptResponse)
def get_prompt(prompt_id: str, service: PromptService = Depends(get_prompt_service)) -> PromptResponse:
    """Consulta um prompt existente pelo identificador."""
    try:
        return _to_prompt_response(service.get_prompt(prompt_id))
    except PromptNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put("/{prompt_id}", response_model=PromptResponse)
def update_prompt(
    prompt_id: str,
    payload: PromptUpdateRequest,
    service: PromptService = Depends(get_prompt_service),
) -> PromptResponse:
    """Atualiza um prompt existente usando payload parcial."""
    try:
        return _to_prompt_response(service.update_prompt(prompt_id, payload))
    except PromptNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except PromptValidationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.delete("/{prompt_id}", response_model=ApiResponse)
def delete_prompt(prompt_id: str, service: PromptService = Depends(get_prompt_service)) -> ApiResponse:
    """Remove um prompt existente."""
    try:
        service.delete_prompt(prompt_id)
        return ApiResponse(success=True, message="Prompt removido com sucesso.")
    except PromptNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post("/{prompt_id}/analyze", response_model=AnalyzePromptResponse)
def analyze_prompt(prompt_id: str, service: PromptService = Depends(get_prompt_service)) -> AnalyzePromptResponse:
    """Executa a analise local de qualidade de um prompt."""
    try:
        return AnalyzePromptResponse(**asdict(service.analyze_prompt(prompt_id)))
    except PromptNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post("/{prompt_id}/priority", response_model=PriorityAdvisorResponse)
def calculate_priority(
    prompt_id: str,
    service: PromptService = Depends(get_prompt_service),
) -> PriorityAdvisorResponse:
    """Calcula a prioridade de melhoria ou uso de um prompt."""
    try:
        return PriorityAdvisorResponse(**asdict(service.calculate_priority(prompt_id)))
    except PromptNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
