class TelaUsuario():

    def mostra_menu(self):
        print("=== MENU USUÁRIOS ===")
        print("1 - Cadastrar usuário")
        print("2 - Alterar usuário")
        print("3 - Listar usuários")
        print("0 - Voltar")
        
        while True:
            try:
                escolha = int(input("Escolha: "))
                if escolha in [0, 1, 2, 3]:
                    return escolha
                else:
                    print("Opção inválida. Escolha entre 0 e 3.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def coleta_dados(self):
        print("--- Cadastro de Usuário ---")
        dados = {}

        dados["nome"] = self.__coleta_campo_str("Nome")
        dados["email"] = self.__coleta_campo_str("E-mail")
        dados["telefone"] = self.__coleta_campo_str("Telefone", permitir_numerico=True)
        dados["departamento"] = self.__coleta_campo_str("Departamento")
        dados["matricula"] = self.__coleta_campo_str("Matrícula", permitir_numerico=True)

        return dados

    def __coleta_campo_str(self, nome_campo, permitir_numerico=False):
        while True:
            valor = input(f"{nome_campo}: ").strip()

            if not valor:
                print(f"{nome_campo} não pode ser vazio.")
            elif not permitir_numerico and valor.isnumeric():
                print(f"{nome_campo} não pode conter apenas números.")
            else:
                return valor
    
    def coleta_matricula_usuario(self):
        matricula = input("Digite o código do usuário: ")
        return matricula
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)