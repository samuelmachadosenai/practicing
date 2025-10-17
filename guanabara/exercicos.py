#15

def ex001():
    print('Olá, mundo.')

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






























# main
opcao = int(input("Insira o exercício a ser executado:\n"))

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