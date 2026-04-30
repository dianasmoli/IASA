from pee.mec_proc.procura_grafo import ProcuraGrafo
from .fronteira_prioridade import FronteiraPrioridade

class ProcuraMelhorPrim(ProcuraGrafo):

    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador

    def _manter(self, no):
         '''Manter se ainda não tiver nos explorados, caso já esteja então é para manter se tiver um custo inferior ao custo
           que está na lista explorados correspondente a esse mesmo nó.'''
         return super()._manter(no) or \
                    no.custo < self._explorados[no.estado].custo