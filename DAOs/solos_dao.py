from DAOs.dao import DAO
from modelo.solo import Solo

#cada entidade terá uma classe dessa, implementação bem simples.
class SoloDAO(DAO):
    def __init__(self):
        super().__init__('solos.pkl')

    def add(self, solo: Solo):
        if((solo is not None) and isinstance(solo, Solo) and isinstance(solo.codigo, str)):
            super().add(solo.codigo, solo)

    def update(self, solo: Solo):
        if((solo is not None) and isinstance(solo, Solo) and isinstance(solo.codigo, str)):
            super().update(solo.codigo, solo)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
