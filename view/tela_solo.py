class TelaSolo():

    def mostra_menu(self):
        print("=== MENU SOLOS ===")
        print("1 - Cadastrar solo")
        print("2 - Retornar solo")
        print("3 - Mostra solos")
        print("0 - Voltar")
        return int(input("Escolha: "))
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)