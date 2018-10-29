import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime
from flask import Flask, request, redirect, url_for, flash, render_template, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes import Base, Restaurante, Refeicao, Cliente, Bebida, Usuario

engine = create_engine("mysql+mysqldb://root:password@localhost/app_proximo")
#engine = create_engine('mysql+mysqldb://gabrielbastoos:mysqlpassword@gabrielbastoos.mysql.pythonanywhere-services.com/gabrielbastoos$default')
#engine = create_engine('mysql+mysqldb://caroluchoa:xcsdwe23@caroluchoa.mysql.pythonanywhere-services.com/caroluchoa$restaurants')
#engine = create_engine('mysql+mysqldb://arthurbarcellos:P@ssw0rd@arthurbarcellos.mysql.pythonanywhere-services.com/arthurbarcellos$mylojas')


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

@app.route("/listar_pedidos")
def selecionar_restaurante():
    restaurantes = session.query(Restaurante).all()
    return render_template('selecionarRestaurante.html', restaurantes=restaurantes) 
    
@app.route("/lista_pedido/<int:restaurante_id>/")
def visualizar_pedidos(restaurante_id):
    
    timestamp = datetime.now().date()
    restaurante = session.query(Restaurante).filter_by(id=restaurante_id).one()
    pedidos = session.query(Cliente).filter_by(restaurante_id=restaurante_id).all()
        
    return render_template('lista_pedido.html', restaurante=restaurante, pedidos=pedidos,data_atual=timestamp)

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
    obs = request.form['obs']

    if(obs == "Deseja tirar algo ?"):
        obs = ""

    restaurante = session.query(Restaurante).filter_by(id=restaurante_id).one()
    refeicao = session.query(Refeicao).filter_by(id=refeicao_escolhida_id).one()
    bebida = session.query(Bebida).filter_by(id=bebida_escolhida_id).one()

    pedido = "Refeicao: "+refeicao.nome+"   Bebida: "+bebida.nome

    preco = (float(refeicao.preco.replace("R$","")) + float(bebida.preco.replace("R$","")))

    time = datetime.now().time()
    data = datetime.now().date()

    cliente = Cliente(nome=nome, cpf=cpf, pagamento=pagamento, obs=obs, preco_pedido = preco, pedido=pedido, data_pedido=data, hora_pedido=time, restaurante_id=restaurante.id)
    session.add(cliente)
    session.commit()

    return render_template('fim.html',preco=preco)

@app.route("/login")
def pagina_login():
    return render_template('login.html')


@app.route("/admin_page" , methods=['POST'])
def pagina_admin():

    username = request.form['username']
    password = request.form['password']
    
    username_db = session.query(Usuario).filter_by(name=username).first()

    if(username_db == None):
        return render_template('login.html')

    if (username_db.password == password):
        return render_template('admin.html')
    else:
        return render_template('login.html')

@app.route("/admin_page/cadastrarRestaurante")
def cadastrarRestaurante():

    return render_template('addRestaurante.html')

@app.route("/admin_page/cadastrarRefeicao")
def cadastrarRefeicao():

    return render_template('addRefeicao.html')

@app.route("/admin_page/cadastrarBebida")
def cadastrarBebida():

    return render_template('addBebida.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)