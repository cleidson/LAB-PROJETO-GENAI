# PromptHub AI Python

Sistema acadêmico para cadastro, versionamento, análise e priorização de prompts de Inteligência Artificial, desenvolvido com API REST, frontend estático, SQLite, Docker, testes automatizados e arquitetura baseada em **Clean Architecture**.

---

## 1. Descrição do Projeto

O **PromptHub AI Python** é um miniprojeto acadêmico criado para demonstrar, de forma prática, como a Engenharia de IA pode ser aplicada no desenvolvimento de software.

A proposta inicial era construir um CRUD simples. Porém, para conectar o projeto ao contexto da pós-graduação em Engenharia de IA, o domínio escolhido foi a gestão de prompts. Dessa forma, o sistema permite cadastrar, consultar, atualizar, excluir, analisar e priorizar prompts usados em soluções baseadas em Inteligência Artificial.

O projeto também registra sua construção assistida por IA no arquivo `prompts\PROMPTS.md`, evidenciando a sequência de prompts usados para planejar, implementar, testar e documentar a solução.

---

## 2. Objetivo Acadêmico

O objetivo do projeto é apresentar uma aplicação simples, funcional e bem estruturada, demonstrando:

- criação de uma API REST com Python e FastAPI;
- aplicação de Clean Architecture;
- persistência de dados com SQLite;
- frontend estático consumindo a API;
- execução local e com Docker;
- testes automatizados com `pytest`;
- documentação técnica;
- uso estruturado de assistentes de IA durante o desenvolvimento;
- análise e priorização de prompts como prática de Engenharia de IA.

---

## 2.1. O que o projeto resolve

O projeto resolve um problema comum em times que usam IA: prompts importantes acabam espalhados, sem padrao, sem versionamento, sem criterio de qualidade e sem clareza sobre o que precisa ser melhorado primeiro.

Com isso, o PromptHub AI Python oferece:

- centralizacao dos prompts em um CRUD simples;
- avaliacao local da qualidade estrutural de cada prompt;
- priorizacao objetiva para revisao ou reutilizacao;
- rastreabilidade do processo de construcao assistida por IA.

---

## 3. Funcionalidades

- CRUD completo de prompts.
- Cadastro de título, descrição, persona, contexto, instruções, saída esperada, tags e status.
- Listagem de prompts cadastrados.
- Consulta de prompt por ID.
- Atualização de prompts com incremento de versão.
- Exclusão de prompts.
- Análise local de qualidade do prompt.
- Sugestão de prioridade de melhoria ou uso.
- Frontend estático em HTML, CSS e JavaScript.
- Documentação automática via Swagger/OpenAPI.
- Execução com Docker e Docker Compose.
- Testes automatizados com `pytest`.

---

## 4. Tecnologias Utilizadas

- Python 3.12+
- FastAPI
- SQLModel
- SQLite
- Pydantic
- Uvicorn
- pytest
- HTTPX / TestClient
- HTML
- CSS
- JavaScript
- Docker
- Docker Compose
- Swagger / OpenAPI
- Git
- GitHub Copilot

---

## 5. Arquitetura Clean Architecture

O projeto foi organizado seguindo os princípios da **Clean Architecture**, separando responsabilidades e reduzindo o acoplamento entre as camadas.

### Camadas do projeto

| Camada | Responsabilidade |
| --- | --- |
| `domain` | Entidades e enums centrais do negócio. |
| `application` | Contratos, DTOs, schemas, casos de uso e serviços de aplicação. |
| `infrastructure` | Banco de dados, modelos de persistência e repositórios. |
| `api` | Inicialização da FastAPI, dependências e rotas REST. |
| `frontend` | Interface web estática para consumo da API. |
| `tests` | Testes automatizados da aplicação. |
| `docs` | Documentação complementar do projeto. |

Essa separação permite que a regra de negócio fique menos dependente de detalhes técnicos, como banco de dados, framework web ou interface de usuário.

---

