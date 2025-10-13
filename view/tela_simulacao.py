from numpy import arange
import matplotlib.pyplot as plt

class TelaSimulacao():

    def mostra_menu(self):
        print("=== MENU SIMULAÇÃO ===")
        print("1 - Criar simulação")
        print("2 - Listar simulações")
        print("3 - Plota resultados")
        print("0 - Voltar")
        return int(input("Escolha: "))
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)
    
    def coleta_dados(self):
        print("--- Coleta de Dados para Simulação ---")
        codigo = input("Defina um código para a simulação (Ex.: EK01): ")
        duracao = int(input("Defina a duracao da simulação (horas): "))

        return codigo, duracao
    
    def coleta_codigo_solo(self):
        codigo = input("Digite o código do solo para simulação: ")
        return codigo
    
    def coleta_codigo_especie_quimica(self):
        codigo = input("Digite o código da espécie química: ")
        return codigo
    
    def coleta_codigo_celula(self):
        codigo = input("Digite o código da célula experimental deseja: ")
        return codigo
    
    def coleta_dados_condicoes(self):
        concentracao_inicial = float(input("Defina a concetração inicial (mg/L) da espécie química no solo: "))
        gradiente_eletrico = float(input("Defina o gradiente elétrico da simulação: "))
        gradiente_hidraulico = float(input("Defina o gradiente hidráulico da simulação: "))
        concentracao_reservatorio = float(input("Defina a concentração no reservatório da célula: "))

        return {"concentracao_inicial": concentracao_inicial,
                "gradiente_eletrico": gradiente_eletrico,
                "gradiente_hidraulico": gradiente_hidraulico,
                "concentracao_reservatorio": concentracao_reservatorio}

    def coleta_codigo_condicoes(self):
        codigo = input("Digite o código da condição de simulação: ")
        return codigo
    
    def coleta_codigo_simulacao(self):
        codigo = input("Digite o código da simulação desejada: ")
        return codigo
    
    def coleta_matricula_usuario(self):
        matricula = input("Digite a matricula do usuário: ")
        return matricula
    
    def plotagem(self, m, incremento_espacial, incremento_temporal, comprimento, duracao, C):
        vetor_espacial = arange(0, comprimento + incremento_espacial, incremento_espacial)
        vetor_temporal = arange(0, duracao + incremento_temporal, incremento_temporal)
        for t in range(0, m, int(m/5)):
            plt.plot(vetor_espacial, C[t, :], label=f"{vetor_temporal[t]:.1f} h", lw=1.5)

        plt.xlabel("Distância (cm)")
        plt.ylabel("Concentração (mg/L)")
        plt.legend()
        plt.grid()
        plt.show()

