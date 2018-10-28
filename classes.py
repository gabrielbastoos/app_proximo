import sys
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Cliente(Base):
	__tablename__ = 'cliente'

	id = Column(Integer, primary_key=True)
	nome = Column(String(250), nullable=False)
	cpf = Column(Integer, nullable=False)
	pagamento = Column(String(250), nullable=False)
	pedido = Column(String(250),nullable=False)

	@property
	def serialize(self):
		return {
		'id': self.id,
		'nome': self.nome,
		'cpf': self.cpf,
		'pagamento': self.pagamento,
		'pedido': self.pedido
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



bd_escolhido = raw_input("Qual banco de dados estara sendo acessado ?")

if (bd_escolhido == "gabriel-local"):
    engine = create_engine("mysql+mysqldb://root:password@localhost/app_proximo")

if (bd_escolhido == "gabriel-online"):
    engine = create_engine('mysql+mysqldb://gabrielbastoos:mysqlpassword@gabrielbastoos.mysql.pythonanywhere-services.com/gabrielbastoos$default')

if (bd_escolhido == "carol"):
    engine = create_engine('mysql+mysqldb://caroluchoa:xcsdwe23@caroluchoa.mysql.pythonanywhere-services.com/caroluchoa$restaurants')

if (bd_escolhido == "arthur"):
    engine = create_engine('mysql+mysqldb://arthurbarcellos:P@ssw0rd@arthurbarcellos.mysql.pythonanywhere-services.com/arthurbarcellos$mylojas')

Base.metadata.create_all(engine)
