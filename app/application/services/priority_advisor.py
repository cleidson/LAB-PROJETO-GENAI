from app.domain.enums.prompt_status import PromptStatus


class PriorityAdvisor:
    LEVELS = ["Low", "Medium", "High", "Critical"]

    def advise(
        self,
        *,
        score: int,
        status: PromptStatus,
        missing_fields: int,
        has_suggestions: bool,
        suggestions_count: int,
    ) -> dict:
        if status == PromptStatus.ARCHIVED:
            return {
                "priority": "Low",
                "reason": "O prompt esta arquivado e nao representa demanda ativa de melhoria.",
                "recommended_action": "Manter arquivado e revisar apenas se ele voltar a uso ativo.",
            }

        level_index = self._priority_index_from_score(score)

        if has_suggestions and (suggestions_count >= 4 or missing_fields >= 3):
            level_index = min(level_index + 1, len(self.LEVELS) - 1)

        priority = self.LEVELS[level_index]
        reason = self._build_reason(priority, score, missing_fields)
        recommended_action = self._build_action(priority)

        return {
            "priority": priority,
            "reason": reason,
            "recommended_action": recommended_action,
        }

    @staticmethod
    def _priority_index_from_score(score: int) -> int:
        if score < 40:
            return 3
        if score < 60:
            return 2
        if score < 80:
            return 1
        return 0

    @staticmethod
    def _build_reason(priority: str, score: int, missing_fields: int) -> str:
        if priority == "Critical":
            return f"O prompt possui score {score} e muitas lacunas estruturais ({missing_fields} criterios ausentes)."
        if priority == "High":
            return f"O prompt precisa de melhorias relevantes para uso seguro e consistente (score {score})."
        if priority == "Medium":
            return f"O prompt ja e utilizavel, mas ainda tem pontos de melhoria identificados (score {score})."
        return "O prompt possui boa estrutura e poucas lacunas."

    @staticmethod
    def _build_action(priority: str) -> str:
        if priority == "Critical":
            return "Revisar imediatamente antes de utilizar o prompt em qualquer fluxo com IA."
        if priority == "High":
            return "Aprimorar o prompt antes de uso recorrente ou compartilhamento."
        if priority == "Medium":
            return "Planejar uma melhoria incremental para elevar clareza e qualidade."
        return "Usar o prompt e monitorar melhorias pontuais."
