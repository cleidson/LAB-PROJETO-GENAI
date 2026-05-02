# PROMPTS.md — PromptHub AI Python

## Projeto
**PromptHub AI Python** — Sistema CRUD em Python para cadastro, versionamento, análise e priorização de prompts de Engenharia de IA.

## Objetivo do arquivo
Este arquivo registra, em ordem sequencial, os prompts que devem ser usados para construir o projeto desde a criação do repositório até a implementação da API, frontend estático, Docker, testes, documentação e apresentação final.

A proposta é demonstrar, na pós-graduação de Engenharia de IA, um projeto simples, funcional e bem documentado, usando IA de forma estruturada durante o desenvolvimento.

---

# Visão Geral do Projeto

## Nome
**PromptHub AI Python**

## Descrição
O PromptHub AI Python é um sistema básico para gerenciar prompts de IA.

O sistema permitirá:

- cadastrar prompts;
- listar prompts;
- consultar prompt por ID;
- atualizar prompts;
- excluir prompts;
- analisar a qualidade de um prompt;
- sugerir prioridade de uso/melhoria do prompt;
- consumir a API por meio de uma tela web estática feita com HTML, CSS e JavaScript.

## Padrão arquitetural
O projeto deve seguir **Clean Architecture**, separando responsabilidades em camadas:

- `domain`: entidades e regras centrais;
- `application`: casos de uso, schemas, serviços e contratos;
- `infrastructure`: banco de dados, repositórios e configurações técnicas;
- `api`: rotas, controllers/routers e inicialização da API;
- `frontend`: página estática para consumir a API.

## Stack sugerida

- Python 3.12+
- FastAPI
- SQLModel
- SQLite
- Pydantic
- Uvicorn
- pytest
- HTTPX/TestClient
- HTML
- CSS
- JavaScript
- Docker
- Docker Compose

---

# 01 — Criação do Repositório, Estrutura Inicial, README, .gitignore e Primeiro Commit

```text
Atue como um Arquiteto de Software Sênior especialista em Python, FastAPI, Clean Architecture, APIs REST, testes automatizados e Engenharia de IA.

Estou criando um miniprojeto para apresentar na pós-graduação de Engenharia de IA.

Nome do projeto:
PromptHub AI Python.

Objetivo:
Criar um sistema simples, porém bem estruturado, para gerenciar prompts de IA. O projeto deve possuir API REST, frontend estático, documentação, testes e Docker.

O projeto deve seguir Clean Architecture.

Neste primeiro passo, gere a estrutura inicial do repositório.

Requisitos:
1. Criar a estrutura de pastas do projeto.
2. Criar o arquivo README.md inicial.
3. Criar o arquivo .gitignore adequado para Python, FastAPI, ambiente virtual, cache, banco SQLite, arquivos .env e arquivos temporários.
4. Criar o arquivo .env.example.
5. Criar o arquivo requirements.txt.
6. Criar a pasta docs.
7. Criar a pasta frontend.
8. Criar a pasta tests.
9. Criar a pasta app com divisão baseada em Clean Architecture.
10. Criar o arquivo PROMPTS.md.
11. Gerar os comandos para criação do repositório Git.
12. Gerar o comando do primeiro commit.

Estrutura esperada:

prompthub-ai-python/
│
├── app/
│   ├── api/
│   │   ├── main.py
│   │   └── routes/
│   │       └── prompt_routes.py
│   │
│   ├── application/
│   │   ├── schemas/
│   │   │   └── prompt_schema.py
│   │   ├── services/
│   │   │   ├── prompt_service.py
│   │   │   ├── prompt_analyzer.py
│   │   │   └── priority_advisor.py
│   │   └── use_cases/
│   │       └── prompt_use_cases.py
│   │
│   ├── domain/
│   │   ├── entities/
│   │   │   └── prompt_template.py
│   │   └── enums/
│   │       └── prompt_status.py
│   │
│   └── infrastructure/
│       ├── database.py
│       └── repositories/
│           └── prompt_repository.py
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
├── tests/
│   └── test_prompts.py
│
├── docs/
│   ├── escopo-mvp.md
│   ├── arquitetura.md
│   ├── backlog.md
│   └── roteiro-apresentacao.md
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── PROMPTS.md

Gere:
1. A estrutura de diretórios.
2. O conteúdo inicial do README.md.
3. O conteúdo do .gitignore.
4. O conteúdo do .env.example.
5. O conteúdo do requirements.txt.
6. Os comandos para inicializar o repositório Git.
7. O comando do primeiro commit com a mensagem:
   "feat: estrutura inicial do projeto com clean architecture"
```

