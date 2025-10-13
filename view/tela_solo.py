class TelaSolo():

    def mostra_menu(self):
        print("=== MENU SOLOS ===")
        print("1 - Cadastrar solo")
        print("2 - Retornar solo")
        print("3 - Mostra solos")
        print("4 - Deleta solo")
        print("0 - Voltar")
        return int(input("Escolha: "))
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)

    def coleta_codigo(self):
        codigo = input("Digite o código do solo: ")
        return codigo