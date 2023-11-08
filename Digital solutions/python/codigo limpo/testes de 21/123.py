import random


class Dealer:
    def __init__(self, identificacao):
        self.cartas_baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.identificacao = identificacao

    def dar_carta(self):
        carta = random.choice(self.cartas_baralho)
        return carta


class Jogador:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.pontos = 0
        self.cartas_da_mao = []


class Jogar(self):
    jogadores = input("Quantos jogadores vão jogar? ")
    for i in range(jogadores):


dea = Dealer("João")

# Distribui uma carta
carta = dea.dar_carta()
print(f"{dea.identificacao} distribuiu a carta: {carta}")
