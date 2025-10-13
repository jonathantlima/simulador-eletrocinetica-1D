from view.tela_celulas import TelaCelulas
from modelo.celula_experimental import CelulaExperimental


class ControladorCelulaExperimental():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaCelulas()
        self.__celulas = []
    
    def abre_tela(self):
        opcoes = {1: self.cadastra_celula,
                  2: self.retorna_celula,
                  3: self.mostra_celulas,
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
    def celulas(self):
        return self.__celulas

    def mostra_celulas(self):
        if self.__celulas:
            self.__tela.imprime_mensagem("--- Lista de Células Experimentais ---")
            print("--- Código --- Comprimento (cm) ---")
            for celula in self.__celulas:
                self.__tela.imprime_mensagem(f"--- {celula.codigo} --- {celula.comprimento}")

    def retorna_celula(self, codigo):
        for celula in self.__celulas:
            if (celula.codigo == codigo):
                return celula
        else:
            print("Célula não cadastrada ou código incorreto.\n")

    def cadastra_celula(self):
        print("--- Nova Célula Experimental ---")
        codigo = input("Código da nova célula: ")
        material = input("Material de fabricação: ")
        comprimento = float(input("Comprimento da célula (cm): "))
        diametro = float(input("Diâmetro da célula (cm): "))

        celula = CelulaExperimental(codigo=codigo,
                                    material=material,
                                    comprimento=comprimento,
                                    diametro=diametro)
        print(f"Nova célula experimental cadastrada (cód: {codigo})\n")        
        self.__celulas.append(celula)
        return celula
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
