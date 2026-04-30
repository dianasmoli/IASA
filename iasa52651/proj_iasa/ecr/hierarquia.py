from .comport_comp import ComportComp

class Hierarquia(ComportComp):
    '''Classe que representa uma forma de escolher uma ação.
    Os comportamentos estão organizados numa hierarquia fixa de subsunção (supressão e substituição).'''

    def seleccionar_accao(self, accoes):

        '''Na lista de accoes existe uma ordem fixa para serem escolhidas. Foram colocadas na mesma ordem que os comportamentos.
        Logo como o comportamento que está no início da lista de comportamento tem mais prioridade, 
        a primeira accao tem mais prioridade.'''

        '''Devem verificar que accoes tem elementos lá dentro, para uma melhor prática.'''

        if accoes:
            accao = accoes[0]
            '''A primeira açção na hierarquia é a que vai ser escolhida, no nosso caso.'''

        return accao