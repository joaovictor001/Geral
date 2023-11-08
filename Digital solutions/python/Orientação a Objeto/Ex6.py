class Caneta:
    def __init__(self, cor: str , marca: str):
        self.cor = cor
        self.marca = marca


    def escrever(self):
        self.cor
        print("Voce esta escrevendo com a  ", self.cor ,"com a caneta da marca",self.marca)

corcaneta = input("fala a cor ai: ")
marcacaneta = input("Fala a marca ai: ")
caneta = Caneta(corcaneta,marcacaneta)
caneta.escrever()