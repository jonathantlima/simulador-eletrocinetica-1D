from DAOs.dao import DAO
from modelo.condicoes import CondicoesDoProblema

#cada entidade terá uma classe dessa, implementação bem simples.
class CondicoesDoProbelamDAO(DAO):
    def __init__(self):
        super().__init__('condicoes.pkl')

    def add(self, condicoes: CondicoesDoProblema):
        if((condicoes is not None) and isinstance(condicoes, CondicoesDoProblema) and isinstance(condicoes.codigo, str)):
            super().add(condicoes.codigo, condicoes)

    def update(self, condicoes: CondicoesDoProblema):
        if((condicoes is not None) and isinstance(condicoes, CondicoesDoProblema) and isinstance(condicoes.codigo, str)):
            super().update(condicoes.codigo, condicoes)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
