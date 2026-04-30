from .avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):
    
    def prioridade(self, no):
        return self.heuristica.h(no.estado)