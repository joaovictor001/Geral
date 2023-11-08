class Cachorro:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        
    @classmethod
    def criar_cachorro(cls, nm, idade, raca):
        return Cachorro(nome=nm, idade=idade, raca=raca)
print('Deseja continuar')
german_pastor = Cachorro.criar_cachorro("Cleitão da massa", 180, 'pastor do alemão')