from enum import Enum
'''Enum é uma classe que permite criar um conjunto de constantes'''

class EventoJogo(Enum):
    '''Classe EventoJogo que herda de Enum, representa o conjunto de entradas(Sigma(Σ)) do jogo'''

    '''Enumeração dos eventos do jogo'''
    SILENCIO = 's'
    RUIDO = 'r'
    ANIMAL = 'a'
    FUGA = 'f'
    FOTOGRAFIA = 'o'
    TERMINAR = 't'

    def mostrar(self):
        '''Método para mostrar o evento'''
        print(f"\nEvento: {self.name}")