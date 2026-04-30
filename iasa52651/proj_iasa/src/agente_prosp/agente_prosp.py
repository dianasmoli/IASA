from agente.agente import Agente
import sae

class AgenteProsp(Agente):
    '''Como foi visto no pdf Introdução de engenharia software - parte 2, no slide 10, um mecanismo de fatorização é delegação'''
    '''Ou seja, ao ínves de herdar de uma classe, ela usa a outra classe, ou seja, Factorização funcional. 
    Tem um nível de acoplamento baixo.'''
    '''Como dito nos mesmo pdf mas no slide 9: "O conceito de factorização refere-se à decomposição das partes de um sistema de 
    modo a eliminar redundância (partes repetidas)"'''
    '''Logo ao utilizar-mos delegação estamos a eliminar redundâncias desnecessárias.'''

    def _percepcionar(self):
        '''Delegar o percepcionar do Transdutor'''
        '''Conceitos: SAE e Fatorização de comportamentos por delegação'''
        return sae.transdutor.percepcionar()

    def _actuar(self, accao):
        
        sae.transdutor.actuar(accao)
        '''Delegar o actuar do Transdutor'''
        '''accao é movimento por isso pode-se passar como parâmetro nesta método'''