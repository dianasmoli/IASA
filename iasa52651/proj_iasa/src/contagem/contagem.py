'''Aplicação contagem'''
from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.melhor_prim.procura_aa import ProcuraAA
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from lib.pee.melhor_prim.procura_sofrega import ProcuraSofrega
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.prof.procura_prof_lim import ProcuraProfLim
from lib.pee.melhor_prim.procura_informada import ProcuraInformada
from mod_prob.heuristica_contagem import HeuristicaContagem
from mod_prob.problema_contagem import ProblemaContagem


'''Todos os mecanismos de procura que implementamos.'''
MECANISMOS_PROCURA = [
    ProcuraProfundidade(), 
    ProcuraLargura(),
    ProcuraProfLim(),
    ProcuraProfIter(),
    ProcuraCustoUnif(),
    #ProcuraSofrega(),
    #ProcuraAA()
]

VALOR_INICIAL = 0
VALOR_FINAL = 8
INCREMENTOS = [1,2,3]
INCREM_CICLO = [1,2,3,-1]

def teste_contagem(valor_inicial, valor_final, incrementos, mecanismos_procura):
    print()
    print("valor inicial: ", valor_inicial)
    print("valor final: ", valor_final)
    print("incrementos: ", incrementos)

    '''Inicializa-se o problema a partir do valor_inicial, valor_final e incrementos.'''
    problema = ProblemaContagem(valor_inicial, valor_final, incrementos)

    '''Corre-se todos os mecanismos de procura.'''
    for mec_proc in mecanismos_procura:

        '''Verifica se é uma procura infromada.'''
        if isinstance(mec_proc, ProcuraInformada):

            '''Se for então inicializa a métrica heurística.'''
            heuristica = HeuristicaContagem(valor_final)

            '''E a partir do problema e da métrica heurística, calcula-se a solução.'''
            solucao = mec_proc.procurar(problema, heuristica)

        else:
            '''Caso não seja uma procura informada, a solução não depende da métrica heurística.'''
            solucao = mec_proc.procurar(problema)

        print()
        '''Obtemos o nome da classe e mostramos os resultados obtidos.'''
        print(mec_proc.__class__.__name__)
        print("Solução: ", [passo.operador.incremento for passo in solucao])
        print("Dimensão: ", solucao.dimensao)
        print("Custo: ", solucao.custo)

print("\nTeste de problema sem ciclos")
teste_contagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS, MECANISMOS_PROCURA)

print("\nTeste de problema com ciclos")
teste_contagem(VALOR_INICIAL, VALOR_FINAL, INCREM_CICLO, MECANISMOS_PROCURA[1:])

'''Resultado:     '''