## Commit esperado

```bash
git init
git add .
git commit -m "feat: estrutura inicial do projeto com clean architecture"
```

---

# 02 — Criação do README Inicial com Passo a Passo do Projeto

```text
Crie o README.md inicial do projeto PromptHub AI Python.

O README deve conter:

1. Título do projeto.
2. Descrição curta.
3. Objetivo acadêmico.
4. Tecnologias utilizadas.
5. Padrão arquitetural adotado: Clean Architecture.
6. Estrutura de pastas.
7. Pré-requisitos.
8. Como criar ambiente virtual.
9. Como instalar dependências.
10. Como executar a API localmente.
11. Como acessar o Swagger.
12. Como executar o frontend estático.
13. Como rodar com Docker.
14. Como executar testes.
15. Como contribuir com commits.
16. Limitações do MVP.
17. Próximos passos.

Use linguagem técnica, clara e objetiva.

Inclua comandos reais, por exemplo:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.api.main:app --reload
pytest
docker compose up --build

Explique também que o projeto mantém um arquivo PROMPTS.md para registrar a construção assistida por IA.
```

---

# 03 — Definição do Escopo do MVP

```text
Crie o arquivo docs/escopo-mvp.md para o projeto PromptHub AI Python.

O sistema será um CRUD para gestão de prompts de Engenharia de IA.

O MVP deve conter:

- cadastro de prompts;
- listagem de prompts;
- consulta de prompt por ID;
- atualização de prompts;
- exclusão de prompts;
- análise local de qualidade do prompt;
- sugestão de prioridade de melhoria do prompt;
- frontend estático em HTML, CSS e JavaScript;
- documentação via Swagger/OpenAPI;
- execução com Docker;
- testes automatizados básicos.

Fora do escopo do MVP:

- autenticação;
- autorização;
- integração real com OpenAI, Azure OpenAI, Vertex AI ou outro provedor;
- banco de dados em produção;
- deploy em nuvem;
- frontend com framework moderno;
- multiusuário.

Gere o conteúdo completo do arquivo contendo:

1. Visão geral.
2. Objetivo.
3. Funcionalidades.
4. Fora do escopo.
5. Critérios de aceite.
6. Limitações conhecidas.
7. Próximos passos.
```

---

# 04 — Modelagem do Domínio

```text
Modele o domínio do projeto PromptHub AI Python seguindo Clean Architecture.

Crie a entidade principal:

PromptTemplate

Campos:

- id
- title
- description
- persona
- context
- instructions
- expected_output
- tags
- status
- version
- created_at
- updated_at

Regras:

- title é obrigatório;
- instructions é obrigatório;
- expected_output é obrigatório;
- status deve aceitar Draft, Active e Archived;
- version inicia em 1;
- created_at é preenchido na criação;
- updated_at é preenchido na atualização;
- a entidade não deve depender de FastAPI diretamente.

Crie também o enum PromptStatus.

Arquivos esperados:

app/domain/entities/prompt_template.py
app/domain/enums/prompt_status.py

Gere:
1. Código completo dos arquivos.
2. Explicação curta das decisões de modelagem.
3. Observação sobre por que a camada domain não deve depender da API.
```

---

# 05 — Criação dos Schemas de Entrada e Saída

