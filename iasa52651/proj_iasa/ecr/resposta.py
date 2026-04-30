class Resposta:
    '''A resposta define uma resposta a estímulos, em termos de acção a realizar e da respectiva prioridade.'''

    def __init__(self,accao = None):
        self._accao = accao

    def activar(self, percepcao, intensidade = 0):
        '''Retorna uma ação e associa a uma itensidade que será atribuído à variável prioridade, da classe Accao.'''

        accao = self._obter_accao(percepcao)
        '''Obtem-se a accao através do método _obter_accao.'''

        if accao is not None:

            accao.prioridade = intensidade
            '''Se existir accao então atribui-se à prioridade o valor da itensidade.
            Essa itensidade vai corresponder à prioridade de cada accao.'''

        return accao

    def _obter_accao(self, percepcao):
        return self._accao
