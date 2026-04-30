from pee.mec_proc.fronteira import Fronteira

class FronteiraLifo(Fronteira):
    '''Esta classe representa a fronteira LIFO (Last In, First Out -> Pilha), que será utilizada pela procura em profundidade.'''

    def inserir(self, no):
        '''Implementação do método abstrato da classe Fronteira, para o mecanismo de procura em profundidade.'''

        self._nos.insert(0,no)
        '''Nós mais recentes, são os primeiros a sair. Por isso, são colocados no ínicio da fila.
        Vai-se buscar a lista de nós da fronteira, da classe Fronteira, e insere-se o nó no início.'''