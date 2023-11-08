class carro:
    def __init__(self, velocidade : int):
        self.velocidade = velocidade


    def acelerar(self):
        if self.velocidade >=0:
            velocidade = 10
            self.velocidade += 10
            print("Agora voce esta a ",self.velocidade)
        else:
            print("Muito devagar")

    def freiar(self):
        if self.velocidade >=0:
            velocidade = 10
            self.velocidade -= 10
            print("Agora voce esta a ",self.velocidade)
        else:
            print("Muito devagar")




svelocidade = int(input("Esta dirigindo a quantos km/s: "))
dirigindo = carro(svelocidade)
while svelocidade > 10:

    escolha = int(input("Digite 1 para Acelerar \n Digite 2 para frear"))
    if escolha == 1 :
        dirigindo.acelerar()
    else:
        dirigindo.freiar()
