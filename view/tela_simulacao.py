from numpy import arange
import matplotlib.pyplot as plt

class TelaSimulacao():

    def mostra_menu(self):
        print("=== MENU SIMULAÇÃO ===")
        print("1 - Criar simulação")
        print("2 - Listar simulações")
        print("3 - Plota resultados")
        print("4 - Gerar relatório")
        print("0 - Voltar")
        
        while True:
            try:
                escolha = int(input("Escolha: "))
                if escolha in [0, 1, 2, 3, 4]:
                    return escolha
                else:
                    print("Opção inválida. Escolha entre 0 e 4.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)
    
    def coleta_dados(self):
        print("--- Coleta de Dados para Simulação ---")
        codigo = input("Defina um código para a simulação (Ex.: EK01): ")
        while True:
            try:
                duracao = int(input("Defina a duração da simulação (horas): "))
                if duracao > 0:
                    break
                else:
                    print("A duração deve ser maior que zero.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
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
        try:
            vetor_espacial = arange(0, comprimento + incremento_espacial, incremento_espacial)
            vetor_temporal = arange(0, duracao + incremento_temporal, incremento_temporal)

            if C.shape[0] < m:
                raise ValueError("O valor de 'm' excede o número de linhas em 'C'.")

            for t in range(0, m, max(1, int(m / 5))):  # Evita divisão por zero
                plt.plot(vetor_espacial, C[t, :], label=f"{vetor_temporal[t]:.1f} h", lw=1.5)

            plt.xlabel("Distância (cm)")
            plt.ylabel("Concentração (mg/L)")
            plt.legend()
            plt.grid()
            plt.show()

        except Exception as e:
            print(f"Erro durante a plotagem: {e}")

