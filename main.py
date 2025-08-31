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
        
num = int(input("Digite um número:"))
print("Escolha uma opção:\n")           
print("a) Verificar se um número é par ou ímpar\n")
print("b) Comparar dois números\n")
print("c) Mostrar a tabuada de um número\n")
opcao = input()


if opcao == "a":
    par_ou_impar(num)
elif opcao == "b":
    num2 = int(input("Digite outro número: "))
    maior_ou_menor(num, num2)
elif opcao == "c":
    tabuada(num)