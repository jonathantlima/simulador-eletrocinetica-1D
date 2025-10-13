class TelaUsuario():

    def mostra_menu(self):
        print("=== MENU USUÁRIOS ===")
        print("1 - Cadastrar usuário")
        print("2 - Altera usuário")
        print("3 - Lista usuários")
        print("0 - Voltar")
        return int(input("Escolha: "))

    def coleta_dados(self):
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        departamento = input("Departamento: ")
        matricula = input("Matrícula: ")

        dados = {"nome": nome,
                 "email": email,
                 "telefone": telefone,
                 "departamento": departamento,
                 "matricula": matricula}

        return dados
    
    def coleta_matricula_usuario(self):
        matricula = input("Digite o código do usuário: ")
        return matricula
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)