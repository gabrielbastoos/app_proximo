from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from classes import Base, Cliente, Restaurante, Refeicao

engine = create_engine('mysql+mysqldb://caroluchoa:xcsdwe23@caroluchoa.mysql.pythonanywhere-services.com/caroluchoa$restaurants')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Truncando tabelas p/ sobrescrever dados
session.execute('''SET FOREIGN_KEY_CHECKS = 0''')
session.execute('''TRUNCATE TABLE restaurante''')
session.execute('''TRUNCATE TABLE refeicao''')
session.execute('''SET FOREIGN_KEY_CHECKS = 1''')
session.commit()
session.close()


#Menu do Burguesao

restaurante1 = Restaurante(nome="Burguesao")

session.add(restaurante1)
session.commit()

refeicao1 = Refeicao(nome="Carne Assada com Fritas", preco="R$15.25", categoria="Refeicao", restaurante=restaurante1)

session.add(refeicao1)
session.commit()


refeicao2 = Refeicao(nome="Strogonoff com Fritas", preco="R$13.25", categoria="Refeicao", restaurante=restaurante1)

session.add(refeicao2)
session.commit()

refeicao3 = Refeicao(nome="Agua com Gas", preco="R$4.00", categoria="Bebida", restaurante=restaurante1)

session.add(refeicao3)
session.commit()



#Menu do Verdinho
restaurante2 = Restaurante(nome="Verdinho")

session.add(restaurante1)
session.commit()

refeicao1 = Refeicao(nome="Penne Carbonara", preco="R$15.25", categoria="Refeicao", restaurante=restaurante2)

session.add(refeicao1)
session.commit()

refeicao2 = Refeicao(nome="Coca-Cola", preco="R$5.00", categoria="Bebida", restaurante=restaurante2)

session.add(refeicao2)
session.commit()

refeicao3 = Refeicao(nome="Frango a Parmegiana com Fritas", preco="R$15.00", categoria="Refeicao", restaurante=restaurante2)

session.add(refeicao3)
session.commit()

#Menu do Projectus
restaurante3 = Restaurante(nome="Projectus")

session.add(restaurante1)
session.commit()

refeicao1 = Refeicao(nome="Frango a Milanesa com Fritas", preco="R$13.25", categoria="Refeicao", restaurante=restaurante3)

session.add(refeicao1)
session.commit()

refeicao2 = Refeicao(nome="Suco de Laranja", preco="R$7.00", categoria="Bebida", restaurante=restaurante3)

session.add(refeicao2)
session.commit()

refeicao3 = Refeicao(nome="Guarana", preco="R$5.00", categoria="Bebida", restaurante=restaurante3)

session.add(refeicao3)
session.commit()


print ("Banco de dados completo")
