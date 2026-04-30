class MaquinaEstados:
    '''A classe MaquinaEstados representa a máquina de estados do programa, um modelo base de organização dos 
    microprocessadores e dos computadores em geral. 
    O estado do sistema é guardado num circuito de memória sequencial, sincronizado por um sinal de tempo que define 
    o ritmo de atualização. Um circuito combinatório recebe as entradas e o estado atual e, com base nessa informação, 
    determina as saídas e o próximo estado do sistema.
    O funcionamento pode ser descrito como uma sequência de comportamentos da personagem:
        - Começa no estado PROCURA animais.
        - Ao detetar um ruído, aproxima-se e passa para o estado INSPECCAO.
        - Se o silêncio voltar, regressa ao estado de PROCURA.
        - Quando deteta um animal, aproxima-se e passa para OBSERVACAO.
        - Caso o animal fuja durante a OBSERVACAO, a personagem volta à INSPECCAO da zona à procura da fonte do ruído.
        - Se o animal continuar presente, passa para o estado de REGISTO.
        - Se o animal permanecer, a personagem fotografa-o.
        - Depois de conseguir a fotografia ou se o animal fugir, a personagem regressa novamente ao estado de PROCURA.
    Assim, o comportamento evolui entre diferentes estados conforme os eventos detetados.'''

    def __init__(self,estado_inicial, transicoes):
        '''Na inicialização da máquina de estados, é necessário definir o estado inicial e as transições de estados'''

        self.__estado = estado_inicial
        self.transicoes = transicoes
        '''transicoes é um dicionário onde a chave é o estado atual e o valor é outro dicionário, 
        onde a chave é o evento e o valor é uma tupla com o estado sucessor e a ação a ser executada'''
        '''Formatos possíveis:
           (EstadoAntecessor, Evento, EstadoSucessor, Acao)
           (EstadoAntecessor, Evento, EstadoSucessor) -> omitido a uma ação nula(None)'''
        
        self.__tte = {}
        '''tabela de transição de estados: δ : Q x Σ → Q (EstadoPersonagem x EventoJogo -> EstadoPersonagem)'''
        '''Temos como entrada um elemento do conjunto de estados do personagem mais um elemento do conjunto de entradas do jogo.
        O que resulta na saída de um novo estado, o próximo estado, do personagem'''
        '''Ou seja, troca o estado do programa.'''
        
        self.__tae = {}
        '''tabela de ações de estados: δ : Q x Σ → Z (EstadoPersonagem x EventoJogo -> ComandoJogo)'''
        '''Temos como entrada um elemento do conjunto de estados do personagem mais um elemento do conjunto de entradas do jogo.
        O que resulta na saída de um elemento do conjunto de saídas do jogo'''
        '''Ou seja, troca ação do programa.'''
        
        if transicoes:
            '''Este if funciona para: false = não existem elementos / true = existem elementos'''
            
            for transicao in transicoes:
                
                estado_ant, evento, estado_suc, accao = transicao \
                    if len(transicao) == 4 else transicao + (None,)
                '''Algumas transições têm ação, outras não, por isso é necessário verificar se a ação existe ou não'''
                '''Verifica se o tuplo tem 4 elementos, caso não tenha então adiciona-se uma ação nula(None) para completar o tuplo'''
                '''Virgula final é para criar um tuplo com um único elemento, caso contrário o Python não reconhece como tuplo e vai achar que é um elemento'''
                '''Nota que "\" serve apenas para quebrar a linha de código, para melhorar a legibilidade do código, mas é tudo apenas uma linha'''
                
                self.definir_transicao(estado_ant, evento, estado_suc, accao)
                '''Chama o método definir_transicao para adicionar a transição à tabela de transiçãos de estados e à tabela de ações de estados'''

   
    def definir_transicao(self,estado_ant, evento, estado_suc, accao):
        '''Esta função define as transições e preenche as tabelas'''
        
        self.__tte[(estado_ant,evento)] = estado_suc
        '''Necessário abrir () para criar uma tupla par (estado_ant, evento) e associar o estado_suc'''
        
        if accao is not None:
            '''Verifica se accao existe ou é None'''
            
            '''Um erro subtil mas muito importante é fazer apenas a verificação "if accao:", porque accao pode obter números 
            inteiros e se for zero, esta linha de código iria ser convertida para false e então a ação não iria ser executada'''
            
            self.__tae[(estado_ant,evento)] = accao
            '''Caso exista então adiciona a accao à tabela de ações de estados'''
        
    
    def processar(self, evento):
        '''A função processar é responsável por processar o seguinte estado e accao'''
        accao = self.__tae.get((self.__estado, evento))
        novo_estado = self.__tte.get((self.__estado, evento))
        if novo_estado is not None:
            self.__estado = novo_estado

        return accao

    
    @property
    def estado(self):
        '''Função de read only'''
        return self.__estado