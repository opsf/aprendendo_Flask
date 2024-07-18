from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['futebol','xadrez','dama']
    return render_template('lista.html', titulo='JOGO', jogos=lista)

app.run()