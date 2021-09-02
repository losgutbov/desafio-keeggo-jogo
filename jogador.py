import random
from definicoes import *


class Jogador():
    
    def __init__(self):
        self.saldo = 300
        self.casa_atual = 1
        self.rodada = 1
        self.ativo = True
    
    def jogar_dado(self):
        return random.randint(1,6)
    
    def desativar_jogador(self):
        if self.saldo < 0:
            self.ativo = False

    def pagar_aluguel(self, valor):
        self.saldo -= valor

    def receber_aluguel(self, valor):
        self.saldo += valor

    def comprar_propriedade(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def acao_jogador(self):
        pass

    def atualiza_casa_do_jogo(self):
        self.casa_atual += self.jogar_dado
        if self.casa_atual > MAXIMO_CASAS:
            self.saldo += 100
            self.casa_atual = 1 # MAXIMO_CASAS - self.casa_atual | Outra possibilidade para o início da próxima rodada
            self.rodada += 1
        else:
            self.acao_jogador()
    
    

    
