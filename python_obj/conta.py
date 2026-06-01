class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite_especial = limite

    #Declaração dos métodos (funções)
    def extrato(self):
        print(f"\nSaldo: {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        if(valor <= 0):
            print("\nValores negativos não podem ser depositados")
        else:
            self.__saldo += valor

    def __saque_permitido(self, valor_saque):
        valor_disponivel_saque = self.__saldo + self.__limite_especial
        return valor_saque <= valor_disponivel_saque
    
    def sacar(self, valor):
        if(self.__saque_permitido(valor)):
            self.__saldo -= valor
        else:
            print(f"\nO valor {valor} passou do limite")
            

    def transferir(self, valor, destino):
        if(self.__saldo < valor) or (valor < 0):
            print("\nNão é possível realizar a tranferência")
        else:
            self.sacar(valor)
            destino.depositar(valor)

    #Métodos apenas para retornar o valor das propriedades
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite_especial
    
    @property
    def numero(self):
        return self.__numero
    
    @staticmethod
    def codigo_banco():
        return '001'
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    #Métodos para manipular os valores das propriedades
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self,limite):
        self.__limite_especial = limite


    @numero.setter
    def numero(self,numero):
        self.__numero = numero

    @titular.setter
    def titular(self,titular):
        self.__titular = titular
#atributo = o que têm
#método = o que consegue fazer
#dentro da classe => métsodo
# "__" é igual ao private()
# "__" deixa privado

#get sempre te um return, ele é um método que pega um valor(dado)
#set sempre tem um get, ele é um método que muda os valores obtidos
#método istático = não depende do objeto