from numpy import arange, zeros
from modelo.solo import Solo
from modelo.especie_quimica import EspecieQuimica
from modelo.condicoes import CondicoesDoProblema
from modelo.celula_experimental import CelulaExperimental
from exceptions.especie_quimica_exception import EspecieQuimicaMalConfigurada

class Simulacao():

    def __init__(self,
                 usuario,
                 codigo: str,
                 duracao: int,
                 solo,
                 especie_quimica,
                 celula_experimental,
                 condicoes_do_problema):
        self.__usuario = usuario
        self.__codigo = codigo
        self.__duracao = duracao
        self.__solo = solo
        self.__especie_quimica = especie_quimica
        self.__celula_experimental = celula_experimental
        self.__condicoes_do_problema = condicoes_do_problema
        self.__C = None
        self.__incremento_temporal = 0.0625
        self.__incremento_espacial = 0.125
    
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, str):
            self.__codigo = codigo
    
    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, duracao):
        if isinstance(duracao, int):
            self.__duracao = duracao
    
    @property
    def solo(self):
        return self.__solo
    
    @solo.setter
    def solo(self, solo):
        if isinstance(solo, Solo):
            self.__solo = solo
    
    @property
    def especie_quimica(self):
        return self.__especie_quimica
    
    @especie_quimica.setter
    def especie_quimica(self, especie):
        if isinstance(especie, EspecieQuimica):
            self.__especie_quimica = especie
    
    @property
    def celula_experimental(self):
        return self.__celula_experimental
    
    @celula_experimental.setter
    def celula_experimental(self, celula):
        if isinstance(celula, CelulaExperimental):
            self.__celula_experimental = celula
    
    @property
    def condicoes_do_problema(self):
        return self.__condicoes_do_problema
    
    @condicoes_do_problema.setter
    def condicoes_do_problema(self, condicoes):
        if isinstance(condicoes, CondicoesDoProblema):
            self.__condicoes_do_problema = condicoes
    
    @property
    def concentracoes(self):
        return self.__C
    
    # Calcula os coeficientes que serão usados na modelagem
    def calcula_coeficientes(self):

        coeficiente_de_retardamento = 1. + (self.__solo.massa_especifica_seca / self.__solo.porosidade) \
            * self.__especie_quimica.coeficiente_de_distribuicao
        
        p = (self.__especie_quimica.coeficiente_de_difusao / coeficiente_de_retardamento) \
            * (self.__incremento_temporal / self.__incremento_espacial ** 2)
        
        if self.__especie_quimica.valencia > 0:   # cátion
            r = ((self.__especie_quimica.coeficiente_migracao_ionica + self.__solo.permeabilidade_eletroosmotica) 
                 * ((self.__incremento_temporal * self.__condicoes_do_problema.gradiente_eletrico) 
                    / (coeficiente_de_retardamento * 2 * self.__incremento_espacial)))
            
        elif self.__especie_quimica.valencia < 0:   # ânion
            r = ((self.__especie_quimica.coeficiente_migracao_ionica - self.__solo.permeabilidade_eletroosmotica) 
                 * ((self.__incremento_temporal * self.__condicoes_do_problema.gradiente_eletrico) 
                    / (coeficiente_de_retardamento * 2 * self.__incremento_espacial)))
        
        else:
            raise EspecieQuimicaMalConfigurada()
        
        s = ((self.__solo.condutividade_hidraulica * self.__incremento_temporal 
              * self.__condicoes_do_problema.gradiente_hidraulico) 
              / (coeficiente_de_retardamento * 2 * self.__incremento_espacial))
        
        return p, r, s
    
    def cria_mesh(self):

        # discretiza espacialmente, em 1D
        vetor_espacial = arange(0, self.__celula_experimental.comprimento +
                                 self.__incremento_espacial, self.__incremento_espacial)
        
        # discretização do tempo
        vetor_temporal = arange(0, self.__duracao + self.__incremento_temporal, self.__incremento_temporal)

        # calcula a quantidade de linhas e colunas da matriz de concentrações
        n = len(vetor_espacial)  # nº de colunas
        m = len(vetor_temporal)  # nº de linhas

        self.__C = zeros((m,n))

        self.__C[0, :] = self.__condicoes_do_problema.concentracao_inicial
        self.__C[:, 0] = self.__condicoes_do_problema.concentracao_reservatorio

        return n, m, self.__C
    
    def execucao(self):

        p, r, s = self.calcula_coeficientes()
        n, m, self.__C = self.cria_mesh()

        
        for i in range(1, m):
            for j in range(1, n-1):
                self.__C[i,j] = self.__C[i-1, j] * (1 - 2*p) \
                                + self.__C[i-1, j+1] * (p + r + s) \
                                + self.__C[i-1, j-1] * (p - r - s)

            # Condição de contorno no final
            self.__C[i, n-1] = self.__C[i, n-2]
        
        return self.__C

