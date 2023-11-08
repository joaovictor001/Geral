import numpy as np
matriz = np.array([[8,7,8],
                   [7,9,10],
                   [10,8,10]])

s1 = np.sum(matriz[0])
s1 = s1/3
s2 = np.sum(matriz[1])
s1 = s1/3
s3 = np.sum(matriz[2])
s1 = s1/3

if s1 > s2 and s1 > s3:
    print("A maior avaliaçao é:  ")
    print(s1)
    print("Do restaurante 1 ")
if s2 > s1 and s2 > s3:
    print("A maior avaliaçao é " )
    print(s2)
    print("Do restaurante 1 ")
if s3 > s1 and s3 > s2:
    print("A maior avaliaçao é " )
    print(s3)
    print("Do restaurante 1 ")


