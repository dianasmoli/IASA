from abc import ABC, abstractmethod

class Estimulo(ABC):
    '''O estimulo define informação ativadora de uma reacção.'''
    
    @abstractmethod
    def detectar(self, percepcao):
        """retorna float"""