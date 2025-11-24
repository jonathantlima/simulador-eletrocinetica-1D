class EspecieQuimicaDuplicada(Exception):
    """Exceção lançada quando uma espécie química está duplicada."""

    def __init__(self, mensagem="A espécie química já existe."):
        super().__init__(mensagem)
