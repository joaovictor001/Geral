class Livro:
    def __init__(self, titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def resumo(self):
        print("Titulo: ",self.titulo,"Autor: ", self.autor)

titulo = input("Qual o Titulo da obra?: ")
autor = input("Qual o nome do autor?: ")

livro = Livro(autor,titulo)
livro.resumo()