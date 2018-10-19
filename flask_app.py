import classes

from flask import Flask, request, render_template
app = Flask(__name__)

verdinho = Restaurante("Verdinho")
verdinho.incluir_pratos()
verdinho.incluir_bedidas()

spobreto = Restaurante("Spobreto")
spobreto.incluir_pratos()
spobreto.incluir_bebidas()


@app.route("/")
def hello():
    lista_restaurantes = [verdinho.nome,spobreto.nome]
    return render_template('restaurante.html', lista_restaurantes=restaurantes)

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

@app.route("/pedido", methods=['POST'])
def pedido():

    restaurante_escolhido = request.form['restaurante_escolhido']

    return render_template('pedido.html', nome=nome, cpf=cpf, forma_pagamento = forma_pagamento)

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

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
