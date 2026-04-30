from pee.mec_proc.fronteira import Fronteira

class FronteiraFifo(Fronteira):
    '''Procura em largura (Fronteira FIFO - First In, First Out -> Fila), que será utilizado pela procura em largura.'''

    def inserir(self, no):
        '''Implementação do método abstrato da classe Fronteira, para o mecanismo de procura em largura.'''

        self._nos.append(no)
        '''Primeiros a entrar, são os primeiros a sair. 
        Para isto, são colocados no fim da fila de forma a seguirem a ordem de chegada.
        Vai-se buscar a lista de nós da fronteira, da classe Fronteira, e insere-se o nó no fim.'''