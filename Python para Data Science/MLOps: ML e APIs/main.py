from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
import pandas as pd
import pickle

modelo = pickle.load(open("modelo.sav", "rb"))
colunas = ["tamanho", "ano", "garagem", "preco"]

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'

basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required
def home():
    return "Welcome to the MLOps ML API!"

@app.route('/sentiment/<frase>')
@basic_auth.required
def sentiment(frase):
    tb = TextBlob(frase)
    polarity = tb.sentiment.polarity
    return f"Sentiment polarity of the phrase '{frase}' is {polarity}"

@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas if col != 'preco']
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])

app.run(debug=True)
