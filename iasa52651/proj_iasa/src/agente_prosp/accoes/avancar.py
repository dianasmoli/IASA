from ecr.accao import Accao
from sae import Movimento

class Avancar(Movimento, Accao):

    def __init__(self):
        '''Representa o avançar na direcao atual do agente'''

        super().__init__(None)
        '''Passa-se none para ele não mudar de direção e continuar na que já está'''