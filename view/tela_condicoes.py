import FreeSimpleGUI as sg

class TelaCondicoes():
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
            [sg.Text('---- CONDIÇÕES INICIAIS E DE CONTORNO ----', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir condições', "RD1", key='1')],
            [sg.Radio('Alterar condições', "RD1", key='2')],
            [sg.Radio('Listar condições', "RD1", key='3')],
            [sg.Radio('Deletar condições', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de condições').Layout(layout)
    
    def coleta_dados(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-- DADOS CONDIÇÕES INICIAIS & CONTORNO --', font=("Helvica", 25))],
            [sg.Text('Código:', size=(30, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Concentração inicial (mg/L):', size=(30, 1)), sg.InputText('', key='concentracao_inicial')],
            [sg.Text('Gradiente elétrico (V/m):', size=(30, 1)), sg.InputText('', key='gradiente_eletrico')],
            [sg.Text('Gradiente hidráulico: ', size=(30, 1)), sg.InputText('', key='gradiente_hidraulico')],
            [sg.Text('Concentração do reservatório (mg/L):', size=(30, 1)), sg.InputText('', key='concentracao_reservatorio')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Cadastro de Espécies').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        concentracao_inicial = float(values['concentracao_inicial'])
        gradiente_eletrico = float(values['gradiente_eletrico'])
        gradiente_hidraulico = float(values['gradiente_hidraulico'])
        concentracao_reservatorio = float(values['concentracao_reservatorio'])

        self.close()
        return {"codigo": codigo,
                'concentracao_inicial': concentracao_inicial,
                'gradiente_eletrico': gradiente_eletrico,
                'gradiente_hidraulico': gradiente_hidraulico,
                'concentracao_reservatorio': concentracao_reservatorio}

    def coleta_codigo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--- DADOS DAS CONDIÇÕES INICIAIS E DE CONTORNO ---', font=("Courrier", 20))],
            [sg.Text('Código das condições:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de condições iniciais e de contorno').Layout(layout)
        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def exibe_condicoes(self, condicoes, title="-Lista de Condições Iniciais e de Contorno-"):
        headings = ['Código', 'Concentração inicial (mg/L)', 'Gradiente elétrico (V/m)', 'Gradiente hidráulico (m/m)', 'Concentração no reservatório (mg/L)']
        layout = [ [sg.Table(values=condicoes, headings=headings, key='-TABLE-',
                             auto_size_columns=True, display_row_numbers=False, 
                             justification='right', enable_events=True,
                             alternating_row_color='lightblue')],
                              [sg.Button('Ok'), sg.Button('Cancel')] ]
        event, values = sg.Window(title, layout).read(close=True)

        if event == "Ok":
            try:
                return values["-LISTBOX-"][0]
            except:
                return None
        else:
            return None
    
    def imprime_mensagem(self, mensagem):
        sg.popup("", mensagem)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values