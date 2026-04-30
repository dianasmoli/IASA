from ecr.prioridade import Prioridade
from .aproximar_dir import AproximarDir
from sae import Direccao

class AproximarAlvo(Prioridade):
    '''Objetivo do comportamento (Antes): o aproximar tem o objetivo de se aproximar do alvo recolhido.'''

    '''Descrição do diagrama: permite aproximar em multiplas direções, divide-se em 4 para ser mais simples. 
    Estas são: AproximarDir(NORTE), AproximarDir(SUL), AproximarDir(ESTE), AproximarDir(OESTE).
    São reações, pois é um comportamento composto de Reaccao.
    Aproximar alvo é um comportamento composto de Prioridade, isto serve para que a direção em que se movimenta seja escolhida 
    de forma prioritário. Apresenta um critério de escolha de prioridade, o alvo mais próximo estará numa determinada direção 
    e vai ser essa direção a escolhida.
    Para tal, o AproximasDir precisa de saber a distância até ao alvo e atribuir à prioridade. 
    Ou seja, cada direção vai ter uma distância até ao alvo e a mais próxima será escolhida porque tem prioridade sobre as outras, 
    o mecanismo de seleção de ação a ser implementado é o de prioridade.
    A partir da percepcao, e na direção correspondente ao alvo mais próximo, vamos obter um estimulo.
    Quando disparado, o estímulo do alvo, gera uma resposta para mover o agente através da classe de aproximação direcional.'''

    def __init__(self):
        super().__init__([AproximarDir(direccao) for direccao in Direccao])
        '''Gera uma lista de AproximarDir para cada direção presente na classe Direccao.
        Forma mais versatil de adicionar à lista as direções, em vez de adicionar uma a uma.'''