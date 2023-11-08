class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir(self):
        print("Seu nome é: ",self.nome ,"E tem ", self.idade,"Anos")
pnome = (input("Qual o nome?: "))
pidade = int(input("Qual a idade?: "))

dados = Pessoas(pnome,pidade)
dados.exibir()