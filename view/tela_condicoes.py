class TelaCondicoes():

    def mostra_menu(self):
        print("=== MENU CONDIÇÕES INICIAS E DE CONTORNO ===")
        print("1 - Cadastrar condições")
        print("2 - Retornar condições")
        print("3 - Listar condições")
        print("0 - Voltar")

        opcao = int(input("Escolha: "))
        return opcao
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)