from ambiente.ambiente_jogo import AmbienteJogo
from personagem.personagem import Personagem
from ambiente.evento_jogo import EventoJogo


class Jogo:
    '''A classe Jogo é a classe de arranque. Inicializa o ambiente e a personagem e executa a inicialização, 
    tanto como as atualizações do programa'''

    def __init__(self):

        self.__ambiente = AmbienteJogo()
        self.__personagem = Personagem(self.__ambiente)
        self.__personagem.mostrar()

        '''O Personagem não pode ser criado antes do que o ambinete pois é necessário passar como parâmetro o 
        ambiente para o personagem'''
        '''Para além do código podemos notar isso no pdf do projeto-parte 1: slides 11 e 8'''
        '''No slide 11, mostra na linha de tempo, que o ambiente deve ser criado antes do personagem'''
        '''No slide 8, mostra o diagrama UML com o construtor da classe Personagem desta forma: 
        + Personagem(ambiente: AmbienteJogo) -> indicando que a personagem requer um parâmetro, o ambiente'''

    def executar(self):

        while True:
            self.__ambiente.evoluir()
            self.__personagem.executar()
            self.__personagem.mostrar()
            if self.__ambiente.observar() == EventoJogo.TERMINAR:
                break

        '''Este loop "while True" é um loop sempre verdadeiro e dentro dele temos uma condição para encontrar o seu fim, 
        que é quando o evento observado no ambiente for igual a EventoJogo.TERMINAR'''
        '''Utiliza-se esta maneira em python para fazer um do-while, para que o código dentro do loop 
        seja executado pelo menos uma vez, e depois verificar a condição de fim do loop'''


# ---------- Executar o jogo ----------
if __name__ == "__main__":
    '''O jogo é executado a partir deste ponto, criando uma instância da classe Jogo e chamando o método executar()'''
    
    Jogo().executar()
