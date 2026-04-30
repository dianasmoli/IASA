from abc import ABC, abstractmethod
'''Abstrac Base Class(ABC), é um modulo que fornece a infraestrutura para definir classes abstratas em Python.'''

class Controlo(ABC):
    '''A classe Controlo é uma interface que representa o controlo do agente.'''

    @abstractmethod
    def processar(self, percepcao):
        '''O método processar é um método abstrato, deve ser implementado 
    por subclasses para processar as percepções e obter ações.'''
    
        """Obter ação do ambiente"""