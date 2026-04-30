from lib.mod.operador.operador import Operador
from .estado_contagem import EstadoContagem

class OperadorIncremento(Operador):
    '''Representa uma ação incrementada.'''

    def __init__(self, incremento):

        self.__incremento = incremento
        '''É o valor de imcrementação, ou seja, quanto é adicionado à contagem no novo estado.'''
    
    def aplicar(self, estado):
        '''Gera um novo estado a partir do estado atual e a incrementação, aumenta o valor da contagem.'''

        return EstadoContagem(estado.contagem + self.__incremento)
    
    def custo(self, estado, estado_suc):
        '''Para observar o efeito do custo na procura, o custo dos operadores corresponde ao quadrado do incremento.
        Representa o custo do percurso até cada nó determina ordem de expansão dos nós.'''

        return self.__incremento**2
    
    @property
    def incremento(self):
        '''Read-only'''
        return self.__incremento
