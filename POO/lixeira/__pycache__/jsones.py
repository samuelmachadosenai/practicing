import json as j
import POO.lixeira.classes as c

data = c.User.users_info



def salvar_user():
    with open("data.json", "a") as file:
        j.dump(data, file, indent=4)

# with open("data.json", "r") as f:
#     dados = j.load(f)  

# def deletar_user():
