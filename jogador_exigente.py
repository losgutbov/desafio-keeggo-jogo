from jogador import Jogador


class JogadorExigente(Jogador):
    
    def __init__(self, identificacao):
        super().__init__(identificacao)

    def acao_jogador(self, propriedade):
        acao = "nada"
        if propriedade.disponivel_para_compra():
            if propriedade.get_valor_aluguel() > 50:
                if self.comprar_propriedade(propriedade.get_custo_venda()):
                    propriedade.novo_proprietario(self)
                    acao = "comprou"
        elif propriedade.get_proprietario != self:
            acao = "alugou"
            valor_recebido = self.pagar_aluguel(propriedade.get_valor_aluguel())
            propriedade.cobrar_aluguel(valor_recebido)
            
        print("++++++++++++", propriedade, "Alguel acima de 50", acao)
    