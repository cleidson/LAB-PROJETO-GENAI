# Forum — Reflexão sobre o Projeto PromptHub AI Python

## 1. Qual foi o mini-projeto escolhido?

O mini-projeto escolhido foi o **PromptHub AI Python**, um sistema acadêmico para cadastro, versionamento, análise e priorização de prompts de Inteligência Artificial.

### Objetivos Principais

O objetivo do projeto é apresentar uma aplicação simples, funcional e bem estruturada, demonstrando:

- Criação de uma API REST com Python e FastAPI
- Aplicação de Clean Architecture com separação clara entre camadas
- Persistência de dados com SQLite
- Frontend estático consumindo a API
- Execução local e com Docker
- Testes automatizados com `pytest`
- Documentação técnica completa
- Uso estruturado de assistentes de IA durante o desenvolvimento
- Análise e priorização de prompts como prática de Engenharia de IA

### Problema Resolvido

O projeto resolve um problema comum em times que usam IA: prompts importantes acabam espalhados, sem padrão, sem versionamento, sem critério de qualidade e sem clareza sobre o que precisa ser melhorado primeiro.

Com isso, o PromptHub AI Python oferece:

- Centralização dos prompts em um CRUD simples
- Avaliação local da qualidade estrutural de cada prompt
- Priorização objetiva para revisão ou reutilização
- Rastreabilidade do processo de construção assistida por IA

### Funcionalidades Principais

1. **CRUD Completo**: Cadastro, listagem, atualização e exclusão de prompts
2. **Análise de Qualidade**: Avalia estrutura do prompt com base em critérios como persona, contexto, instruções, formato de saída e restrições
3. **Prioridade Recomendada**: Sugere nível de prioridade (Low, Medium, High, Critical) para melhoria
4. **Versionamento**: Cada alteração incrementa a versão do prompt
5. **Status de Prompt**: Rastreia se o prompt está Ativo, Arquivado, Em Revisão ou Descontinuado
6. **Frontend Estático**: Interface HTML, CSS e JavaScript para consumo da API
7. **Documentação Swagger**: Documentação interativa automática

---

## 2. Como a IA Generativa Apoiou seu Desenvolvimento?

### Ferramentas de IA Utilizadas

Durante o desenvolvimento, utilizei o **GitHub Copilot CLI**, powered by **GPT-5.4** (model ID: `gpt-5.4`), como agente de IA para acelerar etapas importantes do projeto.

### Etapas onde a IA Acelerou o Desenvolvimento

A IA foi usada em praticamente todas as fases do projeto:

#### 2.1. Concepção do Escopo e Arquitetura
- Definição inicial do problema e escopo
- Proposta de arquitetura em camadas (Clean Architecture)
- Estruturação de pastas e organização do projeto
- Identificação de responsabilidades por camada

#### 2.2. Implementação das Camadas
- **Domain**: Geração das entidades (`PromptTemplate`) e enums (`PromptStatus`)
- **Application**: Criação de schemas Pydantic, contratos de repositório (ports) e serviços
- **Infrastructure**: Implementação do repositório SQLite, modelos de persistência e conversão entidade-modelo
- **API**: Desenvolvimento das rotas FastAPI com tratamento de erros
- **Frontend**: Estruturação da interface HTML, CSS e JavaScript

#### 2.3. Geração e Refinamento de Contratos
- Criação de DTOs explícitos para separação de camadas
- Definição de exceções customizadas para cada cenário de erro
- Implementação de portas (ports) abstratas para reduzir acoplamento

#### 2.4. Escrita e Ampliação dos Testes
- Expansão da suíte de testes de 9 para 15 testes
- Cobertura de cenários positivos (CRUD bem-sucedido)
- Cobertura de cenários negativos (validação, não encontrado, erros internos)
- Geração de fixtures reutilizáveis para isolamento de testes

#### 2.5. Elaboração de Diagramas
- Criação do diagrama de arquitetura em Mermaid
- Diagrama de fluxo de testes mostrando cobertura
- Visualização de camadas e fluxos de dados

#### 2.6. Documentação Técnica
- Revisão e consolidação do README
- Criação de seções sobre objetivos, instalação, execução, endpoints
- Elaboração de roteiro de apresentação
- Criação de roteiro de demonstração técnica
- Documentação de padrões de commit por camada

