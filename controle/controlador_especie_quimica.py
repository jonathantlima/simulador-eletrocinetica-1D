from view.tela_especie_quimica import TelaEspecieQuimica
from modelo.especie_quimica import EspecieQuimica
from modelo.anion import Anion
from modelo.cation import Cation


class ControladorEspecieQuimica():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaEspecieQuimica()
        self.__especies = []
    
    def abre_tela(self):
        opcoes = {1: self.cadastra_especie_quimica,
                  2: self.retorna_especie,
                  3: self.mostra_especies,
                  0: self.retornar
        }
    
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                self.__tela.imprime_mensagem("Opção inválida.")
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def especies(self):
        return self.__especies
    
    def mostra_especies(self):
        self.__tela.imprime_mensagem("--- LISTA DE ESPÉCIES QUÍMICAS CADASTRADAS ---")
        for especie in self.__especies:
            self.__tela.imprime_mensagem(f"Código: {especie.codigo} - Fórmula: {especie.formula} - Coef. Difusão: {especie.coeficiente_de_difusao:.3f}")
            
    def retorna_especie(self, codigo):
        for especie in self.__especies:
            if (especie.codigo == codigo):
                return especie
        else:
            self.__tela.imprime_mensagem("Espécia não cadastrada ou código incorreto.\n")
    
    def cadastra_especie_quimica(self):
        self.__tela.imprime_mensagem("--- Nova espécie química ---")
        codigo = input("Digite o código da espécie química: ")
        nome = input("Nome do composto: ")
        formula = input("Fórmula química: ")
        funcao = input("Função química: ")
        valencia = int(input("Valência: "))
        coeficiente_de_distribuicao = float(input("Coeficiente de distribuição: "))
        coeficiente_de_difusao = float(input("Coeficiente de difusão (cm²/h): "))

        if valencia > 0:
            especie = Cation(codigo=codigo,
                             nome=nome,
                             formula=formula,
                             funcao=funcao,
                             valencia=valencia,
                             coeficiente_de_distribuicao=coeficiente_de_distribuicao,
                             coeficiente_de_difusao=coeficiente_de_difusao)
            self.__tela.imprime_mensagem(f"Nova espécie cadastrada com sucesso (cód: {codigo}).\n")

        elif valencia < 0:
            especie = Anion(codigo=codigo,
                            nome=nome,
                            formula=formula,
                            funcao=funcao,
                            valencia=valencia,
                            coeficiente_de_distribuicao=coeficiente_de_distribuicao,
                            coeficiente_de_difusao=coeficiente_de_difusao)
            self.__tela.imprime_mensagem(f"Nova espécie cadastrada com sucesso (cód: {codigo}).\n")
        else:
            self.__tela.imprime_mensagem("Valência inválida. Espécie não cadastrada.\n")
        
        self.__especies.append(especie)
        return especie
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()