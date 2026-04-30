from ecr.comportamento import Comportamento
from agente_prosp.accoes.avancar import Avancar

class ExplorarMem(Comportamento):
    '''A classe ExplorarMem é um comportamento que tem como objetivo explorar o ambiente e 
    memoriza as posições e direções já visitadas, para evitar repetições.
    Numa arquitectura reactiva com memória, as reacções dependem não só das percepções, mas também da memória de percepções 
    anteriores (ou de informação delas derivada) para gerar as acções.Para esse efeito é necessário manter 
    internamente memória, a qual é actualizada a partir das percepções e das reacções activadas, 
    influenciando essas mesmas reacções, bem como as acções geradas.'''

    def __init__(self, dem_max_mem = 100):

        super().__init__()
        self.dem_max_mem = dem_max_mem
        '''Número máximo de memória.'''

        self.__memoria = []
        '''Lista privada de tuplos, onde cada tuplo é composto por uma posição e uma direção visitadas.'''

    def activar(self, percepcao):
        '''Este método é responsável por ativar o comportamento, utilizando a percepcao 
       do agente para saber a sua direccao e posicao.'''
        
        situacao = (percepcao.posicao, percepcao.direccao)
        
        if situacao not in self.__memoria:
            '''Verifica se a situação já existe, caso não exista então guarda.'''
            
            if len(self.__memoria) >= self.dem_max_mem:
                '''Verifica se chegou ao limite, caso o tenha feito remove o primeiro elemento da memória.'''
                self.__memoria.pop(0)
                
            self.__memoria.append(situacao)
            
            return Avancar()
        return

    