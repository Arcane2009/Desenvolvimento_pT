from conta import Conta

class ContaEs:
    def __init__(self, numero, titular, saldo, limite = 5000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta1 = Conta(1, "Ricardo", 55.0)
conta2 = Conta(2, "Beltrano", 0.0)
conta3 = ContaEs(3, "Sicrano", 0.0)

print(conta1.limite)
#-------------------------------------------------------------------#
class Video:
    def __init__(self, titulo, duracao, views):
        self.titulo = titulo
        self.duracao = duracao
        self.views = views

video = Video("O show de Truman", 1.43, 264)
#-------------------------------------------------------------------#
class Livro:
    def __init__(self, titulo, autor, data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao

livro = Livro("O Seminarista", "Bernardo Guimarães", 1872)
