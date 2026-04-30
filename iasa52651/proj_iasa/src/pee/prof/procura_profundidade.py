from pee.mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLifo

class ProcuraProfundidade(MecanismoProcura):
    '''Esta classe é responsável por explora primeiro os nós mais recentes, ou seja, primeiro aprofunda num ramo até 
    acabar e ter que passar para o próximo. 
    Quando expande um nó, os seus sucessores vão para o incício da fila, ou seja, 
    serão os próximos a ser expandidos e por isso vai de ramo em ramo.'''

    def __init__(self):

        super().__init__(FronteiraLifo())
        '''A classe MecanismoProcura precisa de uma fronteira, então passa-se a fronteira correspondente à procura em profundidade.
        O polimorfismo é utilizado para que o mecanismo de procura possa ser utilizado com diferentes fronteiras.
        A abstração permite a chamada do método de inicialização da classe MecanismoProcura, atribuindo a fronteira correta.'''