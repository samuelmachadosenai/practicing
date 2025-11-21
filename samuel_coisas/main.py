# import os

# Funções

def par_ou_impar(numero): 
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

def maior_ou_menor(numero1, numero2):
    if numero1 > numero2:
        print(f"{numero1} é maior que {numero2}")
    elif numero1 < numero2:
        print(f"{numero2} é maior que {numero1}")
    
def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    
def countdown(numero):
    for i in range(numero, 0, -1):
        print(i)

# Programa principal
    num = int(input("Digite um número:"))
    print("Escolha uma opção:")           
    print("a) Verificar se um número é par ou ímpar")
    print("b) Comparar dois números")
    print("c) Mostrar a tabuada de um número")
    print("d) Contagem regressiva")
    opcao = input()


    if opcao == "a":
        par_ou_impar(num)
    elif opcao == "b":
        num2 = int(input("Digite outro número: "))
        maior_ou_menor(num, num2)
    elif opcao == "c":
        tabuada(num)
    elif opcao == "d":
        countdown(num)



    # while True:
    #     a = input("Tentar novamente?\n1. Sim\n0. Não")
    #     if a == 1:
    #         # os.system("cls")
    #     # else:
    #         # os.system("cls")
    #         print("Encerrado.")
    #     break