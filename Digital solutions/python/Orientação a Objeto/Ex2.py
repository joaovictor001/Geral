class Retangulo:
    def __init__(self, altura: int, largura: int):
        self.altura = altura
        self.largura = largura

    def perimetro(self):
        total = (self.altura + self.largura) * 2
        print(total)


altura = int(input("Informe a  altura:"))
largura = int(input("imforme a largura"))

resultado = Retangulo(altura, largura)
resultado.perimetro()
