class Main:
    pass

# from estudo import Cliente
# from estudo import Conta

# c1 = Cliente("Samuel", "666")
# conta = Conta(c1._nome, 54545, 0)

# conta.deposita(100)

# print(conta.extrato())

from pessoa import Pessoa
pessoas = []

a = 0
id = 0
dici = {}


while a < 3:

    nome = str(input("\nDigite o nome:\n"))
    idade = int(input("\nDigite a idade:\n"))

    
    p = Pessoa(nome, idade)

    n = {
        'nome': nome,
        'idade': idade
        }
    
    a += 1
    id += 1

    id_text = str(id)
    palavra = "pessoa"

    id_text = palavra + id_text

    dici[id_text] = n
    

print("\n", dici)
    