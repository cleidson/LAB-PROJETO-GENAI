# PromptHub AI Python

Sistema acadêmico para cadastro, versionamento, análise e priorização de prompts de IA com API REST, frontend estático, SQLite, Docker e testes automatizados.

## Objetivo acadêmico

O projeto foi estruturado para demonstrar uma implementação simples e didática de um sistema de gestão de prompts, aplicando Clean Architecture, testes automatizados e construção assistida por IA registrada em `PROMPTS.md`.

## Funcionalidades

- CRUD completo de prompts.
- Análise local de qualidade do prompt.
- Sugestão de prioridade de melhoria ou uso.
- Frontend estático em HTML, CSS e JavaScript.
- Documentação via Swagger/OpenAPI.
- Execução local e com Docker Compose.
- Testes automatizados com `pytest`.

## Arquitetura Clean Architecture

O projeto está dividido nas camadas:

- `domain`: entidades e enums centrais.
- `application`: schemas, casos de uso e serviços.
- `infrastructure`: banco SQLite e repositório.
- `api`: inicialização da FastAPI e rotas REST.
- `frontend`: interface estática para consumo da API.

## Estrutura de pastas

```text
.
├── app
│   ├── api
│   │   ├── main.py
│   │   ├── dependencies.py
│   │   └── routes
│   │       └── prompt_routes.py
│   ├── application
│   │   ├── contracts
│   │   │   └── prompt_repository.py
│   │   ├── dto
│   │   │   └── prompt_results.py
│   │   ├── schemas
│   │   │   └── prompt_schema.py
│   │   ├── services
│   │   │   ├── priority_advisor.py
│   │   │   ├── prompt_analyzer.py
│   │   │   └── prompt_service.py
│   │   └── use_cases
│   │       └── prompt_use_cases.py
│   ├── domain
│   │   ├── entities
│   │   │   └── prompt_template.py
│   │   └── enums
│   │       └── prompt_status.py
│   └── infrastructure
│       ├── database.py
│       ├── models
│       │   └── prompt_model.py
│       └── repositories
│           └── prompt_repository.py
├── docs
│   ├── arquitetura
│   │   └── arquitetura.md
│   └── produto
│       ├── backlog.md
│       ├── escopo-mvp.md
│       └── roteiro-apresentacao.md
├── frontend
│   ├── app.js
│   ├── index.html
│   └── styles.css
├── tests
│   └── test_prompts.py
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── PROMPTS.md
├── README.md
├── requests.http
└── requirements.txt
```

## Tecnologias utilizadas

- Python 3.12+
- FastAPI
- SQLModel
- SQLite
- Pydantic
- Uvicorn
- pytest
- HTTPX / TestClient
- HTML, CSS e JavaScript
- Docker e Docker Compose

## Pré-requisitos

- Python 3.12 ou superior
- Docker Desktop opcional para execução via containers

## Instalação local

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Execução local da API

```powershell
uvicorn app.api.main:app --reload
```

API: <http://localhost:8000>

## Acesso ao Swagger

Swagger: <http://localhost:8000/docs>

## Execução do frontend estático

Com a API em execução:

```powershell
python -m http.server 8080 --directory frontend
```

Frontend: <http://localhost:8080>

## Execução com Docker

```powershell
docker build -t prompthub-ai-python .
docker run --rm -p 8000:8000 -e DATABASE_URL=sqlite:///./data/prompthub.db prompthub-ai-python
```

## Execução com Docker Compose

```powershell
docker compose up --build
```

- API: <http://localhost:8000>
- Swagger: <http://localhost:8000/docs>
- Frontend: <http://localhost:8080>

## Testes automatizados

```powershell
pytest
```

## Endpoints da API

| Método | Endpoint | Descrição |
| --- | --- | --- |
| GET | `/health` | Health check |
| POST | `/api/prompts` | Cria um prompt |
| GET | `/api/prompts` | Lista prompts |
| GET | `/api/prompts/{prompt_id}` | Consulta um prompt |
| PUT | `/api/prompts/{prompt_id}` | Atualiza um prompt |
| DELETE | `/api/prompts/{prompt_id}` | Remove um prompt |
| POST | `/api/prompts/{prompt_id}/analyze` | Analisa a qualidade do prompt |
| POST | `/api/prompts/{prompt_id}/priority` | Calcula a prioridade recomendada |

