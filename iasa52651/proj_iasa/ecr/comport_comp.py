from .comportamento import Comportamento
from abc import ABC, abstractmethod

class ComportComp(Comportamento):
    '''Comportamento composto, implementa a interface Comportamento'''

    def __init__(self, comportamentos):
        '''Esta classe agrupa comportamentos destintos'''

        self.__comportamentos = comportamentos
        '''Lista de comportamentos, onde quanto mais perto do início maior prioridade apresentam sobre os outros.'''

    def activar(self, percepcao):
        '''O comportamento composto agrega vários comportamentos, que se ativa com uma percepcao.
        Cada comportamento produz uma accao. 
        Esse conjunto de accoes vai ser aplicado uma selecao de accao, que pega no conjunto de acoes 
        e seleciona uma para ser produzida'''
        '''Tal como é demonstrado no slide 13 do pdf Arquitectura de Agentes Reactivos'''
        
        accoes = []
        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            if accao is not None:
                accoes.append(accao)

        if accoes:
            accao = self.seleccionar_accao(accoes)
        
        return accao

    @abstractmethod
    def seleccionar_accao(self, accoes):
        '''Método abstrato que é para ser implementado pelas classes Hierarquia e Prioridade'''
        '''No slide 6, do pdf Projeto - Parte 2, apresenta uma imagem com as classes e na classe ComportComp 
        este método está em itálico por isso é um metodo abstrato'''
        
        '''Abstração significa definir uma ideia geral, neste caso, uma classe base.
        Esta classe define o que o comportamento composto deve fazer, no entanto não diz 
        como a ação do conjunto ações deve ser escolhida. 
        O método é abstrato e por tanto, as classes Prioridade e Hierarquia, têm que implementar uma lógica de escolha.'''