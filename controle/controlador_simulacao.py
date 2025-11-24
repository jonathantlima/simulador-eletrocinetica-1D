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
        self.__simulacoes_dao = SimulacaoDAO()
    
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
        
        for simulacao in self.__simulacoes_dao.get_all():
                if (simulacao.codigo == codigo_simulacao):
                    self.__tela.imprime_mensagem(f"Simulação código {simulacao.codigo} já existe.")
                    return None

        # DEFINE USUÁRIO
        usuario = self.__controlador_sistema.controlador_usuario.retorna_usuario()

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

        self.__tela.imprime_mensagem(f"Simulação {codigo_simulacao} criada com sucesso!")
        return simulacao
    
    @property
    def simulacoes_dao(self):
        return self.__simulacoes_dao
    
    def lista_simulacoes(self):
        simulacoes = []
        for simulacao in self.__simulacoes_dao.get_all():
            simulacoes.append([simulacao.usuario.matricula, simulacao.codigo, simulacao.duracao, simulacao.solo.codigo, simulacao.especie_quimica.codigo, simulacao.celula_experimental.codigo, simulacao.condicoes_do_problema.codigo])
        self.__tela.exibe_simulacoes(simulacoes)
    
    def plota_grafico(self):
        self.lista_simulacoes()
        codigo = self.__tela.coleta_codigo()
        for simulacao in self.__simulacoes_dao.get_all():
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
        """
        Gera um relatório de estatísticas das simulações cadastradas.
        O relatório inclui:
        1. O usuário que realizou mais simulações.
        2. A célula experimental mais simulada.
        3. O solo mais usado.
        4. A condição mais usada (usando o código da condição).
        5. Estatísticas descritivas da duração das simulações.
        """
        simulacoes = list(self.__simulacoes_dao.get_all())
        
        if not simulacoes:
            self.__tela.imprime_mensagem("Não há simulações cadastradas para gerar o relatório.")
            return

        # 1. Coleta de dados
        duracoes = []
        usuarios_contagem = {}
        solos_contagem = {}
        celulas_contagem = {}
        condicoes_contagem = {}

        for simulacao in simulacoes:
            # Assume-se que 'duracao' é um número (float ou int)
            duracoes.append(simulacao.duracao)
            
            # Contagem de entidades (usando a matrícula/código conforme o usuário informou)
            usuario_id = simulacao.usuario.matricula
            celula_id = simulacao.celula_experimental.codigo
            solo_id = simulacao.solo.codigo
            # A condição é acessada via condicoes_do_problema, e o código é o identificador
            condicao_id = simulacao.condicoes_do_problema.codigo 

            usuarios_contagem[usuario_id] = usuarios_contagem.get(usuario_id, 0) + 1
            celulas_contagem[celula_id] = celulas_contagem.get(celula_id, 0) + 1
            solos_contagem[solo_id] = solos_contagem.get(solo_id, 0) + 1
            condicoes_contagem[condicao_id] = condicoes_contagem.get(condicao_id, 0) + 1

        # 2. Funções Auxiliares para Análise
        def encontrar_mais_usado(contagem_dict):
            if not contagem_dict:
                return "N/A", 0
            mais_usado = max(contagem_dict, key=contagem_dict.get)
            contagem = contagem_dict[mais_usado]
            return mais_usado, contagem

        # 3. Cálculo das Estatísticas Descritivas (usando numpy para robustez)
        try:
            import numpy as np
            estatisticas = {
                "Total de Simulações": len(duracoes),
                "Média (h)": np.mean(duracoes),
                "Mediana (h)": np.median(duracoes),
                "Desvio Padrão (h)": np.std(duracoes),
                "Mínimo (h)": np.min(duracoes),
                "Máximo (h)": np.max(duracoes),
            }
        except ImportError:
            # Fallback simples caso numpy não esteja disponível (embora seja padrão no ambiente)
            estatisticas = {
                "Total de Simulações": len(duracoes),
                "Média (h)": sum(duracoes) / len(duracoes) if duracoes else 0,
                "Mínimo (h)": min(duracoes) if duracoes else 0,
                "Máximo (h)": max(duracoes) if duracoes else 0,
            }
            self.__tela.imprime_mensagem("Aviso: numpy não encontrado. Estatísticas descritivas limitadas.")


        # 4. Geração do Conteúdo do Relatório
        linhas = []
        linhas.append("**************************************************")
        linhas.append("************ RELATÓRIO DE ESTATÍSTICAS ***********")
        linhas.append("**************************************************\n")

        # Seção 1: Entidades Mais Usadas
        linhas.append("--- ENTIDADES MAIS UTILIZADAS ---\n")
        
        usuario_mais_ativo, contagem_usuario = encontrar_mais_usado(usuarios_contagem)
        linhas.append(f"1. Usuário mais ativo (Matrícula): {usuario_mais_ativo} ({contagem_usuario} simulação(ões))")

        celula_mais_usada, contagem_celula = encontrar_mais_usado(celulas_contagem)
        linhas.append(f"2. Célula Experimental mais simulada (Código): {celula_mais_usada} ({contagem_celula} simulação(ões))")

        solo_mais_usado, contagem_solo = encontrar_mais_usado(solos_contagem)
        linhas.append(f"3. Solo mais usado (Código): {solo_mais_usado} ({contagem_solo} simulação(ões))")

        condicao_mais_usada, contagem_condicao = encontrar_mais_usado(condicoes_contagem)
        linhas.append(f"4. Condição mais usada (Código): {condicao_mais_usada} ({contagem_condicao} simulação(ões))\n")

        # Seção 2: Estatísticas Descritivas da Duração
        linhas.append("--- ESTATÍSTICAS DESCRITIVAS DA DURAÇÃO (em horas) ---\n")
        for chave, valor in estatisticas.items():
            # Formata o valor para 2 casas decimais, exceto para o total
            valor_formatado = f"{valor:.2f}" if isinstance(valor, (float, np.float64)) else str(valor)
            linhas.append(f"- {chave}: {valor_formatado}")
        
        linhas.append("\n**************************************************")

        # 5. Salvando o arquivo
        caminho_arquivo = "relatorio_simulacoes.txt"
        try:
            # O arquivo será salvo no diretório do projeto (simulador-eletrocinetica-1D)
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                f.write("\n".join(linhas))
            
            self.__tela.imprime_mensagem(f"Relatório gerado com sucesso em: {caminho_arquivo}")
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao gerar relatório: {e}")
    
    def deleta_simulacao(self):
        try:
            self.lista_simulacoes()
            codigo = self.__tela.coleta_codigo()
            for simulacao in self.__simulacoes_dao.get_all():
                if (simulacao.codigo == codigo):
                    self.__simulacoes_dao.remove(simulacao.codigo)
                    self.__tela.imprime_mensagem(f"Simulação {simulacao.codigo} excluída com sucesso.")
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro {e} ao tentar excluir a simulação {codigo}.")
