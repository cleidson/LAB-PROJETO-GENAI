from app.domain.entities.prompt_template import PromptTemplate


class PromptAnalyzer:
    def analyze(self, prompt: PromptTemplate) -> dict:
        suggestions: list[str] = []
        score = 0
        missing_fields = 0

        if prompt.persona:
            score += 10
        else:
            missing_fields += 1
            suggestions.append("Adicione uma persona para orientar o comportamento esperado da IA.")

        if prompt.context:
            score += 15
        else:
            missing_fields += 1
            suggestions.append("Inclua contexto para delimitar melhor o problema.")

        if prompt.instructions and len(prompt.instructions.split()) >= 6:
            score += 20
        else:
            missing_fields += 1
            suggestions.append("Escreva instrucoes mais claras e objetivas.")

        if prompt.expected_output:
            score += 15
        else:
            missing_fields += 1
            suggestions.append("Defina o formato de saida esperado.")

        objective_source = " ".join(filter(None, [prompt.title, prompt.description, prompt.instructions]))
        lowered_objective = objective_source.lower()
        if any(keyword in lowered_objective for keyword in ["objetivo", "goal", "resultado", "crie", "gere", "liste", "explique"]):
            score += 10
        else:
            missing_fields += 1
            suggestions.append("Deixe o objetivo do prompt mais explicito.")

        lowered_instructions = (prompt.instructions or "").lower()
        if any(keyword in lowered_instructions for keyword in ["nao", "deve", "must", "somente", "limite", "evite"]):
            score += 10
        else:
            missing_fields += 1
            suggestions.append("Inclua restricoes ou regras para reduzir ambiguidades.")

        if prompt.tags:
            score += 10
        else:
            missing_fields += 1
            suggestions.append("Adicione tags para facilitar organizacao e busca.")

        if prompt.description:
            score += 10
        else:
            missing_fields += 1
            suggestions.append("Inclua uma descricao curta para contextualizar o uso do prompt.")

        classification = self._classify(score)
        return {
            "score": score,
            "classification": classification,
            "suggestions": suggestions,
            "missing_fields": missing_fields,
        }

    @staticmethod
    def _classify(score: int) -> str:
        if score < 40:
            return "Poor"
        if score < 60:
            return "Basic"
        if score < 80:
            return "Good"
        return "Excellent"
