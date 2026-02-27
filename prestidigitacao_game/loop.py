#Definição das variáveis#
total = 3
turno = 1
mao_bot = 0

for turno in range(1,total + 1):
    print(f"Rodada {turno} de {total}")
    print("\nPedra = 1, papel = 2 e tesoura = 3")
    entrada = int(input("Digite o número da sua escolha : "))

    if(entrada == 1):
        entrada == 1
        print("\nVocê escolheu pedra")
        mao_bot = mao_bot + 1
    elif entrada == 2:
        entrada == 2
        print("\nVocê escolheu papel")
        mao_bot = mao_bot + 1
    else:
        entrada == 3
        print("\nVocê escolheu tesoura")
        mao_bot = mao_bot + 1

    if(mao_bot == 1 and entrada == 1):
        print(f"\nEmpatamos o turno{turno}")
    elif mao_bot == 2 and entrada == 1:
        print(f"\nGanhei o turno{turno}")
    elif mao_bot == 3 and entrada == 1:
        print(f"\nPerdi o turno{turno}")
    elif mao_bot == 1 and entrada == 2:
        print(f"\Perdi o turno{turno}")
    elif mao_bot == 2 and entrada == 2:
        print(f"\Empatamos o turno{turno}")
    elif mao_bot == 3 and entrada == 2:
        print(f"\nGanhei o turno{turno}")
    elif mao_bot == 1 and entrada == 3:
        print(f"\Ganhei o turno{turno}")
    elif mao_bot == 2 and entrada == 3:
        print(f"\nPerdi o turno{turno}")
    elif mao_bot == 3 and entrada == 3:
        print(f"\Empatamos o turno{turno}")

print("\nFim de jogo")