import random
import os

def gen():
    a = random.randint(10, 90)
    b = random.randint(10, 90)
    return a, b


# Define ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Print colored text
# print(f"{RED}This is red text{RESET}")
# print(f"{GREEN}This is green text{RESET}")


score = 0
questao = 0
acerto = 0

def soma():
    while True:
        os.system("cls")
        num1, num2 = gen()
        global score
        r = num1 + num2
    
        print(f"Score: {score}")
    
        print(f"\nQuanto é {num1} mais {num2}?")
        global questao
        global acerto
        questao += 1
        a = int(input())

        
        if a == r:
            print(f"\n{GREEN}Acertou.{RESET}")
            score += 1
            acerto += 1
        else:
            print(f"\n{RED}Errou.{RESET}")
            print(f"O resultado era {r}.")
            score -= 1

        print("\nContinuar?\n1. Sim\n0. Não")
        op = int(input())

        if op == 1:
            continue
        else:
            os.system("cls")
            print(f"Acertos: {acerto}/{questao}")
            print(f"\nScore final: {score}")
            if score < 0:
                print("Pratique mais.")
            break

total = 0
a = 0
  


def scan():
    venda = []
    # while True:
    #     a = int("Aperte para scanear.")

    #     for c, p in enumerate(produto):
    #         import keyboard
    import time
    import keyboard
    import rand as r

    while True:
    
        if keyboard.is_pressed('space'):
            time.sleep(0.4)  # Pequena pausa para evitar múltiplas detecções

            nome, preco = r.prod()


            

            tupla = (nome, preco)
            
            venda.append(tupla)
            # preco = produto['preço']

            
            global total 
            total += preco

    
            for i in venda:
                
                preco = i[1]

                global a 
                a += 1

                print(f"{a}. {i}")
            
        if keyboard.is_pressed('a'):
                break
    os.system("cls")
    print(venda)
    total = float(total)

    print("Total: {:.2f}".format(total))

def main():
    while True:
        print("""Escolha:
            1. Soma
            2. Subtração
            3. Multiplicação
            4. Divisão""")
        
        opcao = int(input())

        match opcao:
            case 1:
                soma()
            case 2:
                scan()

main()