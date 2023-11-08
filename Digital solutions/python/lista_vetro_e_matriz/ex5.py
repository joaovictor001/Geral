import numpy as np
matriz = np.array([[14, 27, 35, 19],[42, 56, 73,68],[91, 12, 63,54]])
casa1 = np.sum(matriz[0])
casa2 = np.sum(matriz[1])
casa3 = np.sum(matriz[2])

print(f"O consumo da casa 1 é: {casa1} kWh\n"
      f"O consumo da casa 2 é: {casa2} kWh\n"
      f"O consumo da casa 3 é: {casa3} kWh ")