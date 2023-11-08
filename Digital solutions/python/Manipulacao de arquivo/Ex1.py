

with open("meu_arquivo_ex1.txt", "w") as arquivo:
    arquivo.write("ola mundo\n")

with open("meu_arquivo_ex1.txt", "r") as arquivo:
	ler = arquivo.read()
print(ler)
    