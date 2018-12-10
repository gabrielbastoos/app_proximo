from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from classes import Base, Cliente, Restaurante, Refeicao, Bebida

#engine = create_engine("mysql+mysqldb://root:password@localhost/app_proximo")
#engine = create_engine('mysql+mysqldb://gabrielbastoos:mysqlpassword@gabrielbastoos.mysql.pythonanywhere-services.com/gabrielbastoos$default')
#engine = create_engine('mysql+mysqldb://caroluchoa:xcsdwe23@caroluchoa.mysql.pythonanywhere-services.com/caroluchoa$restaurants')
engine = create_engine('mysql+mysqldb://arthurbarcellos:tutuskt0@arthurbarcellos.mysql.pythonanywhere-services.com/arthurbarcellos$newlojas')


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Truncando tabelas p/ sobrescrever dados
session.execute('''SET FOREIGN_KEY_CHECKS = 0''')
session.execute('''TRUNCATE TABLE restaurante''')
session.execute('''TRUNCATE TABLE refeicao''')
session.execute('''TRUNCATE TABLE bebida''')
session.execute('''SET FOREIGN_KEY_CHECKS = 1''')
session.commit()
session.close()


#Menu do Burguesao

restaurante1 = Restaurante(nome="Burguesao")

session.add(restaurante1)
session.commit()

refeicao1 = Refeicao(nome="Carne Assada com Fritas", preco="R$15.25", restaurante=restaurante1)

session.add(refeicao1)
session.commit()


refeicao2 = Refeicao(nome="Strogonoff com Fritas", preco="R$13.25", restaurante=restaurante1)

session.add(refeicao2)
session.commit()

refeicao3 = Refeicao(nome="File de Frango grelhado", preco="R$14.00", restaurante=restaurante1)

session.add(refeicao3)
session.commit()

bebida1 = Bebida(nome="Coca Cola", preco="R$4.00", restaurante=restaurante1)
session.add(bebida1)
session.commit()

bebida2 = Bebida(nome="Guarana", preco="R$4.00", restaurante=restaurante1)
session.add(bebida2)
session.commit()

bebida3 = Bebida(nome="Suco", preco="R$5.00", restaurante=restaurante1)
session.add(bebida3)
session.commit()



#Menu do Verdinho
restaurante2 = Restaurante(nome="Verdinho")

session.add(restaurante1)
session.commit()

refeicao1 = Refeicao(nome="Penne Carbonara", preco="R$15.25",  restaurante=restaurante2)

session.add(refeicao1)
session.commit()

refeicao2 = Refeicao(nome="Lasanha de Frango", preco="R$15.00", restaurante=restaurante2)

session.add(refeicao2)
session.commit()

refeicao3 = Refeicao(nome="Frango a Parmegiana com Fritas", preco="R$15.00", restaurante=restaurante2)

session.add(refeicao3)
session.commit()

bebida1 = Bebida(nome="Coca Cola", preco="R$4.00", restaurante=restaurante2)
session.add(bebida1)
session.commit()

bebida2 = Bebida(nome="Guarana", preco="R$4.00", restaurante=restaurante2)
session.add(bebida2)
session.commit()

bebida3 = Bebida(nome="Suco", preco="R$5.00", restaurante=restaurante2)
session.add(bebida3)
session.commit()


#Menu do Projectus
restaurante3 = Restaurante(nome="Projectus")

session.add(restaurante1)
session.commit()

refeicao1 = Refeicao(nome="Frango a Milanesa com Fritas", preco="R$13.25", restaurante=restaurante3)

session.add(refeicao1)
session.commit()

refeicao2 = Refeicao(nome="Nhoque a Bolonhesa", preco="R$18.00", restaurante=restaurante3)

session.add(refeicao2)
session.commit()

refeicao3 = Refeicao(nome="Escondidinho a Bolonhesa", preco="R$15.00",  restaurante=restaurante3)

session.add(refeicao3)
session.commit()

bebida1 = Bebida(nome="Coca Cola", preco="R$4.00", restaurante=restaurante3)
session.add(bebida1)
session.commit()

bebida2 = Bebida(nome="Guarana", preco="R$4.00", restaurante=restaurante3)
session.add(bebida2)
session.commit()

bebida3 = Bebida(nome="Suco", preco="R$5.00", restaurante=restaurante3)
session.add(bebida3)
session.commit()



print ("Banco de dados completo")
