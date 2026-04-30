from agente.percepcao import Percepcao

class PercepcaoJogo(Percepcao):
    '''A classe PercepcaoJogo representa a perceção do jogo, ou seja, o evento que ocorreu no jogo.'''

    def __init__(self,evento):
        self.__evento = evento

    @property
    def evento(self):
        '''Read only'''
        '''Método para retornar o evento da perceção'''
        return self.__evento