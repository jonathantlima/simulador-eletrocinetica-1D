from view.tela_especie_quimica import TelaEspecieQuimica
from modelo.especie_quimica import EspecieQuimica
from DAOs.especie_quimica_dao import EspecieQuimicaDAO
from modelo.anion import Anion
from modelo.cation import Cation


class ControladorEspecieQuimica():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaEspecieQuimica()
        self.__especies_dao = EspecieQuimicaDAO()
    
    @property
    def especies_dao(self):
        return self.__especies_dao
    
    def abre_tela(self):
        opcoes = {1: self.cadastra_especie_quimica,
                  2: self.altera_especie,
                  3: self.mostra_especies,
                  4: self.deleta_especie,
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
    
    @property
    def especies(self):
        return self.__especies
    
    def mostra_especies(self):
        especies = []
        for especie in self.__especies_dao.get_all():
            especies.append([especie.codigo, especie.nome, especie.formula, especie.funcao, especie.valencia, especie.coeficiente_de_distribuicao, especie.coeficiente_de_difusao])
        self.__tela.exibe_especies(especies)
            
    def altera_especie(self):
        self.mostra_especies()
        codigo = self.__tela.coleta_codigo()
        try:
            for especie in self.__especies_dao.get_all():
                if (especie.codigo == codigo):
                    novos_dados = self.__tela.coleta_dados()
                    especie.codigo = novos_dados["codigo"]
                    especie.nome = novos_dados["nome"]
                    especie.formula = novos_dados["formula"]
                    especie.funcao = novos_dados["funcao"]
                    especie.valencia = novos_dados['valencia']
                    especie.coeficiente_de_distribuicao = novos_dados['coeficiente_de_distribuicao']
                    especie.coeficiente_de_distribuicao = novos_dados['coeficiente_de_distribuicao']
                    self.__tela.imprime_mensagem("Dados atualizados com sucesso.\n")
        except:
            self.__tela.imprime_mensagem("Dados incorretos ou espécie não cadastrada.")
    
    def cadastra_especie_quimica(self):
        try:
            dados = self.__tela.coleta_dados()

            if dados['valencia'] > 0:
                especie = Cation(codigo=dados['codigo'],
                                 nome=dados['nome'],
                                 formula=dados['formula'],
                                 funcao=dados['funcao'],
                                 valencia=dados['valencia'],
                                 coeficiente_de_distribuicao=dados['coeficiente_de_distribuicao'],
                                 coeficiente_de_difusao=dados['coeficiente_de_difusao'])
                self.__especies_dao.add(especie)
                self.__tela.imprime_mensagem(f"Nova espécie cadastrada com sucesso (cód: {especie.codigo}).\n")
                return especie

            elif dados['valencia'] < 0:
                especie = Anion(codigo=dados['codigo'],
                                nome = dados['nome'],
                                formula=dados['formula'],
                                funcao=dados['funcao'],
                                valencia=dados['valencia'],
                                coeficiente_de_distribuicao=dados['coeficiente_de_distribuicao'],
                                coeficiente_de_difusao=dados['coeficiente_de_difusao'])
                self.__especies_dao.add(especie)
                self.__tela.imprime_mensagem(f"Nova espécie cadastrada com sucesso (cód: {especie.codigo}).\n")
                return especie

        except KeyError as e:
            self.__tela.imprime_mensagem(f"Dado ausente: {e}")
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao cadastrar espécie química: {e}")
    
    def deleta_especie(self):
        try:
            if self.__especies_dao is not None:
                self.mostra_especies()
            else:
                self.__tela.imprime_mensagem("Nenhuma célula cadastrada.")
            
            codigo_especie = self.__tela.coleta_codigo()
            for especie in self.__especies_dao.get_all():
                if (especie.codigo == codigo_especie):
                    self.__especies_dao.remove(especie.codigo)
                    self.__tela.imprime_mensagem(f"Célula experimental ({especie.codigo}) excluída com sucesso.")
                    return especie
        
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao tentar excluir a célula experimental {especie.codigo}.")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()