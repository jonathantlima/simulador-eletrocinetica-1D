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
    
    def coleta_dados(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS USUÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Código:', size=(20, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Tipo:', size=(20, 1)), sg.InputText('', key='tipo')],
            [sg.Text('Origem: ', size=(20, 1)), sg.InputText('', key='origem')],
            [sg.Text('Cor:', size=(20, 1)), sg.InputText('', key='cor')],
            [sg.Text('Porosidade: ', size=(20, 1)), sg.InputText('', key='porosidade')],
            [sg.Text('Massa específica seca', size=(20, 1)), sg.InputText('', key='massa_especifica_seca')],
            [sg.Text('Condutividade hidráulica', size=(20, 1)), sg.InputText('', key='condutividade_hidraulica')],
            [sg.Text('Permeabilidade eletro-osmótica', size=(20, 1)), sg.InputText('', key='permeabilidade_eletroosmotica')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Cadastro de Solos').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        tipo = values['tipo'].capitalize()
        origem = values['origem']
        cor = values['cor']
        porosidade = float(values['porosidade'])
        massa_especifica_seca = float(values['massa_especifica_seca'])
        condutividade_hidraulica = float(values['condutividade_hidraulica'])
        permeabilidade_eletroosmotica = float(values['permeabilidade_eletroosmotica'])

        self.close()
        return {"codigo": codigo,
                'tipo': tipo,
                'origem': origem,
                'cor': cor,
                'porosidade': porosidade,
                'massa_especifica_seca': massa_especifica_seca,
                'condutividade_hidraulica': condutividade_hidraulica,
                'permeabilidade_eletroosmotica': permeabilidade_eletroosmotica}
    
    def imprime_mensagem(self, mensagem):
        sg.popup("", mensagem, title='Atenção')

    def coleta_codigo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS DO SOLO ----------', font=("Courrier", 20))],
            [sg.Text('Código do solo:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de solos').Layout(layout)
        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo
    
    def exibe_solos(self, solos, title="---Lista de Solos---"):
        layout = [ [sg.Listbox(solos, size=(60, 12), key="-LISTBOX-", horizontal_scroll=True)],
              [sg.Button('Ok'), sg.Button('Cancel')] ]
        event, values = sg.Window(title, layout).read(close=True)

        if event == "Ok":
            try:
                return values["-LISTBOX-"][0]
            except:
                return None
        else:
            return None
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values