#### 2.7. Refatorações Coordenadas
- Refatorações multiarquivo para melhorar separação de responsabilidades
- Adição de docstrings em todas as funções e classes principais
- Ajustes na organização de imports e dependências

### Ganhos de Produtividade Observados

Os principais ganhos de produtividade vieram da capacidade de acelerar tarefas repetitivas e de alto volume de contexto:

- **Revisão de estrutura**: A IA identificou inconsistências na separação de camadas
- **Atualização de documentação**: Consolidação rápida de conteúdo espalhado
- **Refatorações coordenadas**: Aplicação simultânea de mudanças em múltiplos arquivos
- **Expansão da suíte de testes**: Geração de casos de teste cobrindo cenários de erro
- **Padronização de commits**: Criação de guia para commits semânticos por camada

---

## 3. Quais Desafios Encontrados na Organização, Documentação ou Submissão do Projeto?

### 3.1. Desafio de Organização

#### Separação de Responsabilidades entre Camadas
**Problema**: Inicialmente, havia dúvida sobre onde posicionar certos componentes (como DTOs, validações, converções). A IA sugeriu colocações que faziam sentido isoladamente, mas que violavam os princípios de Clean Architecture quando consideradas no contexto geral.

**Solução**: Estabeleci critérios explícitos:
- **Domain**: Apenas entidades e enums puros (sem dependências externas)
- **Application**: Schemas, contratos, serviços, casos de uso
- **Infrastructure**: Modelos de persistência, repositório, banco de dados
- **API**: Rotas, mapeamento de schemas, tratamento de exceções HTTP

#### Organização de Documentação
**Problema**: A documentação foi criada de forma dispersa em múltiplos locais (raiz, docs/, prompts/). Havia duplicação (PROMPTS.md na raiz e em prompts/).

**Solução**: Consolidei toda a documentação em uma hierarquia clara:
- `docs/arquitetura/`: Arquitetura e diagramas
- `docs/produto/`: Roteiros, escopo, backlog
- `docs/tests/`: Relatórios e diagramas de testes
- `prompts/PROMPTS.md`: Histórico de construção assistida por IA
- `README.md`: Entrada principal com referências cruzadas

### 3.2. Desafio de Documentação

#### Completude da Documentação
**Problema**: O README inicialmente cobria "o quê", mas não cobria adequadamente "por quê" e "como usar".

**Solução**: Expandir o README com:
- Seção "O que o projeto resolve" explicando o problema
- "Guia rápido reprodutível" com passos passo-a-passo
- Seção dedicada a "Como a IA Acelerou Este Projeto" com modelo específico
- Links cruzados para toda documentação complementar
- Diagrama de arquitetura visual

#### Docstrings e Comentários
**Problema**: Código inicial tinha poucas docstrings. A IA gerava comentários genéricos que não agregavam valor.

**Solução**: Aplicar critério:
- Docstrings obrigatórias em classes e funções públicas
- Apenas comentar lógica não-óbvia
- Evitar comentários óbvios como "# incrementa contador"
- Incluir exemplos nos docstrings de métodos complexos

#### Contratos Explícitos
**Problema**: Schemas e DTOs não deixavam claro quais campos eram opcionais, quais validações eram aplicadas, e quais eram as mensagens de erro esperadas.

**Solução**: Estruturar contratos com:
- Tipos explícitos (str, int, List, Optional)
- Validadores Pydantic com mensagens claras
- Exemplos no schema
- Docstring descrevendo o propósito

### 3.3. Desafio de Submissão

#### Rastreabilidade do Processo de IA
**Problema**: Não era claro que o projeto foi desenvolvido com IA. Sem documentação adequada, parecia apenas um código gerado.

**Solução**: Criar arquivo `prompts/PROMPTS.md` registrando:
- Cada prompt utilizado no desenvolvimento
- Sequência cronológica de decisões
- Tela de resultado de cada etapa
- Justificativa para refatorações

Isso transformou o projeto em um "laboratório de IA aplicada" e não apenas um CRUD.

#### Validação de Qualidade
**Problema**: A IA gerou código funcional, mas era necessário garantir que atendesse critérios acadêmicos de qualidade, arquitetura e documentação.

