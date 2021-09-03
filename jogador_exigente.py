from jogador import Jogador


class JogadorExigente(Jogador):
    
    def __init__(self, identificacao):
        super().__init__(identificacao)
        self.comportamento = "Exigente"

    def acao_jogador(self, propriedade):
        if propriedade.disponivel_para_compra():
            if propriedade.get_valor_aluguel() > 50:
                if self.comprar_propriedade(propriedade.get_custo_venda()):
                    propriedade.novo_proprietario(self)
        elif propriedade.get_proprietario != self:
            valor_recebido = self.pagar_aluguel(propriedade.get_valor_aluguel())
            propriedade.cobrar_aluguel(valor_recebido)