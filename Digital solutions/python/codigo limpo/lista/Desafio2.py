def mair_n(n1,n2):
    if n1 > n2:
        print(f"{n1} maior que {n2} ")
    elif n2 > n1:
        print(f"{n2} menor que {n1} ")
    elif n1 == n2:
        print(f"Os dois são iguais")
    else:
        print(f"{n2} menor que {n1} ")

print("O REQUISITO É NO MINIMO DOIS NUMEROS!!!")
while True:
    for t in range (1):
        n1 = int(input("Digite um numero:"))
        for i in range (1):
            n2 = int(input("Digite um numero:"))
    mair_n(n1,n2)



