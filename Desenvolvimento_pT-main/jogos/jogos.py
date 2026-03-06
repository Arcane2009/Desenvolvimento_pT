import adivinhacao
import forca
import joke

print("-------------------------------")
print("\nEscolha se Jogo\n")
print("-------------------------------")

print ("\n(1) é Adivinhação (2) é Forca (3) é Jokenpo\n")

opcao_jogo = int(input("Escolha Seu Jogo: "))

if(opcao_jogo == 1):
    print("\nEscolhendo Adivinhação")
    adivinhacao.jogar_adivinhacao()
elif(opcao_jogo == 2):
    print("\nEscolhendo Forca")
    forca.jogar_forca()
elif(opcao_jogo == 3):
    print("\nEscolhendo Jokenpo")
    joke.jogar_jokenpo()