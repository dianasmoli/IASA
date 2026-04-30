from abc import ABC
from .no import No
from .solucao import Solucao

class MecanismoProcura(ABC):
    '''Esta classe representa o mecanismo de procura que permite procurar uma solução para um problema e 
    utiliza uma fronteira de exploração para memorizar e gerir nós explorados.
    
    Pode-se expandir em dois tipos de mecanismos de procura: Procura em profundidade e em largura.

    Procura em profundidade (Fronteira LIFO - Last In, First Out -> Pilha): Explora primeiro os nós mais recentes, ou seja, 
    primeiro aprofunda num ramo até acabar e ter que passar para o próximo. Quando expande um nó, os seus sucessoress 
    vão para o incício da fila, ou seja, serão os próximos a ser expandidos e por isso vai de ramo em ramo.
    
    Procura em largura (Fronteira FIFO - First In, First Out -> Fila): Explora os nós mais antigos, isto é, 
    explora todos os sucessores do nó expandido e só quando não tiver mais é que passa para expandir os próximos. 
    Ou seja, os nós são adicionados ao fim da lista e os que já estavão lá têm prioridade.'''

    def __init__(self, fronteira):
        self._fronteira = fronteira


    def _iniciar_memoria(self):
        '''Polimorfismo para diferentes mecanismos.'''

        self._fronteira.iniciar()
        '''Comum para todos os mecanismos de procura. Começa por inicializar a fronteira.'''


    def _memorizar(self, no):
        '''Polimorfismo para diferentes mecanismos.'''

        self._fronteira.inserir(no)
        '''Comum para todos os mecanismos de procura. Adiciona o nó passado como argumento.'''

    def procurar(self, problema):

        self._iniciar_memoria()
        '''Para inicializar a estrutura de dados da memória.'''

        no = No(problema.estado_inicial)
        '''Cria o nó inicial, a partir do atributo da classe Problema correspondente ao estado inicial do problema.'''

        self._memorizar(no)
        '''Adiciona o primiero nó à fronteira.'''

        while not self._fronteira.vazia:
            '''Enquanto a fronteira não for vazia, ou seja, existem nós a explorar.'''

            no = self._fronteira.remover()
            '''Remove-se o primeiro nó da fronteira.'''

            if problema.objectivo(no.estado):
                '''Verifica se o estado associado ao nó é o objetivo do problema.

                Caso seja, então cria-se a solução a partir da classe Solução, passando o nó como argumento.'''
                return Solucao(no)
            
            for no_suc in self._expandir(problema, no):
                '''Vai-se expandir o nó removido da fronteira, gerando os sucessores.
                
                De seguida, armazena-se o nó sucessor na fronteira.'''
                self._memorizar(no_suc)


    def _expandir(self, problema, no):
        sucessores = []
        '''Lista dos nós sucessores do nó a expandir.'''

        estado = no.estado
        '''Estado do nó a expandir.'''

        for operador in problema.operadores:
            '''A classe Problema tem um método de leitura apenas, para os operadores.'''

            estado_suc = operador.aplicar(estado)
            '''Aplica-se o operador do estado atual para gerar e transitar para o estado sucessor.'''

            if estado_suc is not None:

                custo = no.custo + operador.custo(estado, estado_suc)
                '''Custo do nó mais o custo da transição.'''

                no_suc = No(estado_suc, operador, no, custo)
                '''Cada nó tem o estado sucessor, o operador que o gerou, o nó pai e o custo.'''

                sucessores.append(no_suc)
                '''Adiciona-se o nó sucessor à lista dos sucessores.'''

        return sucessores

