from abc import ABC, abstractmethod

class Comportamento(ABC):
    '''Interface que define a funcionalidade geral de um comportamento'''
    
    @abstractmethod
    def activar(self, percepcao):
        """Retorna accao"""