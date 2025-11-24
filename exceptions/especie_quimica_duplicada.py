class EspecieQuimicaDuplicada(Exception):
    """Exceção lançada quando uma espécie química está duplicada."""

    def __init__(self, mensagem="A espécie química já existe."):
        super().__init__(mensagem)

class EspecieQuimicaMalConfigurada(Exception):
    """Exceção lançada quando uma espécie química está mal configurada."""
    def __init__(self, mensagem="A espécie química está mal configurada."):
        super().__init__(mensagem)

