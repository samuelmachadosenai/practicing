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

def main():
    while True:
        print("""Escolha:
            1. Soma
            2. Subtração
            3. Multiplicação
            4. Divisão""")
        
        opcao = input()

        match opcao:
            case 1:
                soma()
            case 2:
                scan()