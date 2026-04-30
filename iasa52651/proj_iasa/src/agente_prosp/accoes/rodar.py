from ecr.accao import Accao
from sae import Movimento

class Rodar(Movimento, Accao):

    def __init__(self, direccao):
        '''Representa uma roda na direção indicada com um passo de zero unidades, logo não anda'''

        super().__init__(direccao, 0)