```text
Crie os schemas do projeto PromptHub AI Python usando Pydantic/SQLModel.

Arquivos:
app/application/schemas/prompt_schema.py

Schemas necessários:

1. PromptCreateRequest
2. PromptUpdateRequest
3. PromptResponse
4. AnalyzePromptResponse
5. PriorityAdvisorResponse
6. ApiResponse

Regras:

- PromptCreateRequest deve exigir title, instructions e expected_output.
- PromptUpdateRequest deve permitir atualização parcial.
- PromptResponse deve retornar os principais dados do prompt.
- AnalyzePromptResponse deve retornar score, classificação e sugestões.
- PriorityAdvisorResponse deve retornar prioridade e justificativa.
- ApiResponse deve padronizar respostas de sucesso e erro.

Gere o código completo com validações simples e mensagens amigáveis.
```

---

# 06 — Configuração do Banco de Dados SQLite

```text
Configure o banco SQLite usando SQLModel.

Arquivo:
app/infrastructure/database.py

Requisitos:

- criar engine SQLite;
- usar variável de ambiente DATABASE_URL;
- usar sqlite:///./prompthub.db como valor padrão;
- criar função get_session;
- criar função create_db_and_tables;
- preparar o banco para uso local e com Docker;
- manter o código simples.

Gere:
1. Código completo do database.py.
2. Explicação do papel deste arquivo na camada infrastructure.
```

---

# 07 — Criação do Repository

```text
Crie o repository da entidade PromptTemplate.

Arquivo:
app/infrastructure/repositories/prompt_repository.py

Classe:
PromptRepository

Métodos:

- create
- get_all
- get_by_id
- update
- delete

Requisitos:

- usar Session do SQLModel;
- não colocar regra de negócio no repository;
- retornar None quando o prompt não existir;
- manter o repository focado em persistência;
- seguir Clean Architecture.

Gere:
1. Código completo.
2. Explicação curta sobre a responsabilidade do repository.
```

---

# 08 — Criação dos Use Cases

```text
Crie os casos de uso da aplicação.

Arquivo:
app/application/use_cases/prompt_use_cases.py

Responsabilidades:

- criar prompt;
- listar prompts;
- consultar prompt por ID;
- atualizar prompt;
- excluir prompt.

Regras:

- validar dados obrigatórios;
- ao atualizar, incrementar version;
- atualizar updated_at;
- tratar prompt inexistente;
- não expor detalhes de banco para a camada API.

Gere:
1. Código completo da classe PromptUseCases.
2. Exceptions simples de aplicação, se necessário.
3. Explicação curta sobre por que os use cases ficam na camada application.
```

---

# 09 — Criação do Serviço de Análise de Prompt

```text
Crie o serviço local de análise de qualidade do prompt.

Arquivo:
app/application/services/prompt_analyzer.py

Classe:
PromptAnalyzer

Objetivo:
Avaliar se um prompt possui elementos mínimos de boa Engenharia de Prompt.

Critérios de análise:

1. Possui persona.
2. Possui contexto.
3. Possui instruções claras.
4. Define formato de saída esperado.
5. Possui objetivo explícito.
6. Possui restrições ou regras.
7. Possui tags.
8. Possui descrição.

Retorno:

- score de 0 a 100;
- classification:
  - Poor
  - Basic
  - Good
  - Excellent
- suggestions: lista de melhorias.

Regras:

- Não usar API externa de IA.
- A análise deve ser local, simples e explicável.
- O objetivo é demonstrar raciocínio de Engenharia de Prompt sem depender de chave externa.

Gere:
1. Código completo do prompt_analyzer.py.
2. Explicação da heurística de pontuação.
3. Exemplo de resposta.
```

---

# 10 — Criação do Serviço priority_advisor.py

