class Jogadores:
    def __init__(self, nome=None, idade = None, saldo = 1000):
        self.cartas = []
        self.pontuacao = 0
        self.nome = nome  
        self.idade = idade  
        self.saldo = saldo  


    def calcular_pontuacao(self):
        total_pontos = sum([min(10, carta.valor) for carta in self.cartas])
        # Check for aces and add 11 points if not busting
        for carta in self.cartas:
            if carta.valor == 1 and total_pontos + 10 <= 21:
                total_pontos += 10
        return total_pontos

    def pegar_carta(self, baralho):
        carta = baralho.distribuir()
        self.cartas.append(carta)
        self.pontuacao = self.calcular_pontuacao()
        if carta.valor == 1:
            self.pontuacao += 1  

    def estourou(self):
        return self.pontuacao > 21