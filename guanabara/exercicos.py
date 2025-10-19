import time

#1

def ex001():
    while True:
        print('Olá, mundo.')
        break

#2 

def ex002():
    msg = "Olá, mundo."
    print(msg)

#3

def ex003():
    nome = input("Digite seu nome:\n")
    print("É um prazer te conhecer, {}!".format(nome))

#4 

def ex004():
    n1 = int(input("Digite um número:\n"))
    n2 = int(input("Digite outro número:\n"))
    s = n1 + n2
    # print("A soma entre", n1, "e", n2, "é igual a", s)
    print("A soma entre {} e {} vale {}".format(n1, n2, s))

#5

def ex005():
    a = input("Digite alguma coisa:\n")
    print("O tipo primitivo desse valor é", type(a))
    print("Só tem espaços?", a.isspace())
    print("É um número?", a.isnumeric())
    print("É alfabético?", a.isalpha())
    print("É alfanumérico?", a.isalnum())
    print("Está capitalizado?", a.istitle())
    print("Está em letras maíusculas?", a.isupper())
    print("Está em minúsculas?", a.islower())

#6

# raiz cúbica = ? ** (1/3)
# raiz quadrada = ? ** (1/2)


def ex006():
    a = int(input("Qual a raiz quadrada de:\n"))
    raiz = a ** (1/2)
    print("A raiz de quadrada {} é {}.".format(a, raiz))

#7 

def ex007():
    a = int(input("Digite um valor:\n"))
    b = int(input("Digite outro valor:\n"))
    s = a + b
    p = a * b
    d = a / b
    di = a // b
    e = a ** b

    print("A soma é {}, o produto é {} e a divisão é {}.".format(s, p, d), end=" ")
    print("divisão inteira:", di, end=". ")
    print("potência:", e)

#8

def ex008():
    while True:
        num = int(input("Digite um número:\n"))
        print(f"O antecessor de {num} é {num-1}.\nO sucessor de {num} é {num+1}.")
        opcao = int(input("\nTentar novamente?\n1 - Sim\n0 - Voltar ao Menu\n"))
                    
        match opcao:
            case 1:
                ex008()
        break

def ex009():
    while True:
        num = int(input("Digite um valor:\n"))
        print(f"O dobro de {num} é {num*2}.\nO triplo de {num} é {num*3}.\nA raiz quadrada de {num} é {num**(1/2)}.")

        opcao = int(input("\nTentar novamente?\n1 - Sim\n0 - Voltar ao Menu\n"))

        match opcao:
                    case 1:
                        ex009()
        break


def ex010():
        num1 = float(input("Digite a primeira nota:\n"))
        num2 = float(input("Digite a segunda nota:\n"))

        print("A média entre {:.1f} e {:.1f} é igual a {:.1f}.".format(num1, num2, (num1+num2)/2))


def ex011():
        medida = float(input("Uma distância em metros:\n"))
        cm = medida * 100
        mm = medida * 1000

        print("Conversão para centímetros: {:.0f}\nConversão para milímetros: {:.0f}\n".format(cm, mm))





















# main





while True:

    print("Carregando", end="")
    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    opcao = int(input("\nMENU PRINCIPAL\nInsira o exercício a ser executado (1-8):\n"))

    match opcao:
        case 1:
            ex001()
        case 2:
            ex002()
        case 3:
            ex003()
        case 4: 
            ex004()
        case 5:
            ex005()
        case 6:
            ex006()
        case 7:
            ex007()
        case 8:
            ex008()
        case 9:
            ex009()
        case 10:
            ex010()
        case 11:
              ex011()
        case _:
            print("\nValor inválido. Tente novamente.")