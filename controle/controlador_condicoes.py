from view.tela_condicoes import TelaCondicoes
from modelo.condicoes import CondicoesDoProblema


class ControladorCondicoes():

    def __init__(self, controlador_sistema):
        self.__tela = TelaCondicoes()
        self.__controlador_sistema = controlador_sistema
        self.__condicoes = []
    
    def abre_tela(self):
        opcoes = {1: self.cadastra_condicoes,
                  2: self.retorna_condicao,
                  3: self.mostra_condicoes,
                  0: self.retornar
        }
    
        while True:
            try:
                opcao = self.__tela.mostra_menu()
                if opcao in opcoes:
                    try:
                        opcoes[opcao]()
                    except Exception as e:
                        self.__tela.imprime_mensagem(f"Erro ao executar a opção: {e}")
                else:
                    self.__tela.imprime_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela.imprime_mensagem(f"Erro inesperado no menu: {e}")
    
    @property
    def controlador_condicoes(self):
        return self.__controlador_sistema
    
    @property
    def condicoes(self):
        return self.__condicoes
    
    def mostra_condicoes(self):
        self.__tela.imprime_mensagem(f"--- Código --- Concentração inicial --- Concentração no reservatório")
        for condicao in self.__condicoes:
            self.__tela.imprime_mensagem(f"--- {condicao.codigo} --- {condicao.concentracao_inicial} --- {condicao.concentracao_reservatorio}")
    
    def retorna_condicao(self, codigo):
        for condicao in self.__condicoes:
            if (condicao.codigo == codigo):
                return condicao
        else:
            self.__tela.imprime_mensagem("Condição não cadastrada ou código incorreto.\n")
    
    def cadastra_condicoes(self):
        self.__tela.imprime_mensagem("Novo Conjunto de Condições Iniciais e de Contorno")
        codigo = input("Código: ")
        concentracao_inicial = float(input("Concentração inicial (mg/L): "))
        gradiente_eletrico = float(input("Gradiente elétrico (V/cm): "))
        gradiente_hidraulico = float(input("Gradiente hidráulico (cm/cm): "))
        concentracao_reservatorio = float(input("Concentração no reservatório (mg/L): "))

        condicao = CondicoesDoProblema(codigo,
                                       concentracao_inicial,
                                       gradiente_eletrico,
                                       gradiente_hidraulico,
                                       concentracao_reservatorio)
        
        self.__tela.imprime_mensagem(f"Novas condições inicial e de contorno criadas (cód: {codigo}).\n")        
        self.__condicoes.append(condicao)
        return condicao
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()