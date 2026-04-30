from .avaliador import Avaliador
from abc import ABC

class AvaliadorHeur(Avaliador, ABC):

    def __init__(self):
        self.__heuristica = None

    @property
    def heuristica(self):
        return self.__heuristica
    
    @heuristica.setter
    def heuristica(self, valor):
        self.__heuristica = valor