**Solução**: Criar checklist de validação:
- [ ] Arquitetura limpa com separação de camadas
- [ ] Testes cobrindo fluxo principal e cenários de erro
- [ ] Documentação reprodutível
- [ ] Docstrings em todos os públicos
- [ ] Mensagens de erro claras
- [ ] Diagramas descrevendo arquitetura e testes
- [ ] Commit semântico com histórico rastreável

---

## 4. Quais Cuidados Foram Necessários para Revisar, Testar e Validar as Sugestões da IA?

### 4.1. Cuidados na Revisão de Código

#### Verificação de Arquitetura
**Prática Aplicada**: Após cada sugestão da IA, revisei se:
- A entidade de domínio (`PromptTemplate`) é realmente pura (sem imports de banco, HTTP, etc.)
- O repositório implementa corretamente o contrato (port) definido na camada de aplicação
- As rotas da API não contêm lógica de negócio (delegam para serviço)
- Os schemas de entrada/saída estão na camada apropriada

**Exemplo**: A IA sugeriu inicialmente que o repositório retornasse SQLModel diretamente para a aplicação. Corrigi para que o repositório converta o modelo SQLite em entidade de domínio, reduzindo acoplamento.

#### Verificação de Nomes e Semântica
**Prática Aplicada**: Revisei se nomes de variáveis, funções e classes:
- Eram significativos no contexto do domínio (prompt, persona, análise, prioridade)
- Seguiam convenções Python (snake_case para variáveis, PascalCase para classes)
- Não conflitavam com palavras-chave ou imports
- Tinham length razoável (nem muito curto, nem muito longo)

#### Verificação de Tratamento de Erros
**Prática Aplicada**: Validei se:
- Exceções customizadas eram levantadas nos lugares corretos
- Mensagens de erro eram claras e acionáveis
- Códigos HTTP estavam corretos (404 para não encontrado, 400 para validação, 500 para erro interno)
- Não havia erros silenciosos (catch sem re-raise ou logging)

### 4.2. Cuidados em Testes

#### Isolamento de Testes
**Prática Aplicada**: Garantir que:
- Cada teste usasse um banco SQLite temporário (via `tmp_path` do pytest)
- Testes não dependessem um do outro (ordem não importa)
- Fixtures preparassem dados apenas necessários para o teste
- Limpeza automática após cada teste

**Verificação**: Rodar testes múltiplas vezes em ordem aleatória com `pytest -x --tb=short` para garantir determinismo.

#### Cobertura de Cenários
**Prática Aplicada**: Expandir a suíte de testes para cobrir:
- **Cenários positivos**: CRUD bem-sucedido, análise com resultado esperado, prioridade calculada
- **Cenários negativos**: Validação de campo obrigatório, prompt não encontrado (404), erro interno (500)
- **Casos-limite**: Strings vazias, títulos duplicados, valores None

**Verificação**: Revisar `docs/tests/resultado-testes.md` e `docs/tests/diagrama-testes.md` para garantir cobertura visual.

#### Validação de Asserções
**Prática Aplicada**: Verificar que cada asserção era:
- Específica (não apenas verificar se a resposta não é None)
- Legível (estrutura clara do que está sendo testado)
- Razoável (não testa comportamento de bibliotecas externas, apenas seu código)

**Exemplo**: Em vez de `assert response.status_code == 200`, usar `assert response.status_code == 201 and response.json()["id"]` para validar tanto o status quanto a estrutura da resposta.

### 4.3. Cuidados em Validação Funcional

#### Teste Manual de Fluxos
**Prática Aplicada**: Antes de validar a IA como concluída:
1. Subir a API com `uvicorn app.api.main:app --reload`
2. Testar cada endpoint no Swagger em `http://localhost:8000/docs`
3. Executar o frontend em `http://localhost:8080`
4. Criar, listar, atualizar, analisar e priorizar um prompt completo
5. Verificar que o banco SQLite persistiu os dados

#### Teste com Docker
**Prática Aplicada**: Verificar que:
- A imagem Docker era construída sem erros
- Os containers iniciavam sem travamentos
- A API respondia em `http://localhost:8000`
- O frontend carregava corretamente
- O banco SQLite era criado e persistido

**Comando**: `docker compose up` seguido de validação manual.