## 6. Estrutura de Pastas

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
│   │   ├── arquitetura.md
│   │   └── diagramas
│   │       └── arquitetura-sistema.md
│   ├── produto
│   │   ├── backlog.md
│   │   ├── escopo-mvp.md
│   │   └── roteiro-apresentacao.md
│   └── tests
│       ├── diagrama-testes.md
│       └── resultado-testes.md
├── frontend
│   ├── app.js
│   ├── index.html
│   └── styles.css
├── prompts
│   └── PROMPTS.md
├── tests
│   └── test_prompts.py
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requests.http
└── requirements.txt
```

---

## 7. Pré-requisitos

Para executar o projeto localmente, é necessário ter instalado:

- Python 3.12 ou superior;
- Git;
- Docker Desktop, opcional para execução com containers;
- Visual Studio Code ou outro editor de preferência.

---

## 8. Instalação Local

Se estiver usando o código local já clonado, entre na pasta do projeto e execute:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Caso queira clonar o repositório antes:

```powershell
git clone <url-do-repositorio>
cd LAB-PROJETO-GENAI
```

---

## 9. Execução Local da API

Execute a API com Uvicorn:

```powershell
uvicorn app.api.main:app --reload
```

A API ficará disponível em:

```text
http://localhost:8000
```

---

## 10. Acesso ao Swagger

A documentação interativa da API pode ser acessada em:

```text
http://localhost:8000/docs
```

O Swagger permite testar os endpoints diretamente pelo navegador.

---

## 11. Execução do Frontend Estático

Com a API em execução, execute o frontend estático com o servidor HTTP do Python:

```powershell
python -m http.server 8080 --directory frontend
```

Acesse:

```text
http://localhost:8080
```

---

## 12. Execução com Docker

Crie a imagem Docker:

```powershell
docker build -t prompthub-ai-python .
```

Execute o container:

```powershell
docker run --rm -p 8000:8000 -e DATABASE_URL=sqlite:///./data/prompthub.db prompthub-ai-python
```

Acesse:

```text
http://localhost:8000
```

---

## 13. Execução com Docker Compose

Para subir a API e o frontend com Docker Compose:

```powershell
docker compose up --build
```

URLs disponíveis:

```text
API:      http://localhost:8000
Swagger:  http://localhost:8000/docs
Frontend: http://localhost:8080
```

Para encerrar os containers:

```powershell
docker compose down
```

---

## 13.1. Guia rapido reprodutivel

Para reproduzir o projeto localmente do zero:

1. Clone o repositorio e entre na pasta do projeto.
2. Crie o ambiente virtual com `python -m venv .venv`.
3. Ative o ambiente com `.venv\Scripts\activate`.
4. Instale as dependencias com `pip install -r requirements.txt`.
5. Suba a API com `uvicorn app.api.main:app --reload`.
6. Em outro terminal, suba o frontend com `python -m http.server 8080 --directory frontend`.
7. Acesse a API em `http://localhost:8000`, o Swagger em `http://localhost:8000/docs` e o frontend em `http://localhost:8080`.
8. Execute os testes com `pytest`.

## 13.2. Documentacao complementar

- Arquitetura: `docs\arquitetura\arquitetura.md`
- Diagrama de arquitetura: `docs\arquitetura\diagramas\arquitetura-sistema.md`
- Escopo do MVP: `docs\produto\escopo-mvp.md`
- Backlog: `docs\produto\backlog.md`
- Roteiro de apresentacao: `docs\produto\roteiro-apresentacao.md`
- Roteiro de demonstracao tecnica: `docs\produto\roteiro-demonstracao-tecnica.md`
- Relatorio de testes: `docs\tests\resultado-testes.md`
- Diagrama de testes: `docs\tests\diagrama-testes.md`
- Historico de prompts usados no desenvolvimento: `prompts\PROMPTS.md`

---

## 14. Endpoints da API

| Método | Endpoint | Descrição |
| --- | --- | --- |
| GET | `/health` | Health check da aplicação. |
| POST | `/api/prompts` | Cria um novo prompt. |
| GET | `/api/prompts` | Lista prompts cadastrados. |
| GET | `/api/prompts/{prompt_id}` | Consulta um prompt por ID. |
| PUT | `/api/prompts/{prompt_id}` | Atualiza um prompt existente. |
| DELETE | `/api/prompts/{prompt_id}` | Remove um prompt. |
| POST | `/api/prompts/{prompt_id}/analyze` | Analisa a qualidade do prompt. |
| POST | `/api/prompts/{prompt_id}/priority` | Calcula a prioridade recomendada. |

---

## 15. Exemplos de Uso

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

---

## 16. Serviço de Análise de Prompt

O serviço `PromptAnalyzer` aplica heurísticas locais e explicáveis para avaliar a qualidade estrutural de um prompt.

A análise considera critérios como:

- existência de persona;
- existência de contexto;
- clareza das instruções;
- definição da saída esperada;
- objetivo explícito;
- presença de restrições ou regras;
- tags;
- descrição.

A saída da análise contém:

- pontuação de 0 a 100;
- classificação;
- sugestões de melhoria.

