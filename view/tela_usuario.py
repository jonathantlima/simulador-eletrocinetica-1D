import FreeSimpleGUI as sg

class TelaUsuario():
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
            [sg.Text('-------- USUÁRIOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar usuário', "RD1", key='1')],
            [sg.Radio('Alterar usuário', "RD1", key='2')],
            [sg.Radio('Listar usuários', "RD1", key='3')],
            [sg.Radio('Deletar usuário', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro de solos').Layout(layout)

    def coleta_dados(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS USUÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(20, 1)), sg.InputText('', key='nome')],
            [sg.Text('email:', size=(20, 1)), sg.InputText('', key='email')],
            [sg.Text('Telefone: ', size=(20, 1)), sg.InputText('', key='telefone')],
            [sg.Text('Departamento:', size=(20, 1)), sg.InputText('', key='departamento')],
            [sg.Text('Matrícula: ', size=(20, 1)), sg.InputText('', key='matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema de Usuários').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        email = values['email']
        telefone = values['telefone']
        departamento = values['departamento']
        matricula = values['matricula']

        self.close()
        return {"nome": nome, "email": email, 'telefone': telefone, "departamento": departamento, "matricula": matricula}
    
    
    def __coleta_campo_str(self, nome_campo, permitir_numerico=False):
        while True:
            valor = input(f"{nome_campo}: ").strip()

            if not valor:
                print(f"{nome_campo} não pode ser vazio.")
            elif not permitir_numerico and valor.isnumeric():
                print(f"{nome_campo} não pode conter apenas números.")
            else:
                return valor
    
    '''def coleta_matricula_usuario(self):
        matricula = input("Digite o código do usuário: ")
        return matricula'''
    
    def coleta_matricula_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS DO USUÁRIO ----------', font=("Courrier", 20))],
            [sg.Text('Matrícula do usuário:', size=(15, 1)), sg.InputText('', key='matrícula')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Registro/atualização de usuário').Layout(layout)
        button, values = self.open()
        matricula = values['matrícula']
        self.close()
        return matricula
    
    def mostra_usuarios(self, users, title="---Lista de Usuários---"):
        headings = ['Nome', 'E-mail', 'Telefone', 'Departamento', 'Matrícula']
        layout = [ [sg.Table(values=users, headings=headings, key='-TABLE-',
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
        sg.popup("", mensagem, title="Atenção")
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values