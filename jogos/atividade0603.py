print("\nEscolha uma receita Pão (1) e Ovo (2)\n")

escolha = int(input("Defina um nível: "))

if(escolha == 1):
    print("\nIngredientes\n")

    for item in zip(range(6), ['2 xícaras de farinha', '1 colher de sopa de fermento biológico seco', '1 colher de sopa de açúcar', '1 colher de sopa de óleo', '½ xícara de água morna', '½ colher de chá de sal', '1 ovo']):
        print(f"{item}\n")

    print("Modo de Preparo\n")
    print("- Numa vasilha, coloque toda a sua farinha e faça uma pequena cavidade no centro.\n")
    print("- Nessa cavidade, coloque o seu fermento e dissolva ele com a água morna. Não será necessário utilizar toda a água, apenas o suficiente para formar uma pastinha no fermento.\n")
    print("- Cubra o fermento com a farinha das laterais e deixe parado até formar rachaduras na superfície da farinha, aproximadamente 10 minutos. Caso nenhuma rachadura se forme, você terá que descartar essa massa e começar do zero novamente, pois seu fermento não ativou.\n")
    print("- Após visualizar as rachaduras, acrescente na massa os ovos, o açúcar e o óleo.\n")
    print("- Vá misturando tudo e acrescentando o restante da água aos poucos, até que todos os ingredientes estejam bem incorporados numa massa só.\n")
    print("- Depois disso, acrescente o sal e sove a massa até que a mesma fique lisa e grude levemente na ponta dos dedos. Em torno de 5 minutos na batedeira ou 15 minutos sovando na mão.\n")
    print("- Coloque sua massa numa vasilha untada com óleo, cubra-a com plástico filme e panos de prato, e leve para descansar num local quentinho da sua cozinha.\n")
    print("- Após 30 minutos, sua massa deve ter dobrado de tamanho, e está pronta para ser modelada.\n")
    print("- Para a modelagem, é só pegar toda a massa, abrir grosseiramente com a palma da mão mesmo, até que fique retangular/oval, e então ir enrolando de uma ponta à outra, de maneira que forme um rolinho, como se fosse um rocambole.\n")
    print("- Coloque seu pão modelado dentro de uma forma untada com óleo. Importante: a forma tem que ser grande o suficiente para entrar o pão modelado e ainda sobrar um espacinho para que o pão possa crescer.\n")
    print("- Cubra o pão com plástico filme e panos de prato novamente, e deixe-o descansar novamente por mais 20 minutos.\n")
    print("- Após o descanso, leve o seu pão para assar em forno pré aquecido a 200º por, aproximadamente, 40 minutos, ou até que toda a superfície e lateral dele estejam bem dourados.\n")
    print("- - Se quiser um pão com casquinha brilhosa, existem duas técnicas que você pode aplicar: antes de assar, pincele um ovo batido por toda a superfície e lateral do seu pão; ou, se preferir, assim que tirar o pão do forno, com ele ainda quente, pincele uma mistura de água com açúcar sobre o seu pão. Isso fará com que sua casca fique brilhosa, e dará um leve sabor adocicado para a mesma. De qualquer jeito, fica uma delícia!\n")

    else:
        print("Ovo")