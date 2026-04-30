from abc import ABC, abstractmethod

class Avaliador(ABC):
    '''Define o contrato funcional (interface) de avaliação da prioridade de um nó para ordenação da fronteira 
    por prioridade, é concretizado de acordo o tipo de procura. 
    Permite criar diferentes estratégias de avaliação, obrigando a implementar um método que calcula 
    a prioridade de um nó conforme o contexto do problema.'''

    @abstractmethod
    def prioridade(self, no):
        '''Retorna double'''