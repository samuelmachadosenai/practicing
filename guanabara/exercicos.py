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
        km = medida / 1000
        cm = medida * 100
        mm = medida * 1000



        print("Conversão para centímetros: {:.0f}\nConversão para milímetros: {:.0f}\nConversão para quilômetros: {:.2f}".format(cm, mm, km))

def ex012():
    while True:
        num = int(input("Digite um número para ver sua tabuada.\n"))

        print("-" * 12)
        print("{} X {:2} = {}".format(num, 1, num*1))
        print("{} X {:2} = {}".format(num, 2, num*2))
        print("{} X {:2} = {}".format(num, 3, num*3))
        print("{} X {:2} = {}".format(num, 4, num*4))
        print("{} X {:2} = {}".format(num, 5, num*5))
        print("{} X {:2} = {}".format(num, 6, num*6))
        print("{} X {:2} = {}".format(num, 7, num*7))
        print("{} X {:2} = {}".format(num, 8, num*8))
        print("{} X {:2} = {}".format(num, 9, num*9))
        print("{} X {:2} = {}".format(num, 10, num*10))
        print("-" * 12)

        opcao = int(input("\nTentar novamente?\n1 - Sim\n0 - Voltar ao Menu\n"))

        match opcao:
                        case 1:
                            continue
        break

def ex013():
    real = float(input("Quanto dinheiro você tem na carteira?\nR$"))
    dolar = real / 5.4
    euro = real / 6.3
    print("Com R${:.2f} você pode comprar US${:.2f}\n".format(real, dolar))
    print("Com R${:.2f} você pode comprar €{:.2f}\n".format(real, euro))

def ex014():
    p = float(input("Digite o preço do produto:\nR$"))
    d = int(input("Digite o desconto (%):\n"))
    print("O preço com {}% de desconto é R${:.2f}".format(d, p - (p*d/100)))


def ex015():
    s = float(input("Digite o salário do colaborador.\nR$"))
    r = int(input("Digite o reajuste (%):\n"))
    print("O salário com {}% de reajuste é R${:.2f}".format(r, s + (s*r/100)))


def ex016():
    while True:
        opcao = int(input("Conversor\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n"))

        match opcao:
            case 1:
                c = float(input("Digite a temperatura (°C):\n"))
                print("\n{:.1f} graus Celsius equivalem a {:.1f} graus Fahrenheit.\n".format(c, c * 1.8 + 32))
                break
            case 2:
                f = float(input("\nDigite a temperatura (°F):"))
                print("\n{:.1f} graus Fahrenheit equivalem a {:.1f} graus Celsius.\n".format(f, (f - 32) / 1.8))

def ex017():
    d = int(input("O carro foi alugado por quantos dias?\n"))
    km = int(input("Quantos km rodados?\n"))

    t = (d * 60) + (km * 0.15)

    print(f"Total a pagar: R${t}")

def ex018():
    import math
    num = int(input("Digite um número:\n"))
    raiz = math.sqrt(num)
    print("A raiz quadrada de {} é {:.2f}.".format(num, raiz))

def ex019():
    import math

    num = float(input("Digite um valor:\n"))
    print("O valor digitado foi {} e sua porção inteira é {:.0f}.".format(num, math.floor(num)))



def ex020():
    import math

    co = float(input("Comprimento do cateto oposto:\n"))
    ca = float(input("Comprimento do cateto adjacente:\n"))

    print("A hipotenusa é igual a {:.2f}".format(math.hypot(co, ca)))

def ex021():
    import math

    ang = float(input("Digite o ângulo que você deseja:\n"))
    ang = math.radians(ang)
    print("Seno: {:.2f}\n".format(math.sin(ang)))
    print("Cosseno: {:.2f}\n".format(math.cos(ang)))
    print("Tangente: {:.2f}\n".format(math.tan(ang)))

