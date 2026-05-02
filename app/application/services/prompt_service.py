from app.application.dto.prompt_results import PromptAnalysisResult, PromptPriorityResult
from app.application.schemas.prompt_schema import PromptCreateRequest, PromptUpdateRequest
from app.application.services.priority_advisor import PriorityAdvisor
from app.application.services.prompt_analyzer import PromptAnalyzer
from app.application.use_cases.prompt_use_cases import PromptUseCases
from app.domain.entities.prompt_template import PromptTemplate


class PromptService:
    def __init__(
        self,
        use_cases: PromptUseCases,
        analyzer: PromptAnalyzer,
        priority_advisor: PriorityAdvisor,
    ) -> None:
        self.use_cases = use_cases
        self.analyzer = analyzer
        self.priority_advisor = priority_advisor

    def create_prompt(self, payload: PromptCreateRequest) -> PromptTemplate:
        return self.use_cases.create_prompt(payload)

    def list_prompts(self) -> list[PromptTemplate]:
        return self.use_cases.list_prompts()

    def get_prompt(self, prompt_id: str) -> PromptTemplate:
        return self.use_cases.get_prompt(prompt_id)

    def update_prompt(self, prompt_id: str, payload: PromptUpdateRequest) -> PromptTemplate:
        return self.use_cases.update_prompt(prompt_id, payload)

    def delete_prompt(self, prompt_id: str) -> None:
        self.use_cases.delete_prompt(prompt_id)

    def analyze_prompt(self, prompt_id: str) -> PromptAnalysisResult:
        prompt = self.use_cases.get_prompt(prompt_id)
        analysis = self.analyzer.analyze(prompt)
        return PromptAnalysisResult(
            score=analysis["score"],
            classification=analysis["classification"],
            suggestions=analysis["suggestions"],
        )

    def calculate_priority(self, prompt_id: str) -> PromptPriorityResult:
        prompt = self.use_cases.get_prompt(prompt_id)
        analysis = self.analyzer.analyze(prompt)
        priority = self.priority_advisor.advise(
            score=analysis["score"],
            status=prompt.status,
            missing_fields=analysis["missing_fields"],
            has_suggestions=bool(analysis["suggestions"]),
            suggestions_count=len(analysis["suggestions"]),
        )
        return PromptPriorityResult(**priority)
