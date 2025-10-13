from modelo.solo import Solo

class Silte(Solo):

    def __init__(self,
                 codigo: str,
                 tipo: str,
                 origem: str,
                 cor: str,
                 porosidade: float,
                 massa_especifica_seca: float,
                 condutividade_hidraulica: float,
                 permeabilidade_eletroosmotica: float
    ):
        super().__init__(codigo,
                         tipo,
                         origem,
                         cor,
                         porosidade,
                         massa_especifica_seca,
                         condutividade_hidraulica,
                         permeabilidade_eletroosmotica
        )
