import random
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

class Dealer:
    def __init__(self,indentificacao):
        self.indetificacao = indentificacao
        valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4
        self.cartas = [Carta(valor) for valor in valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self):
        return self.cartas.pop()
    


class Jogadores:
    def __init__(self, nome=None, idade = None, saldo = 1000):
        self.cartas = []
        self.pontuacao = 0
        self.nome = nome  
        self.idade = idade  
        self.saldo = saldo  


    def calcular_pontuacao(self):
        total_pontos = sum([min(10, carta.valor) for carta in self.cartas])
        # logica do Ás
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


class Jogar:   
    def __init__(self):
        self.baralho = Dealer("Xavier")
        self.baralho.embaralhar()
        self.jogadores = [] 
        self.mao_dealer = Jogadores()
    

        #Onde sao adicionado os jogadores
        
        
    def adicionar_jogador(self):
        nome = input(f"Nome do Novo Jogador: ")
        idade = int(input("Idade do Novo Jogador: "))
        if idade < 18:
            print("Desculpe, você deve ter pelo menos 18 anos para jogar.")
            exit()
        jogador = Jogadores(nome, idade)
        self.jogadores.append(jogador)


        # Logica para ver quem ganhou ou perdeu o jogo
        #junto eu coloque ja para fazer a conta de sua aposta 

    def calcular_resultados_individuais(self):
        for jogador in self.jogadores:
            print(f"\nMão do Jogador: {jogador.nome}")
            print([c.__repr__() for c in jogador.cartas])
            print(f"Pontuação do Jogador: {jogador.pontuacao}")
            if jogador.estourou():
                print(f"{jogador.nome} estourou! Perdeu {jogador.aposta} fichas.")
                jogador.saldo -= jogador.aposta             
                
            else:
                print(f"{jogador.nome} escolheu parar.")
                if self.mao_dealer.estourou():
                    print("O dealer estourou! Jogador ganhou!")
                    jogador.saldo += jogador.aposta * 2
                    print(f"Ganhou {jogador.aposta} X2 fichas.")
                    print(f"Saldo Total:{jogador.saldo}")
                    

                elif self.mao_dealer == 21:
                    print("Dealer acertou um BlackJack! Jogador perdeu.")
                    
                    jogador.saldo -= jogador.aposta 
                    print(f"Perdeu {jogador.aposta} fichas.")
                    print(f"Saldo Atual:{jogador.saldo}")
                   

                elif self.mao_dealer == 21 and jogador.potuacao == 21:
                    print("É um empate! Aposta devolvida.")
                   
                    print("Perdeu 0 fichas.")
                    print(f"Saldo Atual:{jogador.saldo}")

                elif jogador.pontuacao > self.mao_dealer.pontuacao:
                    print("Jogador tem uma pontuação mais alta! Jogador ganhou!")
                    jogador.saldo += jogador.aposta * 2
                    print(f"Saldo Atual:{jogador.saldo}")
                    

                elif jogador.pontuacao < self.mao_dealer.pontuacao:
                    print("O dealer tem uma pontuação mais alta! Jogador perdeu.")
                    jogador.saldo -= jogador.aposta 
                    print(f"Saldo Atual:{jogador.saldo}")

                elif jogador.pontuacao == 21:
                    print("Jogador acertou um BlackJack! Dealer perdeu.")
                    jogador.saldo += jogador.aposta *2
                    print(f"Saldo Atual:{jogador.saldo}")
                    

                elif self.mao_dealer == jogador.pontuacao:
                    print("É um empate! Aposta devolvida.")
                    print(f"Saldo Atual:{jogador.saldo}")
                    
                print("=-=" * 20)

    def realizar_aposta(self, jogador):
        while True:
            aposta = int(input(f"{jogador.nome}, seu saldo atual é {jogador.saldo}. Quanto você deseja apostar? "))
            if aposta <= jogador.saldo and aposta > 0:
                jogador.aposta = aposta
                break
            else:
                print("Aposta inválida. Certifique-se de que sua aposta seja maior que zero e não exceda seu saldo.")


    def jogar_jogo(self):

        # Osjogadores iniciam com duas carta 
        for jogador in self.jogadores:
            jogador.pegar_carta(self.baralho)
            jogador.pegar_carta(self.baralho)
        self.mao_dealer.pegar_carta(self.baralho)
        self.mao_dealer.pegar_carta(self.baralho)

        print("Mão do Dealer:")
        dealer_first_card = self.mao_dealer.cartas[0]
        print([dealer_first_card.__repr__()]) 

        for jogador in self.jogadores:
            self.realizar_aposta(jogador)

        # Depois de verem sua cartas fazer a aposta ate onde seu saldo permitir
        for jogador in self.jogadores:
            while True:
                print(f"Mão do Jogador: {jogador.nome}")
                print([c.__repr__() for c in jogador.cartas])
                print('Pontos:', jogador.pontuacao)
                acao = input("Você deseja pedir uma carta (Pedir) ou parar (Parar)? ")
                if acao.lower() == 'pedir':
                    jogador.pegar_carta(self.baralho)
                    if jogador.estourou():
                        print("Você estourou!")
                        break
                elif acao.lower() == 'parar':
                    break
                else:
                    print("Ação inválida. Por favor, escolha 'Pedir' ou 'Parar.")
                    continue

        # O Delaeler.pontuacao < 17:r não para de puar car ate que ele fique com 17 ou mais que 17
        while self.mao_dealer:
            self.mao_dealer.pegar_carta(self.baralho)



if __name__ == "__main__":
    
    jogo = Jogar()
    
    
    num_jogadores = int(input("Quantos jogadores desejam jogar? "))

    for i in range(num_jogadores):
        jogo.adicionar_jogador()
    
    jogo.jogar_jogo()
    jogo.calcular_resultados_individuais()



    print("\nMão do Dealer:")
    print([c.__repr__() for c in jogo.mao_dealer.cartas])
    print(f"Pontuação do Dealer: {jogo.mao_dealer.pontuacao}")
