from view.tela_simulacao import TelaSimulacao
from modelo.usuario import Usuario
from modelo.simulacao import Simulacao
from datetime import date


class ControladorSimulacao():

    def __init__(self, controlador_sistema):
        self.__tela = TelaSimulacao()
        self.__simulacoes = []
        self.__controlador_sistema = controlador_sistema
    
    def abre_tela(self):
        opcoes = {1: self.cria_simulacao,
                  2: self.lista_simulacoes,
                  3: self.plota_grafico,
                  0: self.retornar
        }
    
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                self.__tela.imprime_mensagem("Opção inválida.")
    
    def cria_simulacao(self):
        # coleta os dados elementares da simulação
        codigo_simulacao, duracao = self.__tela.coleta_dados()

        # define o usuário inicial
        self.__tela.imprime_mensagem("--- Registra usuário ---")
        self.__controlador_sistema.controlador_usuario.lista_usuarios()
        matricula = self.__tela.coleta_matricula_usuario()
        usuario = self.__controlador_sistema.controlador_usuario.retorna_usuario(matricula)

        # define o solo que será usado
        self.__tela.imprime_mensagem("--- Seleção do solo ---")
        self.__controlador_sistema.controlador_solo.mostra_solos()
        codigo_solo = self.__tela.coleta_codigo_solo()
        solo = self.__controlador_sistema.controlador_solo.retorna_solo(codigo_solo)

        # define a espécie química que será analisada
        self.__tela.imprime_mensagem("--- Seleção da espécie química ---")
        self.__controlador_sistema.controlador_especie_quimica.mostra_especies()
        codigo_especie = self.__tela.coleta_codigo_especie_quimica()
        especie_quimica = self.__controlador_sistema.controlador_especie_quimica.retorna_especie(codigo_especie)

        # define a célula experimental que será simulada
        self.__tela.imprime_mensagem("--- Seleção da célula experimental ---")
        self.__controlador_sistema.controlador_celula_experimental.mostra_celulas()
        codigo_celula = self.__tela.coleta_codigo_celula()
        celula_experimental = self.__controlador_sistema.controlador_celula_experimental.retorna_celula(codigo_celula)

        # define as condicoes iniciais e de contorno do problema
        self.__tela.imprime_mensagem("--- Definição das condições iniciais e de contorno ---")
        self.__controlador_sistema.controlador_condicoes.mostra_condicoes()
        codigo_condicao = self.__tela.coleta_codigo_condicoes()
        condicao = self.__controlador_sistema.controlador_condicoes.retorna_condicao(codigo_condicao)

        # CRIA A SIMULAÇÃO
        simulacao = Simulacao(usuario,
                              codigo_simulacao,
                              duracao,
                              solo,
                              especie_quimica,
                              celula_experimental,
                              condicao)
        
        simulacao.calcula_coeficientes()
        simulacao.cria_mesh()
        simulacao.execucao()
        self.__simulacoes.append(simulacao)

        return simulacao
    
    def lista_simulacoes(self):
        self.__tela.imprime_mensagem("--- Código --- Usuário --- Duração (horas) ---")
        for simulacao in self.__simulacoes:
            print(simulacao.codigo, simulacao.usuario.nome, simulacao.duracao)
    
    def plota_grafico(self):
        self.lista_simulacoes()
        codigo = self.__tela.coleta_codigo_simulacao()
        for simulacao in self.__simulacoes:
            if (simulacao.codigo == codigo):
                Conc = simulacao.concentracoes
                incremento_espacial = 0.125
                incremento_temporal = 0.0625
                comprimento = simulacao.celula_experimental.comprimento
                duracao = simulacao.duracao
                n, m, self.__C = simulacao.cria_mesh()
                return self.__tela.plotagem(m, incremento_espacial, incremento_temporal, comprimento, duracao, Conc)
        else:
            self.__tela.imprime_mensagem("Simulação não cadastrada ou código incorreto.\n")
        
    def retornar(self):
        self.__controlador_sistema.abre_tela()
