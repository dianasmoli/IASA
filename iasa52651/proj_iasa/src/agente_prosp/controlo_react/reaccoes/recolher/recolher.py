from ecr.hierarquia import Hierarquia
from agente_prosp.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente_prosp.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from agente_prosp.controlo_react.reaccoes.explorar.explorar import Explorar
from agente_prosp.controlo_react.reaccoes.explorar.explorar_mem import ExplorarMem

class Recolher(Hierarquia):
    '''Objetivo do comportamento (Antes): o recolher tem o objetivo de recolher alvos.
    Tem como sub-conjuntos: aproximar, evitar e explorar, e gera uma ação.'''

    def __init__(self):
        super().__init__([AproximarAlvo(), EvitarObst(), ExplorarMem(), Explorar()])
        '''A Classe Hierarquia já tem os métodos implementados, então basta chamar o construtor 
        e associar as ações de cada sub-conjunto. A ordem em que as reações são associadas é importante, 
        pois a hierarquia tem um mecanismo de seleção de ação, onde a reação mais prioritária, a primeira da lista, é escolhida.'''