
from flask import Flask, request, redirect, url_for, flash, render_template, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes import Base, Restaurante, Refeicao, Cliente, Bebida

engine = create_engine("mysql+mysqldb://root:password@localhost/app_proximo")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#verdinho = classes.Restaurante("Verdinho")
#verdinho.incluir_prato()
#verdinho.incluir_bedida()

#spobreto = classes.Restaurante("Spobreto")
#spobreto.incluir_prato()
#spobreto.incluir_bebida()

#burguesao = classes.Restaurante("Burguesao")
#burguesao.incluir_prato()
#burguesao.incluir_bebida()



@app.route("/")
@app.route('/#')
@app.route('/restaurantes/')
def hello():
	restaurantes = session.query(Restaurante).all()
	return render_template('restaurante.html', restaurantes=restaurantes)


@app.route('/restaurantes/<int:restaurante_id>/')
@app.route('/restaurantes/<int:restaurante_id>/menu/')
def mostrarRefeicao(restaurante_id):

	restaurante = session.query(Restaurante).filter_by(id=restaurante_id).one()
	refeicao = session.query(Refeicao).filter_by(restaurante_id=restaurante.id)

	return render_template('refeicao.html', restaurante=restaurante, refeicao=refeicao)


@app.route('/restaurantes/<int:restaurante_id>/<string:refeicao>/')
@app.route('/restaurantes/<int:restaurante_id>/menu/<string:refeicao>/menu')
def mostrarBebida(restaurante_id,refeicao):
    
    restaurante = session.query(Restaurante).filter_by(id=restaurante_id).one()
    bebida = session.query(Bebida).filter_by(restaurante_id=restaurante.id)
    return render_template('bebida.html', restaurante=restaurante, bebida=bebida,refeicao=refeicao)

@app.route("/dados")
def dados():
    
    refeicao_escolhida = request.form['refeicao_escolhida']
    bebida_escolhida = request.form['bebida_escolhida']

    return render_template('dados.html', refeicao_escolhida=refeicao_escolhida, bebida_escolhida=bebida_escolhida)

'''@app.route("/pedido", methods=['POST'])
def pedido():

    restaurante_escolhido = request.form['lista_restaurantes']

    return render_template('refeicao.html', restaurante_escolhido=restaurante_escolhido)

@app.route("/ingrediente", methods=['POST'])
def ingrediente():

    refeicao_escolhida = request.form['refeicao']
    bebida_escolhida = request.form['bebida']

    return render_template('ingrediente.html', refeicao_escolhida=refeicao_escolhida,bebida_escolhida=bebida_escolhida)

@app.route("/fim", methods=['POST'])
def fim():
    return render_template('fim.html')
'''
if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)

