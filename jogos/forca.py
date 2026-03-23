def jogar_forca():
    print("-------------------------------")
    print("\nBem vindo ao jogo da forca!\n")
    print("-------------------------------")

    palavra_secreta = "cordeiro"
    perdeu = False
    acertou = False

    while not perdeu and not acertou:
        chute = input("Escreva uma letra: ")
        chute = chute.strip()

        #index define a posição da letra
        index = 0

        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                print(f"A letra {chute} está na posição {index}")
            index = index + 1

if(__name__ == "__main__"):
    jogar_forca()

