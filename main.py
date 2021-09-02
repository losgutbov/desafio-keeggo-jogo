from definicoes import *
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

    rodadas = 0
    total_jogadores = 4
    while rodadas < MAXIMO_RODADAS:
        for jogador_ in jogadores:
            if jogador_.continuar_jogando():
                total_jogadores += jogador_.realizar_jogada(propriedades)
                print("JOGADOR:", jogador_)
        if total_jogadores < 2:
            return "Jogo Terminado"
        rodada = jogador_.get_rodada()
        if rodada > rodadas:
            rodadas = rodada
        print("----------------------------------------")
    


if __name__ == "__main__":
    execucao_simples()