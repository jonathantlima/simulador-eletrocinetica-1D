
class CondicoesDoProblema():

    def __init__(self,
                 codigo: str,
                 concentracao_inicial: float,
                 gradiente_eletrico: float,
                 gradiente_hidraulico: float,
                 concentracao_reservatorio: float
    ):
        if isinstance(codigo, str):
            self.__codigo = codigo
        if isinstance(concentracao_inicial, float):
            self.__concentracao_inicial = concentracao_inicial
        if isinstance(gradiente_eletrico, float):
            self.__gradiente_eletrico = gradiente_eletrico
        if isinstance(gradiente_hidraulico, float):
            self.__gradiente_hidraulico = gradiente_hidraulico
        if isinstance(concentracao_reservatorio, float):
            self.__concentracao_reservatorio = concentracao_reservatorio
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, str):
            self.__codigo = codigo

    @property
    def concentracao_inicial(self):
        return self.__concentracao_inicial
    
    @concentracao_inicial.setter
    def concentracao_inicial(self, concentracao: float):
        if isinstance(concentracao, float):
            self.__concentracao_inicial = concentracao
    
    @property
    def gradiente_eletrico(self):
        return self.__gradiente_eletrico
    
    @gradiente_eletrico.setter
    def gradiente_eletrico(self, grad_elet: float):
        if isinstance(grad_elet, float):
            self.__gradiente_eletrico = grad_elet
    
    @property
    def gradiente_hidraulico(self):
        return self.__gradiente_hidraulico
    
    @gradiente_hidraulico.setter
    def gradiente_hidraulico(self, grad_hidr: float):
        self.__gradiente_hidraulico = grad_hidr
    
    @property
    def concentracao_reservatorio(self):
        return self.__concentracao_reservatorio
    
    @concentracao_reservatorio.setter
    def concentracao_reservatorio(self, concentracao: float):
        if isinstance(concentracao, float):
            self.__concentracao_reservatorio = concentracao
