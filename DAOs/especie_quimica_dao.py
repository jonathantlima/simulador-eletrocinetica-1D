from DAOs.dao import DAO
from modelo.especie_quimica import EspecieQuimica

#cada entidade terá uma classe dessa, implementação bem simples.
class EspecieQuimicaDAO(DAO):
    def __init__(self):
        super().__init__('especies.pkl')

    def add(self, especie: EspecieQuimica):
        if((especie is not None) and isinstance(especie, EspecieQuimica) and isinstance(especie.codigo, str)):
            super().add(especie.codigo, especie)

    def update(self, especie: EspecieQuimica):
        if((especie is not None) and isinstance(especie, EspecieQuimica) and isinstance(especie.codigo, str)):
            super().update(especie.codigo, especie)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
