class Colaborador_bosch:
    cnpj = '45.990.181/0001-89'

    def __init__(self, nome, edv, salario):
        self.nome = nome
        self. edv = edv
        self.salario = salario

    @staticmethod
    def retornar_cnpj():
        return Colaborador_bosch.cnpj



Colaborador_bosch.retornar_cnpj()