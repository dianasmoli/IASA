from ecr.reaccao import Reaccao
from .estimulo_alvo import EstimuloAlvo
from .resposta_mover import RespostaMover

class AproximarDir(Reaccao):
    '''Esta classe tem como objetivo aproximar o agente do alvo, movendo-se numa determinada direção.'''

    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))
        '''Basta invocar o construtor da classe Reaccao, que precisa de um estimulo e de uma resposta.
        Então cria-se uma instancia do EstimuloAlvo e da RespostaMover passando a direccao como parâmetro.'''
