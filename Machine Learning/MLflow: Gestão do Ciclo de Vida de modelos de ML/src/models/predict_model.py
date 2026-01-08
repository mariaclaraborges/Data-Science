import mlflow
import pandas as pd

logged_model = '/home/mborges/estudos/mlflow/mlruns/2/models/m-eb2f49a2374c4a2581c78befb71435f9/artifacts'

# Use pyfunc para carregar o modelo - aceita DataFrame
loaded_model = mlflow.pyfunc.load_model(logged_model)

data = pd.read_csv('data/processed/casas_X.csv')
predicted = loaded_model.predict(data) 

data['predicted'] = predicted
data.to_csv('data/processed/precos.csv', index=False)

'''
Este é o ciclo completo de ML em produção:

Treinamento (train_model.py): Treina o modelo com dados históricos
Registro (MLflow): Versiona e armazena o modelo
Inferência (predict_model.py): Usa o modelo para prever novos casos

'''