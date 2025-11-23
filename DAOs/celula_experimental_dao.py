from DAOs.dao import DAO
from modelo.celula_experimental import CelulaExperimental

#cada entidade terá uma classe dessa, implementação bem simples.
class CelulaExperimentalDAO(DAO):
    def __init__(self):
        super().__init__('celulas.pkl')

    def add(self, celula: CelulaExperimental):
        if((celula is not None) and isinstance(celula, CelulaExperimental) and isinstance(celula.codigo, str)):
            super().add(celula.codigo, celula)

    def update(self, celula: CelulaExperimental):
        if((celula is not None) and isinstance(celula, CelulaExperimental) and isinstance(celula.codigo, str)):
            super().update(celula.codigo, celula)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
