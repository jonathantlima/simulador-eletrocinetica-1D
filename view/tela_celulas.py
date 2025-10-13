class TelaCelulas():

    def mostra_menu(self):
        print("=== MENU CÉLULAS EXPERIMENTAIS ===")
        print("1 - Cadastrar célula")
        print("2 - Retornar célula")
        print("3 - Lista células")
        print("0 - Voltar")

        opcao = int(input("Escolha: "))
        return opcao
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)