from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.larg.fronteira_fifo import FronteiraFifo

class ProcuraLargura(ProcuraGrafo):
    '''Esta classe é responsável por explora os nós mais antigos, isto é, explora todos os sucessores do nó expandido 
    e só quando não tiver mais é que passa para expandir os próximos. 
    Ou seja, os nós são adicionados ao fim da lista e os que já estavão lá têm prioridade.'''

    def __init__(self):
        super().__init__(FronteiraFifo())
        '''Chama o método de inicialização da classe mãe, vai buscar à classe MecanismoProcura, 
        precisa de uma fronteira, então passa-se a fronteira correspondente à procura em largura.'''