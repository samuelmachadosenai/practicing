import classes as c
import jsones as j
import os
import time

usuario = None

def loading():
    while True:
        
        os.system("cls")
        print(".\n")
        time.sleep(0.8)
        os.system("cls")
        print("..\n")
        time.sleep(0.8)
        os.system("cls")
        print("...\n")
        time.sleep(0.9)
        os.system("cls")
        break



def criar():
    loading()
    global usuario
    usuario = c.User.criar_user()
    j.salvar_user()

    # global log
    # log = c.User.dic
    print(c.User.users_info, "\n")





def login():
    loading()
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
    loading()
    print("-"*24, "\nMENU FODA")
    # print(valor)

login()
menu()


# valor = log["nome"]
# menu()
