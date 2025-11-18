import FreeSimpleGUI as sg

class TelaSolo():
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
            [sg.Text('-------- SOLOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir solo', "RD1", key='1')],
            [sg.Radio('Alterar solo', "RD1", key='2')],
            [sg.Radio('Listar solos', "RD1", key='3')],
            [sg.Radio('Deletar solos', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de solos').Layout(layout)
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)

    def coleta_codigo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS DO SOLO ----------', font=("Courrier", 20))],
            [sg.Text('Código do solo:', size=(15, 1)), sg.InputText('', key='código')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de solos').Layout(layout)
        button, values = self.open()
        codigo = values['código']
        self.close()
        return {"código": codigo}
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values