
# Preços de Imóveis Utilizando Regressão Linear

## Objetivo

O objetivo deste notebook é **estimar os preços de imóveis** utilizando técnicas de regressão linear. O trabalho busca:
- Identificar os fatores que mais contribuem para a precificação dos imóveis.
- Entender qual aspecto é mais relevante e influencia mais no preço.
- Precificar imóveis novos a partir do modelo ajustado.

---

## 1. Importação de Bibliotecas

Foram importadas bibliotecas para manipulação de dados (`pandas`, `numpy`), visualização (`matplotlib`, `seaborn`, `plotly`), e modelagem estatística/machine learning (`sklearn`, `statsmodels`).

---

## 2. Carregamento e Exploração dos Dados

- Os dados foram lidos de um arquivo CSV.
- Foi feita uma análise inicial das colunas e tipos de dados.
- A coluna de identificação (`Id`) foi removida por não ser relevante para a análise.

---

## 3. Análise de Correlação

- Calculou-se a matriz de correlação de Pearson entre as variáveis.
- Visualização da matriz de correlação com um heatmap para identificar relações lineares entre as variáveis.
- Discussão sobre as correlações mais relevantes, como a relação entre garagem, área e banheiros.

---

## 4. Visualização de Relações Entre Variáveis

- Foram feitos gráficos de dispersão para analisar a relação entre área construída e preço do imóvel.
- Utilização de linhas de tendência (reta de regressão) para visualizar o comportamento linear.

---

## 5. Definição das Variáveis

- Definição da variável resposta (`preco_de_venda`) e das variáveis preditoras.
- Separação dos dados em conjuntos de treino e teste (70% treino, 30% teste).

---

## 6. Ajuste do Primeiro Modelo de Regressão Linear

- Ajuste de um modelo simples usando apenas a área do primeiro andar como preditora.
- Análise dos coeficientes do modelo e interpretação do intercepto e do coeficiente angular.
- Avaliação do R² para medir o quanto da variação do preço é explicada pela área.

---

## 7. Análise dos Resíduos

- Análise da distribuição dos resíduos do modelo para verificar possíveis problemas de ajuste.

---

## 8. Avaliação do Modelo em Dados de Teste

- Previsão dos preços no conjunto de teste e cálculo do R² para avaliar a capacidade preditiva do modelo.

---

## 9. Expansão do Modelo com Novas Variáveis

- Análise exploratória de outras variáveis que podem influenciar o preço (banheiros, área do segundo andar, garagem, qualidade da cozinha).
- Ajuste de modelos múltiplos, incluindo diferentes combinações de variáveis explicativas.
- Comparação entre modelos usando o R² e o número de parâmetros.

---

## 10. Seleção de Modelos

- Discussão sobre métodos de seleção de variáveis (forward, backward, stepwise).
- Escolha do modelo final (modelo_3) com base em desempenho e simplicidade.

---

## 11. Precificação de Imóveis

- Utilização do modelo escolhido para prever o preço de imóveis novos, tanto para um imóvel específico quanto para um conjunto de novos imóveis.
- Adição de constante aos dados para compatibilidade com o modelo.

---

## 12. Multicolinearidade

- Cálculo do Fator de Inflação da Variância (VIF) para verificar multicolinearidade entre as variáveis explicativas dos modelos.
- Interpretação dos valores de VIF para identificar possíveis problemas.

---

## 13. Análise dos Resíduos do Modelo Final

- Visualização da relação entre valores previstos e reais.
- Análise dos resíduos em função das previsões para identificar padrões ou problemas de ajuste, especialmente em imóveis mais caros.

---

## Conclusão

O notebook apresenta um fluxo completo de análise de dados, modelagem, avaliação e interpretação de modelos de regressão linear para precificação de imóveis. O processo inclui desde a exploração dos dados até a avaliação de modelos múltiplos e análise de resíduos, permitindo identificar os fatores mais relevantes para o preço dos imóveis e prever valores para novos casos.
