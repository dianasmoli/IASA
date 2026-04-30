from agente.accao import Accao

class AccaoJogo(Accao):
    '''A classe AccaoJogo representa a acção do jogo, ou seja, o comando que o agente irá executar no jogo'''

    def __init__(self, comando):
        self.__comando = comando

    @property
    def comando(self):
        '''Read only property, Propriedade de apenas leitura, para o comando da acção do jogo'''
        return self.__comando