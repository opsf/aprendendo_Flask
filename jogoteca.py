from flask import Flask, render_template, request, redirect

class Jogo():
    def __init__(self, nome, categoria, console):
        self._nome=nome
        self._categoria = categoria
        self._console = console

jogo1 = Jogo('xadrez','tabuleiro','pau')
jogo2 = Jogo('dama','tabuleiro','pc')
jogo3 = Jogo('futebol', 'equipe',  'campo')
lista = [jogo1, jogo2,jogo3]

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('lista.html', titulo='JOGO', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['senha']=='orivalda':
        return redirect('/')
    else:
        return redirect('/login')



app.run(debug=True)