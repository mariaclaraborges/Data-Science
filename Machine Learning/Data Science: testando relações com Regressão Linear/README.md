# Análise de Regressão Linear - MLRegressionAlura

Este notebook tem como objetivo aplicar técnicas de **regressão linear** para análise e previsão de preços de imóveis, utilizando dados e ferramentas de ciência de dados em Python.

## Etapas realizadas

1. **Importação e preparação dos dados**
   - Carregamento do dataset.
   - Limpeza e tratamento de dados faltantes.
   - Conversão de variáveis categóricas em variáveis dummy (one-hot encoding).

2. **Análise exploratória**
   - Visualização de distribuições das variáveis.
   - Análise de correlação entre variáveis.

3. **Construção do modelo**
   - Separação dos dados em variáveis independentes (features) e variável dependente (target).
   - Criação do modelo de regressão linear utilizando o método dos mínimos quadrados ordinários (OLS) com a biblioteca `statsmodels`.
   - Avaliação dos coeficientes e interpretação dos resultados.

4. **Diagnóstico do modelo**
   - Cálculo do Fator de Inflação da Variância (VIF) para verificar multicolinearidade entre as variáveis.
   - Análise dos resíduos do modelo para verificar suposições da regressão.

5. **Avaliação de desempenho**
   - Cálculo de métricas como R² e erro médio.
   - Discussão sobre a qualidade do ajuste e possíveis melhorias.

## Bibliotecas utilizadas

- pandas
- numpy
- matplotlib / seaborn
- scikit-learn
- statsmodels

## Como executar

1. Instale as dependências:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
   ```
2. Execute o notebook em um ambiente Jupyter Notebook ou JupyterLab.

## Observações

- O notebook está organizado em células comentadas para facilitar o entendimento.
- Os resultados estatísticos detalhados são apresentados ao longo do notebook, incluindo tabelas de coeficientes, métricas de avaliação e gráficos de diagnóstico.
