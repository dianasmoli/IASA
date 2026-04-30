from enum import Enum
'''Enum é uma classe que permite criar um conjunto de constantes'''

class EstadoPersonagem(Enum):
    '''A classe EstadoPersonagem representa um enumerado dos estados que o jogador pode ter, sendo um conjnto de estados(Q)'''

    '''Enumerado dos estados das personagens'''
    PROCURA = 1
    INSPECCAO = 2
    OBSERVACAO = 3
    REGISTO = 4