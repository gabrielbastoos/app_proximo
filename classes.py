class Aluno:
    #construtor
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    #verificacao de cadastro
    def estou_cadastrado(self):
        return "Estou cadastrado"

class Cliente:
    
    def __init__(self,nome,cpf,refeicao,pagamento):
        self.nome = nome
        self.cpf = cpf
        self.pagamento = pagamento

    def definir_refeicao(self,nome,refeicao):
        self.refeicao = refeicao
        return self.refeicao