```text
Crie o serviço priority_advisor.py dentro da camada application/services.

Arquivo:
app/application/services/priority_advisor.py

Classe:
PriorityAdvisor

Objetivo:
Sugerir a prioridade de melhoria ou uso de um prompt com base na análise local de qualidade.

Entrada esperada:
- score do prompt;
- status do prompt;
- quantidade de campos ausentes;
- existência ou não de sugestões de melhoria.

Saída esperada:
- priority:
  - Low
  - Medium
  - High
  - Critical
- reason: justificativa textual;
- recommended_action: ação recomendada.

Regras de negócio sugeridas:

1. Se o score for menor que 40, prioridade Critical.
2. Se o score for entre 40 e 59, prioridade High.
3. Se o score for entre 60 e 79, prioridade Medium.
4. Se o score for 80 ou maior, prioridade Low.
5. Se o status estiver Archived, reduzir a prioridade para Low, pois não é um prompt ativo.
6. Se houver muitas sugestões de melhoria, aumentar a prioridade em um nível.
7. A resposta deve ser simples, clara e adequada para apresentação acadêmica.

Exemplo de resposta:

{
  "priority": "High",
  "reason": "O prompt possui baixa pontuação e ausência de contexto e formato de saída.",
  "recommended_action": "Revisar o prompt antes de utilizá-lo em um fluxo com IA."
}

Gere:
1. Código completo do priority_advisor.py.
2. Explicação das regras de prioridade.
3. Exemplo de uso dentro do endpoint /api/prompts/{prompt_id}/priority.
```

---

# 11 — Criação da Camada de Serviços

```text
Crie o serviço principal de aplicação para orquestrar os casos de uso, análise e prioridade.

Arquivo:
app/application/services/prompt_service.py

Classe:
PromptService

Responsabilidades:

- criar prompt;
- listar prompts;
- consultar prompt por ID;
- atualizar prompt;
- excluir prompt;
- analisar prompt usando PromptAnalyzer;
- calcular prioridade usando PriorityAdvisor.

Dependências:

- PromptRepository;
- PromptAnalyzer;
- PriorityAdvisor.

Requisitos:

- manter a API simples;
- centralizar a orquestração;
- não acessar diretamente banco fora do repository;
- não misturar regra de apresentação com regra de negócio.

Gere o código completo do prompt_service.py.
```

---

# 12 — Criação das Rotas da API

```text
Crie as rotas da API usando FastAPI.

Arquivo:
app/api/routes/prompt_routes.py

Rotas:

- POST /api/prompts
- GET /api/prompts
- GET /api/prompts/{prompt_id}
- PUT /api/prompts/{prompt_id}
- DELETE /api/prompts/{prompt_id}
- POST /api/prompts/{prompt_id}/analyze
- POST /api/prompts/{prompt_id}/priority

Requisitos:

- usar APIRouter;
- usar Depends para obter sessão;
- retornar status codes corretos;
- usar schemas de entrada e saída;
- tratar 404 quando prompt não existir;
- tratar 400 para dados inválidos;
- não expor detalhes internos;
- manter respostas amigáveis para apresentação.

Gere:
1. Código completo do arquivo de rotas.
2. Exemplos de requests e responses.
```

---

# 13 — Criação do main.py da API

```text
Crie o arquivo principal da API.

Arquivo:
app/api/main.py

Requisitos:

- criar instância FastAPI;
- configurar título, descrição e versão;
- inicializar banco no startup;
- incluir router de prompts;
- criar endpoint /health;
- configurar CORS para permitir o frontend estático local;
- deixar a API pronta para rodar com uvicorn.

Gere o código completo.

A API deve rodar com:

uvicorn app.api.main:app --reload
```

---

# 14 — Criação do Frontend Estático

```text
Crie um frontend estático básico e bonito usando HTML, CSS e JavaScript puro.

Pasta:
frontend/

Arquivos:

- index.html
- styles.css
- app.js

Objetivo:
Consumir a API PromptHub AI Python.

Funcionalidades da tela:

1. Formulário para cadastrar prompt.
2. Listagem de prompts cadastrados.
3. Botão para editar prompt.
4. Botão para excluir prompt.
5. Botão para analisar prompt.
6. Botão para calcular prioridade.
7. Área para exibir resultado da análise.
8. Área para exibir prioridade recomendada.
9. Layout simples, limpo e bonito.
10. Usar fetch API para consumir o backend.

API base:
http://localhost:8000/api/prompts

Requisitos visuais:

- layout centralizado;
- cards para prompts;
- cores leves;
- botões bem identificados;
- responsivo básico;
- sem framework frontend.

Gere:
1. Código completo do index.html.
2. Código completo do styles.css.
3. Código completo do app.js.
4. Instruções de como abrir o frontend localmente.
```

