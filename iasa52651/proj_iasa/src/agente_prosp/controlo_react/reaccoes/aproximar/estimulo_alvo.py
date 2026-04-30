from ecr.estimulo import Estimulo
from sae import Elemento

class EstimuloAlvo(Estimulo):
    '''A classe EstimuloAlvo é responsável por implementar a interface Estimulo.
    Tem como objetivo detecar a itensidade de um determinado estimulo de uma percepcao.'''

    def __init__(self, direccao, gama = 0.9):

        self.__direccao = direccao

        self.__gama = gama
        '''Fator de decaimento.'''

    def detectar(self, percepcao):
        '''Dado uma percepcao, gera uma itensidade.'''
        '''Retorna a intensidade com que o alvo está a ser detetado, se o alvo estiver na posição imediata do agente, 
        a itensidade é 1. À medida a que se afasta, distancia aumenta, a itensidade diminui.'''

        elemento, distancia, _ = percepcao[self.__direccao]
        '''obter um tuplo (elemento, distancia, posição) da percepcao.'''

        '''cremento exponencial'''
        return self.__gama ** distancia if elemento == Elemento.ALVO else 0
    '''Se o elemento detetado for o alvo, a itensidade é calculada com base gama elevado à distancia, 
    caso contrário, a itensidade é 0.'''

    @property
    def gama(self):
        '''Getter/ Read only do atributo gama.'''
        
        return self.__gama