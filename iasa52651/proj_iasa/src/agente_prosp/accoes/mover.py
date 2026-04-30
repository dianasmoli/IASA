from ecr.accao import Accao
from sae import Movimento

class Mover(Movimento, Accao):
    '''Herança múltipla'''
    '''É preciso ter cuidado porque pode existir colisão na árvore de herança, pois ao usar o metodo super() não expecifica 
    de qual das mães é, mas o python permite destinguir'''
    '''A class movimento tem que vir antes da classe ação, porque quando se faz super(), por omissão, 
    vai buscar a primeira classe a ser apresentada como mãe'''
    
    def __init__(self, direccao):
        '''Representa um movimento na direção indicada com um passo de uma unidade'''

        super().__init__(direccao)
