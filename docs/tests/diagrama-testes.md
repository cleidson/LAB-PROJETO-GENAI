# Diagrama de Testes

Este diagrama descreve como a suite automatizada atual valida o fluxo principal e os cenarios de erro da API.

```mermaid
flowchart TB
    START[Execucao do pytest]
    FIXTURE[Fixture client<br/>cria banco SQLite temporario]
    API[TestClient + FastAPI]

    subgraph MAINFLOW[Fluxo principal coberto]
        CREATE[POST /api/prompts<br/>criar prompt]
        LIST[GET /api/prompts<br/>listar]
        GETONE[GET /api/prompts/{id}<br/>consultar]
        UPDATE[PUT /api/prompts/{id}<br/>atualizar versao]
        ANALYZE[POST /api/prompts/{id}/analyze]
        PRIORITY[POST /api/prompts/{id}/priority]
        DELETE[DELETE /api/prompts/{id}]
    end

    subgraph ERRORS[Casos de erro cobertos]
        INVALIDCREATE[POST /api/prompts<br/>payload invalido]
        MISSINGGET[GET /api/prompts/not-found]
        MISSINGUPDATE[PUT /api/prompts/not-found]
        EMPTYUPDATE[PUT /api/prompts/{id}<br/>sem campos]
        MISSINGDELETE[DELETE /api/prompts/not-found]
        MISSINGANALYZE[POST /api/prompts/not-found/analyze]
        MISSINGPRIORITY[POST /api/prompts/not-found/priority]
        HEALTH[GET /health]
    end

    START --> FIXTURE --> API
    API --> CREATE --> LIST --> GETONE --> UPDATE --> ANALYZE --> PRIORITY --> DELETE
    API --> INVALIDCREATE
    API --> MISSINGGET
    API --> MISSINGUPDATE
    API --> EMPTYUPDATE
    API --> MISSINGDELETE
    API --> MISSINGANALYZE
    API --> MISSINGPRIORITY
    API --> HEALTH
```

## Leitura do diagrama

- A fixture cria um banco temporario para isolar a execucao.
- O fluxo principal cobre o ciclo de vida completo do prompt.
- Os casos de erro validam ausencia de recurso, payload invalido e operacoes incompletas.
- O endpoint `/health` funciona como smoke check minimo da aplicacao.
