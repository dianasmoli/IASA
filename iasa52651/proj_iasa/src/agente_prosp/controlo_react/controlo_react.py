from agente.controlo import Controlo

class ControloReact(Controlo):
    '''O controlo reactivo é um controlo que tem um comportamento interno, 
    e esse comportamento é o que gera a accao a partir da percepcao.'''

    def __init__(self, comportamento):

        self.__comportamento = comportamento

    def processar(self, percepcao):
        '''O processar recebece uma percepcao, e o método processar, juntamente com o comportamento, geram uma accao. 
        (pdf Arquitetura de agentes reactivos - Parte 2, slide 11)'''

        return self.__comportamento.activar(percepcao)
    '''A classe comportamento tem uma método activar que precisa de uma percepcao para gerar uma accao.'''