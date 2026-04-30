from abc import ABC, abstractmethod

class Operador(ABC):
    '''Esta interface representa um operador, ou seja, representa uma ação que produz a mudança (transformação) de estado.
    Operam sobre as representações internas de estado, produzindo transições de estado que correspondem à geração de novos estados.
    
    Os operadores abstraem as transformações que podem ocorrer no estado de um problema ou sistema. São a dinâmica.'''

    @abstractmethod
    def aplicar(self, estado):
        """Retorna estado"""

    @abstractmethod
    def custo(self, estado, estado_suc):
        '''É uma avaliação de opções de recursos necessários para realizar a ação.'''
        """Retorna double"""