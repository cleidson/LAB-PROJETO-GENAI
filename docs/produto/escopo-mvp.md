# Escopo do MVP

## Visão geral

O PromptHub AI Python é um sistema CRUD para gestão de prompts de Engenharia de IA, com foco em organização, análise local de qualidade e priorização de melhoria.

## Objetivo

Entregar um MVP simples, funcional e bem estruturado para apresentação acadêmica, demonstrando Clean Architecture, API REST, frontend estático, persistência local e testes automatizados.

## Funcionalidades do MVP

1. Cadastro de prompts.
2. Listagem de prompts.
3. Consulta de prompt por ID.
4. Atualização de prompts com incremento de versão.
5. Exclusão de prompts.
6. Análise local da qualidade do prompt.
7. Sugestão de prioridade de melhoria ou uso.
8. Frontend estático em HTML, CSS e JavaScript.
9. Documentação via Swagger/OpenAPI.
10. Execução local e via Docker Compose.
11. Testes automatizados básicos com `pytest`.

## Fora do escopo

- Autenticação.
- Autorização.
- Multiusuário.
- Integração real com OpenAI, Azure OpenAI, Vertex AI ou similares.
- Banco de produção.
- Deploy em nuvem.
- Frontend com framework moderno.

## Critérios de aceite

- A API responde em `http://localhost:8000`.
- O Swagger está disponível em `http://localhost:8000/docs`.
- O frontend consegue criar, listar, editar, analisar e priorizar prompts.
- Os testes automatizados cobrem CRUD, análise e prioridade.
- O projeto pode ser executado com `docker compose up --build`.
