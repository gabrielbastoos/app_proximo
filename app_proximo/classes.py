class Aluno:
    #construtor
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    #verificacao de cadastro
    def estou_cadastrado(self):
        return "Estou cadastrado"

