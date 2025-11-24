class UsuarioDuplicado(Exception):
    """Exceção lançada quando um usuário está duplicado."""

    def __init__(self, mensagem="O usuário já existe."):
        super().__init__(mensagem)