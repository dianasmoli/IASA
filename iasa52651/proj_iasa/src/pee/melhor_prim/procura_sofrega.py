from .procura_informada import ProcuraInformada
from .aval.avaliador_sof import AvaliadorSof

class ProcuraSofrega(ProcuraInformada):

    def  __init__(self):
        super().__init__(AvaliadorSof())