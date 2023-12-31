from InputDataValidator import InputDataValidator
from math import pi as math_pi

class Species:
    def __init__(self,
                 nome                : str,
                 tipo_folhagem       : str,
                 produz_fruto        : bool,
                 tipo_planta         : str,
                 raio_max            : float,
                 num_medio_anos_vida : int):
        self.__nome                = InputDataValidator.get_valid_species_name(input_text=nome)
        self.__tipo_folhagem       = InputDataValidator.get_valid_follage_type(species_name=self.__nome, input_text=tipo_folhagem)
        self.__produz_fruto        = bool(produz_fruto)
        self.__tipo_planta         = InputDataValidator.get_valid_plant_type(species_name=self.__nome, input_text=tipo_planta)
        self.__raio_max            = InputDataValidator.get_valid_positive_radius(species_name=self.__nome, input_value=raio_max)
        self.__num_medio_anos_vida = InputDataValidator.get_valid_positive_avg_life(species_name=self.__nome, input_value=num_medio_anos_vida)


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


    def area_de_ocupacao_circular(self) -> None:
        return round(math_pi * (self.__raio_max ** 2), 2)


    def __str__(self) -> str:
        return f"\nNome da espécie: {self.__nome}\n"                         \
               f"Tipo de planta: {self.__tipo_planta}\n"                     \
               f"Tipo de folhagem: {self.__tipo_folhagem}\n"                 \
               f"Produz fruto?: {self.__produz_fruto}\n"                     \
               f"Raio máximo de ocupação: {self.__raio_max}\n"               \
               f"Número médio de anos de vida: {self.__num_medio_anos_vida}\n"


    def __eq__(self, other) -> bool:
        return isinstance(other, Species) and self.__nome == other.__nome




if __name__ == "__main__":
    """
    Este if permite correr o ficheiro como um
    script independente e as instruções abaixo
    não serão executadas se o ficheiro for importado
    de outro ficheiro. Deste modo podemos testar a
    classe de forma isolada.
    """

    species_1 = Species(
        nome                = "castanheiro",
        tipo_folhagem       = "caduca",
        produz_fruto        = True,
        tipo_planta         = "erva",
        raio_max            = 8.1,
        num_medio_anos_vida = 100
    )

    species_2 = Species("Camomila", "semicaduca", False, "árvore", "eoi", "coiso")
    species_3 = Species("", "pesistent", True, "árvore", 3.1, 100)
    species_4 = Species("cedro", "perenee", False, "árvore", 1.5, 80)

    print(species_1.nome)
    print(species_1.tipo_folhagem)
    print(species_1.produz_fruto)
    print(species_1.tipo_planta)
    print(species_1.raio_max)
    print(species_1.num_medio_anos_vida)

    print(species_1.area_de_ocupacao_circular())
    print(species_2.area_de_ocupacao_circular())
    print(species_3.area_de_ocupacao_circular())

    print(species_1)
    print(species_2)
    print(species_3)

    print("species_1 == species_2:", species_1 == species_2)