#### Reprodutibilidade
**Prática Aplicada**: Seguir o "Guia rápido reprodutível" do README do zero:
1. Clonar repositório em pasta limpa
2. Criar venv do zero
3. Instalar requirements.txt
4. Executar API, testes, frontend
5. Verificar que tudo funciona sem modificações

Isso garantiu que a documentação era realmente reprodutível e não dependia de artefatos locais não documentados.

### 4.4. Cuidados na Revisão de Documentação

#### Validação de Links e Referências
**Prática Aplicada**: Verificar que:
- Todos os links internos (ex: `docs\arquitetura\arquitetura.md`) existiam
- Caminhos de arquivo eram corretos (Windows-style com backslash)
- Referências cruzadas mantinham consistência
- Exemplos de código eram compiláveis/executáveis

#### Validação de Diagrama
**Prática Aplicada**: Revisar Mermaid para:
- Sintaxe correta (sem erros de parsing)
- Completude (todas as camadas, fluxos e decisões representadas)
- Legibilidade (sem boxes sobrepostos, fluxo lógico claro)

#### Clareza da Narrativa
**Prática Aplicada**: Reler documentação com mindset de novo desenvolvedor:
- Instruções de instalação eram passo-a-passo sem pulos?
- Seções sobre IA mencionavam modelo específico e versão?
- Exemplos eram reais e testados?
- Limitações eram claras sobre o que o MVP não fazia?

### 4.5. Cuidados Específicos com IA

#### Não Substituir Decisão Arquitetural
**Cuidado Aplicado**: A IA sugeriu várias soluções arquiteturais (ex: usar ORM full como SQLAlchemy, usar decoradores complexos, usar herança múltipla). Revisei cada uma com critério:
- Alinha com Clean Architecture?
- Adiciona complexidade desnecessária para um MVP?
- Pode ser facilmente estendida depois?
- Tem suporte e documentação disponível?

**Decisão Tomada**: Manter SQLModel simples (não usar ORM full), usar Depends() do FastAPI (não criar DI custom), herança única ou composição (não múltipla).

#### Revisar Explicações da IA sobre seu próprio Código
**Cuidado Aplicado**: A IA às vezes gera código correto, mas explica incorretamente. Exemplo:
- "Este decorator aplica autenticação" (mas na verdade só valida formato de token)
- "Esta função é O(1)" (mas na verdade é O(n) por causa do loop interno)

**Ação**: Testar comportamento real do código, não confiar apenas na explicação.

#### Validar Afirmações sobre Conformidade
**Cuidado Aplicado**: A IA afirmou que "O projeto segue SOLID" após refatoração. Revisei manualmente:
- Single Responsibility: Cada classe tem uma razão para mudar? ✓
- Open/Closed: Posso estender sem modificar existente? ✓
- Liskov Substitution: Subclasses são substituíveis? (N/A, poucas heranças)
- Interface Segregation: Interfaces não forçam métodos não usados? ✓
- Dependency Inversion: Dependo de abstrações, não implementações? ✓

---

## 5. Conclusão

O desenvolvimento do **PromptHub AI Python** demonstrou que a IA generativa é uma ferramenta poderosa para acelerar desenvolvimento, mas não substitui o julgamento técnico e a revisão cuidadosa.

Os principais aprendizados:

1. **IA acelera tarefas conhecidas**: Expansão de testes, refatoração, documentação
2. **IA não substitui decisão arquitetural**: Humano define direção, IA sugere implementação
3. **Revisão é essencial**: Código correto ≠ código bem estruturado
4. **Rastreabilidade importa**: Manter histórico de decisões torna o projeto mais valioso
5. **Testes e documentação são mais críticos com IA**: Amplificam confiança no código gerado

O arquivo `prompts/PROMPTS.md` registra esse processo de forma transparente, permitindo que qualquer pessoa entenda não apenas o resultado final, mas como a IA foi utilizada conscientemente como ferramenta de engenharia.

---

## Referências

- **README.md**: Documentação principal do projeto
- **prompts/PROMPTS.md**: Histórico completo de prompts e decisões
- **docs/arquitetura/arquitetura.md**: Documentação de arquitetura
- **docs/tests/resultado-testes.md**: Resultado de testes e checklist QA
- **docs/produto/roteiro-demonstracao-tecnica.md**: Guia de demonstração técnica
