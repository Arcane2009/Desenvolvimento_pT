#numero_conta = 1227939
#titular = "Gustavo"
#saldo = 100.0
#limite = 1000.0

def criar_conta(numero, titular, saldo, limite):
    conta = {
    "numero":numero,
    "titular":titular,
    "saldo":saldo,
    "limite":limite
    }
    return conta

conta = criar_conta(345, "João", 200.0, 1000.)

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f"Seu saldo atual é {conta["saldo"]}")

depositar(conta, 400.0)
extrato(conta)
sacar(conta, 200)
extrato(conta)