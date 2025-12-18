# Tupla

def ex001():
    lanche = ("Hambúrguer", "Suco", "Pudim", "Pizza")
    print(lanche[1])

    # r = []
    # for c in lanche:
    #     print(f"do u like {c}?\n 1. yes\n0. no")
    #     re = int(input())
    #     r.append(re)



    # for c in lanche:
    #     print(f"Eu vou comer {c}.")
    # print('Comi pra caramba.')

def ex002():
    cont = ("zero", "um", "dois", "três", "quatro", "cinco")
    n = int(input("digita um number ai\n"))
    print(f"\nvc digitou o número {cont[n]}.")

def ex003():
    import random
    s = random.randint(15, 55)
    d = random.randint(15, 55)
    c = random.randint(15, 55)

    b = (s, d, c)
    
    print(b)
    print(max(b), min(b))

def ex004():
    tupla = ()
    for i in range(1, 5):
        print(f"digita o {i}o numero ai pfv\n")
        tupla = i

    print(tupla)

def ex005():
    listagem = ("Pão", 1, "Leite", 3.5)

    # for pos in range(0, len(listagem)):
def ex006():
    lista = []
    for i in range(0, 5):
        print("digite o número na posição", i)
        n = int(input())
        lista.append(n)

    print(lista)
    print("maior:", max(lista), "posição:", lista.index(max(lista)))
    print("menor:", min(lista), "posição:", lista.index(min(lista)))

        
        



while True:

    opcao = int(input(f"\nMENU PRINCIPAL\nInsira o exercício a ser executado (1-100):\n"))

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
        case 33:
            ex033()
        case 34:
            ex034()
        case 35:
            ex035()
        case 36:
            ex036()
        case 37:
            ex037()
        case 38:
            ex038()
        case 39:
            ex039()
        case 40:
            ex040()
        case 41:
            ex041()
        case 42:
            ex042()
        case 43:
            ex043()
        case 44:
            ex044()
        case 45:
            ex045()
        case 46:
            ex046()
        case 47:
            ex047()
        case 48:
            ex048()
        case 49:
            ex049()
        case 50:
            ex050()
        case 51:
            ex051()
        case 52:
            ex052()
        case 53:
            ex053()
        case 54:
            ex054()
        case 55:
            ex055()
        case 56:
            ex056()
        case 57:
            ex057()
        case 58:
            ex058()
        case 59:
            ex059()
        case 60:
            ex060()
        case 61:
            ex061()
        case 62:
            ex062()
        case 63:
            ex063()
        case 64:
            ex064()
        case 65:
            ex065()
        case 66:
            ex066()
        case 67:
            ex067()
        case 68:
            ex068()
        case 69:
            ex069()
        case _:
            print("\nValor inválido. Tente novamente.")
