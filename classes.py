class Cliente:
    
    def __init__(self,nome,cpf,refeicao,pagamento):
        self.nome = nome
        self.cpf = cpf
        self.pagamento = pagamento

    def definir_refeicao(self,nome,refeicao):
        self.refeicao = refeicao
        return self.refeicao

class Refeicao:
    def __init__(self, nome, ingredientes):
        self.nome = nome
        self.ingredientes = ingredientes

class Bebida:
    def __init__(self, nome):
        self.nome = nome

class Restaurante:
    def __init__(self,nome,pratos,bebidas):
        self.nome = nome
        self.pratos = pratos
        self.bebidas = bebidas

    def incluir_prato(self,pratos):
        quant_pratos = input("Quantos pratos serão incluídos?")
        for a in range(0, quant_pratos):
            self.pratos[a] = Refeicao()
            self.pratos[a].nome = input("Qual nome do prato ?")
            quant_ingredientes = input("Qual a quantidade de ingredientes?")
            for b in range(0,quant_ingredientes):
                self.pratos[a].ingredientes[b] = input("Ingrediente %i" %b)

        return " Pratos incluídos com sucesso\nTotal de %i pratos" %quant_pratos
    
    def incluir_bebida(self,bebidas):
        quant_bebidas = input("Quantas bebidas serão incluídas?")
        for a in range(0, quant_bebidas):
            self.bebida[a] = Bebida()
            self.bebidas[a].nome = input("Qual nome da bebida %i?" %a)

        return " Bebidas incluídas com sucesso\nTotal de %i bebidas" %quant_bebidas
            