Esse serviço não utiliza API externa de IA. A decisão foi manter a análise local para facilitar a execução acadêmica, evitar dependência de chaves externas e permitir que o comportamento fosse demonstrado de forma simples e previsível.

---

## 17. Serviço `priority_advisor.py`

O serviço `PriorityAdvisor`, implementado no arquivo `priority_advisor.py`, interpreta o resultado da análise do prompt e sugere uma prioridade de melhoria ou uso.

As prioridades possíveis são:

- `Low`;
- `Medium`;
- `High`;
- `Critical`.

A prioridade é calculada com base em fatores como:

- score do prompt;
- status do prompt;
- quantidade de campos ausentes;
- número de sugestões de melhoria.

Esse serviço ajuda a transformar a análise técnica do prompt em uma recomendação prática, indicando se o prompt pode ser utilizado ou se precisa ser revisado antes do uso.

---

## 18. Testes Automatizados

Os testes automatizados são executados com `pytest`.

```powershell
pytest
```

Os testes validam cenários como:

- criação de prompt válido;
- tentativa de criação com dados inválidos;
- listagem de prompts;
- consulta de prompt existente;
- consulta de prompt inexistente;
- atualização de prompt;
- exclusão de prompt;
- análise de qualidade;
- cálculo de prioridade.

Os contratos de entrada e saida da API ficam explicitos em `app\application\schemas\prompt_schema.py`, e os testes exercitam esses contratos via HTTP usando `TestClient`.

---

## 19. Decisões Técnicas

As principais decisões técnicas do projeto foram:

- usar **FastAPI** para criar uma API REST simples, moderna e com Swagger automático;
- usar **SQLite** para facilitar a demonstração local;
- usar **Docker Compose** para simplificar a execução da API e do frontend;
- manter o frontend sem framework para reduzir complexidade;
- separar a entidade de domínio `PromptTemplate` do modelo de persistência `PromptModel`;
- manter o domínio independente da camada de API e do ORM;
- usar contratos na camada `application`;
- manter a implementação concreta de repositório na camada `infrastructure`;
- centralizar a composição das dependências em `app/api/dependencies.py`;
- criar uma análise local de prompts sem dependência de APIs externas;
- registrar a construção assistida por IA em `prompts\PROMPTS.md`.

---

## 20. Como a IA Acelerou Este Projeto

O **PromptHub AI Python** nasceu a partir de uma proposta simples: criar um CRUD acadêmico para demonstrar os conhecimentos adquiridos na pós-graduação em Engenharia de IA. Porém, em vez de desenvolver um cadastro genérico, como produtos, clientes ou tarefas, a decisão foi transformar o próprio objeto de estudo da disciplina em domínio do sistema: **prompts de Inteligência Artificial**.

A partir dessa escolha, o projeto passou a ter uma narrativa mais conectada ao contexto da pós-graduação. O sistema não apenas cadastra informações; ele organiza, versiona, analisa e prioriza prompts, demonstrando na prática como a Engenharia de IA pode ser aplicada ao desenvolvimento de software.

Durante a construção, utilizei o **GitHub Copilot CLI**, powered by **GPT-5.4** (model ID: `gpt-5.4`), como agente de IA para acelerar etapas importantes do projeto, como definição do escopo, estruturação da arquitetura, criação e refino de arquivos, organização do README, geração de ideias para testes, elaboração de diagramas e consolidação da documentação técnica. Esse apoio permitiu evoluir rapidamente de uma ideia inicial para um projeto mais estruturado, com separação de responsabilidades, documentação e execução local via Docker.

Na pratica, a IA foi usada em praticamente todas as fases do projeto: concepcao do escopo, definicao da arquitetura, organizacao das pastas, geracao e refino dos contratos, escrita e ampliacao dos testes, elaboracao dos diagramas, revisao do README, consolidacao da documentacao e ajuste incremental da qualidade tecnica.

Os principais ganhos de produtividade vieram da capacidade de acelerar tarefas repetitivas e de alto volume de contexto, como revisão de estrutura, atualização de documentação, refatorações coordenadas entre múltiplos arquivos, expansão da suíte de testes e padronização dos commits. Isso tornou o fluxo de desenvolvimento mais rápido e mais consistente.

Ao mesmo tempo, a **revisao humana continuou essencial**. A IA nao substituiu o raciocinio tecnico nem a tomada de decisao arquitetural. As definicoes mais importantes, como adotar Clean Architecture, separar a entidade de dominio do modelo de persistencia, manter a analise de prompts local e evitar dependencia de APIs externas no MVP, foram revisadas e validadas manualmente conforme o objetivo academico do projeto.

