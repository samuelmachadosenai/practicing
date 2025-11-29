class User:
    users_info = []
    dic = {}
    def __init__(self, id, nome, senha, status):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.status = status
        # adiciona users à lista de existentes
        global dic
        dic = self.__dict__
        global users_info
        users_info = User.users_info.append(dic)
    


    def criar_id():
        import random as r
        
        n = r.randint(100, 300)
            
        num = str(n)
        
        low = ["a", "b", "c", "d", "e"]
        
        letra = r.choice(low)
        
        l = str(letra)

        id = num + l
   

        return id

    @classmethod
    def criar_user(cls):  
        id = cls.criar_id()
        nome = str(input("Digite o nome: "))
        senha = int(input("Digite a sua senha: "))
        status = True
        return cls(id, nome, senha, status)
    

    
    # def mostrar_users():