---

# 15 — Criação do Dockerfile

```text
Crie o Dockerfile para o projeto PromptHub AI Python.

Requisitos:

- usar imagem oficial Python;
- instalar dependências do requirements.txt;
- copiar código da aplicação;
- expor porta 8000;
- executar a API com uvicorn;
- preparar para ambiente local de demonstração;
- manter o Dockerfile simples.

Comando esperado para rodar no container:

uvicorn app.api.main:app --host 0.0.0.0 --port 8000

Gere:
1. Dockerfile completo.
2. Explicação das instruções.
```

---

# 16 — Criação do docker-compose.yml

```text
Crie o arquivo docker-compose.yml para subir a API do PromptHub AI Python.

Requisitos:

- serviço api;
- build usando o Dockerfile;
- expor porta 8000;
- configurar DATABASE_URL;
- montar volume para persistir SQLite, se necessário;
- permitir teste local com:
  docker compose up --build

Opcional:
- adicionar serviço frontend usando nginx para servir os arquivos estáticos da pasta frontend.

Se optar por frontend com nginx, configurar:
- porta 8080 para frontend;
- volume apontando para ./frontend;
- dependência do serviço api.

Gere:
1. docker-compose.yml completo.
2. Explicação de como subir.
3. URLs de acesso:
   - API: http://localhost:8000
   - Swagger: http://localhost:8000/docs
   - Frontend: http://localhost:8080
```

---

# 17 — Arquivo requests.http para Testes Manuais

```text
Crie um arquivo requests.http para testar a API pelo VS Code, Visual Studio ou Rider.

Arquivo:
requests.http

Incluir chamadas:

1. Health check.
2. Criar prompt.
3. Listar prompts.
4. Consultar prompt por ID.
5. Atualizar prompt.
6. Analisar prompt.
7. Calcular prioridade.
8. Excluir prompt.

Use exemplos realistas de Engenharia de IA.

API base:
http://localhost:8000

Gere o conteúdo completo do arquivo.
```

---

# 18 — Testes Automatizados com pytest

```text
Crie testes automatizados com pytest para o projeto PromptHub AI Python.

Arquivo:
tests/test_prompts.py

Cobrir:

1. Criar prompt válido.
2. Erro ao criar prompt sem título.
3. Listar prompts.
4. Consultar prompt existente.
5. Consultar prompt inexistente.
6. Atualizar prompt incrementando version.
7. Excluir prompt.
8. Analisar prompt retornando score.
9. Calcular prioridade do prompt.

Requisitos:

- usar TestClient do FastAPI;
- criar banco de teste isolado;
- evitar depender do banco local de desenvolvimento;
- nomes dos testes devem explicar o comportamento esperado;
- código simples e didático.

Gere:
1. Código completo dos testes.
2. Explicação de como executar:

pytest
```

---

# 19 — Documentação da Arquitetura

```text
Crie o arquivo docs/arquitetura.md.

Conteúdo obrigatório:

1. Visão geral da arquitetura.
2. Justificativa para uso de Clean Architecture.
3. Responsabilidade de cada camada:
   - domain;
   - application;
   - infrastructure;
   - api;
   - frontend.
4. Diagrama Mermaid de componentes.
5. Fluxo de criação de prompt.
6. Fluxo de análise de prompt.
7. Fluxo de cálculo de prioridade.
8. Limitações da arquitetura no MVP.
9. Possíveis evoluções.

Inclua Mermaid compatível com Markdown.
```

---

# 20 — Backlog do Projeto

```text
Crie o arquivo docs/backlog.md.

Organize o backlog em tabela com as colunas:

- ID
- Item
- Descrição
- Prioridade
- Status

Categorias:

1. Implementado no MVP.
2. Melhorias futuras.
3. Funcionalidades com IA.
4. Segurança.
5. Persistência.
6. Observabilidade.
7. Interface web futura.
8. Deploy.

Inclua itens como:

- autenticação com JWT;
- integração com OpenAI/Azure OpenAI/Vertex AI;
- banco PostgreSQL;
- histórico de versões de prompts;
- login de usuários;
- dashboard de qualidade de prompts;
- exportação de prompts;
- deploy em nuvem;
- observabilidade com logs estruturados.
```

