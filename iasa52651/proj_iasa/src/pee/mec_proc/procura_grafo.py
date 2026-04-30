from abc import ABC
from .mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura, ABC):
    '''Esta classe representa uma procura em grafos, evitando explorar estados repetidos a partir de uma memória.
    A procura em árvore não se preocupa com repetições, logo pode visitar o mesmo estado várias vezes, o que pode gerar 
    caminhos redundantes e acaba por ter custos maiores ou trabalho extra.
    Ao contrário da procura em grafo que armazena os estados, evitando repetições'''

    def _iniciar_memoria(self):
        '''Fatorização, algo que já está feito não é repetido. 
        Na classe MecanismoProcura o método _iniciar_memoria() inicia a fronteira.'''

        super()._iniciar_memoria()
        '''Invoca-se então o método para iniciar a fronteira.'''

        self._explorados = {}

    def _memorizar(self, no):
        '''Se o nó for para manter memoriza, se não descarta.'''

        if self._manter(no):
            '''Verifica se é para manter o nó.'''

            self._explorados[no.estado] = no
            '''Associar o nó ao estado do nó a ser guardado.'''

            super()._memorizar(no)
            '''Invoca-se o método da classe mãe para inserir esse nó na fronteira, que é o que esse método na classe mãe faz.
            Só se invoca se for para manter o nó, para não existir repetições.'''

    def _manter(self, no):
        '''Método que verifica se o nó já existe, para evitar repetições.'''
    
        return no.estado not in self._explorados