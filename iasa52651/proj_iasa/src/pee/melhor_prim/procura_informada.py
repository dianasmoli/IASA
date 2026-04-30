from .procura_melhor_prim import ProcuraMelhorPrim
from abc import ABC

class ProcuraInformada(ProcuraMelhorPrim, ABC):

    def procurar(self, problema, heuristica):
        self._avaliador.heuristica = heuristica
        return super().procurar(problema)