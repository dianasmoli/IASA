from agente.agente_jogo import AgenteJogo
from .controlo_personagem import ControloPersonagem

class Personagem(AgenteJogo):
    '''Classe Personagem que herda de AgenteJogo, é responsável por inicializar o ambiente e o controloPersonagem'''
    def __init__(self, ambiente):
        '''Chama o construtor da classe mãe para inicializar os atributos comuns'''
        '''O personagem é um agente específico para o jogo, com um controlo específico para o personagem, 
        que será usado para controlar as ações do personagem no ambiente'''
        super().__init__(ambiente, ControloPersonagem())

    def mostrar(self):
        '''Função responsável por mostrar o estado do controlo'''
        print(f"\nEstado: {self._controlo.estado}")