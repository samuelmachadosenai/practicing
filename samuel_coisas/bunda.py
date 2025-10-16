def bunda():

    while True:
        frase = input("Digite a frase:\n")
        uservezes = int(input("Defina o número de vezes a ser repetida:\n"))
        vezes = 1

        if uservezes > 100:
            print("Acima do limite. Tente novamente.\n")
        else:
            while vezes <= uservezes:
                print(frase)
                vezes += 1
            break


opcao = int(input("digite 1 para bunda\n"))
