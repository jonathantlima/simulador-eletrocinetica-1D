from view.tela_celulas import TelaCelulas
from modelo.celula_experimental import CelulaExperimental
from DAOs.celula_experimental_dao import CelulaExperimentalDAO


class ControladorCelulaExperimental():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaCelulas()
        self.__celulas_dao = CelulaExperimentalDAO()
    
    @property
    def celulas_dao(self):
        return self.__celulas_dao
    
    def abre_tela(self):
        opcoes = {1: self.cadastra_celula,
                  2: self.altera_celula,
                  3: self.mostra_celulas,
                  4: self.deleta_celula,
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
    def celulas(self):
        return self.__celulas

    def mostra_celulas(self):
        dados_celulas = []
        for cell in self.__celulas_dao.get_all():
            dados_celulas.append([cell.codigo, cell.material, cell.comprimento, cell.diametro])
        self.__tela.exibe_celulas(dados_celulas)

    def altera_celula(self):
        self.mostra_celulas()
        codigo = self.__tela.coleta_codigo()
        try:
            for cell in self.__celulas_dao.get_all():
                if (cell.codigo == codigo):
                    novos_dados = self.__tela.coleta_dados()
                    cell.codigo = novos_dados["codigo"]
                    cell.material = novos_dados["material"]
                    cell.comprimento = novos_dados["comprimento"]
                    cell.diametro = novos_dados["diametro"]
                    self.__tela.imprime_mensagem("Dados atualizados com sucesso.\n")
        except:
            self.__tela.imprime_mensagem("Dados incorretos ou célula não cadastrada.")

    def cadastra_celula(self):
        try:
            dados = self.__tela.coleta_dados()

            for celula in self.__celulas_dao.get_all():
                if (celula.codigo == dados['codigo']):
                    self.__tela.imprime_mensagem(f"Célula experimental código {celula.codigo} já existe.")
                    return None

            celula = CelulaExperimental(codigo=dados['codigo'],
                                    material=dados['material'],
                                    comprimento=dados['comprimento'],
                                    diametro=dados['diametro'])
            self.__tela.imprime_mensagem(f"Nova célula experimental cadastrada (cód: {celula.codigo})\n")
            self.__celulas_dao.add(celula)
            return celula

        except KeyError as e:
            self.__tela.imprime_mensagem(f"Dado ausente: {e}")
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao cadastrar usuário: {e}")
    
    def deleta_celula(self):
        try:
            if self.__celulas_dao is not None:
                self.mostra_celulas()
            else:
                self.__tela.imprime_mensagem("Nenhuma célula cadastrada.")
            
            codigo_celula = self.__tela.coleta_codigo()
            for cell in self.__celulas_dao.get_all():
                if (cell.codigo == codigo_celula):
                    self.__celulas_dao.remove(cell.codigo)
                    self.__tela.imprime_mensagem(f"Célula experimental ({cell.codigo}) excluída com sucesso.")
                    return cell
        
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao tentar excluir a célula experimental {cell.codigo}.")
    
    def retorna_celula(self):
        self.mostra_celulas()
        codigo_celula = self.__tela.coleta_codigo()
        for celula in self.__celulas_dao.get_all():
            if (celula.codigo == codigo_celula):
                return celula
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
