from view.tela_simulacao import TelaSimulacao
from modelo.usuario import Usuario
from modelo.simulacao import Simulacao
from DAOs.simulacao_dao import SimulacaoDAO


class ControladorSimulacao():

    def __init__(self, controlador_sistema):
        self.__tela = TelaSimulacao()
        self.__simulacoes_dao = SimulacaoDAO()
        self.__controlador_sistema = controlador_sistema
        # Adicionado para manter a lista de simulações em memória,
        # pois o DAO armazena em disco, mas o código original usa uma lista em memória para listagem e plotagem.
        self.__simulacoes = list(self.__simulacoes_dao.get_all())
    
    def abre_tela(self):
        opcoes = {1: self.cria_simulacao,
                  2: self.lista_simulacoes,
                  3: self.plota_grafico,
                  4: self.gerar_relatorio,
                  5: self.deleta_simulacao,
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
    
    def cria_simulacao(self):
        # 1. Validação corrigida: verifica se as coleções (retornadas por .get_all()) estão vazias.
        #    Assume-se que as propriedades nos outros controladores retornam o objeto DAO.
        try:
            usuarios = list(self.__controlador_sistema.controlador_usuario.usuarios_dao.get_all())
            solos = list(self.__controlador_sistema.controlador_solo.solos_dao.get_all())
            especies = list(self.__controlador_sistema.controlador_especie_quimica.especies_dao.get_all())
            celulas = list(self.__controlador_sistema.controlador_celula_experimental.celulas_dao.get_all())
            condicoes = list(self.__controlador_sistema.controlador_condicoes.condicoes_dao.get_all())
        except AttributeError as e:
            self.__tela.imprime_mensagem(f"Erro de atributo ao acessar DAO: {e}. Verifique se as propriedades nos controladores retornam o objeto DAO.")
            return

        if not (usuarios and solos and especies and celulas and condicoes):
            self.__tela.imprime_mensagem('Alguns objetos ainda não foram gerados. Certifique-se de cadastrar: Usuário, Solo, Espécie Química, Célula Experimental e Condições.')
            self.retornar()
            return

        # 2. Correção do desempacotamento: espera-se que coleta_codigo_e_duracao retorne 2 valores.
        try:
            codigo_simulacao, duracao = self.__tela.coleta_codigo_e_duracao()
        except Exception as e:
            self.__tela.imprime_mensagem(f"Falha ao coletar dados: {e}")
            return # Adicionado return para evitar prosseguir com dados incompletos

        # DEFINE USUÁRIO
        try:
            # Lista usuários
            self.__controlador_sistema.controlador_usuario.lista_usuarios()

            # Loop para garantir matrícula válida
            usuario = None
            while usuario is None:
                matricula = self.__tela.coleta_matricula_usuario()
                usuario = self.__controlador_sistema.controlador_usuario.retorna_usuario(matricula)
                if usuario is None:
                    self.__tela.imprime_mensagem("Matrícula inválida. Tente novamente.")
            self.__tela.imprime_mensagem(f"Usuário selecionado: {usuario.nome}\n")

        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao selecionar usuário: {e}")
            return

        # DEFINE O SOLO QUE SERÁ USADO
        solo = self.__controlador_sistema.controlador_solo.retorna_solo()

        # DEFINE A ESPÉCIE QUÍMICA QUE SERÁ SIMULADA
        especie_quimica = self.__controlador_sistema.controlador_especie_quimica.retorna_especie()

        # DEFINE A CÉLULA EXPERIMENTAL QUE SERÁ SIMULADA
        celula_experimental = self.__controlador_sistema.controlador_celula_experimental.retorna_celula()

        # DEFINE AS CONDIÇÕES INICIAIS E DE CONTORNO DO PROBLEMA
        condicao = self.__controlador_sistema.controlador_condicoes.retorna_condicao()

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
        
        # Salva no DAO e adiciona à lista em memória
        self.__simulacoes_dao.add(simulacao)
        self.__simulacoes.append(simulacao)

        self.__tela.imprime_mensagem(f"Simulação {codigo_simulacao} criada com sucesso!")
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
    
    def gerar_relatorio(self):

        # Será usada para armazenar as durações das simulações e calcular estatísticas
        duracao_dict = dict()
        usuarios_dict = dict()
        solos_dict = dict()
        celulas_dict = dict()
        especies_dict = dict()
        concentracao_inicial = dict()   # coluna, flushing

        for simulacao in self.__simulacoes:
            duracao_dict[simulacao.duracao] = duracao_dict.get(simulacao.duracao, 0) + 1
            usuarios_dict[simulacao.usuario.matricula] = usuarios_dict.get(simulacao.usuario.matricula, 0) + 1
            solos_dict[simulacao.solo.codigo] = solos_dict.get(simulacao.solo.codigo, 0) + 1
            celulas_dict[simulacao.celula_experimental.codigo] = celulas_dict.get(simulacao.celula_experimental.codigo, 0) + 1
            especies_dict[simulacao.especie_quimica.codigo] = especies_dict.get(simulacao.especie_quimica.codigo, 0) + 1
            concentracao_inicial[simulacao.condicoes_do_problema.concentracao_inicial] = concentracao_inicial.get(simulacao.condicoes_do_problema.concentracao_inicial, 0) + 1
        
        # Início do conteúdo do relatório
        linhas = []
        linhas.append("************ RELATÓRIO DE SIMULAÇÕES ***************\n")

        def formatar_secao(titulo, dicionario, unidade=None):
            linhas.append(f"\n--- {titulo} ---\n")
            for chave, valor in dicionario.items():
                unidade_str = f" {unidade}" if unidade else ""
                linhas.append(f"{str(chave)}: {valor} simulação(ões){unidade_str}")
            linhas.append("\n")

        # Adiciona todas as seções ao relatório
        formatar_secao("Duração das Simulações", duracao_dict, "s")
        formatar_secao("Simulações por Usuário (matrícula)", usuarios_dict)
        formatar_secao("Simulações por Solo", solos_dict)
        formatar_secao("Simulações por Célula Experimental", celulas_dict)
        formatar_secao("Simulações por Espécie Química", especies_dict)
        formatar_secao("Concentração Inicial (mg/L)", concentracao_inicial)

        # Salvando o arquivo
        caminho_arquivo = "relatorio_simulacoes.txt"
        try:
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                for linha in linhas:
                    f.write(linha + "\n")
            print(f"Relatório gerado com sucesso em: {caminho_arquivo}")
        except Exception as e:
            print(f"Erro ao gerar relatório: {e}")
    
    def deleta_simulacao(self):
        self.lista_simulacoes()
        codigo = self.__tela.coleta_codigo_simulacao()
        simulacao_encontrada = None
        for simulacao in self.__simulacoes:
            if simulacao.codigo == codigo:
                simulacao_encontrada = simulacao
                break
        
        if simulacao_encontrada:
            self.__simulacoes_dao.remove(codigo)
            self.__simulacoes.remove(simulacao_encontrada)
            self.__tela.imprime_mensagem(f"Simulação {codigo} excluída com sucesso.")
        else:
            self.__tela.imprime_mensagem("Simulação não cadastrada ou código incorreto.")