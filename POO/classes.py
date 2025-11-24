import random as r

n = r.randint(100, 300)
num = str(n)
letra = r.choice("a", "b", "c", "d", "e")

id = num + letra




class User:
    users_info = []

    def __init__(self, nome, senha):


        self.nome = nome
        self.senha = senha

        # adiciona users à lista de existentes
        dic = self.__dict__
        global users_info
        User.users_info.append(dic)


    
    @classmethod
    def criar_user(cls):

        id = 
        nome = str(input("Digite o nome: "))
        senha = int(input("Digite a sua senha: "))
        return cls(id, nome, senha)


    


    
    # def mostrar_users():

