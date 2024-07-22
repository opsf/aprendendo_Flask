from flask import Flask, render_template, request, redirect, session, flash

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
app.secret_key='bela'

@app.route('/')
def index():  
    if 'usuario_logado'  not in session or session["usuario_logado"]==None:
        return redirect('/login')
    return render_template('lista.html', titulo='JOGO', jogos=lista)

@app.route('/novo')
def novo():    
    if 'usuario_logado'  not in session or session["usuario_logado"]==None:
        return redirect('/login?proxima=novo')
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
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['senha']=='orivalda':
        session['usuario_logado']=request.form['usuario']
        flash(session['usuario_logado']+ ' logado com sucesso')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário não logado')
        return redirect('/login')

@app.route('/logout')
def logout():
    session["usuario_logado"]=None
    flash("logout efetuado com sucesso")
    return redirect('/')


app.run(debug=True)