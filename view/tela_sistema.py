import FreeSimpleGUI as sg

class TelaSistema():
    def __init__(self):
        self.__window = None
        self.init_components()
    
    def menu(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def close(self):
        self.__window.Close()
    
    def init_components(self):
        #sg.theme_previewer()
        texto='''
EKSTC: Esse sistema permite criar simulações para o
transporte de contaminantes em solos, considerando
a condição de fluxo acoplado
            '''
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
            [sg.Text(texto, font=("Courier", 15))],
            [sg.Text('Escolha sua opção', font=("Helvica", 18))],
            [sg.Radio('Usuários',"RD1", key='1')],
            [sg.Radio('Solos',"RD1", key='2')],
            [sg.Radio('Espécies químicas',"RD1", key='3')],
            [sg.Radio('Células experimentais',"RD1", key='4')],
            [sg.Radio('Condições iniciais e de contorno',"RD1", key='5')],
            [sg.Radio('Simulação',"RD1", key='6')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema EKSTC').Layout(layout)
    
    def imprime_mensagem(self, mensagem):
        sg.popup("", mensagem)