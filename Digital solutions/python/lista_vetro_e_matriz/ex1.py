import numpy as np


vetor = np.array(list(map(int, input("Digite 5 números separados por espaço: ").split(","))))
soma = np.sum(vetor/5)

print(soma)