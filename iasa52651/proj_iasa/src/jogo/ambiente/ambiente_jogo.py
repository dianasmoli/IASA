from .evento_jogo import EventoJogo

class AmbienteJogo:
    '''Classe que representa o ambiente do jogo, é responsável por gerar eventos, observar o estado atual do ambiente e executar comandos'''

    def __init__(self):
        '''Dicionário de eventos do jogo'''
        '''Padrão de geração (evento.value: evento)'''
        '''Padrão gerado (for evento in EventoJogo)'''
        self.__eventos = {evento.value: evento for evento in EventoJogo}
        self.__evento = None
        '''__ indica que é privado'''
    
    @property
    def evento(self):
        '''Read only - Propriedade publicamente acessível, mas somente leitura'''
        return self.__evento
    
    def evoluir(self):
        '''Método responsável por gerar um novo evento e evoluir o estado do ambiente do jogo'''
    
        '''Gerar um novo evento'''
        self.__evento = self.__gerar_evento()
        '''Mostrar o evento gerado, caso exista'''
        if self.__evento is not None:
            self.__evento.mostrar()
    
    def observar(self):
        '''Método para observar o evento atual do ambiente do jogo'''
    
        return self.__evento

    def executar(self, comando):
        '''Método para executar um comando no ambiente do jogo, ou seja, mostrar o comando executado (chamando o método mostrar da classe ComandoJogo)'''
    
        comando.mostrar()
    
    def __gerar_evento(self):
        '''Método privado para gerar um evento a partir do teclado'''
    
        '''Obtem um evento a partir do teclado'''
        texto = input("\nEvento? ")
        '''O método get do dicionário retorna o valor associado à chave, ou None se a chave não existir'''
        return self.__eventos.get(texto) 

    