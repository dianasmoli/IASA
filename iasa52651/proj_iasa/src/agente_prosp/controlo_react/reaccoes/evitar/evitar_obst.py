from ecr.reaccao import Reaccao
from .estimulo_obst import EstimuloObst
from .resposta_evitar import RespostaEvitar

class EvitarObst(Reaccao):
    '''Objetivo do comportamento (Antes): o evitar tem o objetivo de evitar os obstáculos que surgirem no seu trajeto.'''

    def __init__(self):
        super().__init__(EstimuloObst(), RespostaEvitar())
        '''A classe Reaccao precisa de um estimulo e de uma resposta. Apresenta os métodos implementados, 
        então basta chamar o construtor e associar um estimulo e resposta.'''