def imc(peso,altura):
    altura= altura*altura
    imc = peso/altura
    print(imc)

peso = float(input("qual seu peso"))
altura = float(input("qual sua altura"))

imc(peso,altura)
