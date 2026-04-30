from mod.problema.problema import Problema
from .estado_contagem import EstadoContagem
from .operador_incremento import OperadorIncremento

class ProblemaContagem(Problema):
    '''Representa o problema de procura onde o objetivo é atingir ou ultrapassar um valor numérico a partir
      de um valor inicial, aplicando incrementos possíveis.'''

    def __init__(self, contagem_inicial, contagem_final, incrementos):
        '''É preciso dominio do problema, contagem inicial, final e os incrementos possíveis, 
        para converter em estados e operadores.'''

        super().__init__(EstadoContagem(contagem_inicial), 
                         [OperadorIncremento(incremento) for incremento in incrementos])
        '''É preciso passar por parâmetro o estado inicial e uma lista de operadores.'''

        self.__contagem_final = contagem_final

    def objectivo(self, estado):
        '''Incrementos a realizar para atingir ou superar a contagem final.'''

        return estado.contagem >= self.__contagem_final