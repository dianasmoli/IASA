from .comport_comp import ComportComp

class Prioridade(ComportComp):
    '''Classe que representa uma forma de escolher uma ação. 
    As acções são seleccionadas de acordo com uma prioridade associada que varia ao longo da execução.'''

    def seleccionar_accao(self, accoes):
        '''Acontece polimorfismo na repetição deste método, pois a classe Hierarquia tambêm o implementa, 
        e em cada classe é implementado de forma diferente.'''

        if accoes:
            '''Cada accao herda da classe Accao e está associado um valor de prioridade. 
            A que tiver mais prioridade é a escolhida.'''

            return max(accoes, key = lambda accao: accao.prioridade) 
        '''Parâmetro key define como os elemntos vão ser comparados, porque as accoes não dá para serem comparadas entre si, 
        precisam da prioridade para tal.
        lambda accao: função anónia (para não criar uma função nova).
        accao.prioridade: chama o método da classe Accao para sabermos o valor de cada prioridade de accao.''' 