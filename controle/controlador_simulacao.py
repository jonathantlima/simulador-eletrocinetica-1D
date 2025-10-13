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
                  4: self.gerar_relatorio,
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

        # VALIDA A POSSIBILIDADE DE CRIAR UMA SIMULAÇÃO
        try:
            usuarios = self.__controlador_sistema.controlador_usuario.usuarios
            solos = self.__controlador_sistema.controlador_solo.solos
            especies = self.__controlador_sistema.controlador_especie_quimica.especies
            celulas = self.__controlador_sistema.controlador_celula_experimental.celulas
            condicoes = self.__controlador_sistema.controlador_condicoes.condicoes

            entidades = {
                "Usuários": usuarios,
                "Solos": solos,
                "Espécies": especies,
                "Células": celulas,
                "Condições": condicoes
            }

            mensagens = []
            for nome_entidade, lista_entidade in entidades.items():
                if not lista_entidade:
                    mensagens.append(f"{nome_entidade} não cadastrados(as).")

            if mensagens:
                for msg in mensagens:
                    self.__tela.imprime_mensagem(msg)
                self.__tela.imprime_mensagem("Simulação abortada. Retornando...")
                self.retornar()
                return

        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao criar simulação: {e}")
        
        # coleta os dados elementares da simulação
        codigo_simulacao, duracao = self.__tela.coleta_dados()

        # DEFINE USUÁRIO
        try:
            # Verifica se há usuários cadastrados
            usuarios = self.__controlador_sistema.controlador_usuario.usuarios
            if not usuarios:
                self.__tela.imprime_mensagem("Nenhum usuário cadastrado. Simulação cancelada.")
                return

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
        try:
            solos = self.__controlador_sistema.controlador_solo.solos
            if not solos:
                self.__tela.imprime_mensagem("Nenhum solo cadastrado. Simulação cancelada.")
                return
            
            # Lista os solos cadastrados
            self.__controlador_sistema.controlador_solo.mostra_solos()

            solo = None
            while solo is None:
                codigo_solo = self.__tela.coleta_codigo_solo()
                solo = self.__controlador_sistema.controlador_solo.retorna_solo(codigo_solo)
                if solo is None:
                    self.__tela.imprime_mensagem("Código inválido. Tente novamente.")
            self.__tela.imprime_mensagem(f"Solo selecionado: {solo.codigo}\n")
        
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao selecionar solo: {e}")
            return

        # DEFINE A ESPÉCIE QUÍMICA QUE SERÁ SIMULADA
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


