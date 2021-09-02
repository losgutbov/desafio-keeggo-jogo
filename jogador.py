import random
from definicoes import *


class Jogador():
    
    def __init__(self, identificacao):
        self.identificacao = identificacao
        self.saldo = 300
        self.casa_atual = 0
        self.rodada = 1
        self.ativo = True
    
    def __str__(self):
        return "Identificacao: "+str(self.identificacao) \
                +" Status: "+str(self.ativo) \
                +" Saldo: "+str(self.saldo) \
                +" Casa Atual: "+str(self.casa_atual) \
                +" Rodada: "+str(self.rodada) 

    def get_rodada(self):
        return self.rodada
    
    def continuar_jogando(self):
        if self.ativo:
            return True
        return False

    def jogar_dado(self):
        return random.randint(1,6)
    
    def desativar_jogador(self):
        if self.saldo < 0:
            self.ativo = False
            return True
        return False

    def pagar_aluguel(self, valor):
        self.saldo -= valor
        return valor if self.saldo >= 0 else valor-self.saldo

    def receber_aluguel(self, valor):
        self.saldo += valor

    def comprar_propriedade(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def acao_jogador(self, propriedade):
        acao = "nada"
        if propriedade.disponivel_para_compra():
            if self.comprar_propriedade(propriedade.get_custo_venda()):
                propriedade.novo_proprietario(self)
                acao = "comprou"
        elif propriedade.get_proprietario != self:
            acao = "alugou"
            valor_recebido = self.pagar_aluguel(propriedade.get_valor_aluguel())
            propriedade.cobrar_aluguel(valor_recebido)
            
        print("++++++++++++", propriedade, acao)

    def realizar_jogada(self, propriedades):
        self.casa_atual += self.jogar_dado()
        if self.casa_atual > MAXIMO_CASAS:
            self.saldo += 100
            self.casa_atual = self.casa_atual - MAXIMO_CASAS # Outra possibilidade é voltar para 0 ou 1
            self.rodada += 1
        self.acao_jogador(propriedades[self.casa_atual-1])
        if self.desativar_jogador():
            for propriedade_ in propriedades:
                propriedade_.remover_proprietario(self)
            return -1
        return 0
        
    

    