---

# 21 — Roteiro de Apresentação

```text
Crie o arquivo docs/roteiro-apresentacao.md.

Monte um roteiro de apresentação de 5 a 7 minutos para o PromptHub AI Python.

Estrutura:

1. Abertura.
2. Problema.
3. Solução proposta.
4. Arquitetura usando Clean Architecture.
5. Demonstração do CRUD.
6. Demonstração do analisador de prompt.
7. Demonstração do priority_advisor.py.
8. Demonstração do frontend estático.
9. Demonstração do Docker.
10. Como a IA ajudou na construção.
11. Importância do PROMPTS.md.
12. Aprendizados.
13. Próximos passos.
14. Encerramento.

Tom:
Profissional, objetivo e seguro.

Inclua uma versão falada, como se eu fosse apresentar para a turma.
```

---

# 22 — Atualização Final do README com Passo a Passo Completo

```text
Atualize o README.md final do projeto PromptHub AI Python.

O README deve conter:

1. Título.
2. Descrição.
3. Objetivo acadêmico.
4. Funcionalidades.
5. Arquitetura Clean Architecture.
6. Estrutura de pastas.
7. Tecnologias utilizadas.
8. Pré-requisitos.
9. Instalação local.
10. Execução local da API.
11. Acesso ao Swagger.
12. Execução do frontend estático.
13. Execução com Docker.
14. Execução com Docker Compose.
15. Testes automatizados.
16. Endpoints da API.
17. Exemplos de JSON.
18. Serviço de análise de prompt.
19. Serviço priority_advisor.py.
20. Decisões técnicas.
21. Limitações do MVP.
22. Próximos passos.
23. Roteiro rápido de apresentação.
24. Histórico de prompts usados no PROMPTS.md.
25. Comandos Git utilizados.

Inclua comandos reais:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.api.main:app --reload
pytest
docker compose up --build

Inclua URLs:

API:
http://localhost:8000

Swagger:
http://localhost:8000/docs

Frontend:
http://localhost:8080
```

---

# 23 — Revisão Final do Projeto

```text
Revise o projeto PromptHub AI Python como se fosse uma entrega acadêmica de pós-graduação em Engenharia de IA.

Verifique:

1. Se a estrutura segue Clean Architecture.
2. Se o README está completo.
3. Se o PROMPTS.md demonstra construção sequencial com IA.
4. Se o CRUD funciona.
5. Se o frontend consome a API.
6. Se o Docker sobe corretamente.
7. Se o endpoint de análise de prompt funciona.
8. Se o priority_advisor.py foi criado corretamente.
9. Se os testes cobrem o básico.
10. Se a documentação está clara.
11. Se o projeto pode ser explicado em 5 a 7 minutos.

Gere:

1. Checklist final.
2. Pontos fortes.
3. Pontos de melhoria.
4. Riscos.
5. Sugestões para apresentação.
```

---

# 24 — Sequência Recomendada de Commits

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

## Padrão de commits por camada

Use este guia sempre que precisar gerar um commit de acordo com a camada alterada no projeto.

### Regra geral

- gerar commits pequenos e coerentes com uma única intenção;
- usar prefixo semântico no início da mensagem;
- citar a camada, módulo ou objetivo principal da mudança;
- evitar misturar `docs`, `test`, `feat`, `refactor` e `chore` no mesmo commit, salvo quando a alteração for inseparável.

### Prefixos recomendados

- `feat`: nova funcionalidade ou evolução funcional;
- `fix`: correção de bug;
- `refactor`: melhoria estrutural sem mudar comportamento esperado;
- `docs`: atualização de documentação;
- `test`: criação ou melhoria de testes;
- `chore`: ajustes operacionais, setup, Docker, scripts ou manutenção.

### Convenção por camada

