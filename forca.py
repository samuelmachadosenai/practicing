import os
import random

def cls():
    os.system("cls")



# lista_palavras = ["amor", "argentina", "anjo", "maçã", "lâmpada"]

# palavra = random.choice(lista_palavras)
palavra = "amor"
espaco = []

def coisar(palavra):
    global espaco

    for i in range(0, len(palavra)):
        espaco.append("_")

    espaco_str = str(espaco)
    espaco_str = espaco_str.replace(",", "")
    espaco_str = espaco_str.replace("]", "")
    espaco_str = espaco_str.replace("[", "")
    espaco_str = espaco_str.replace("'", "")
    
    espaco_str = replace

    print(espaco_str)

while True:
    cls()
    print("A palavra tem {} letras.".format(len(palavra)))

    coisar(palavra)


  
        
        

    letr = str(input("\n\nDigite uma letra:\n"))


    if letr in palavra:
        posicao = palavra.index(letr)



        posicao_print = posicao + 1
        
        # _, _, _, _

        

        print("A letra '{}' está na posição {}.".format(letr.capitalize(), posicao_print))

        print(palavra)
    else:
        print("Não há letra '{}' na palavra.".format(letr.capitalize()))


    
    break