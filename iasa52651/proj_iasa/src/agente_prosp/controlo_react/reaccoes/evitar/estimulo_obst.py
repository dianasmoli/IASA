from ecr.estimulo import Estimulo

class EstimuloObst(Estimulo):

    INTENS_OBST = 1
    '''Parâmetro estático da classe, como está fora de um método, é partilhados por todas as instâncias da classe.
    Não é alterável, é uma constante, para quem acede à instância, é só de leitura, para os que o utilizarem. 
    Para ser alterado é preciso chamar a classe (EstimuloObst.INTENS_OBST = 2).'''
    

    def detectar(self, percepcao):
        '''O método detectar é responsável por detetar se o agente está em contacto com um obstáculo 
        e retorna a itensidade do estímulo.'''

        return self.INTENS_OBST if percepcao.contacto_obst() else 0
    '''O método contacto_obst() pertence à classe Percepcao da biblioteca SAE, e visto que a nossa classe Percepcao 
    herda dessa classe é possível utilizar esse método.
    O método retorna um valor booleano, indicando se o agente está em contacto com um obstáculo ou não.'''
