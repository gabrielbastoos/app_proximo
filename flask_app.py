<<<<<<< HEAD
import classes

from flask import Flask, request, render_template
app = Flask(__name__)

verdinho = classes.Restaurante("Verdinho")
#verdinho.incluir_prato()
#verdinho.incluir_bedida()

spobreto = classes.Restaurante("Spobreto")
#spobreto.incluir_prato()
#spobreto.incluir_bebida()

burguesao = classes.Restaurante("Burguesao")
#burguesao.incluir_prato()
#burguesao.incluir_bebida()


@app.route("/")
def hello():
    lista_restaurantes = [verdinho.nome,spobreto.nome,burguesao.nome]
    return render_template('restaurante.html', lista_restaurantes=lista_restaurantes)

@app.route("/echo", methods=['POST'])
def echo():

    # Aqui sao os dados do formulario
    nome = request.form['nome']
    cpf = request.form['cpf']
    forma_pagamento = request.form['formas_pagamento']

    return render_template('pedido.html', nome=nome, cpf=cpf, forma_pagamento = forma_pagamento)


@app.route("/ingrediente", methods=['POST'])
def ingrediente():
    
    refeicao_escolhida = request.form['refeicao']
    bebida_escolhida = request.form['bebida']

    return render_template('ingrediente.html', refeicao_escolhida=refeicao_escolhida,bebida_escolhida=bebida_escolhida)


@app.route("/pedido", methods=['POST'])
def pedido():

    restaurante_escolhido = request.form['lista_restaurantes']

    return render_template('refeicao.html', restaurante_escolhido=restaurante_escolhido)

@app.route("/dados", methods=['POST'])
def dados():

    refeicao_escolhida = request.form['refeicao_escolhida']
    bebida_escolhida = request.form['bebida_escolhida']
    
    return render_template('dados.html',refeicao_escolhida=refeicao_escolhida,bebida_escolhida=bebida_escolhida)

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)

    '''arq = open('lista.txt', 'w')
    arq.write(registro)
    arq.close()
    '''
=======
import classes

from flask import Flask, request, render_template
app = Flask(__name__)

verdinho = classes.Restaurante("Verdinho")
#verdinho.incluir_prato()
#verdinho.incluir_bedida()

spobreto = classes.Restaurante("Spobreto")
#spobreto.incluir_prato()
#spobreto.incluir_bebida()

burguesao = classes.Restaurante("Burguesao")
#burguesao.incluir_prato()
#burguesao.incluir_bebida()


@app.route("/")
def hello():
    lista_restaurantes = [verdinho.nome,spobreto.nome,burguesao.nome]
    return render_template('restaurante.html', lista_restaurantes=lista_restaurantes)

@app.route("/echo", methods=['POST'])
def echo():
    if request.form.get('completo'):
        return redirect(url_for('ingredientes'))
    else:
    # Aqui sao os dados do formulario
    nome = request.form['nome']
    cpf = request.form['cpf']
    forma_pagamento = request.form['formas_pagamento']

    return render_template('pedido.html', nome=nome, cpf=cpf, forma_pagamento = forma_pagamento)

@app.route("/ingredientes", methods=['POST'])
def ingredientes():
    return render_template('ingredientes.html')


@app.route("/pedido", methods=['POST'])
def pedido():

    restaurante_escolhido = request.form['lista_restaurantes']

    return render_template('refeicao.html', restaurante_escolhido=restaurante_escolhido)

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
>>>>>>> 77bb25e82da4c3445e49ac696612531e958f64b1
