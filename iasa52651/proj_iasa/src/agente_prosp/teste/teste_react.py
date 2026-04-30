from agente_prosp.agente_prosp import AgenteProsp
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.controlo_react.reaccoes.recolher.recolher import Recolher
from sae import Simulador

if __name__ == "__main__":

    agente = AgenteProsp(ControloReact(Recolher()))
    '''Cria uma instância do agente prospetivo, que tem um controlo reativo com o comportamento Explorar associado.'''

    '''Embora que a classe AgenteProsp não tenha parâmetros, como ela herda de Agente, que tem como parâmetro o controlo,
    a partir da herança, é possivel passar como parâmetro e associar esse controlo reativo. 
    Já o ControloReact tem o parâmetro de comportamento e a classe Explorar implementa a interface Comportamento, 
    por tanto passa a ser um objeto dessa classe.'''

    simulador = Simulador(1, agente)
    '''Instanciar o simulador da SAE, com o parÂmetro do mapa e o agente.'''

    simulador.executar()

    '''Nota problema: O agente no jogo colide com um obstáculo e então fica vermelha, isto acontece porque a classe que trata 
    deste problema, a classe EvitarObst, ainda não foi implementada. Então essa classe não está a ser utilizada e 
    não está a fazer o seu trabalho, que é evitar colisões.
    
    Resolução do problema: Para resolver este problema, é necessário implementar a classe EvitarObst, para ser possível 
    desviar dos objetos sem correr o risco de colisões. Na implementação, é necessário ter um campo para saber se o 
    agente pode andar em frente sem colidir.'''
