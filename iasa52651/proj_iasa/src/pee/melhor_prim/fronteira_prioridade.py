from pee.mec_proc.fronteira import Fronteira
from heapq import heappush, heappop

class FronteiraPrioridade(Fronteira):
    '''Representa outro tipo de fronteira de procura, que organiza os nós por prioridade e garante que o próximo nó a ser 
    explorado é sempre o de menor valor segundo um avaliador.'''
    
    def __init__(self, avaliador):
        super().__init__()
        self.__avaliador = avaliador

    def inserir(self, no):
        '''Biblioteca de filas com prioridades - heapq, pega na lista e atribuí-lhe uma estrutura de dados.
        Este método insere na fronteira um nó avaliado com prioridade.'''

        no.prioridade = self.__avaliador.prioridade(no)
        '''O avaliador dá-lhe a prioridade.'''

        heappush(self._nos, no)
        '''heappush - quando se coloca um novo elemento, ele vai organizar para ficarem por ordem de prioridade.'''

    def remover(self):
        '''Remove o nó que tiver menor prioridade. Estas comparações são feitas pelo do método __lt__ implementado na classe No.'''
        return heappop(self._nos)