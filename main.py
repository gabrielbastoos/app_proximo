import classes

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('acesso.html')

@app.route("/echo", methods=['POST'])
def echo():

    # Aqui sao os dados do formulario
    nome = request.form['nome']
    cpf = request.form['cpf']
    forma_pagamento = request.form['formas_pagamento']

    return render_template('pedido.html', nome=nome, cpf=cpf, forma_pagamento = forma_pagamento)

'''@app.route("/app_proximo/cadastro")
def cadastro():
    return render_template('cadastro.html')
'''

@app.route("/echo2", methods=['POST'])
def echo2():

   ''' # Aqui sao os dados do formulario
    texto = request.form['name']
    senha = request.form['pass']
    nota = request.form['grade']

    registro = texto + "-" + senha + "-" + nota
    print(registro)
    #vou jogar no arquivo
    arq = open('lista.txt', 'w')
    arq.write(registro)
    arq.close()
'''

    return render_template('cadastrado.html')

