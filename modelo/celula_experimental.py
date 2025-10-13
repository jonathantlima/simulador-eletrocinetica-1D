class CelulaExperimental:

    def __init__(self, codigo: str, material: str, comprimento: float, diametro: float):
        if isinstance(codigo, str):
            self.__codigo = codigo
        if isinstance(material, str):
            self.__material = material
        if isinstance(comprimento, float):
            self.__comprimento = comprimento
        if isinstance(diametro, float):
            self.__diametro = diametro
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: str):
        if isinstance(codigo, str):
            self.__codigo = codigo   

    @property
    def material(self) -> str:
        return self.__material
    
    @material.setter
    def material(self, material: str):
        if isinstance(material, str):
            self.__material = material
    
    @property
    def comprimento(self) -> float:
        return self.__comprimento
    
    @comprimento.setter
    def comprimento(self, comprimento: float):
        if isinstance(comprimento, float):
            self.__comprimento = comprimento
    
    @property
    def diametro(self) -> float:
        return self.__diametro
    
    @diametro.setter
    def diametro(self, diametro: float):
        if isinstance(diametro, float):
            self.__diametro = diametro
