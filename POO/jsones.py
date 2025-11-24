import json as j
import classes as c

data = c.User.dic



def salvar_user():
    with open("data.json", "a") as file:
        j.dump(data, file, indent=4)

# with open("data.json", "r") as f:
#     dados = j.load(f)  

# def deletar_user():
