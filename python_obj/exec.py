from conta import Conta

conta1 = Conta(535, "Ricardo", 55.0, 5000.0)
conta2 = Conta(555, "Luana", 100.0, 1000.0)

valor = 50

conta2.extrato()
conta1.transferir(valor, conta2)
conta1.extrato()
conta2.extrato()
#WuW WwW WvW WoW WxW; UwU UuU UvU UxU; VuV VvV 
#atributo = o que têm
#método = o que consegue fazer
#dentro da classe => métsodo