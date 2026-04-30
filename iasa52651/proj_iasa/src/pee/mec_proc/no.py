class No:
    '''Elemento constituinte da árvore de procura, mantendo informação correspondente.'''

    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        self.__estado = estado
        '''Estado a que corresponde o nó.'''

        self.__operador = operador
        '''Operador que gerou o estado a que corresponde o nó (pode não existir).'''

        self.__antecessor = antecessor
        '''Nó antecessor na árvore de procura (pode não existir).'''

        self.__custo = custo
        '''Custo do percurso até ao nó. Comparável com outros nós em termos de custo.
        É acumulado a partir da soma dos antecessores.'''

        self.__prioridade = 0

        self.__profundidade = antecessor.profundidade + 1 if antecessor else 0
        '''Profundidade do nó, na árvore de procura.Profundidade acumula a do antecessor e adiciona 1.'''


    def __lt__(self, no):
        '''Operador less than serve para comparar dois nós e ordena os nós de acordo com a prioridade.'''
        return self.__prioridade < no.__prioridade


    '''====== Read-only properties ======'''
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor

    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def prioridade(self):
        return self.__prioridade
    

    '''====== Setter ======'''
    @prioridade.setter
    def prioridade(self, valor):
        self.__prioridade = valor