class Circulo:
    def __init__(self, raio:int):
        self.raio = raio
    def Area(self):
        area = self.raio * self.raio
        print(area)

num = int(input("Qual o raio?: "))
circulo = Circulo(num)

circulo.Area()