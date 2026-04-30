from lib.pee.melhor_prim.heuristica import Heuristica

class HeuristicaContagem(Heuristica):
    '''Heurística é uma métrica medida de custo de um estado para o outro.'''

    def __init__(self, valor_final):
        self.__valor_final = valor_final

    def h(self, estado):
        return abs(self.__valor_final) - abs(estado.contagem)