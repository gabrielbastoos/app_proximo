import sys
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuario(Base):
	__tablename__ = 'usuario'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	password = Column(String(250), nullable=False)

	@property
	def serialize(self):
		return {
		'id': self.id,
		'name': self.name,
		'password': self.password,
		}

class Cliente(Base):
	__tablename__ = 'cliente'

	id = Column(Integer, primary_key=True)
	nome = Column(String(250), nullable=False)
	cpf = Column(Integer, nullable=False)
	pagamento = Column(String(250), nullable=False)
	obs = Column(String(250))
	pedido = Column(String(250),nullable=False)
	preco_pedido = Column(Integer,nullable=False)
	data_pedido = Column(String(250), nullable=False)
	hora_pedido = Column(String(250), nullable=False)
	restaurante_id = Column(Integer, ForeignKey('restaurante.id'))

	@property
	def serialize(self):
		return {
		'id': self.id,
		'nome': self.nome,
		'cpf': self.cpf,
		'pagamento': self.pagamento,
		'obs' :self.obs,
		'pedido': self.pedido,
		'preco_pedido': self.preco_pedido,
		'data_pedido':self.data_pedido,
		'hora_pedido':self.hora_pedido,
		'restaurante_id': self.restaurante_id
		}

class Restaurante(Base):
	__tablename__ = 'restaurante'
	id = Column(Integer, primary_key=True)
	nome = Column(String(250), nullable=False)
	@property
	def serialize(self):
		return {
		'id': self.id,
		'nome': self.nome
		}

class Refeicao(Base):
	__tablename__ = 'refeicao'

	id = Column(Integer, primary_key=True)
	nome = Column(String(250), nullable=False)
	preco = Column(String(25), nullable=False)
	restaurante_id = Column(Integer, ForeignKey('restaurante.id'))
	restaurante = relationship(Restaurante)

	@property
	def serialize(self):
		return {
		'id': self.id,
		'nome': self.nome,
		'preco': self.preco,
		'restaurante_id': self.restaurante_id
		}


class Bebida(Base):
	__tablename__ = 'bebida'

	id = Column(Integer, primary_key=True)
	nome = Column(String(250), nullable=False)
	preco = Column(String(25), nullable=False)
	restaurante_id = Column(Integer, ForeignKey('restaurante.id'))
	restaurante = relationship(Restaurante)

	@property
	def serialize(self):
		return {
		'id': self.id,
		'nome': self.nome,
		'preco': self.preco,
		'restaurante_id': self.restaurante_id
		}

#engine = create_engine("mysql+mysqldb://root:password@localhost/app_proximo")
#engine = create_engine('mysql+mysqldb://gabrielbastoos:mysqlpassword@gabrielbastoos.mysql.pythonanywhere-services.com/gabrielbastoos$default')
#engine = create_engine('mysql+mysqldb://caroluchoa:xcsdwe23@caroluchoa.mysql.pythonanywhere-services.com/caroluchoa$restaurants')
engine = create_engine('mysql+mysqldb://arthurbarcellos:tutuskt0@arthurbarcellos.mysql.pythonanywhere-services.com/arthurbarcellos$newlojas')

Base.metadata.create_all(engine)
