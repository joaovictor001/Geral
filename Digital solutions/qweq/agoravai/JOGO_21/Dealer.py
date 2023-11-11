import random
class Dealer:
    def __init__(self,indentificacao):
        self.indetificacao = indentificacao
        valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4
        self.cartas = [Carta(valor) for valor in valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self):
        return self.cartas.pop()
#retornei com str
class Carta:
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        if self.valor == 11:
            return "J"
        elif self.valor == 12:
            return "Q"
        elif self.valor == 13:
            return "K"
        elif self.valor == 1:
            return "A"
        else:
            return str(self.valor)