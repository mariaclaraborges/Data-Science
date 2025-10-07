# Churn Prediction – EDA, Feature Engineering e Modeling

Projeto de análise exploratória de dados (EDA), engenharia de atributos e treinamento de modelos de Machine Learning para prever churn (cancelamento) de clientes utilizando o dataset [“Customer Churn Prediction: Analysis” (Kaggle)](https://www.kaggle.com/datasets/abdullah0a/telecom-customer-churn-insights-for-analysis/data).
## 1. Dataset

- Fonte: Kaggle – Customer Churn Prediction: Analysis  
- Arquivo principal: `customer_churn_data.csv`
- Alvo (variável dependente): `Churn` (Yes / No)

### Principais variáveis usadas (neste primeiro experimento)
- Age  
- Gender  
- Tenure  
- MonthlyCharges  
- Churn (alvo binário convertido para 0/1)

## 2. Objetivo

Construir um baseline de predição de churn testando alguns algoritmos clássicos de classificação e preparar o terreno para melhorias futuras (novos atributos, métricas adicionais, balanceamento etc.).

## 3. Etapas Realizadas

### 3.1 Carregamento e Inspeção Inicial
- Leitura do CSV com `pandas`.
- `df.head()`, `df.info()`, `df.describe()` para visão geral de tipos, volume e estatísticas.
- Contagem de valores ausentes: `df.isna().sum()` e total de NaNs.
- Verificação de duplicados: `df.duplicated().sum()`.

### 3.2 Tratamento de Dados
- Observado valor ausente apenas (no contexto usado) em `InternetService`; preenchido com string vazia:  
  `df["InternetService"] = df["InternetService"].fillna("")`
- Não foi aplicado `dropna()` para evitar perda maciça de linhas.
- (Possível melhoria futura: analisar se preenchimento vazio é semanticamente adequado.)

### 3.3 Análise Exploratória (EDA)
- Distribuição de `Churn` com gráfico de pizza (desejável complementar com counts absolutos).
- Estatísticas por grupo:
  - `df.groupby("Churn")["MonthlyCharges"].mean()`
  - `df.groupby("Churn")["Tenure"].mean()`
  - `df.groupby("Churn")["Age"].mean()`
  - `df.groupby("ContractType")["MonthlyCharges"].mean()`
  - `df.groupby(["Churn", "Gender"])["MonthlyCharges"].mean()`
- Histogramas de `MonthlyCharges` e `Tenure`.
- Matriz de correlação apenas com colunas numéricas (`select_dtypes(include=['number'])`).
  - Ex.: correlação forte entre `Tenure` e `TotalCharges` (quando presente).
  - Correlação fraca ou nula entre pares como `Age` e `Tenure`.

### 3.4 Feature Engineering (primeira versão simples)
- Seleção de preditores: `["Age", "Gender", "Tenure", "MonthlyCharges"]`
- Transformação de categóricas binárias:
  - `Gender`: Female → 1, caso contrário → 0
  - `Churn`: Yes → 1, No → 0
- (Melhorias futuras: one-hot encoding de variáveis como ContractType, PaymentMethod, InternetService, etc.)

### 3.5 Split Treino/Teste
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```
- Proporção: 80% treino / 20% teste (pode-se adicionar `stratify=y` futuramente para manter proporção de classes).

### 3.6 Padronização
```python
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)   # Ajuste só no treino
X_test  = scaler.transform(X_test)        # Usa estatísticas do treino
joblib.dump(scaler, "scaler.pkl")
```
- Evita data leakage.
- Importante para modelos baseados em distância (KNN, SVM) e otimização numérica.

### 3.7 Modelos Testados

| Modelo | Ajuste de Hiperparâmetros | Observações |
|--------|---------------------------|-------------|
| LogisticRegression | Default | Baseline interpretável |
| KNeighborsClassifier | GridSearchCV (n_neighbors, weights) | Sensível à escala |
| SVC | GridSearchCV (C, kernel) | Pode ganhar com ajuste de mais parâmetros (gamma) |
| DecisionTreeClassifier | GridSearchCV (criterion, splitter, max_depth, etc.) | Risco de overfitting sem poda |
| RandomForestClassifier | GridSearchCV (n_estimators, max_features, bootstrap) | Robustez e importância de features |

Exemplo de grid (KNN):
```python
param_grid = {
  "n_neighbors": [3, 5, 7, 9],
  "weights": ["uniform", "distance"]
}
```

### 3.8 Métrica de Avaliação
- Utilizado apenas `Accuracy`:
  ```python
  def modelperformance(predictions):
      print(f"Accuracy: {accuracy_score(y_test, predictions)}")
  ```
- Observação: Churn costuma ser desbalanceado – só acurácia pode ser enganosa.
- Recomenda-se adicionar:
  - `precision_score, recall_score, f1_score`
  - `classification_report`
  - `roc_auc_score`
  - Matriz de confusão

