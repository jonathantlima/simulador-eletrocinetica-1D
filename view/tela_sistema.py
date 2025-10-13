class TelaSistema():

    def menu(self):
        print(">>> SISTEMA DE SIMULAÇÃO DE EXPERIMENTOS COM ELETROCINÉTICA <<<")
        print("1 - Usuários")
        print("2 - Solos")
        print("3 - Espécies químicas")
        print("4 - Célula experimentais")
        print("5 - Condições iniciais e de contorno")
        print("6 - Simulação")
        print("0 - Finalizar")
    
        opcao = int(input("Selecione uma opção: "))
        return opcao
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)