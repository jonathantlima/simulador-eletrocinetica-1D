from view.tela_usuario import TelaUsuario
from modelo.usuario import Usuario

class ControladorUsuario():

    def __init__(self, controlador_sistema):
        self.__tela = TelaUsuario()
        self.__usuarios = []
        self.__controlador_sistema = controlador_sistema
    
    def abre_tela(self):
        opcoes = {1: self.novo_usuario,
                  2: self.altera_usuario,
                  3: self.lista_usuarios,
                  0: self.retornar
        }
    
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                self.__tela.imprime_mensagem("Opção inválida.")
    
    def novo_usuario(self):
        dados = self.__tela.coleta_dados()
        novo_usuario = Usuario(dados["nome"],
                               dados["email"],
                               dados["telefone"],
                               dados["departamento"],
                               dados["matricula"])
        print(f"Novo usuário cadastrado (Dept. {dados["departamento"]})\n")
        
        self.__usuarios.append(novo_usuario)
        return novo_usuario
    
    def altera_usuario(self):
        self.lista_usuarios()
        matricula = self.__tela.coleta_matricula_usuario()
        for usuario in self.__usuarios:
            if (usuario.matricula == matricula):
                novos_dados = self.__tela.coleta_dados()
                usuario.nome = novos_dados["nome"]
                usuario.email = novos_dados["email"]
                usuario.telefone = novos_dados["telefone"]
                usuario.departamento = novos_dados["departamento"]
                usuario.matricula = novos_dados["matricula"]
            self.__tela.imprime_mensagem("Dados atualizados com sucesso.\n")
        else:
            self.__tela.imprime_mensagem("Usuário não cadastrado ou matrícula incorreta.\n")
        
        return usuario

    def retorna_usuario(self, matricula):
        for usuario in self.__usuarios:
            if (usuario.matricula == matricula):
                return usuario
        else:
            print("Usuário não cadastrado ou matrícula incorreta.\n")

    def lista_usuarios(self):
        print("Lista de Usuários")
        print("--- Nome --- Matrícula ---")
        for user in self.__usuarios:
            print(user.nome, user.matricula)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()