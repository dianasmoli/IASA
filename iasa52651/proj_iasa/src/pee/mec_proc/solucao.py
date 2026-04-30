from .passo_solucao import PassoSolucao

class Solucao:
    '''A classe Solucao representa um percurso correspondente a uma solução de um problema.
    Tem um sequência de nós que representa um percurso no espaço de estados, 
    permite acesso indexado e iteração sobre o percurso e  permite remover o primeiro nó do percurso'''

    def __init__(self, no_final):
        self.no_final = no_final

        self.__dimensao = no_final.profundidade
        '''Dimensão da solução (número de nós do percurso / passos).
        A profundidade do nó final dá a dimensão, isto porque a profundidade é calculada apartir do antecessor e mais um. 
        Ou seja, no nó inicial a profundidade é igual a 0, e ao expandir esse nó, os próximos serão de profundidade 1 
        e assim sucessivamente. Logo a dimensão da solução é igual à profundidade do nó final.'''

        self.__custo = no_final.custo
        '''Por sua vez, o custo da solução é igual ao custo do nó final, já que este tem o custo do percurso todo.'''

        self.__passos = []
        '''Lista de passos da solução, ou seja, lista do percurso.'''

        no = no_final
        '''Variável auxiliar que vais percorrer todos os nós do percurso.'''

        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            '''Cada passo da solução tem um estado e um operador aplicar nesse estado. 
            O estado vai-se buscar ao antecessor, enquanto que o operador vai-se buscar ao nó atual, 
            já que este armazeno o operador que o gerou.'''

            self.__passos.insert(0, passo)
            '''Este while percorre do fim para o início do percurso, por isso, para manter a forma ordenada e correta do percurso,
            adiciona-se cada passo sempre ao início da lista.'''

            no = no.antecessor
            '''Atualiza-se o nó auxiliar para percorrer o antecessor do antecessor até chegar ao nó inicial.'''
    
    def __iter__(self):
        '''Permite gerar um iterador para a solução. 
        Assim, é possível iterar sobre os passos da solução, por exemplo, num ciclo for.'''

        '''Gera um iterador a partir da lista de passos da solução.'''
        return iter(self.__passos)


    def __getitem__(self, index):
        '''Permite aceder a um passo específico da solução, através do seu índice. Como se fosse um array.'''

        return self.__passos[index]
    
    '''====== Read-only properties ======'''
    @property
    def dimensao(self):
        return self.__dimensao
    

    @property
    def custo(self):
        return self.__custo
    