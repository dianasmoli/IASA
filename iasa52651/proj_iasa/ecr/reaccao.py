from .comportamento import Comportamento

class Reaccao(Comportamento):
    '''A classe Reaccao implementa a interface Comportamento'''
    '''Reaccao é um comportamento simples, que precisa de um estimulo e de uma resposta para gerar uma accao'''
    '''Regra Estimulo-Resposta'''

    def __init__(self, estimulo, resposta):

        self.__estimulo = estimulo 
        '''Representa a detecção de um estímulo presente numa percepção'''

        self.__resposta = resposta
        '''Representa a detecção de um estímulo presente numa percepção'''

    def activar(self, percepcao):
        '''O método activar é responsável por gerar uma accao apartir da percepcao do ambiente.'''

        itensidade = self.__estimulo.detectar(percepcao)
        '''Através do estimulo obtêm-se a itensidade detetada a partir da percepcao'''
        
        if itensidade > 0:
            '''Se essa itensidade for maior que zero, logo significa que existe uma accao a retornar'''

            accao = self.__resposta.activar(percepcao, itensidade)
            '''Através da resposta obtemos a accao a activar a partir da percepcao do ambiente e da itensidade calculada anteriormente'''
            
            return accao