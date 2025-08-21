import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
response = requests.get(url)

print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = [] #cria uma lista vazia para o nome do restaurante
        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else:
    print(f'Erro ao buscar dados: {response.status_code}')

#criação e manipulação de arquivos
for nome_restaurante, dados in dados_restaurante.items(): #só os itens que existem no dicionário de cada restaurante
    nome_do_arquivo = f'{nome_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
