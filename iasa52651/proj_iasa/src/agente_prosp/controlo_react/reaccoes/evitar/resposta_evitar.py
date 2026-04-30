from ecr.resposta import Resposta
from agente_prosp.accoes.rodar import Rodar

class RespostaEvitar(Resposta):
    '''A classe RespostaEvitar herda de Resposta, e é responsável por gerar uma resposta de evitar colisões.'''

    def _obter_accao(self, percepcao):
        '''O método _obter_accao é responsável por obter a ação a ser executada, com base na percepccao do agente.'''

        dir_agente = percepcao.direccao
        '''Saber qual a direccao atual do agente. 
        A classe Percepcao, da biblioteca SAE, tem o atributo direccao que indica a sua direção atual.'''

        dir_resposta = dir_agente.rodar()
        '''Gera uma direccao resposta, fazendo uma rotação da direção atual do agente.'''

        return Rodar(dir_resposta)
    '''Cria uma instância da classe Rodar, passando a direção resposta, ou seja, a direção que o agente vai rodar.'''