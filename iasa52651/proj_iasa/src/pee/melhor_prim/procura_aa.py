from .procura_informada import ProcuraInformada
from .aval.avaliador_aa import AvaliadorAA

class ProcuraAA(ProcuraInformada):

    def  __init__(self):
        super().__init__(AvaliadorAA())