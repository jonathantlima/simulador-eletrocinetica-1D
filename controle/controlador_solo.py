from view.tela_solo import TelaSolo
from modelo.areia import Areia
from modelo.argila import Argila
from modelo.silte import Silte
from DAOs.solos_dao import SoloDAO


class ControladorSolo():

    def __init__(self, controlador_sistema):
        #self.__solos = []
        self.__solos_dao = SoloDAO()
        self.__tela = TelaSolo()
        self.__controlador_sistema = controlador_sistema
    
    @property
    def solos_dao(self):
        return self.__solos_dao
    
    def abre_tela(self):
        opcoes = {1: self.cadastra_solo,
                  2: self.alterar_solo,
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
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def mostra_solos(self):        
        dados_solos = []
        for solo in self.__solos_dao.get_all():
            dados_solos.append(f"Código: {solo.codigo}, Tipo: {solo.tipo}, Origem: {solo.origem}, Cor: {solo.cor}, Porosidade: {solo.porosidade}, Massa específica seca (kg/L): {solo.massa_especifica_seca}, Condutividade hidráulica (m/m): {solo.condutividade_hidraulica}, Permeabilidade eletro-osmótica (m2/V.s): {solo.permeabilidade_eletroosmotica}"
                #{"Matrícula:": usuario.matricula, "Nome:": usuario.nome, "E-mail:":usuario.email, "Telefone:": usuario.telefone, "Departamento:": usuario.departamento}
                )
        self.__tela.exibe_solos(dados_solos)
    
    def alterar_solo(self):
        self.mostra_solos()
        codigo = self.__tela.coleta_codigo()
        try:
            for solo in self.__solos_dao.get_all():
                if (solo.codigo == codigo):
                    novos_dados = self.__tela.coleta_dados()
                    solo.codigo = novos_dados["codigo"]
                    solo.tipo = novos_dados["tipo"]
                    solo.origem = novos_dados["origem"]
                    solo.porosidade = novos_dados["porosidade"]
                    solo.massa_especifica_seca = novos_dados["massa_especifica_seca"]
                    solo.condutividade_hidraulica = novos_dados["condutividade_hidraulica"]
                    solo.permeabilidade_eletroosmotica = novos_dados["permeabilidade_eletroosmotica"]
                    self.__tela.imprime_mensagem("Dados atualizados com sucesso.\n")
        except:
            self.__tela.imprime_mensagem("Dados incorretos ou solo não cadastrado.")

        return solo
    
    def cadastra_solo(self):
        try:
            dados = self.__tela.coleta_dados()

            if dados['tipo'].strip().lower() == "areia":
                solo = Areia(codigo=dados['codigo'],
                             tipo=dados['tipo'],
                             origem=dados['origem'],
                             cor=dados['cor'],
                             porosidade=float(dados['porosidade']),
                             massa_especifica_seca=float(dados['massa_especifica_seca']),
                             condutividade_hidraulica=float(dados['condutividade_hidraulica']),
                             permeabilidade_eletroosmotica=float(dados['permeabilidade_eletroosmotica']))
                self.__solos_dao.add(solo)
                self.__tela.imprime_mensagem("Novo solo cadastrado com sucesso.\n")
                return solo

            elif dados['tipo'].strip().lower() == "argila":
                solo = Argila(codigo=dados['codigo'],
                              tipo=dados['tipo'],
                              origem=dados['origem'],
                              cor=dados['cor'],
                              porosidade=dados['porosidade'],
                              massa_especifica_seca=dados['massa_especifica_seca'],
                              condutividade_hidraulica=dados['condutividade_hidraulica'],
                              permeabilidade_eletroosmotica=dados['permeabilidade_eletroosmotica'])
                self.__solos_dao.add(solo)
                self.__tela.imprime_mensagem("Novo solo cadastrado com sucesso.\n")
                return solo

            elif dados['tipo'].strip().lower() == "silte":
                solo = Silte(codigo=dados['codigo'],
                              tipo=dados['tipo'],
                              origem=dados['origem'],
                              cor=dados['cor'],
                              porosidade=dados['porosidade'],
                              massa_especifica_seca=dados['massa_especifica_seca'],
                              condutividade_hidraulica=dados['condutividade_hidraulica'],
                              permeabilidade_eletroosmotica=dados['permeabilidade_eletroosmotica'])
                self.__solos_dao.add(solo)
                self.__tela.imprime_mensagem("Novo solo cadastrado com sucesso.\n")
                return solo
        
        except KeyError as e:
            self.__tela.imprime_mensagem(f"Dado ausente: {e}")
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao cadastrar solo: {e}")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def deleta_solo(self):
        try:
            if self.__solos_dao is not None:
                self.mostra_solos()
            else:
                self.__tela.imprime_mensagem("Nenhum solo cadastrado.")
            
            codigo_solo = self.__tela.coleta_codigo()
            for solo in self.__solos_dao.get_all():
                if (solo.codigo == codigo_solo):
                    self.__solos_dao.remove(solo.codigo)
                    self.__tela.imprime_mensagem(f"Solo ({solo.codigo}) excluído com sucesso.")
                    return solo
        
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao tentar excluir o solo {solo.codigo}.")
    
    def retorna_solo(self):
        try:
            self.mostra_solos()
            codigo_solo = self.__tela.coleta_codigo()
            if codigo_solo:
                for solo in self.__solos_dao.get_all():
                        if (solo.codigo == codigo_solo):
                            return solo
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao tentar retornar o solo {solo.codigo}.")