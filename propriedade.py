

class Propriedade():
    
    def __init__(self, identificacao, custo_venda, valor_aluguel):
        self.identificacao = identificacao
        self.custo_venda = custo_venda
        self.valor_aluguel = valor_aluguel
        self.proprietario = None

    def __str__(self):
        return "Identificacao: "+str(self.identificacao) \
                +" Custo de Venda: "+str(self.custo_venda) \
                +" Valor do Aluguel: "+str(self.valor_aluguel) \
                +" \n Proprietario Atual: " \
                    +str(self.proprietario if self.proprietario is not None else "-")
    
    def get_valor_aluguel(self):
        return self.valor_aluguel
    
    def get_custo_venda(self):
        return self.custo_venda
    
    def get_proprietario(self):
        return self.proprietario

    def novo_proprietario(self, jogador):
        self.proprietario = jogador

    def remover_proprietario(self, jogador):
        if self.proprietario == jogador:
            self.proprietario = None

    def disponivel_para_compra(self):
        if self.proprietario is None:
            return True
        return False

    def cobrar_aluguel(self, valor_recebido):
        self.proprietario.receber_aluguel(valor_recebido)    

    