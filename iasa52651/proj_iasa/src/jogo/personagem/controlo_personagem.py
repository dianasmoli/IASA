from agente.accao_jogo import AccaoJogo
from agente.controlo import Controlo
from ambiente.comando_jogo import ComandoJogo
from maqest.maquina_estados import MaquinaEstados
from .estado_personagem import EstadoPersonagem
from ambiente.evento_jogo import EventoJogo

'''Quando se quer importar uma classe de um ficheiro que está na mesma pasta, utiliza-se um import relativo com .
Exemplo: from .nome_modelo import NomeClasse'''
'''Quando se quer importar classes de outras pastas, utiliza-se o caminho do módulo: from nome_pasta.nome_modulo import NomeClasse'''
'''As importações podem dar um erro circular (circular import error), ou seja, duas ou mais classes estão a dar import uma da outra, 
criando um ciclo de dependências que impede o Python de terminar o carregamento dos módulos'''
'''Não se deve dar import desta forma, por exemplo: jogo.accao_jogo; 
Pois dentro da pasta jogo existe um ficheiro jogo, e ao chamar daquela forma, o python não distingue qual está a ser chamado, 
o que cria um conflito de nomes entre módulos e packages'''
'''Então é importante organizar bem as importações e a estrutura do projeto para evitar dependências circulares entre módulos'''

class ControloPersonagem(Controlo):
    '''Classe ControloPersonagem que herda de Controlo, é um controlo específico para o personagem do jogo'''

    def __init__(self): 
        self.procurar = AccaoJogo(ComandoJogo.PROCURAR)
        self.aproximar = AccaoJogo(ComandoJogo.APROXIMAR)
        self.observar = AccaoJogo(ComandoJogo.OBSERVAR)
        self.fotografar = AccaoJogo(ComandoJogo.FOTOGRAFAR)
        self.__maq_est = MaquinaEstados(EstadoPersonagem.PROCURA, 
                                        [(EstadoPersonagem.PROCURA, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, self.aproximar),
                                        (EstadoPersonagem.PROCURA, EventoJogo.RUIDO, EstadoPersonagem.INSPECCAO, self.aproximar),
                                        (EstadoPersonagem.PROCURA, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA, self.procurar),
                                        (EstadoPersonagem.INSPECCAO, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA),
                                        (EstadoPersonagem.INSPECCAO, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, self.aproximar),
                                        (EstadoPersonagem.INSPECCAO, EventoJogo.RUIDO, EstadoPersonagem.INSPECCAO, self.procurar),
                                        (EstadoPersonagem.OBSERVACAO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, self.observar),
                                        (EstadoPersonagem.OBSERVACAO, EventoJogo.FUGA, EstadoPersonagem.INSPECCAO),
                                        (EstadoPersonagem.REGISTO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, self.fotografar),
                                        (EstadoPersonagem.REGISTO, EventoJogo.FUGA, EstadoPersonagem.PROCURA),
                                        (EstadoPersonagem.REGISTO, EventoJogo.FOTOGRAFIA, EstadoPersonagem.PROCURA)],)

    def processar(self, percepcao):
        '''Método que processa a perceção do ambiente e a partir disso retorna uma ação a ser tomada pelo personagem'''
        evento = percepcao.evento
        '''Buscar o read only da classe PercepcaoJogo, ou seja, chamar a função que retorna o valor de evento'''
        accao = self.__maq_est.processar(evento)
        '''A partir do evento, processa-se a próxima ação a ser executada a partir da função processar() da classe MaquinaEstados'''
        return accao
    
    @property
    def estado(self):
        '''Função para read only, que vai buscar à máquina de estado a função que também apenas lê o estado atual'''
        return self.__maq_est.estado
