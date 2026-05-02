from dataclasses import dataclass


@dataclass(slots=True)
class PromptAnalysisResult:
    score: int
    classification: str
    suggestions: list[str]


@dataclass(slots=True)
class PromptPriorityResult:
    priority: str
    reason: str
    recommended_action: str