## Exemplos de JSON

### Criar prompt

```json
{
  "title": "Gerador de plano de estudos",
  "description": "Prompt para montar um plano semanal de estudos em IA.",
  "persona": "Tutor especialista em IA aplicada",
  "context": "O usuário está iniciando uma pós-graduação.",
  "instructions": "Crie um plano semanal de 4 semanas com foco em prática.",
  "expected_output": "Tabela com semana, objetivos e entregas.",
  "tags": ["educacao", "planejamento"],
  "status": "Active"
}
```

### Resposta de análise

```json
{
  "score": 85,
  "classification": "Excellent",
  "suggestions": []
}
```

### Resposta de prioridade

```json
{
  "priority": "Low",
  "reason": "O prompt possui boa estrutura e poucas lacunas.",
  "recommended_action": "Usar o prompt e monitorar melhorias pontuais."
}
```

## Serviço de análise de prompt

`PromptAnalyzer` aplica heurísticas locais e explicáveis para avaliar se o prompt possui persona, contexto, instruções claras, formato de saída, objetivo explícito, restrições, tags e descrição.

## Serviço `priority_advisor.py`

`PriorityAdvisor` combina score, status, quantidade de campos ausentes e sugestões de melhoria para definir a prioridade `Low`, `Medium`, `High` ou `Critical`.

## Decisões técnicas

- Persistência simples em SQLite para facilitar demonstração local.
- `PromptTemplate` modelado como entidade de dominio pura para reduzir acoplamento com persistencia.
- `PromptTemplate` mantido como entidade de dominio pura, separado do modelo ORM `PromptModel`.
- A camada `application` depende de uma porta de repositorio, e a implementacao concreta fica em `infrastructure`.
- Frontend sem framework para simplificar a apresentação.
- Análise de prompts sem dependência de APIs externas.

## Limitações do MVP

- Sem autenticação e autorização.
- Sem integração real com provedores de IA.
- Sem histórico completo de versões.
- Sem deploy em nuvem.
- Sem observabilidade avançada.

## Próximos passos

- Adicionar autenticação JWT.
- Migrar para PostgreSQL.
- Criar dashboard de qualidade de prompts.
- Adicionar histórico de versões e exportação.

## Roteiro rápido de apresentação

1. Contextualizar o problema de gestão de prompts.
2. Mostrar a arquitetura em camadas.
3. Demonstrar CRUD pela API e frontend.
4. Executar análise e prioridade.
5. Mostrar testes e Docker Compose.
6. Encerrar com limitações e próximos passos.

## Histórico de prompts usados no `PROMPTS.md`

O arquivo `PROMPTS.md` registra a construção assistida por IA em sequência, cobrindo estrutura inicial, domínio, backend, frontend, Docker, testes, documentação e revisão final.

## Comandos Git utilizados

```bash
git init
git add .
git commit -m "feat: estrutura inicial do projeto com clean architecture"
git add .
git commit -m "docs: adiciona readme inicial e escopo do mvp"
git add .
git commit -m "feat: adiciona dominio e schemas de prompts"
git add .
git commit -m "feat: adiciona persistencia sqlite e repository"
git add .
git commit -m "feat: adiciona casos de uso e servico de prompts"
git add .
git commit -m "feat: adiciona analisador local de prompts"
git add .
git commit -m "feat: adiciona priority advisor para prompts"
git add .
git commit -m "feat: adiciona rotas da api de prompts"
git add .
git commit -m "feat: adiciona frontend estatico para consumo da api"
git add .
git commit -m "chore: adiciona docker e docker compose"
git add .
git commit -m "test: adiciona testes automatizados da api"
git add .
git commit -m "docs: atualiza documentacao final e roteiro de apresentacao"
```
