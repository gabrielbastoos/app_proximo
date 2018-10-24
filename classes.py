# -*- coding: utf-8 -*-
import sys
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Cliente(Base):
    
#    def __init__(self,nome,cpf,refeicao,pagamento):
#        self.nome = nome
#        self.cpf = cpf
#        self.pagamento = pagamento
#        self.refeicao = refeicao

	__tablename__ = 'cliente'

	nome = Column(String(250), nullable=False)
	cpf = Column(String(250))
	pagamento = Column(String(25), nullable=False)
	@property
	def serialize(self):
		return {
		'nome': self.nome,
		'cpf': self.cpf,
		'pagamento': self.pagamento
		}

class Refeicao(Base):
	__tablename__ = 'refeicao'

	id = Column(Integer, primary_key=True)
	nome = Column(String(250), nullable=False)
	categoria = Column(String(250))
	preco = Column(String(25), nullable=False)
	restaurante_id = Column(Integer, ForeignKey('restaurante.id'))
	restaurante = relationship(Restaurante)

	@property
	def serialize(self):
		return {
		'id': self.id,
		'nome': self.nome,
		'preco': self.preco,
		'categoria': self.categoria,
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

#    def incluir_prato(self):
#       quant_pratos = input("Quantos pratos serão incluídos?")
#        for a in range(0, quant_pratos):
#            nome = input("Qual nome do prato ?")
#            quant_ingredientes = input("Qual a quantidade de ingredientes?")
#            for b in range(0,quant_ingredientes):
#                ingredientes[b] = input("Ingrediente %i: " %b)
#            print(ingredientes)
#            prato[a] = Refeicao(nome,ingredientes)    
#            #Arquivar objeto !!!!!!!

#        print(" Pratos incluídos com sucesso\nTotal de %i pratos" %quant_pratos)
        
#        return prato
    
#    def incluir_bebida(self):
#        quant_bebidas = input("Quantas bebidas serão incluídas?")
#        for a in range(0, quant_bebidas):
#            nome = input("Qual nome da bebida %i?" %a)
#            bebida[a] = Bebida(nome)

#        print(" Bebidas incluídas com sucesso\nTotal de %i bebidas" %quant_bebidas)

#        return bebida   
