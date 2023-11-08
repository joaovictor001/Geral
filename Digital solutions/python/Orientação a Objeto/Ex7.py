class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Não é possível dividir por zero"
        return a / b


calculadora = Calculadora()

resultado_soma = calculadora.somar(5, 3)
resultado_subtracao = calculadora.subtrair(10, 4)
resultado_multiplicacao = calculadora.multiplicar(6, 2)
resultado_divisao = calculadora.dividir(8, 2)

print("Soma: ", resultado_soma)
print("Subtração: ", resultado_subtracao)
print("Multiplicação: ", resultado_multiplicacao)
print("Divisão: ", resultado_divisao)