from abc import ABC, abstractmethod

class Solo(ABC):

    @abstractmethod
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
        if isinstance(codigo, str):
            self.__codigo = codigo
        if isinstance(tipo, str):
            self.__tipo = tipo
        if isinstance(origem, str):
            self.__origem = origem
        if isinstance(cor, str):
            self.__cor = cor
        if isinstance(porosidade, float):
            self.__porosidade = porosidade
        if isinstance(massa_especifica_seca, float):
            self.__massa_especifica_seca = massa_especifica_seca
        if isinstance(condutividade_hidraulica, float):
            self.__condutividade_hidraulica = condutividade_hidraulica
        if isinstance(permeabilidade_eletroosmotica, float):
            self.__permeabilidade_eletroosmotica = permeabilidade_eletroosmotica
        super().__init__()
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: str):
        if isinstance(codigo, str):
            self.__codigo = codigo

    @property
    def tipo(self) -> str:
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo
    
    @property
    def origem(self) -> str:
        return self.__origem
    
    @origem.setter
    def origem(self, origem: str):
        if isinstance(origem, str):
            self.__origem = origem
    
    @property
    def cor(self) -> str:
        return self.__cor
    
    @cor.setter
    def cor(self, cor: str):
        if isinstance(cor, str):
            self.__cor = cor
    
    @property
    def porosidade(self) -> float:
        return self.__porosidade
    
    @porosidade.setter
    def porosidade(self, porosidade: float):
        if isinstance(porosidade, float):
            self.__porosidade = porosidade
    
    @property
    def massa_especifica_seca(self) -> float:
        return self.__massa_especifica_seca
    
    @massa_especifica_seca.setter
    def massa_especifica_seca(self, massa_especifica_seca: float):
        if isinstance(massa_especifica_seca, float):
            self.__massa_especifica_seca = massa_especifica_seca
    
    @property
    def condutividade_hidraulica(self) -> float:
        return self.__condutividade_hidraulica
    
    @condutividade_hidraulica.setter
    def condutividade_hidraulica(self, condutividade_hidraulica: float):
        if isinstance(condutividade_hidraulica, float):
            self.__condutividade_hidraulica = condutividade_hidraulica
    
    @property
    def permeabilidade_eletroosmotica(self) -> float:
        return self.__permeabilidade_eletroosmotica
    
    @permeabilidade_eletroosmotica.setter
    def permeabilidade_eletroosmotica(self, permeabilidade_eletroosmotica: float):
        if isinstance(permeabilidade_eletroosmotica, float):
            self.__permeabilidade_eletroosmotica = permeabilidade_eletroosmotica
