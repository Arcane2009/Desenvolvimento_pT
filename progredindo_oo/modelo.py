#Filmes e series tem as seguintes características

#Filme: Nome, ano, duração, curtir
#Séries: Nome, ano, temporadas, curtir

class Filmes:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__curtir = 0

    @property
    def valor_curtir(self):
        return self.__curtir
    
    @property
    def valor_nome(self):
        return self.__nome
    
    def curtida(self):
        self.__curtir += 1

class Series:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__curtir = 0

    @property
    def valor_curtir(self):
        return self.__curtir
    
    @property
    def valor_nome(self):
        return self.__nome
    
    def curtida(self):
        self.__curtir += 1

#Instanciar é salvar em uma variável

aventuras_superman = Series("Minhas Aventuras com Superman", 2023, 3)
aventuras_superman.curtida()
print(f"\nNome: {aventuras_superman.__nome} - Ano: {aventuras_superman.ano} - Temporadas: {aventuras_superman.temporadas}")

avatar = Filmes("Avatar", 2009, 177)
print(f"\nNome: {avatar.__nome} - Ano: {avatar.ano} - Duração: {avatar.duracaos}")