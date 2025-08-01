
# Documentação: Agente de Pesquisa com LangGraph

## 1. Visão Geral
Este notebook implementa um agente de pesquisa inteligente usando LangGraph, que pode buscar informações na web e em artigos científicos com base nas consultas do usuário.

## 2. Configuração Inicial
- Configuração de variáveis de ambiente (`OPENAI_API_KEY`, `TAVILY_API_KEY`)
- Importação das bibliotecas necessárias (LangChain, LangGraph)
- Inicialização do modelo de linguagem GPT-4o

## 3. Conceitos Básicos do LangChain
- Demonstração do uso de `PromptTemplate` para criar templates de prompts
- Criação de uma cadeia simples com `modelo_de_prompt | llm | StrOutputParser()`
- Obtenção de resposta básica sobre IA na agricultura

## 4. Implementação de Ferramentas (Tools)
- Configuração da ferramenta de busca na web usando Tavily API (`busca_web`)
- Configuração da ferramenta de busca de artigos científicos (`tool_cientifica`) usando Arxiv
- Vinculação das ferramentas ao modelo de linguagem (`llm_com_ferramenta`)

## 5. Criação de Agentes ReAct
- Implementação de um agente ReAct para busca web (`agente_web`)
- Implementação de um agente ReAct para busca científica (`agente_cientifico`)
- Demonstração de invocação desses agentes com consultas específicas

## 6. Estrutura de Estado do Agente
- Definição da classe `AgentState` como `TypedDict` para manter o estado do agente:
  - `user_query`: consulta do usuário
  - `web_answer`: resposta da busca na web
  - `scientific_answer`: resposta da busca científica
  - `final_answer`: resposta final combinada

## 7. Agentes como Funções
- Implementação da função `funcao_agente_web` que integra o agente ReAct de busca na web
- Implementação da função `funcao_agente_cientifico` para busca no Arxiv
- Cada função recebe e atualiza o estado do agente

## 8. Construção de Grafo Simples
- Criação de um grafo inicial usando `StateGraph(AgentState)`
- Adição de um único nó (`agente_web`) e conexão entre START e END
- Compilação e visualização do grafo usando Mermaid

## 9. Implementação de Supervisor
- Criação da função `supervisor_node` para combinar resultados de diferentes fontes
- Expansão do grafo para incluir busca web, busca científica e supervisor
- Fluxo linear de execução: web → científico → supervisor

## 10. Roteador Inteligente
- Implementação da função `router_agent` para decidir qual ferramenta usar
- O roteador analisa a consulta e escolhe entre busca web ou científica
- Adição de bordas condicionais no grafo baseadas na decisão do roteador

## 11. Fluxo Final
- Grafo completo com roteamento, busca web, busca científica e supervisor
- Demonstração de consultas com diferentes instruções:
  - "Use apenas fontes da Web"
  - "Use apenas fontes científicas" 
  - Consulta genérica (decisão automática pelo roteador)

O resultado final é um agente flexível que pode escolher automaticamente a fonte de informação mais apropriada e combinar os resultados em uma resposta formatada, dependendo do tipo de consulta do usuário.
