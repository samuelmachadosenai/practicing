import random
import time
import os

def repetidor_de_frases():

    while True:
        os.system("cls")
        frase = input("Digite a frase:\n")
        uservezes = int(input("Defina o número de vezes a ser repetida:\n"))
        vezes = 1

        if uservezes > 100:
            print("Acima do limite. Tente novamente.\n")
        else:
            while vezes <= uservezes:
                time.sleep(1)
                print(frase)
                vezes += 1


                
            opcao = int(input("\nTentar novamente?\n1 - Sim\n0 - Voltar ao Menu\n"))
                
            match opcao:
                case 1:
                    repetidor_de_frases()
            break
        

def acerte_a_conta():
    score = 0
    
    # Adicionar sistema de SCORE (acerto +1, erro -1)


    while True:
        os.system("cls")
        print("SCORE:", score)
        while True:
            

            
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            r = 0
            operacao = int(input("\nEscolha uma operação:\n1. Soma\n2. Substração\n3. Multiplicação\n4. Divisão\n"))

            match operacao:
                case 1:
                    r = int(input("\nQuanto é {} mais {}?\n".format(a, b)))
                    if r != (a + b):
                        print("Errado.\nVocê é burro.\nO resultado é {}.".format(a + b))

                    else:
                        print("Mandou bem!\nO resultado é {}.".format(a + b))
                        
                    

                case 2:
                    r = int(input("\nQuanto é {} menos {}?\n".format(a, b)))
                    if r != (a-b):
                        print("Errado.\nVocê é burro.\nO resultado é {}.".format(a - b))
                    else:
                        print("Mandou bem!\nO resultado é {}.".format(a - b))
                
                case 3:
                    r = int(input("Quanto é {} multiplicado por {}?\n".format(a, b)))
                    if r != (a*b):
                        print("Errado.\nVocê é burro.\nO resultado é {}.".format(a*b))
                    else:
                        print("Mandou bem!\nO resultado é {}.".format(a*b))
                     

                case 4: 
                    r = int(input("Quanto é {} dividido por {}?\n".format(a, b)))
                    if r != (a/b):
                        print("Errado.\nVocê é burro.\nO resultado é {}.".format(a/b))
                    else:
                        print("Mandou bem!\nO resultado é {}.".format(a/b))
                
                case 5:
                    r = int(input("Qual a raiz quadrada de {}?\n".format(a)))
                    if r != (a ** (1/2)):
                        print("Errado.\nVocê é burro.\nO resultado é {}.".format(a ** (1/2)))
                    else:
                        print("Mandou bem!\nO resultado é {}.".format(a ** (1/2)))
           
                



            opcao = int(input("\n1. Outra operação\n0 - Voltar ao Menu.\n"))
            if opcao == 1:
                acerte_a_conta()
            else:
                break

