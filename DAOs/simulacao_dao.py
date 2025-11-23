from DAOs.dao import DAO
from modelo.simulacao import Simulacao

#cada entidade terá uma classe dessa, implementação bem simples.
class SimulacaoDAO(DAO):
    def __init__(self):
        super().__init__('simulacoes.pkl')

    def add(self, simulacao: Simulacao):
        if((simulacao is not None) and isinstance(simulacao, Simulacao) and isinstance(simulacao.codigo, str)):
            super().add(simulacao.codigo, simulacao)

    def update(self, simulacao: Simulacao):
        if((simulacao is not None) and isinstance(simulacao, Simulacao) and isinstance(simulacao.codigo, str)):
            super().update(simulacao.codigo, simulacao)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)