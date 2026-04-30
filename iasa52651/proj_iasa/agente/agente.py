from abc import ABC, abstractmethod
'''Abstrac Base Class(ABC), é um modulo que fornece a infraestrutura para definir classes abstratas em Python.'''

class Agente(ABC):
    '''A classe Agente representa um agente inteligente que interage com o ambiente. 
    Ela possui um controlo para processar percepções e obter ações, 
    e métodos protegidos para obter percepções e executar ações.
    A letra "a" no módulo está em minúscula enquanto a da classe 
    está maíscula para evitar erros de importação.'''
    
    def __init__(self, controlo):
        '''O método __init__ é o construtor da classe, que recebe um controlo como parâmetro e o atribui a um atributo da classe.'''
        self._controlo = controlo

    @abstractmethod
    def _percepcionar(self):
        '''O método abstrato, que deve ser implementado por subclasses, _percepcionar é responsável por obter a percepção do ambiente.'''
        '''O _ representa um método protegido.'''
        '''Forma de encapsulamento, onde o método é protegido e não deve ser acessado diretamente fora da classe ou de suas subclasses.'''
        """Obter percepção do ambiente"""
    
    @abstractmethod
    def _actuar(self, accao):
        '''O método protegido abstrato _actuar é responsável por obter a ação a ser executada no ambiente'''
    
    def executar(self):
        '''O método executar é responsável por executar a ação no ambient.'''
        '''Começa por fazer ação e obter o objeto de percepcao'''
        percepcao = self._percepcionar()
        '''De seguida, procesa esse objeto enviado'''
        accao = self._controlo.processar(percepcao)
        '''Depois verificar se accao é None ou não'''
        if accao is not None:
            '''Se não for None, executa a ação'''
            self._actuar(accao)
        else:
            '''Se for None, não executa a ação e o método acaba aqui'''
            print("Nenhuma ação a executar.")
    
