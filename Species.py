class Species:
    def __init__(self,
                 nome: str,
                 tipo_folhagem: str,
                 produz_fruto: bool,
                 tipo_planta: str,
                 raio_max: float,
                 num_medio_anos_vida: int):
        self.__nome = nome
        self.__tipo_folhagem = tipo_folhagem
        self.__produz_fruto = produz_fruto
        self.__tipo_planta = tipo_planta
        self.__raio_max = raio_max
        self.__num_medio_anos_vida = num_medio_anos_vida

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def tipo_folhagem(self) -> str:
        return self.__tipo_folhagem

    @property
    def produz_fruto(self) -> bool:
        return self.__produz_fruto

    @property
    def tipo_planta(self) -> str:
        return self.__tipo_planta

    @property
    def raio_max(self) -> float:
        return self.__raio_max

    @property
    def num_medio_anos_vida(self) -> int:
        return self.__num_medio_anos_vida

    @property
    def area_de_ocupacao_circular(self) -> float:
        return 3.14 * (self.__raio_max ** 2)
