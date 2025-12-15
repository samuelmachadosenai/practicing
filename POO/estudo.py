class Cliente:
    def __init__(self, n, tel):
        self._nome = n
        self._telefone = tel

    #método get
    def get_nome(self):
        return self._nome

    #método set
    def set_nome(self, nome):
        self._nome = nome
        
        
class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular

    
    @property
    def saldo(self):
        return self._saldo
    
 
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("O saldo não pode ser negativo.")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if self.saldo>=valor:
            self.saldo-=valor
        else:
            print("Saldo insuficiente")
    
    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print("Cliente:", self.titular, "Saldo:", self.saldo)