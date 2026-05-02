# Diagrama de Arquitetura do Sistema

Diagrama regenerado a partir da implementacao atual do PromptHub AI Python, refletindo a separacao entre `domain`, `application`, `infrastructure`, `api` e `frontend`.

```mermaid
flowchart TB
    USER[Usuario]

    subgraph FRONT[Frontend]
        WEB[frontend/index.html<br/>app.js + styles.css]
        SWAGGER[Swagger UI]
        REQUESTS[requests.http]
    end

    subgraph API[Camada API]
        MAIN[app/api/main.py<br/>FastAPI + CORS + health]
        ROUTES[app/api/routes/prompt_routes.py]
        DEP[app/api/dependencies.py<br/>get_prompt_service]
    end

    subgraph APP[Camada Application]
        SCHEMAS[schemas/prompt_schema.py<br/>requests e responses]
        SERVICE[services/prompt_service.py]
        USECASES[use_cases/prompt_use_cases.py]
        ANALYZER[services/prompt_analyzer.py]
        PRIORITY[services/priority_advisor.py]
        PORT[contracts/prompt_repository.py<br/>PromptRepositoryPort]
        DTO[dto/prompt_results.py]
    end

    subgraph DOMAIN[Camada Domain]
        ENTITY[entities/prompt_template.py<br/>PromptTemplate]
        ENUM[enums/prompt_status.py<br/>PromptStatus]
    end

    subgraph INFRA[Camada Infrastructure]
        DB[database.py<br/>engine + session + create tables]
        MODEL[models/prompt_model.py<br/>PromptModel]
        REPO[repositories/prompt_repository.py]
        SQLITE[(SQLite / prompthub.db)]
    end

    TESTS[tests/test_prompts.py<br/>pytest + TestClient]

    USER --> WEB
    USER --> SWAGGER

    WEB -->|HTTP| ROUTES
    SWAGGER -->|HTTP| ROUTES
    REQUESTS -->|HTTP| ROUTES
    TESTS -->|HTTP/TestClient| ROUTES

    MAIN --> ROUTES
    ROUTES --> SCHEMAS
    ROUTES --> DEP
    DEP --> SERVICE
    DEP --> DB

    SERVICE --> USECASES
    SERVICE --> ANALYZER
    SERVICE --> PRIORITY
    SERVICE --> DTO

    USECASES --> PORT
    USECASES --> ENTITY
    ANALYZER --> ENTITY
    PRIORITY --> ENUM
    ENTITY --> ENUM

    REPO -. implementa .-> PORT
    REPO --> MODEL
    REPO --> DB
    DB --> SQLITE
```

## Leitura do diagrama

- A camada `api` recebe chamadas do frontend, Swagger, `requests.http` e testes.
- `api/dependencies.py` centraliza a composicao do `PromptService`.
- `PromptService` orquestra os casos de uso e os servicos de analise e prioridade.
- `PromptUseCases` depende da porta `PromptRepositoryPort`, nao da implementacao concreta.
- `PromptRepository` implementa a porta e converte entre `PromptTemplate` e `PromptModel`.
- A entidade `PromptTemplate` permanece no dominio, sem dependencia de ORM.
- A persistencia continua simples com SQLite e SQLModel na infraestrutura.
