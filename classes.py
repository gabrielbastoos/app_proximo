# -*- coding: utf-8 -*-
class Cliente:
    
    def __init__(self,nome,cpf,refeicao,pagamento):
        self.nome = nome
        self.cpf = cpf
        self.pagamento = pagamento
        self.refeicao = refeicao

class Refeicao:
    def __init__(self,nome,ingredientes):
        self.nome = nome
        self.ingredientes = ingredientes

class Bebida:
    def __init__(self, nome):
        self.nome = nome

class Restaurante:
    def __init__(self,nome):
        self.nome = nome

    def incluir_prato(self):
        quant_pratos = input("Quantos pratos serão incluídos?")
        for a in range(0, quant_pratos):
            nome = input("Qual nome do prato ?")
            quant_ingredientes = input("Qual a quantidade de ingredientes?")
            for b in range(0,quant_ingredientes):
                ingredientes[b] = input("Ingrediente %i: " %b)
            print(ingredientes)
            prato[a] = Refeicao(nome,ingredientes)    
            #Arquivar objeto !!!!!!!

        print(" Pratos incluídos com sucesso\nTotal de %i pratos" %quant_pratos)
        
        return prato
    
    def incluir_bebida(self):
        quant_bebidas = input("Quantas bebidas serão incluídas?")
        for a in range(0, quant_bebidas):
            nome = input("Qual nome da bebida %i?" %a)
            bebida[a] = Bebida(nome)

        print(" Bebidas incluídas com sucesso\nTotal de %i bebidas" %quant_bebidas)

        return bebida   
