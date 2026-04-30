from abc import ABC, abstractmethod

class Problema(ABC):
    '''Esta classe representa o problema , isto é, representa o estado inicial, os operadores e o objetivo.
    O problema é um conceito principal no raciocínio automático. Representa a configuração inicial, 
    as ações possíveis e o objetivo a alcançar na resolução de um problema.'''

    def __init__(self, estado_inicial, operadores):

        self.__estado_inicial = estado_inicial

        self.__operadores = operadores

    @abstractmethod
    def objectivo(self, estado):
        '''Define a condição de satisfação do problema, ou seja, o ponto de chegada.'''
        """Retorna booleano"""

    @property
    def operadores(self):
        '''Read-only'''
        return self.__operadores



    @property
    def estado_inicial(self):
        '''Representa o ponto de partida para a resolução do problema.'''
        '''Read-only'''

        return self.__estado_inicial