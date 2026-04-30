from lib.mod.estado.estado import Estado

class EstadoContagem(Estado):
    '''Esta classe serve como uma representação de estado de contagem, ou seja, em que número se encontra a contagem.'''

    def __init__(self, valor):

        self.__contagem = valor
        '''Valor da contagem, cada estado tem um valor e pode ser o próprio valor do estado.
        É diferente do id_valor.
        Enquanto que a contagem refere-se a um valor lógico, o id_valor refere-se a um identificador, ou seja um valor técnico.'''

    def id_valor(self):
        return self.__contagem
    
    @property
    def contagem(self):
        '''Read-only, para que esta contagem não seja alterada e que seja apenas de leitura única.'''

        return self.__contagem