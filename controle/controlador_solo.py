from view.tela_solo import TelaSolo
from modelo.areia import Areia
from modelo.argila import Argila
from modelo.silte import Silte


class ControladorSolo():

    def __init__(self, controlador_sistema):
        self.__solos = []
        self.__tela = TelaSolo()
        self.__controlador_sistema = controlador_sistema
    
    @property
    def solos(self):
        return self.__solos
    
    def abre_tela(self):
        opcoes = {1: self.cadastra_solo,
                  2: self.retorna_solo,
                  3: self.mostra_solos,
                  4: self.deleta_solo,
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
    def solos(self):
        return self.__solos
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def mostra_solos(self):
        if self.__solos:
            self.__tela.imprime_mensagem("--- Lista de Solos ---")
            for solo in self.__solos:
                self.__tela.imprime_mensagem(f"Código: {solo.codigo} Origem: {solo.origem} ke: {solo.permeabilidade_eletroosmotica}")
        else:
            self.__tela.imprime_mensagem("Nenhum solo cadastrado.\n")
    
    def retorna_solo(self, codigo):
        for solo in self.__solos:
            if (solo.codigo == codigo):
                return solo
        else:
            self.__tela.imprime_mensagem("Solo não cadastrado ou código incorreto.")
    
    def cadastra_solo(self):
        print("--- Novo Cadastro de Solo ---")
        codigo = input("Digite o código do solo: ").strip()
        tipo = input("Digite o tipo do solo: ").strip()
        origem = input("Origem do solo: ").strip()
        cor = input("Descreva a cor do solo: ").strip()
        porosidade = float(input("Porosidade: "))
        massa_especifica_seca = float(input("Massa específica seca (g/cm³): "))
        condutividade_hidraulica = float(input("Condutividade hidraulica (cm/h): "))
        permeabilidade_eletroosmotica = float(input("Permeabilidade eletro-osmótica (cm²/V.h): "))

        if tipo.strip().lower() == "areia":
            solo = Areia(codigo=codigo,
                         tipo=tipo,
                         origem=origem,
                         cor=cor,
                         porosidade=porosidade,
                         massa_especifica_seca=massa_especifica_seca,
                         condutividade_hidraulica=condutividade_hidraulica,
                         permeabilidade_eletroosmotica=permeabilidade_eletroosmotica)
            self.__tela.imprime_mensagem("Novo solo cadastrado com sucesso.\n")

        elif tipo.strip().lower() == "argila":
            solo = Argila(codigo=codigo,
                          tipo=tipo,
                          origem=origem,
                          cor=cor,
                          porosidade=porosidade,
                          massa_especifica_seca=massa_especifica_seca,
                          condutividade_hidraulica=condutividade_hidraulica,
                          permeabilidade_eletroosmotica=permeabilidade_eletroosmotica)
            self.__tela.imprime_mensagem("Novo solo cadastrado com sucesso.\n")

        elif tipo.strip().lower() == "silte":
            solo = Silte(codigo=codigo,
                         tipo=tipo,
                         origem=origem,
                         cor=cor,
                         porosidade=porosidade,
                         massa_especifica_seca=massa_especifica_seca,
                         condutividade_hidraulica=condutividade_hidraulica,
                         permeabilidade_eletroosmotica=permeabilidade_eletroosmotica)
            self.__tela.imprime_mensagem("Novo solo cadastrado com sucesso.\n")
        
        self.__solos.append(solo)
        return solo
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def deleta_solo(self):
        try:
            if self.solos is not None:
                self.mostra_solos()
            else:
                self.__tela.imprime_mensagem("Nenhum solo cadastrado.")
            
            codigo_solo = self.__tela.coleta_codigo()
            solo = self.retorna_solo(codigo_solo)
            self.__solos.remove(solo)
            self.__tela.imprime_mensagem(f"Solo ({solo.codigo}) excluído com sucesso.")
        
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao tentar excluir o solo {solo.codigo}.")
