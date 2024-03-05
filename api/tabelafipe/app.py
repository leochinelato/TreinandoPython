from src.utils import pegar_carro
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

tipos = ['carros', 'motos', 'caminhoes']


@app.route('/')
def index():
    return render_template('index.html', title='Veículos', tipos=tipos)

@app.route('/carros')
def carros():
    return render_template('carros.html', title='Carros')

@app.route('/motos')
def motos():
    return render_template('motos.html', title='Motos')

@app.route('/caminhoes')
def caminhoes():
    return render_template('caminhoes.html', title='Caminhoes')

app.run(debug=True)