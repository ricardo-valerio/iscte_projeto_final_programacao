class Species:
    def __init__(self, nome, tipo_folhagem, produz_fruto, tipo_planta, raio_max, num_medio_anos_vida):
        self.__nome = nome
        self.__tipo_folhagem = tipo_folhagem
        self.__produz_fruto = produz_fruto
        self.__tipo_planta = tipo_planta
        self.__raio_max = raio_max
        self.__num_medio_anos_vida = num_medio_anos_vida

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo_folhagem(self):
        return self.__tipo_folhagem

    @property
    def produz_fruto(self):
        return self.__produz_fruto

    @property
    def tipo_planta(self):
        return self.__tipo_planta

    @property
    def raio_max(self):
        return self.__raio_max

    @property
    def num_medio_anos_vida(self):
        return self.__num_medio_anos_vida

    @property
    def area_de_ocupacao_circular(self):
        return 3.14 * (self.__raio_max ** 2)

