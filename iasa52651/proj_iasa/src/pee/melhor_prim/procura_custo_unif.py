from .procura_melhor_prim import ProcuraMelhorPrim
from .aval.avaliador_custo_unif import AvaliadorCustoUnif

class ProcuraCustoUnif(ProcuraMelhorPrim):

    def __init__(self):
        super().__init__(AvaliadorCustoUnif())