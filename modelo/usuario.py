
class Usuario:

    def __init__(self, nome: str, email: str, telefone: str, departamento: str, matricula: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(email, str):
            self.__email = email
        if isinstance(telefone, str):
            self.__telefone = telefone
        if isinstance(departamento, str):
            self.__departamento = departamento
        if isinstance(matricula, str):
            self.__matricula = matricula

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        if isinstance(email, str):
            self.__email = email

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone

    @property
    def departamento(self) -> str:
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento: str):
        if isinstance(departamento, str):
            self.__departamento = departamento

    @property
    def matricula(self) -> str:
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: str):
        if isinstance(matricula, str):
            self.__matricula = matricula
