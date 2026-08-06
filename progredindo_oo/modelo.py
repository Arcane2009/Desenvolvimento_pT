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

class Playlist():
    def __init__(self, nomePl, elementos):
        self.nomePl = nomePl
        self._elementos = elementos

    @property
    def listagem(self):
        return self._elementos
    
    @property
    def tamanho(self):
        return self._elementos

#Séries
aventuras_superman = Series("Minhas Aventuras com Superman", 2023, 3)
bro99 = Series("Brooklyn Nine-Nine", 2013, 8)
ratched = Series("Ratched", 2020, 1)

#Filmes
avatar = Filmes("Avatar", 2009, 177)
hereditario = Filmes("Hereditário", 2018, 127)
it = Filmes("It: A Coisa", 2017, 135)

#Curtidas
avatar.curtida()
aventuras_superman.curtida()
bro99.curtida()
hereditario.curtida()
it.curtida()
ratched.curtida()

filmes_series = [aventuras_superman, avatar, hereditario, ratched, it, bro99]
plFim_de_Semana = Playlist("Fim de semana", filmes_series)

print(f"Tamanho da Playlist: {len(plFim_de_Semana)}")
print(f"\nEstá na lista? {avatar in plFim_de_Semana}")

for programas in plFim_de_Semana:
    print(programas)
        
#Instanciar é salvar em uma variável
#nome, programas, tamanho()
#nomePl = nome da playlist