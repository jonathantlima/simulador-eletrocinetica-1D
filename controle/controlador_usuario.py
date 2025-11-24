from view.tela_usuario import TelaUsuario
from modelo.usuario import Usuario
from DAOs.usuarios_dao import UsuarioDAO
from exceptions.usuario_exception import UsuarioDuplicado


class ControladorUsuario():

    def __init__(self, controlador_sistema):
        self.__tela = TelaUsuario()
        self.__usuarios_dao = UsuarioDAO()
        self.__controlador_sistema = controlador_sistema

    @property
    def usuarios_dao(self):
        return self.__usuarios_dao

    def abre_tela(self):
        opcoes = {1: self.novo_usuario,
                  2: self.altera_usuario,
                  3: self.lista_usuarios,
                  4: self.deleta_usuario,
                  0: self.retornar
                  }

        while True:
            try:
                opcao = self.__tela.mostra_menu()
                if opcao in opcoes:
                    try:
                        opcoes[opcao]()
                    except Exception as e:
                        self.__tela.imprime_mensagem(
                            f"Erro ao executar a opção: {e}")
                else:
                    self.__tela.imprime_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela.imprime_mensagem(f"Erro inesperado no menu: {e}")

    def novo_usuario(self):
        try:
            dados = self.__tela.coleta_dados()

            for usuario in self.__usuarios_dao.get_all():
                if (usuario.matricula == dados['matricula']):
                    raise UsuarioDuplicado()
                    return None

            novo_usuario = Usuario(
                dados["nome"],
                dados["email"],
                dados["telefone"],
                dados["departamento"],
                dados["matricula"]
            )
            #self.__usuarios.append(novo_usuario)
            self.__usuarios_dao.add(novo_usuario)
            self.__tela.imprime_mensagem(f"Novo usuário cadastrado (Dept. {dados['departamento']})\n")
            return novo_usuario

        except KeyError as e:
            self.__tela.imprime_mensagem(f"Dado ausente: {e}")
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao cadastrar usuário: {e}")

    def altera_usuario(self):
        self.lista_usuarios()
        matricula = self.__tela.coleta_matricula_usuario()
        try:
            for usuario in self.__usuarios_dao.get_all():
                if (usuario.matricula == matricula):
                    novos_dados = self.__tela.coleta_dados()
                    usuario.nome = novos_dados["nome"]
                    usuario.email = novos_dados["email"]
                    usuario.telefone = novos_dados["telefone"]
                    usuario.departamento = novos_dados["departamento"]
                    usuario.matricula = novos_dados["matricula"]
                    self.__tela.imprime_mensagem("Dados atualizados com sucesso.\n")
        except:
            self.__tela.imprime_mensagem("Dados incorretos ou usuário não cadastrado.")

        return usuario

    def retorna_usuario(self):
        try:
            self.lista_usuarios()
            matricula = self.__tela.coleta_matricula_usuario()
            for usuario in self.__usuarios_dao.get_all():
                if (usuario.matricula == matricula):
                    return usuario
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro {e} ao tentar retornar usuário de matrícula {matricula}.")
    
    def lista_usuarios(self):
        dados_usuarios = []
        for usuario in self.__usuarios_dao.get_all():
            dados_usuarios.append([usuario.matricula, usuario.nome, usuario.email, usuario.telefone, usuario.departamento])
        self.__tela.mostra_usuarios(dados_usuarios)
        return dados_usuarios

    def deleta_usuario(self):
        self.lista_usuarios()
        matricula = self.__tela.coleta_matricula_usuario()
        usuario = self.retorna_usuario(matricula)

        if (usuario is not None):
            self.__usuarios_dao.remove(usuario.matricula)
            self.lista_usuarios()
        else:
            self.__tela.imprime_mensagem(
                "Usuário não cadastrado ou matrícula incorreta.\n")

    def retornar(self):
        self.__controlador_sistema.abre_tela()
