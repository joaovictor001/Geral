class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


conta = ContaBancaria()

conta.depositar(100)
print("Saldo após depósito: R$", conta.saldo)

conta.sacar(50)
print("Saldo após saque: R$", conta.saldo)

conta.sacar(80)
