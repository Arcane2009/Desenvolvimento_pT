#Filmes e series tem as seguintes características

#Filme: Nome, ano, duração, curtir
#Séries: Nome, ano, temporadas, curtir

#Classe mãe/principal
#Super classe
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

    def __str__(self):
        return f"\n{self._nome} - {self.ano} - {self._curtir} Curtidas"

class Filmes(Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"\n{self._nome} - {self.ano} - {self.duracao} minutos - {self._curtir} curtidas"

class Series(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"\n{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._curtir} curtidas"

#Instanciar é salvar em uma variável

aventuras_superman = Series("Minhas Aventuras com Superman", 2023, 3)
aventuras_superman.curtida()
print(f"\nNome: {aventuras_superman.valor_nome} - Ano: {aventuras_superman.ano} - Temporadas: {aventuras_superman.temporadas} - Curtidas: {aventuras_superman.valor_curtir}")

avatar = Filmes("Avatar", 2009, 177)
print(f"\nNome: {avatar.valor_nome} - Ano: {avatar.ano} - Duração: {avatar.duracao} - Curtidas: {avatar.valor_curtir}")

filmes_series = [aventuras_superman, avatar]

for programas in filmes_series:
    print(programas)
        
