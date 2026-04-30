from .procura_prof_lim import ProcuraProfLim

class ProcuraProfIter(ProcuraProfLim):
    '''Esta classe representa a procura em profundidade iterativa, e utiliza a profundidade iterativa com limites de profundidade 
    crescentes e não é mantida memória de nós explorados entre procuras. Mantém as características de complexidade da procura 
    em profundidade e possibilita a limitação da procura a uma profundidade máxima.
    Este tipo de procura profunda corrige o erro da procura limitada. Porque se aumentar muito a limitação, perdemos eficiencia
    e voltamos ao problema de perda de tempo e memória. Por tanto, a profundidade iterativa elimina a necessidade de adivinhar 
    o limite correto, tornando a busca completa e eficiente e ocupa menos memória. Desde que o incremento seja uma unidade é ótima.'''
    
    def procura(self, problema, inc_prof = 1, limite_prof = 100):
        '''Método completo, ótimo e tem em conta à memória computacional.'''

        for prof_max in range(0, limite_prof + 1, inc_prof):
            '''(inicio, fim -1, incremento)'''

            solucao = super().procurar(problema, prof_max)
            '''Procura em profundidade limitada. Chama o método da classe ProcuraProfLim, que precisa de uma profundidade máxima.'''

            if solucao:
                '''Verifica se solucao não é none e retorna caso não o seja.'''
                return solucao