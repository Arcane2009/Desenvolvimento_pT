class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo: {self.saldo} do titular {self.titular}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if(self.saldo < valor):
            print("saldo insuficiente")
        else:
            self.saldo -= valor