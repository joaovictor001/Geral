import numpy as np
vetor = np.array(list(map(int, input("Informe os gastos: ").split(","))))
soma = np.sum(vetor)

print(soma)