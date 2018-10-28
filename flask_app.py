
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



@app.route('/restaurantes/<int:restaurante_id>/<int:refeicao_id>/')
@app.route('/restaurantes/<int:restaurante_id>/menu/<int:refeicao_id>/menu')
def mostrarBebida(restaurante_id,refeicao_id):
    
    restaurante = session.query(Restaurante).filter_by(id=restaurante_id).one()
    refeicao = session.query(Refeicao).filter_by(id=refeicao_id).one()
    bebida = session.query(Bebida).filter_by(restaurante_id=restaurante.id)
    return render_template('bebida.html', restaurante=restaurante, bebida=bebida,refeicao=refeicao)



@app.route('/restaurantes/<int:restaurante_id>/<int:refeicao_id>/<int:bebida_id>')
@app.route('/restaurantes/<int:restaurante_id>/menu/<int:refeicao_id>/<int:bebida_id>/dados')
def dados(restaurante_id,refeicao_id,bebida_id):

    restaurante = session.query(Restaurante).filter_by(id=restaurante_id).one()
    refeicao = session.query(Refeicao).filter_by(id=refeicao_id).one()
    bebida = session.query(Bebida).filter_by(id=bebida_id).one()

    return render_template('dados.html', restaurante=restaurante, refeicao_escolhida=refeicao, bebida_escolhida=bebida)

@app.route("/pedido", methods=['POST'])
def pedido():

    restaurante_id = request.form['restaurante']
    refeicao_escolhida_id = request.form['refeicao_escolhida']
    bebida_escolhida_id = request.form['bebida_escolhida']
    nome = request.form['nome']
    cpf = request.form['cpf']
    pagamento = request.form['pagamento'] 

    restaurante = session.query(Restaurante).filter_by(id=restaurante_id).one()
    refeicao = session.query(Refeicao).filter_by(id=refeicao_escolhida_id).one()
    bebida = session.query(Bebida).filter_by(id=bebida_escolhida_id).one()

    pedido = "Refeicao: "+refeicao.nome+"\t Bebida: "+bebida.nome

    return render_template('fim.html', pedido=pedido)
'''
@app.route("/fim", methods=['POST'])
def fim():
    return render_template('fim.html')
'''
if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)

