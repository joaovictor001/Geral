try:
    numero = int(input("Difite um número: "))
    print(f"O numero digitado pe {numero}")
    numero += 1
except ValueError as log:
    print("valor inserido invalido")
    print(log)

    with open("logv.txt", "w") as arquivo:
        arquivo.write(log)