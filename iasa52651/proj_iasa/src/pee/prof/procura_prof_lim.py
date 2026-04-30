from .procura_profundidade import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):
    '''Esta classe representa a procura em profundidade limitada, é uma procura com limite de profundidade, o que leva à 
    exploração de nós em largura, mantendo a complexidade de memória linear.
    O problema é que a profundidade a que se encontra a solução pode não ser conhecida, porque pode passar dessa limitação.'''

    def procurar(self, problema, prof_max = 10):
        '''Este método serve para inicializar a variável privada e faz a procura do problema para ter
        uma solução, a partir de um método existente.'''

        self.__prof_max = prof_max
        '''Profuniddade máxima (limite)'''

        '''Retorna a solução, calculada no método da classe superior MecanismoProcura. Reutilizar código já feito.'''
        return super().procurar(problema)

    def _expandir(self, problema, no):
        '''Invoca o método responsável por expandir o nó, se este não atingiu o limite.
        Caso tenha chegado ao limite, retorna-se uma lista vazia.'''
        return super()._expandir(problema, no) if no.profundidade < self.__prof_max else []