from ecr.comportamento import Comportamento
from random import random, choice
from sae import Direccao
from agente_prosp.accoes.avancar import Avancar
from agente_prosp.accoes.rodar import Rodar

'''Na importação da biblioteca sae não é necessário colocar o caminho completo, porque a partir do __init__.py dessa biblioteca, 
o caminho já é definido. O que é uma boa prática, porque as pessoas não têm que se preocupar com o caminho completo.'''

class Explorar(Comportamento):
    '''Objetivo do comportaamento (Antes): o explorar tem o objetivo de explorar o ambiente.'''
    '''Objetivo do comportamento (Depois): o explorar tem o objetivo de avançar e rodar, dado uma probabilidade de rotação. 
    Ou seja, explorar o ambiente à sua volta'''

    def __init__(self, prob_rotacao = 0.7):
        '''prob_rotacao é um parametro oculto, que tem um valor por defeito de 0.7, ou seja, 70% de probabilidade de rotação.'''

        self.__prob_rotacao = prob_rotacao

    def activar(self, percepcao):
        '''Não se utiliza o parâmetro percepcao, porque o explorar não depende de nenhum estímulo.'''
        
        valor_aleatorio = random()
        '''Gerar um número aleatório entre 0 e 1.'''

        if valor_aleatorio <= self.__prob_rotacao:
            '''Verificar se é menor que a probabilidade de rotação, porque se for roda.'''

            lista_direcoes = list(Direccao)
            '''Torna um enum em lista, para aplicar o método choice (só trabalha com listas).'''

            direcao_aleatoria = choice(lista_direcoes)
            '''Escolhe da lista de direções uma direccao.'''
            
            accao = Rodar(direcao_aleatoria)
            '''Chama a classe correspondente à ação Rodar, que precisa de uma direção.'''
        
        else:
        
            accao = Avancar()
            ''' O avançar não necessita de direção porque ele mantem a direção atual do agente.'''

        return accao