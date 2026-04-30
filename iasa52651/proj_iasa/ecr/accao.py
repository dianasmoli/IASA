from agente.accao import Accao as AccaoAgente
'''Esta linha de import permitiu uma melhor compreensão do código. Ou seja, ao invés de colocar a herança: Accao(Accao) 
(o que parece que herda de ela mesma).
A partir desta linha renomiou-se, apenas neste módulo, o nome da classe de que herdamos'''
'''No slide 3, do pdf do Projeto - Parte 2, aparece "{alias=AccaoAgente}". 
Logo temos que alterar o nome para evitar conflitos de nomes e manter o código mais claro'''

class Accao(AccaoAgente):

    def __init__(self, prioridade=0):
        super().__init__()
        self.__prioridade = prioridade

    @property
    def prioridade(self):
        '''Método de apenas leitura (getter e read only)'''
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, valor):
        '''Método que altera o valor da variável prioridade (setter)'''
        self.__prioridade = valor