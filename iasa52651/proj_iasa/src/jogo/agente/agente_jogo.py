from agente.agente import Agente
from .percepcao_jogo import PercepcaoJogo

class AgenteJogo(Agente):
    '''Classe AgenteJogo herda de Agente, é um agente específico para o jogo'''
    '''A herança, que é um mecanismo de fatorização, é utilizada para reutilizar o código comum a todos os agentes, 
    e para especializar o comportamento do agente para o ambiente do jogo'''

    def __init__(self, ambiente, controlo):
        '''Como a classe AgenteJogo herda de Agente, chama-se o construtor da classe mãe para inicializar os atributos comuns'''
        
        super().__init__(controlo)
        '''O controlo é utilizado para controlar a personagem do jogo, a partir da sua percepção do ambiente, e que resultará numa ação'''
        
        self.__ambiente = ambiente
        '''O ambiente serve para o agente perceber o estado do jogo e executar ações'''
        

    def _percepcionar(self):
        '''Método para perceber o ambiente do jogo e retornar a perceção'''
    
        evento = self.__ambiente.observar()
        return PercepcaoJogo(evento)

    def _actuar(self, accao):
        '''Método para actuar no ambiente do jogo, ou seja, executar um comando a partir de uma acção'''
    
        self.__ambiente.executar(accao.comando)