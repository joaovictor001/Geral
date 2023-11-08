class Relogio_Apple:
    def __init__(self, modelo:int, cor: str , usuario: str, senha: str , Bateria: int):
        self.modelo = modelo
        self.cor = cor
        self.__usuario = usuario
        self.__senha = senha
        self.Bateria = Bateria

    def  get_usuario(self):
        return self.__usuario
    def get_senha(self):
        return self.__senha

    def set_usuario(self, novo_user):
        self.__usuario = novo_user
    def set_senha(self, nova_senha):
        self.__senha = nova_senha

    @property
    def login(self):
        return self.__senha, self.__usuario
    @login.setter
    def login(self, value):
        nova_senha, novo_user = value
        self.__senha = nova_senha
        self.__usuario = novo_user
        

    def logar(self):
        Usuario = input("Imforme o usuario> ")
        senha = input("Imforme a senha>  ")

        if Usuario == self.__usuario and senha == self.__senha:
            print("login correto voce entrou")
        else:
            self.esqueceu_senha()


    def esqueceu_senha(self):
        tentar_Novamente = int(input("Para tentar novamente, Digite 1\n Para recuperar senha, Digite 2"))
        if tentar_Novamente == 2:
            new_user =  input("Novo nome de user:")
            new_senha = input("Novo nome de user:")
            self.set_login(new_senha,new_user)
        else:
            print("a")

    def carregar(self):
        if self.Bateria <= 50: 
            print("E preciso carregar seu relogio")
        else:
          print("a")




Relogio = Relogio_Apple (3,"rosa","joao","123",90)
Relogio.logar()
