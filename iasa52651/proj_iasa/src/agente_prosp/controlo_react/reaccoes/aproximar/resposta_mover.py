from ecr.resposta import Resposta
from agente_prosp.accoes.mover import Mover

class RespostaMover(Resposta):
    '''A classe RespostaMover é responsável por implementar a interface Resposta.'''
        
    def __init__(self, direccao = None):

        super().__init__(Mover(direccao))
        '''A classe Resposta já tem os métodos implementados, então basta chamar o construtor e associar a accao mover. 
        É passada uma instâncisa da classe Mover que tem como parâmetro uma direção.
        Desta forma, reduz a complexidade e evita repetições de código.'''