from modelo.especie_quimica import EspecieQuimica

class Cation(EspecieQuimica):

    def __init__(self,
                 codigo: str,
                 nome: str,
                 formula: str,
                 funcao: str,
                 valencia: int,
                 coeficiente_de_distribuicao: float,
                 coeficiente_de_difusao: float
    ):
        super().__init__(codigo,
                         nome,
                         formula,
                         funcao,
                         valencia,
                         coeficiente_de_distribuicao,
                         coeficiente_de_difusao
        )
