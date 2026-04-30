from .avaliador import Avaliador

class AvaliadorCustoUnif(Avaliador):

    def prioridade(self, no):
        '''g é o custo acumulado até ao nó.'''
        return no.custo