A criação do arquivo `prompts\PROMPTS.md` foi uma parte essencial dessa abordagem. Ele registra a sequência de prompts utilizados durante o desenvolvimento, funcionando como uma trilha de auditoria da construção assistida por IA. Dessa forma, o projeto não mostra apenas o resultado final, mas também o processo de criação, experimentação e refinamento.

Outro ponto importante foi a escolha de implementar dois serviços relacionados à qualidade dos prompts: o `PromptAnalyzer` e o `PriorityAdvisor`. O primeiro avalia a estrutura do prompt com base em critérios como persona, contexto, instruções, formato de saída e restrições. O segundo interpreta essa análise e sugere uma prioridade de melhoria, tornando o sistema mais próximo de um assistente de governança de prompts.

Com isso, o **PromptHub AI Python** deixa de ser apenas um CRUD e passa a representar um pequeno laboratório de Engenharia de IA aplicada. Ele demonstra como prompts podem ser tratados como ativos importantes de um projeto, exigindo organização, avaliação, melhoria contínua e rastreabilidade.

Em resumo, a IA foi utilizada neste projeto como uma ferramenta de apoio à engenharia de software, contribuindo para acelerar a criação, melhorar a documentação, reforçar os testes e fortalecer a narrativa técnica da entrega. O resultado é um MVP simples, porém alinhado com os conceitos de arquitetura, automação, documentação e uso consciente de Inteligência Artificial.

---

## 21. Histórico de Construção Assistida por IA

O arquivo `prompts\PROMPTS.md` registra a construção assistida por IA de forma sequencial, desde a criação do repositório até a implementação da API, frontend, Docker, testes e documentação.

Essa abordagem foi utilizada para demonstrar que o uso de IA no desenvolvimento de software pode ser organizado, rastreável e validável. Cada prompt representa uma etapa de evolução do projeto, permitindo compreender não apenas o código final, mas também as decisões tomadas ao longo do processo.

Esse histórico evidencia três pontos principais:

- a IA foi usada como apoio para acelerar a engenharia do projeto;
- as decisões técnicas foram revisadas e adaptadas conforme o objetivo acadêmico;
- o desenvolvimento foi conduzido de forma incremental, mantendo clareza, documentação e controle sobre o resultado final.

---

## 22. Limitações do MVP

O projeto foi desenvolvido como um MVP acadêmico. Por isso, algumas funcionalidades ficaram fora do escopo inicial:

- sem autenticação e autorização;
- sem integração real com provedores de IA;
- sem banco de dados em produção;
- sem histórico completo de versões;
- sem controle de usuários;
- sem deploy em nuvem;
- sem observabilidade avançada;
- sem dashboard analítico;
- sem frontend com framework moderno.

---

## 23. Próximos Passos

Possíveis evoluções do projeto:

- adicionar autenticação JWT;
- migrar de SQLite para PostgreSQL;
- integrar com OpenAI, Azure OpenAI ou Vertex AI;
- criar histórico completo de versões dos prompts;
- criar dashboard de qualidade dos prompts;
- permitir exportação de prompts;
- adicionar logs estruturados;
- adicionar monitoramento e observabilidade;
- criar controle de usuários;
- criar frontend com React, Vue ou Angular;
- realizar deploy em nuvem.

---

## 24. Roteiro Rápido de Apresentação

1. Contextualizar o problema de gestão de prompts.
2. Explicar a proposta do PromptHub AI Python.
3. Mostrar a arquitetura em camadas.
4. Demonstrar o CRUD pela API e pelo frontend.
5. Executar a análise de qualidade do prompt.
6. Demonstrar o cálculo de prioridade pelo `priority_advisor.py`.
7. Mostrar o Swagger.
8. Mostrar os testes automatizados.
9. Mostrar a execução com Docker Compose.
10. Explicar como a IA apoiou o desenvolvimento.
11. Apresentar limitações e próximos passos.

---

## 25. Comandos Git Utilizados

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

---

## 26. Considerações Finais

O **PromptHub AI Python** demonstra como um projeto acadêmico simples pode ser enriquecido com boas práticas de arquitetura, documentação e uso consciente de IA.

Mais do que entregar um CRUD, o projeto apresenta uma narrativa completa de construção: da ideia inicial ao código, dos prompts à documentação, dos testes à execução com Docker. Essa abordagem torna o projeto mais claro, rastreável e adequado para uma apresentação de pós-graduação em Engenharia de IA.
