#Filmes e series tem as seguintes características

#Filme: Nome, ano, duração, curtir
#Séries: Nome, ano, temporadas, curtir

#Classe mãe/principal
class Programas:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtir = 0

    @property
    def valor_curtir(self):
        return self._curtir
    
    @property
    def valor_nome(self):
        return self._nome
    
    def curtida(self):
        self._curtir += 1

class Filmes(Programas):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._curtir = 0

class Series(Programas):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._curtir = 0

#Instanciar é salvar em uma variável

aventuras_superman = Series("Minhas Aventuras com Superman", 2023, 3)
aventuras_superman.curtida()
print(f"\nNome: {aventuras_superman.valor_nome} - Ano: {aventuras_superman.ano} - Temporadas: {aventuras_superman.temporadas} - Curtidas: {aventuras_superman.valor_curtir}")

avatar = Filmes("Avatar", 2009, 177)
print(f"\nNome: {avatar.valor_nome} - Ano: {avatar.ano} - Duração: {avatar.duracao} - Curtidas: {avatar.valor_curtir}")