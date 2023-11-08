try:
    x = int(input("Enter a number: ")) #Digite uma letra.
    x = x + 10
    print(x) #A resposta precisa ser um número.
except ValueError:
    print("Numero invalido!!!")

