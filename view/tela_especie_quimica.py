import FreeSimpleGUI as sg

class TelaEspecieQuimica():

    def mostra_menu(self):
        print("=== MENU ESPÉCIES QUÍMICAS ===")
        print("1 - Cadastrar espécie")
        print("2 - Retornar espécie")
        print("3 - Lista espécies")
        print("0 - Voltar")

        opcao = int(input("Escolha: "))
        return opcao
    
    def imprime_mensagem(self, mensagem):
        sg.popup("", mensagem)