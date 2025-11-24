import FreeSimpleGUI as sg

class TelaEspecieQuimica():
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
            [sg.Text('---- ESPÉCIES QUÍMICAS ----', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir espécie', "RD1", key='1')],
            [sg.Radio('Alterar espécie', "RD1", key='2')],
            [sg.Radio('Listar espécie', "RD1", key='3')],
            [sg.Radio('Deletar espécie', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de espécies').Layout(layout)

    def coleta_dados(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('---- DADOS ESPÉCIES QUÍMICAS ----', font=("Helvica", 25))],
            [sg.Text('Código:', size=(20, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Nome:', size=(20, 1)), sg.InputText('', key='nome')],
            [sg.Text('Fórmula:', size=(20, 1)), sg.InputText('', key='formula')],
            [sg.Text('Função: ', size=(20, 1)), sg.InputText('', key='funcao')],
            [sg.Text('Valência:', size=(20, 1)), sg.InputText('', key='valencia')],
            [sg.Text('Coeficiente de distribuição (kg/L): ', size=(20, 1)), sg.InputText('', key='coeficiente_de_distribuicao')],
            [sg.Text('Coeficiente de difusão (m²/h)', size=(20, 1)), sg.InputText('', key='coeficiente_de_difusao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Cadastro de Espécies').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        nome = values['nome']
        formula = values['formula']
        funcao = values['funcao']
        valencia = int(values['valencia'])
        coeficiente_de_distribuicao = float(values['coeficiente_de_distribuicao'])
        coeficiente_de_difusao = float(values['coeficiente_de_difusao'])

        self.close()
        return {"codigo": codigo,
                'nome': nome,
                'formula': formula,
                'funcao': funcao,
                'valencia': valencia,
                'coeficiente_de_distribuicao': coeficiente_de_distribuicao,
                'coeficiente_de_difusao': coeficiente_de_difusao}

    def coleta_codigo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('---- DADOS DA ESPÉCIE QUÍMICA ----', font=("Courrier", 20))],
            [sg.Text('Código da espécie:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de espécies').Layout(layout)
        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def exibe_especies(self, especies, title="Lista de Espécies Químicas"):
        headings = ['Código', 'Nome', 'Fórmula', 'Função', 'Valência', 'Coeficiente de distribuição (kg/L)', 'Coeficiente de difusão (m²/h)']
        layout = [ [sg.Table(values=especies, headings=headings, key='-TABLE-', 
                             auto_size_columns=True, display_row_numbers=False, 
                             justification='right', enable_events=True)],
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