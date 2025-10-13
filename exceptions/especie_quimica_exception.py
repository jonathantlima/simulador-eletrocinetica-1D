class EspecieQuimicaMalConfigurada(Exception):
    """Exceção lançada quando uma espécie química está mal configurada."""

    def __init__(self, mensagem="A espécie química não foi corretamente definida."):
        super().__init__(mensagem)
