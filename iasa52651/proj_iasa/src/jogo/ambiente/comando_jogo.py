from enum import Enum
'''Enum é uma classe que permite criar um conjunto de constantes'''

class ComandoJogo(Enum):
    '''Classe ComandoJogo que herda de Enum, representa o conjunto de saídas(Zeta(Z)) do jogo'''

    '''Enumeração dos comandos do jogo'''
    PROCURAR = 1
    APROXIMAR = 2
    OBSERVAR = 3
    FOTOGRAFAR = 4

    def mostrar(self):
        '''Método para mostrar o comando'''
        print(f"\nAção: {self.name}")