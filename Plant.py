from math import sqrt as math_sqrt
from Species import *

class Plant:
    def __init__(self,
                 especie            : Species,
                 localizacao_coords : tuple[float, float],
                 ano_plantacao      : int):
        self.__especie          = especie
        self.localizacao_coords = localizacao_coords
        self.__ano_plantacao    = ano_plantacao

    @property
    def especie(self) -> Species:
        return self.__especie

    @property
    def ano_plantacao(self) -> int:
        return self.__ano_plantacao

    def area_de_ocupacao_circular(self) -> float:
        return self.__especie.area_de_ocupacao_circular()

    def idade(self, ano_a_verificar) -> int:
        # perguntar aos profs qual a melhor forma de implementar
        if ano_a_verificar < self.__ano_plantacao:
           print(
                f"A planta {self.especie.nome} "
                f"localizada em {self.localizacao_coords} "
                f"só foi plantada em {self.__ano_plantacao}."
            )
            return 0
        return ano_a_verificar - self.__ano_plantacao

    def pertence_a_area_de_ocupacao_plantacao(self, dadas_as_coordenadas) -> bool:
        distancia = math_sqrt(
            (self.localizacao_coords[0] - dadas_as_coordenadas[0])**2 +
            (self.localizacao_coords[1] - dadas_as_coordenadas[1])**2
        )
        return distancia < self.__especie.raio_max

    def __str__(self) -> str:
        return f"Nome da espécie da planta: {self.__especie.nome}\n"      \
               f"Localização GPS: {self.localizacao_coords}\n"            \
               f"Ano de plantação: {self.__ano_plantacao}\n"




if __name__ == "__main__":
    """
    Este if permite correr o ficheiro como um
    script independente e as instruções abaixo
    não serão executas se o ficheiro for importado
    de outro ficheiro. Deste modo podemos testar a
    classe de forma isolada.
    """

    species_1 = Species(
        nome                = "castanheiro",
        tipo_folhagem       = "caduca",
        produz_fruto        = True,
        tipo_planta         = "árvore",
        raio_max            = 8.1,
        num_medio_anos_vida = 100
    )

    plant_1 = Plant(
        especie            = species_1,
        localizacao_coords = (10.0, 5.0),
        ano_plantacao      = 2020
    )


    print("plant_1.especie.nome:", plant_1.especie.nome)
    print("plant_1.especie.tipo_folhagem:", plant_1.especie.tipo_folhagem)

    print("plant_1.localizacao_coords:", plant_1.localizacao_coords)
    print("plant_1.ano_plantacao:", plant_1.ano_plantacao)
    print("plant_1.area_de_ocupacao_circular():", plant_1.area_de_ocupacao_circular())

    print("plant_1.idade(ano_a_verificar=2022):", plant_1.idade(ano_a_verificar=2022))
    print("plant_1.idade(ano_a_verificar=1904):", plant_1.idade(ano_a_verificar=1904))

    print("plant_1.pertence_a_area_de_ocupacao_plantacao(dadas_as_coordenadas=(12.0, 6.0)):", plant_1.pertence_a_area_de_ocupacao_plantacao(dadas_as_coordenadas=(12.0, 6.0)))

    print(plant_1)
