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
            try:
                opcao = self.__tela.mostra_menu()
                if opcao in opcoes:
                    try:
                        opcoes[opcao]()
                    except Exception as e:
                        self.__tela.imprime_mensagem(f"Erro ao executar a opção: {e}")
                else:
                    self.__tela.imprime_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela.imprime_mensagem(f"Erro inesperado no menu: {e}")
    
    def novo_usuario(self):
        try:
            dados = self.__tela.coleta_dados()

            # Verifica se já existe usuário com a mesma matrícula
            if any(u.matricula == dados["matricula"] for u in self.__usuarios):
                self.__tela.imprime_mensagem("Erro: Matrícula já cadastrada.\n")
                return

            novo_usuario = Usuario(
                dados["nome"],
                dados["email"],
                dados["telefone"],
                dados["departamento"],
                dados["matricula"]
            )
            self.__usuarios.append(novo_usuario)
            print(f"Novo usuário cadastrado (Dept. {dados['departamento']})\n")
            return novo_usuario

        except KeyError as e:
            self.__tela.imprime_mensagem(f"Dado ausente: {e}")
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao cadastrar usuário: {e}")
    
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