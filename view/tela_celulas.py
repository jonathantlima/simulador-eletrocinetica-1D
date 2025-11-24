import FreeSimpleGUI as sg

class TelaCelulas():
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
            [sg.Text('---- CÉLULAS EXPERIMENTAIS ----', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar célula', "RD1", key='1')],
            [sg.Radio('Alterar célula', "RD1", key='2')],
            [sg.Radio('Listar células', "RD1", key='3')],
            [sg.Radio('Deletar célula', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de solos').Layout(layout)
    
    def coleta_dados(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS USUÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Código:', size=(20, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Material:', size=(20, 1)), sg.InputText('', key='material')],
            [sg.Text('Comprimento (cm): ', size=(20, 1)), sg.InputText('', key='comprimento')],
            [sg.Text('Diâmetro (cm):', size=(20, 1)), sg.InputText('', key='diametro')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Registro de solos').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        material = values['material']
        comprimento = float(values['comprimento'])
        diametro = float(values['diametro'])

        self.close()
        return {'codigo': codigo, 'material': material, 'comprimento': comprimento, 'diametro': diametro}

    def coleta_codigo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS DA CÉLULA ----------', font=("Courrier", 20))],
            [sg.Text('Código da célula:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de células').Layout(layout)
        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def exibe_celulas(self, cells, title="---Lista de Usuários---"):
        headings = ['Código', 'Material', 'Comprimento (cm)', 'Diâmetro (cm)']
        layout = [ [sg.Table(values=cells, headings=headings, key='-TABLE-',
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