| Camada / Área | Prefixo mais comum | Exemplo de mensagem |
| --- | --- | --- |
| `domain` | `feat` / `refactor` | `feat: adiciona entidade e regras de dominio de prompts` |
| `application` | `feat` / `refactor` | `refactor: reorganiza use cases e contratos da camada application` |
| `infrastructure` | `feat` / `fix` / `refactor` | `feat: adiciona persistencia sqlite e repository` |
| `api` | `feat` / `fix` | `feat: adiciona rotas da api de prompts` |
| `frontend` | `feat` / `fix` | `feat: adiciona frontend estatico para consumo da api` |
| `tests` | `test` | `test: amplia cobertura de erros da api de prompts` |
| `docs` | `docs` | `docs: atualiza arquitetura, testes e readme` |
| `docker` / setup | `chore` | `chore: ajusta docker compose e configuracao local` |

### Como decidir a mensagem

1. Identifique a camada principal alterada.
2. Identifique a natureza da mudança: nova funcionalidade, correção, refatoração, documentação, teste ou manutenção.
3. Gere a mensagem no formato:

```text
<prefixo>: <acao principal> <camada/modulo/objetivo>
```

### Exemplos prontos

```bash
git commit -m "feat: adiciona regras de dominio para prompts"
git commit -m "refactor: desacopla application da infrastructure"
git commit -m "fix: corrige retorno de erro nas rotas da api"
git commit -m "test: amplia cobertura dos fluxos de analise e prioridade"
git commit -m "docs: atualiza readme e documentacao de arquitetura"
git commit -m "chore: ajusta execucao local com docker compose"
```

### Instrução para uso com IA

Ao pedir geração de commit, use a orientação:

```text
Gere o commit seguindo a padronização do projeto, considerando a camada principal alterada e o tipo da mudança.
```

Se houver alterações em mais de uma camada, priorize a camada dominante da mudança. Se documentação ou testes forem alterados junto com código apenas como suporte, mantenha o prefixo da mudança principal. Se a alteração for exclusivamente documentação ou testes, use `docs` ou `test`.

---

# 25 — Prompt para Geração Completa do Projeto em Uma Única Execução

```text
Atue como um Engenheiro de Software Sênior especialista em Python, FastAPI, Clean Architecture, Docker, frontend estático e Engenharia de IA.

Gere o projeto completo PromptHub AI Python.

Objetivo:
Criar um sistema simples para gestão de prompts de IA, contendo API REST, frontend estático, análise local de qualidade de prompt, sugestão de prioridade, testes, Docker e documentação.

Arquitetura:
Use Clean Architecture com as camadas:

- domain;
- application;
- infrastructure;
- api;
- frontend.

Funcionalidades:

1. CRUD de prompts:
   - criar;
   - listar;
   - consultar por ID;
   - atualizar;
   - excluir.

2. Análise local de prompt:
   - score de 0 a 100;
   - classificação Poor, Basic, Good e Excellent;
   - sugestões de melhoria.

3. Priority Advisor:
   - criar app/application/services/priority_advisor.py;
   - sugerir prioridade Low, Medium, High ou Critical;
   - retornar justificativa;
   - retornar ação recomendada.

4. Frontend:
   - HTML, CSS e JavaScript puro;
   - formulário de cadastro;
   - listagem;
   - edição;
   - exclusão;
   - análise;
   - prioridade.

5. Docker:
   - Dockerfile;
   - docker-compose.yml;
   - API em localhost:8000;
   - frontend em localhost:8080.

6. Testes:
   - pytest;
   - TestClient;
   - testes para CRUD, análise e prioridade.

7. Documentação:
   - README.md completo;
   - docs/escopo-mvp.md;
   - docs/arquitetura.md;
   - docs/backlog.md;
   - docs/roteiro-apresentacao.md;
   - PROMPTS.md.

Gere todos os arquivos do projeto com código completo, funcional e simples para apresentação acadêmica.

Mantenha a linguagem técnica, didática e objetiva.
```

---

# Observação Final

Este arquivo deve ser versionado no repositório para demonstrar a trilha de construção assistida por IA.

Ele serve como evidência de:

- uso estruturado de prompts;
- desenvolvimento incremental;
- aplicação de Clean Architecture;
- documentação técnica;
- uso de IA como apoio ao processo de engenharia de software.
