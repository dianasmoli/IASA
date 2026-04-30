from abc import ABC, abstractmethod

class Estado(ABC):
    '''Esta classe representa uma configuração de um sistema ou problema. 
    Os estados é um conceito principal no raciocínio automático. Representam situações (configurações) possíveis de um problema.
    
    Os estados abstraem os aspectos estruturais de um problema ou sistema (as configurações que podem ocorrer). São a estrutura.'''

    @abstractmethod
    def id_valor(self):
        '''Define identificação única do estado em função da sua informação (valor de estado). Conteúdo do objeto.'''
        """Retorna inteiro"""

    def __hash__(self):
        '''Método convencionado para tornar a identificação única.'''

        return self.id_valor()
    
    def __eq__(self, objecto):
        '''Método convencionado parar comparar objectos.'''

        if isinstance(objecto, Estado):
            '''Se o objecto for do tipo Estado, então compara-se com a idenficação única.'''
            return self.__hash__() == objecto.__hash__()
        else:
            return False