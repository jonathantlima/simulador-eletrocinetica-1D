from view.tela_condicoes import TelaCondicoes
from modelo.condicoes import CondicoesDoProblema
from DAOs.condicoes_dao import CondicoesDoProbelamDAO


class ControladorCondicoes():

    def __init__(self, controlador_sistema):
        self.__tela = TelaCondicoes()
        self.__controlador_sistema = controlador_sistema
        self.__condicoes_dao = CondicoesDoProbelamDAO()
    
    @property
    def condicoes_dao(self):
        return self.__condicoes_dao
    
    def abre_tela(self):
        opcoes = {1: self.cadastra_condicoes,
                  2: self.altera_condicoes,
                  3: self.mostra_condicoes,
                  4: self.deleta_condicoes,
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
        condicoes = []
        for condicao in self.__condicoes_dao.get_all():
            condicoes.append([condicao.codigo, condicao.concentracao_inicial, condicao.gradiente_eletrico, condicao.gradiente_hidraulico, condicao.concentracao_reservatorio])
        self.__tela.exibe_condicoes(condicoes)
        return condicoes
    
    def altera_condicoes(self):
        self.mostra_condicoes()
        codigo = self.__tela.coleta_codigo()
        try:
            for condicao in self.__condicoes_dao.get_all():
                if (condicao.codigo == codigo):
                    novos_dados = self.__tela.coleta_dados()
                    condicao.codigo = novos_dados["codigo"]
                    condicao.concentracao_inicial = novos_dados["concentracao_inicial"]
                    condicao.gradiente_eletrico = novos_dados["gradiente_eletrico"]
                    condicao.gradiente_hidraulico = novos_dados["gradiente_hidraulico"]
                    condicao.concentracao_reservatorio = novos_dados['concentracao_reservatorio']
                    self.__tela.imprime_mensagem("Dados atualizados com sucesso.\n")
        except:
            self.__tela.imprime_mensagem("Dados incorretos ou condições iniciais e de contorno não cadastradas.")
    
    def cadastra_condicoes(self):
        try:
            dados = self.__tela.coleta_dados()

            for condicao in self.__condicoes_dao.get_all():
                if (condicao.codigo == dados['codigo']):
                    self.__tela.imprime_mensagem(f"Condições inicial e de contorno código {condicao.codigo} já existe.")
                    return None

            condicao = CondicoesDoProblema(dados['codigo'],
                                       dados['concentracao_inicial'],
                                       dados['gradiente_eletrico'],
                                       dados['gradiente_hidraulico'],
                                       dados['concentracao_reservatorio'])
            self.__tela.imprime_mensagem(f"Novas condições iniciais e de contorno cadastradas (cód: {condicao.codigo})\n")
            self.__condicoes_dao.add(condicao)
            return condicao

        except KeyError as e:
            self.__tela.imprime_mensagem(f"Dado ausente: {e}")
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao cadastrar condições inicial e de contorno: {e}")
    
    def deleta_condicoes(self):
        try:
            if self.__condicoes_dao is not None:
                self.mostra_condicoes()
            else:
                self.__tela.imprime_mensagem("Nenhuma condicao cadastrada.")
            
            codigo_condicao = self.__tela.coleta_codigo()
            for condicao in self.__condicoes_dao.get_all():
                if (condicao.codigo == codigo_condicao):
                    self.__condicoes_dao.remove(condicao.codigo)
                    self.__tela.imprime_mensagem(f"Condições iniciais e de contorno ({condicao.codigo}) excluídas com sucesso.")
                    return condicao
        
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao tentar excluir a célula experimental {condicao.codigo}.")
    
    def retorna_condicao(self):
        self.mostra_condicoes()
        codigo_condicao = self.__tela.coleta_codigo()
        for condicao in self.__condicoes_dao.get_all():
            if (condicao.codigo == codigo_condicao):
                return condicao
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()