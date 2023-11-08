class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        return self.nota >= 7


estudante1 = Estudante("João", 8)
estudante2 = Estudante("Maria", 5)

print("Aprovado:", estudante1.aprovado())
print("Aprovado:", estudante2.aprovado())
