class PassoSolucao:
    '''Objeto imutável.
    Tem duas propriedades de leitura que permitem aceder à informação desses objetos sem alterar o seu conteúdo.'''

    def __init__(self, estado, operador):
        self.estado = estado
        self.operador = operador