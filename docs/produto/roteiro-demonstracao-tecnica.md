# Roteiro de Demonstração Técnica

## PromptHub AI Python — Demonstração em 3-5 minutos

Este roteiro orienta uma apresentação técnica rápida e objetiva do sistema. Siga os passos abaixo para cobrir os pontos essenciais.

---

## 1. Problema e Escopo (30 segundos)

**O que dizer:**

"O projeto resolve um problema comum: prompts importantes ficam espalhados, sem padrão, sem versionamento, sem critério de qualidade e sem clareza sobre o que precisa ser melhorado primeiro.

O PromptHub AI Python oferece um CRUD simples com análise local de qualidade e sugestão de prioridade, tudo funcionando local sem dependência de APIs externas."

**Visual:**
- Mostrar a página do projeto ou o README no terminal.
- Apontar os campos principais de um prompt: `title`, `description`, `persona`, `context`, `instructions`, `expected_output`, `tags`, `status`.

---

## 2. Arquitetura Resumida (1 minuto)

**O que dizer:**

"A arquitetura segue Clean Architecture com cinco camadas:

- **Domain**: entidades (`PromptTemplate`) e enums (`PromptStatus`).
- **Application**: schemas, casos de uso, serviços e contratos.
- **Infrastructure**: banco SQLite, modelos de persistência e repositório.
- **API**: FastAPI com rotas REST.
- **Frontend**: interface estática em HTML, CSS e JavaScript."

**Visual:**
- Abrir `docs/arquitetura/diagramas/arquitetura-sistema.md` no navegador ou editor.
- Apontar as camadas no diagrama Mermaid.
- Mencionar que a separação reduz acoplamento e facilita testes.

---

## 3. Execução da API (1 minuto)

**O que fazer:**

1. Abrir um terminal na pasta do projeto.
2. Ativar o ambiente virtual: `.venv\Scripts\activate`.
3. Subir a API: `uvicorn app.api.main:app --reload`.
4. Abrir `http://localhost:8000/docs` no navegador.

**O que mostrar:**

- O Swagger rodando.
- Os endpoints principais: `POST /api/prompts`, `GET /api/prompts`, `GET /api/prompts/{id}`, `PUT /api/prompts/{id}`, `DELETE /api/prompts/{id}`, `POST /api/prompts/{id}/analyze`, `POST /api/prompts/{id}/priority`.
- Clicar em um endpoint para mostrar o schema.

**Menção:**
"A API responde em `localhost:8000` e oferece documentação automática via Swagger."

---

## 4. Fluxo CRUD e Prioridade (2 minutos)

**O que fazer:**

### 4.1 Criar um prompt

No Swagger, expanda `POST /api/prompts` e clique em "Try it out".

Preencha um payload de exemplo:

```json
{
  "title": "Gerador de resumo acadêmico",
  "description": "Cria um resumo estruturado de artigos científicos.",
  "persona": "Pesquisador sênior em IA",
  "context": "Artigo científico em inglês com 5-10 páginas.",
  "instructions": "Resuma em 3 parágrafos os pontos principais, contribuições e limitações.",
  "expected_output": "Resumo estruturado em português com até 200 palavras.",
  "tags": ["pesquisa", "IA", "resumo"],
  "status": "Active"
}
```

Clique em "Execute" e mostre o resultado: `201 Created` com `version: 1`.

### 4.2 Listar prompts

Clique em `GET /api/prompts` e execute. Mostre que o prompt foi persistido.

### 4.3 Analisar qualidade

Copie o `id` do prompt criado.

Expanda `POST /api/prompts/{prompt_id}/analyze`, clique em "Try it out", cole o `id` e execute.

**Resultado esperado:**
```json
{
  "score": 75,
  "classification": "Good",
  "suggestions": ["Adicione tags para facilitar organização e busca."]
}
```

**Mencione:** "O score é local, sem chamar APIs externas. A análise avalia persona, contexto, instruções, saída esperada, objetivo, restrições, tags e descrição."

### 4.4 Calcular prioridade

Expanda `POST /api/prompts/{prompt_id}/priority`, execute.

**Resultado esperado:**
```json
{
  "priority": "Medium",
  "reason": "O prompt já é utilizável, mas ainda tem pontos de melhoria identificados (score 75).",
  "recommended_action": "Planejar uma melhoria incremental para elevar clareza e qualidade."
}
```

**Mencione:** "A prioridade é recomendada como Low, Medium, High ou Critical, ajudando a organizar revisões."

---

## 5. Evidência de Testes (1 minuto)

**O que fazer:**

1. Abrir um novo terminal na pasta do projeto.
2. Rodar: `pytest`.

**Resultado esperado:**
```
collected 15 items
tests\test_prompts.py ...............  [100%]
================================================= 15 passed in 1.03s ==================================================
```

**O que mostrar:**

- Abrir `docs/tests/resultado-testes.md` no editor.
- Apontar a matriz de cobertura: 15 testes aprovados cobrindo CRUD, análise, prioridade e tratamento de erros.
- Mencionar que os testes usam `TestClient` com banco SQLite temporário para isolamento.

**Mencione:** "A suite valida o fluxo principal, cenários de erro e cenários de sucesso. Testes rodam em ~1 segundo."

---

## Tempo Total

- Problema e escopo: 30 segundos
- Arquitetura: 1 minuto
- API: 1 minuto
- CRUD e prioridade: 2 minutos
- Testes: 1 minuto
- **Total: ~5 minutos**

---

## Dicas para a Apresentação

1. **Prepare o ambiente:** Tenha a API rodando antes de começar a apresentar.
2. **Tenha um prompt pronto:** Se quiser economizar tempo, já crie um prompt no banco antes de apresentar.
3. **Use o Swagger:** Evita ter que digitar comandos curl; a interface é intuitiva.
4. **Destaque ganhos:** Mencione que tudo roda local, sem APIs externas, em um ambiente simples.
5. **Finalize com contexto de IA:** Mencione que o projeto foi desenvolvido com o auxílio do GitHub Copilot CLI e registra o histórico em `prompts\PROMPTS.md`.

---

## Referências Rápidas

- **README principal:** `README.md`
- **Arquitetura completa:** `docs/arquitetura/arquitetura.md`
- **Diagrama da arquitetura:** `docs/arquitetura/diagramas/arquitetura-sistema.md`
- **Resultado dos testes:** `docs/tests/resultado-testes.md`
- **Roteiro de apresentação:** `docs/produto/roteiro-apresentacao.md`
- **Histórico de construção com IA:** `prompts/PROMPTS.md`