def ex022():
    import random

    n1 = input("Primeiro aluno:\n")
    n2 = input("Segundo aluno:\n")
    n3 = input("Terceiro aluno:\n")
    n4 = input("Quarto aluno:\n")

    lista = [n1, n2, n3, n4]

    escolhido = random.choice(lista)

    print("\nO escolhido foi", escolhido)

def ex023():
    import random

    n1 = input("Primeiro aluno:\n")
    n2 = input("Segundo aluno:\n")
    n3 = input("Terceiro aluno:\n")
    n4 = input("Quarto aluno:\n")

    lista = [n1, n2, n3, n4]

    random.shuffle(lista)
    print(lista)

def ex024():
    print("Indisponível.")
    # import pygame

    # pygame.init()
    # pygame.mixer.init()

    # pygame.mixer.music.load("weird_fishes.mp3")
    # pygame.mixer.music.play()
    # pygame.event.wait()

def ex025():
    frase = input()

    print(len(frase))

    if 'Samuel' in frase:
        print("Oi, Samuel.")


    print(frase.upper())
    print(frase.lower())

def ex026():
    frase = input("Digite uma frase:\n")
    print(frase[3:10])
    print("\n", frase[3:10:2])

def salmo23():
    print("""O Senhor é o meu pastor; de nada terei falta.

2 Em verdes pastagens me faz repousar
e me conduz a águas tranquilas;

3 restaura-me o vigor.
Guia-me nas veredas da justiça
por amor do seu nome.

4 Mesmo quando eu andar
por um vale de trevas e morte,
não temerei perigo algum, pois tu estás comigo;
a tua vara e o teu cajado me protegem.

5 Preparas um banquete para mim
à vista dos meus inimigos.
Tu me honras,
ungindo a minha cabeça com óleo
e fazendo transbordar o meu cálice.

6 Sei que a bondade e a fidelidade
me acompanharão todos os dias da minha vida,
e voltarei à casa do Senhor enquanto eu viver.""")
    
def ex028():
    nome = str(input("Digite seu nome completo:\n")).strip()

    print(nome.upper())
    print(nome.lower())
    print(len(nome) - nome.count(" "))
    print(nome.find(" "))
    separa = nome.split()
    print("{} tem {} letras.".format(separa[0], len(separa[0])))

def ex029():
    cid = str(input("Qual sua cidade?")).strip()
    cid = cid.lower()
    print(cid[:5] == 'santo')

def ex030():
    num = int(input("Informe um número:\n"))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

    print("\nNúmero {}.".format(num))
    print("Unidade: {}.".format(u))
    print("Dezena: {}.".format(d))
    print("Centena: {}.".format(c))
    print("Milhar: {}.".format(m))

def ex031():
    n = str(input("Digite seu nome completo:\n")).strip()

    print('silva' in n.lower())

def ex032():
    frase = str(input("Digite uma frase:\n")).lower().strip()
    print("A frase tem {} letras A.".format(frase.count('a')))
    print("Primeira ocorrência: {}.\nÚltiima ocorrência: {}.".format(frase.find('a') + 1, frase.rfind('a') + 1))



def ex033():
    n = str(input("Digite seu nome completo:\n")).split()
    n



    


    






# main





while True:

    opcao = int(input("\nMENU PRINCIPAL\nInsira o exercício a ser executado (1-100):\n"))

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
        case 12:
            ex012()
        case 13:
            ex013()
        case 14:
            ex014()
        case 15:
            ex015()
        case 16:
            ex016()
        case 17:
            ex017()
        case 18:
            ex018()
        case 19:
            ex019()
        case 20:
            ex020()
        case 21:
            ex021()
        case 22:
            ex022()
        case 23:
            ex023()
        case 24:
            ex024()
        case 25:
            ex025()
        case 26:
            ex026()
        case 27:
            salmo23()
        case 28:
            ex028()
        case 29:
            ex029()
        case 30:
            ex030()
        case 31:
            ex031()
        case 32:
            ex032()
        case _:
            print("\nValor inválido. Tente novamente.")