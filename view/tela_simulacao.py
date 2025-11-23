from numpy import arange
import FreeSimpleGUI as sg
import matplotlib.pyplot as plt

class TelaSimulacao():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def mostra_menu(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def init_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Text('---- SIMULAÇÕES ----', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Criar simulacao', "RD1", key='1')],
            [sg.Radio('Listar simulacao', "RD1", key='2')],
            [sg.Radio('Plotar gráfico', "RD1", key='3')],
            [sg.Radio('Gerar relatório', "RD1", key='4')],
            [sg.Radio('Deletar simulacao', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de simulações').Layout(layout)
    
    def imprime_mensagem(self, mensagem):
        sg.popup("", mensagem)
    
    def coleta_codigo_e_duracao(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- DADOS DA SIMULAÇÃO ---', font=("Courrier", 20))],
            [sg.Text('Código da simulação:', size=(25, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Duração da simulação (horas):', size=(25, 1)), sg.InputText('', key='duracao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de simulações').Layout(layout)
        button, values = self.open()
        codigo = values['codigo']
        duracao = int(values['duracao'])
        self.close()
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

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values