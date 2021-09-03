from definicoes import *
from jogador import Jogador
from jogador_impulsivo import JogadorImpulsivo
from jogador_exigente import JogadorExigente
from jogador_cauteloso import JogadorCauteloso
from jogador_aleatorio import JogadorAleatorio
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
    
    jogadores = [JogadorImpulsivo("João"), JogadorExigente("Maria"), \
                 JogadorCauteloso("Bruna"), JogadorAleatorio("Tales")]

    rodadas = 0
    total_jogadores = 4
    vencedor = None
    while rodadas < MAXIMO_RODADAS and total_jogadores > 1:
        for jogador_ in jogadores:
            if jogador_.continuar_jogando():
                total_jogadores += jogador_.realizar_jogada(propriedades)
            rodada = jogador_.get_rodada()
            if rodada > rodadas:
                rodadas = rodada
    
    if total_jogadores == 1:
        for jogador_ in jogadores:
            if jogador_.get_status():
                vencedor = jogador_

    return rodadas, vencedor

def execucao_completa():
    resultados = {"Impulsivo":0, "Exigente":0, "Cauteloso":0, "Aleatório":0}
    total_rodadas = 0
    timeout = 0 
    for n in range(MAXIMO_SIMULACOES):
        rodadas, ganhador = execucao_simples()
        if ganhador is not None:
            resultados[ganhador.comportamento] += 1
            total_rodadas += rodadas
            print("Simulação:", n, "Rodadas:", rodadas, "Comportamento Vencedor:", ganhador.comportamento)
        else:
            timeout += 1
            print("Simulação:", n, "Rodadas:", rodadas, "Finalizado por Timeout")

    print()
    print("*****************Relatorio*****************")
    print("Partidas finalizadas por timeout:", timeout)
    print("Duracao media das partidas em rodadas:", int(total_rodadas/MAXIMO_SIMULACOES))
    print("Porcentagem de vitorias por comportamentos:")
    print("     Impulsivo:", round((resultados["Impulsivo"]/MAXIMO_SIMULACOES)*100, 2), "%")
    print("     Exigente:", round((resultados["Exigente"]/MAXIMO_SIMULACOES)*100, 2), "%")
    print("     Cauteloso:", round((resultados["Cauteloso"]/MAXIMO_SIMULACOES)*100, 2), "%")
    print("     Aleatório:", round((resultados["Aleatório"]/MAXIMO_SIMULACOES)*100, 2), "%")
    maior_vencedor = max(resultados, key=resultados.get)
    print("O comportamento com mais vitorias foi:", maior_vencedor)


if __name__ == "__main__":
    execucao_completa()