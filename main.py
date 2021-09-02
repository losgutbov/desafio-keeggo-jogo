from jogador import Jogador


def execucao_simples():
    jog1 = Jogador("1")
    jog2 = Jogador("2")
    jog3 = Jogador("3")
    jog4 = Jogador("4")
    jogadores = [jog1, jog2, jog3, jog4]

    for jog in jogadores:
        if jog.continuar_jogando():
            print(jog)


if __name__ == "__main__":
    execucao_simples()