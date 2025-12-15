class Main:
    pass

from estudo import Cliente
from estudo import Conta

c1 = Cliente("Samuel", "666")
conta = Conta(c1._nome, 54545, 0)

conta.deposita(100)

print(conta.extrato())