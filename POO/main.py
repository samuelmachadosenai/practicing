import classes as c
import jsones as j
import os
import time

usuario = None





def criar():
    os.system("cls")
    global usuario
    usuario = c.User.criar_user()
    j.salvar_user()
    # global log
    # log = c.User.dic
    print(c.User.users_info, "\n")




def login():
    os.system("cls")
    print("1. Logar")
    print("2. Criar usuário")
    o = int(input())

    if o == 2:
            while True:
                criar()
                break
    elif o == 1:
        while True:
            n = input("Digite seu nome:")
            s = input("Digite sua senha")
            break

def menu():
    os.system("cls")
    # print(valor)


while True:
    
    print(".\n")
    time.sleep(0.8)
    os.system("cls")
    print("..\n")
    time.sleep(0.8)
    os.system("cls")
    print("...\n")
    time.sleep(0.8)
    break

login()


# valor = log["nome"]
# menu()
