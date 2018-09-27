import classes.py

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('login.html')

@app.route("/echo", methods=['POST'])
def echo():

    # Aqui sao os dados do formulario
    texto = request.form['text']
    senha = request.form['text2']

    #verificacao de senha
    if texto == "claudio" and senha == "1234":
        texto = "Acesso permitido"
    else: texto = "Acesso negado"

    return render_template('login2.html', text=texto)

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/echo2", methods=['POST'])
def echo2():

    # Aqui sao os dados do formulario
    texto = request.form['name']
    senha = request.form['pass']
    nota = request.form['grade']

    registro = texto + "-" + senha + "-" + nota
    print(registro)
    #vou jogar no arquivo
    arq = open('lista.txt', 'w')
    arq.write(registro)
    arq.close()


    return render_template('cadastrado.html', text=texto)

