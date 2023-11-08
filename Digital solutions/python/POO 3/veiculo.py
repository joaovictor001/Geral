class Veiculo:
    def __init__(self, tank):
        self.marca = 'Honda'
        self.tank = tank

    def acelerar(self):
        print("VRUUUUUUUUMMMMMMMMMMM")


class Carro(Veiculo):
    def __init__(self, marca, tank, qtdportas):
        super.__init__(marca, tank)
        self.ports = qtdportas

vaiculo1 = Veiculo('Honda', 200000)

vaiculo1.acelerar()

carro1 = Carro('ferrari', 555555555555, 2)

carro1.acelerar()