def elogiador():
    while True:
        os.system("cls")
        g = int(input("Você é menino ou menina?\n1. Menino\n2. Menina\n0. Voltar ao menu principal\n"))

        if g == 1:
            while True:
                elogio = ["incrível", "inteligente", "forte", "corajoso", "talentoso", "dedicado", "gentil", "carismático", "engraçado", "amigável", "criativo", "brilhante", "resiliente", "honesto", "leal", "humilde", "determinado", "educado", "notável", "generoso", "sábio", "autêntico", "inspirador", "persistente", "paciente", "observador", "confiante", "capaz", "prestativo", "discreto", "respeitoso", "compassivo", "flexível", "disciplinado", "confiável", "compreensivo", "talentoso", "sincero", "educado", "atento", "otimista", "organizado", "eficiente", "brando", "tranquilo", "maduro", "alegre", "positivo", "diplomático", "prudente", "reflexivo", "decidido", "apaixonado", "empático", "encantador", "modesto", "valoroso", "virtuoso", "agradável", "prestigioso", "luminoso", "versátil", "zeloso", "visionário", "pacificador", "curioso", "sagaz", "destemido", "honrado", "audaz", "proativo", "laborioso", "focado", "ponderado", "eloquente", "gentleman", "engenhoso", "bem-humorado", "confidente", "humorístico", "bondoso", "dinâmico", "autossuficiente", "sensato", "simpático", "determinado", "valente", "poderoso", "justo", "cauteloso", "dócil", "inovador", "articulado", "astuto", "honrado", "benevolente", "centrado", "equilibrado", "respeitável", "ilustre", "heróico", "fiel", "caridoso", "paciente", "ponderado", "racional", "visionário", "magnífico", "eficaz", "prudente", "notável", "motivado", "entusiasmado", "sociável", "bravo", "valioso", "prestativo", "esforçado", "concentrado", "habilidoso", "intenso", "calmo", "devoto", "expressivo", "atencioso", "inovador", "competente", "solidário", "vibrante", "espontâneo", "dedicado", "valente", "observador", "criativo", "disciplinado", "alegre", "encantador", "humilde", "brilhante", "autêntico", "inspirador", "gentil", "fascinante", "resiliente", "leal", "honesto", "determinado", "positivo", "notável", "carismático", "generoso", "paciente", "reflexivo", "persistente", "corajoso", "inteligente", "forte", "incrível"]
                print("Você é", random.choice(elogio), end=".")
                opcao = int(input("\n1. Mais um elogio\n0 - Voltar.\n"))
                if opcao == 1:
                    continue
                else:
                    elogiador()
                

        elif g == 2:
             while True:
                elogio = ["incrível", "inteligente", "forte", "corajosa", "talentosa", "dedicada", "gentil", "carismática", "engraçada", "amigável", "criativa", "brilhante", "resiliente", "honesta", "leal", "humilde", "determinada", "educada", "notável", "generosa", "sábia", "autêntica", "inspiradora", "persistente", "paciente", "observadora", "confiante", "capaz", "prestativa", "discreta", "respeitosa", "compassiva", "flexível", "disciplinada", "confiável", "compreensiva", "sincera", "atenta", "otimista", "organizada", "eficiente", "tranquila", "madura", "alegre", "positiva", "diplomática", "prudente", "reflexiva", "decidida", "apaixonada", "empática", "encantadora", "modesta", "valorosa", "virtuosa", "agradável", "prestigiosa", "luminosa", "versátil", "zelosa", "visionária", "pacificadora", "curiosa", "sagaz", "destemida", "honrada", "audaz", "proativa", "laboriosa", "focada", "ponderada", "eloquente", "engenhosa", "bem-humorada", "confidente", "humorística", "bondosa", "dinâmica", "autossuficiente", "sensata", "simpática", "valente", "poderosa", "justa", "cautelosa", "doce", "inovadora", "articulada", "astuta", "benevolente", "centrada", "equilibrada", "respeitável", "ilustre", "heroica", "fiel", "caridosa", "racional", "magnífica", "eficaz", "motivadíssima", "entusiasmada", "sociável", "valiosa", "prestativa", "esforçada", "concentrada", "habilidosa", "intensa", "calma", "devota", "expressiva", "atenciosa", "competente", "solidária", "vibrante", "espontânea", "criativa", "disciplinada", "encantadora", "humilde", "brilhante", "autêntica", "inspiradora", "gentil", "fascinante", "resiliente", "leal", "honesta", "determinada", "positiva", "notável", "carismática", "generosa", "paciente", "reflexiva", "persistente", "corajosa", "inteligente", "forte", "incrível"]
                print("Você é", random.choice(elogio), end=".")
                opcao = int(input("\n1. Mais um elogio\n0 - Voltar.\n"))
                if opcao == 1:
                    continue
                else:
                    elogiador()
        
        elif g == 3:
            print("\nNão concordo, mas respeito.\nTenho vários amigos que são.\n")

            opcao = int(input("\n1. Voltar\n"))
            if opcao == 1:
                elogiador()

        opcao = int(input("\n1. Menu principal\n0 - Voltar.\n"))
        if opcao == 1:
            break
        else:
            continue
        


# MAIN
while True:

    os.system("cls")
    print("\n", "="*20, "Coisas Inúteis", "="*20)
    print("Selecione uma opção\n", end="             :)")
    print("\n1. Repetidor de frase\n2. Gerador de operação\n3. Algoritmo elogiador\n4. Pedra Papel Tesoura")
    opcao = int(input())

    match opcao:
        case 1:
            repetidor_de_frases()
        case 2:
            acerte_a_conta()
        case 3:
            elogiador()
        case 4:
            pedra_papel_tesoura()



    cpf_str = str(input("Digite seu CPF (sem pontuação):\n"))
    #123234345
    lista = []

    n1 = int(cpf_str[0])
    n2 = int(cpf_str[1])
    n3 = int(cpf_str[2])
    n4 = int(cpf_str[3])
    n5 = int(cpf_str[4])
    n6 = int(cpf_str[5])
    n7 = int(cpf_str[6])
    n8 = int(cpf_str[7])
    n9 = int(cpf_str[8])

    n1 *= 1
    n2 *= 2
    n3 *= 3
    n4 *= 4
    n5 *= 5
    n6 *= 6
    n7 *= 7
    n8 *= 8
    n9 *= 9

    numero_final = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9

    print(numero_final)


    # lista.append(n1, n2, n3, n4, n5, n6, n7, n8, n9)




   

