from controle.controlador_solo import ControladorSolo
from controle.controlador_usuario import ControladorUsuario
from controle.controlador_condicoes import ControladorCondicoes
from controle.controlador_especie_quimica import ControladorEspecieQuimica
from controle.controlador_celula_experimtental import ControladorCelulaExperimental
from controle.controlador_simulacao import ControladorSimulacao
from view.tela_sistema import TelaSistema


class ControladorSistema():

    def __init__(self):
        self.__controlador_solo = ControladorSolo(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_condicoes = ControladorCondicoes(self)
        self.__controlador_especie_quimica = ControladorEspecieQuimica(self)
        self.__controlador_celula_experimental = ControladorCelulaExperimental(self)
        self.__controlador_simulacao = ControladorSimulacao(self)
        self.__tela = TelaSistema()
    
    @property
    def controlador_solo(self):
        return self.__controlador_solo
    
    @property
    def controlador_usuario(self):
        return self.__controlador_usuario
    
    @property
    def controlador_condicoes(self):
        return self.__controlador_condicoes
    
    @property
    def controlador_especie_quimica(self):
        return self.__controlador_especie_quimica
    
    @property
    def controlador_celula_experimental(self):
        return self.__controlador_celula_experimental
    
    @property
    def controlador_simulacao(self):
        return self.__controlador_simulacao
    
    def abre_tela(self):
        opcoes = {1: self.usuarios,
                  2: self.solos,
                  3: self.especie,
                  4: self.celulas,
                  5: self.condicoes,
                  6: self.opcoes_simulacao,
                  0: self.encerra_sistema
        }
        
        while True:
            try:
                opcao = self.__tela.menu()
                if opcao in opcoes:
                    try:
                        opcoes[opcao]()
                    except Exception as e:
                        self.__tela.imprime_mensagem(f"Erro ao executar a opção: {e}")
                else:
                    self.__tela.imprime_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela.imprime_mensagem(f"Erro inesperado no menu: {e}")

    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def usuarios(self):
        self.__controlador_usuario.abre_tela()
    
    def solos(self):
        self.__controlador_solo.abre_tela()
    
    def especie(self):
        self.__controlador_especie_quimica.abre_tela()
    
    def celulas(self):
        self.__controlador_celula_experimental.abre_tela()
    
    def condicoes(self):
        self.__controlador_condicoes.abre_tela()
    
    def opcoes_simulacao(self):
        self.__controlador_simulacao.abre_tela()
    
    def encerra_sistema(self):
        self.__tela.imprime_mensagem("Finalizando...")
        exit(0)