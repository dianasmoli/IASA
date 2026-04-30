from abc import ABC, abstractmethod

class Fronteira(ABC):
    '''A fronteira representa a fronteira de exploração, ou seja, a lista de nós a ser explorados.
    Como podemoso observar no pdf Procura em Espaços de Estados - Parte 1, slide 23 por exemplo, a fronteira corresponde ao nós
    que ainda não foram expandidos. Permite também adicionar e remover nós de forma ordenada.'''

    @property
    def vazia(self):
        '''Indica se a fronteira, ou seja, a lista de nós está vazia.
        Read-only. 
        Valor dinamico, isto é, é calculado a partir de outro atributo.'''
        return len(self._nos) == 0

    def __init__(self):
        self.iniciar()

    def iniciar(self):
        self._nos = []
        '''Limpa a fronteira.'''

    @abstractmethod
    def inserir(self, no):
        """Abstrato para diferentes tipos de fronteiras, assim diferentes mecanismos podem implementar este método."""

    def remover(self):
        '''Remove o primeiro nó da fronteira, ou seja, o primeiro da lista.'''

        return self._nos.pop(0)