# Roteiro de Apresentação

## Estrutura

1. Abertura.
2. Problema.
3. Solução proposta.
4. Arquitetura usando Clean Architecture.
5. Demonstração do CRUD.
6. Demonstração do analisador de prompt.
7. Demonstração do `priority_advisor.py`.
8. Demonstração do frontend estático.
9. Demonstração do Docker.
10. Como a IA ajudou na construção.
11. Importância do `prompts\PROMPTS.md`.
12. Aprendizados.
13. Próximos passos.
14. Encerramento.

## Versão falada

Boa tarde. Vou apresentar o PromptHub AI Python, um projeto acadêmico criado para organizar prompts de IA de forma simples, mas com boa estrutura de engenharia de software.

O problema que motivou o projeto é que muitos prompts são criados de forma dispersa, sem versionamento, sem padrão de qualidade e sem um critério claro de prioridade para revisão.

Como solução, desenvolvi um sistema com API REST, frontend estático, banco SQLite, análise local de qualidade de prompt e um serviço de priorização. A proposta foi manter o projeto viável para demonstração, mas ainda assim aderente a boas práticas.

Na arquitetura, utilizei Clean Architecture. A camada `domain` concentra o modelo principal. A camada `application` reúne schemas, casos de uso e serviços. A camada `infrastructure` lida com banco e repositório. A camada `api` expõe os endpoints com FastAPI. E a camada `frontend` faz o consumo da API com HTML, CSS e JavaScript puro.

Na demonstração do CRUD, eu mostro a criação de um prompt, a listagem dos registros, a consulta por ID, a edição com incremento de versão e a exclusão.

Depois, apresento o analisador local de prompts. Ele avalia critérios como persona, contexto, instruções, saída esperada, objetivo explícito, restrições, tags e descrição. O resultado é um score com classificação e sugestões de melhoria.

Em seguida, mostro o `priority_advisor.py`, que utiliza o score, o status do prompt e a quantidade de lacunas para sugerir uma prioridade entre Low, Medium, High e Critical, além de explicar a recomendação.

No frontend estático, a interface permite cadastrar, editar, excluir, analisar e priorizar prompts de forma simples, centralizando os fluxos principais para apresentação.

Também demonstro a execução com Docker Compose, subindo a API em `localhost:8000` e o frontend em `localhost:8080`.

Um ponto importante é que a IA também participou da construção do sistema. Para tornar esse processo auditável, o projeto mantém um arquivo `prompts\PROMPTS.md` com a sequência de prompts usada na construção.

Como aprendizado, o projeto mostra que é possível combinar engenharia de software, IA aplicada e documentação clara em um MVP enxuto e didático.

Como próximos passos, eu destacaria autenticação, integração com provedores reais de IA, uso de PostgreSQL, histórico de versões e observabilidade.

Para encerrar, o PromptHub AI Python entrega um fluxo completo e funcional para gestão de prompts, com foco em clareza arquitetural e valor acadêmico.
