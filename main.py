from jogador import Jogador
from propriedade import Propriedade


def execucao_simples():
    propriedades = [Propriedade(1, 50, 10), Propriedade(2, 70, 15), \
                    Propriedade(3, 150, 40), Propriedade(4, 100, 20), \
                    Propriedade(5, 80, 30), Propriedade(6, 120, 40), \
                    Propriedade(7, 100, 25), Propriedade(8, 170, 50), \
                    Propriedade(9, 40, 5), Propriedade(10, 140, 60), \
                    Propriedade(11, 210, 120), Propriedade(12, 200, 100), \
                    Propriedade(13, 220, 100), Propriedade(14, 190, 90), \
                    Propriedade(15, 300, 10), Propriedade(16, 270, 170), \
                    Propriedade(17, 200, 130), Propriedade(18, 160, 75), \
                    Propriedade(19, 50, 10), Propriedade(20, 235, 100)]
    
    jogadores = [Jogador("João"), Jogador("Maria"), Jogador("Bruna"), Jogador("Tales")]

    for simulacao in range(5):
        for jog in jogadores:
            if jog.continuar_jogando():
                jog.realizar_jogada(propriedades)
                print("JOGADOR:", jog)
        print("----------------------------------------")
    


if __name__ == "__main__":
    execucao_simples()