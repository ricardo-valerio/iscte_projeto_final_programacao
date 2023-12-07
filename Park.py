from InputDataValidator import InputDataValidator
from Species import Species
from Plant import Plant
from math import sqrt as math_sqrt

class Park:
    def __init__(self, name: str, largura: float, comprimento: float):
        self.__name = name
        self.__largura = InputDataValidator.get_valid_park_height(park_name=self.__name, input_value=largura)
        self.__comprimento = InputDataValidator.get_valid_park_width(park_name=self.__name, input_value=comprimento)
        self.__plants = list()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def largura(self) -> float:
        return self.__largura

    @property
    def comprimento(self) -> float:
        return self.__comprimento

    @property
    def planting_area(self) -> float:
        return self.__largura * self.__comprimento

    @property
    def plants(self) -> list[Plant, ..., Plant]:
        return self.__plants


    def add_plant(self, planta_a_adicionar, success_prints_are_silenced=False) -> None:
        """
            A razão pela qual não juntei as duas condições abaixo num único if
            foi para poder fazer print das mensagens específicas, caso uma
            delas não se verifique verdadeira.
        """
        # verificar se localização está dentro dos limites do parque
        if self.is_within_park_boundaries(plant_to_add=planta_a_adicionar):
            # Verificar se há espaço antes de adicionar
            if self.is_there_space_available_for_the_plant(planta_a_adicionar):
                # verificar se localização está ocupada antes de adicionar
                if not self.is_location_occupied_by_another_plant(at_coords=planta_a_adicionar.localizacao_coords):
                    if not self.is_there_plant_area_intersection(plant_to_add=planta_a_adicionar):
                        self.__plants.append(planta_a_adicionar)
                        if not success_prints_are_silenced:
                            print("\n✅ Planta adicionada ao parque com sucesso.")
                    else:
                        print("\n❌ Não foi possível adicionar a planta pois existia sobreposição com outra planta.")
                else:
                    print("\n❌ Não foi possível adicionar a planta pois a localização já se encontra ocupada.")
            else:
                print("\n❌ Não há espaço suficiente para adicionar a planta.")
        else:
            print("\n❌ Localização da planta não está dentro dos limites do parque.")


    def remove_plant(self, plant_location) -> None:
        for plant in self.__plants:
            if plant.localizacao_coords == plant_location:
                self.__plants.remove(plant)
                print("\n✅ Planta removida com sucesso.")
                return
        print("\n❌ Não foi encontrada qualquer planta na localização especificada.")


    def list_plants(self) -> None:
        if self.is_empty():
            print("\nℹ️ O parque não tem plantas.")
            return

        for plant in self.plants:
            print(plant)


    def is_empty(self) -> bool:
        """
        função helper para ajudar a verificar se o parque tem ou não plantas
        """
        return len(self.plants) == 0


    def total_area_occupied(self) -> float:
        total_area = 0
        for plant in self.__plants:
            total_area += plant.area_de_ocupacao_circular()

        return total_area


    def available_planting_area(self) -> float:
        return self.planting_area - self.total_area_occupied()


    def is_within_park_boundaries(self, plant_to_add):
        return (plant_to_add.localizacao_coords[0] + plant_to_add.especie.raio_max < self.largura and \
                plant_to_add.localizacao_coords[1] + plant_to_add.especie.raio_max < self.comprimento) and \
               (plant_to_add.localizacao_coords[0] - plant_to_add.especie.raio_max > 0 and \
                plant_to_add.localizacao_coords[1] - plant_to_add.especie.raio_max > 0)


    def is_there_space_available_for_the_plant(self, plant) -> bool:
        return self.available_planting_area() >= plant.area_de_ocupacao_circular()


    def is_there_plant_area_intersection(self, plant_to_add) -> bool:
        for plant in self.plants:
            distance_between_them = math_sqrt(
                (plant_to_add.localizacao_coords[0] - plant.localizacao_coords[0])**2 +
                (plant_to_add.localizacao_coords[1] - plant.localizacao_coords[1])**2
            )
            if distance_between_them < (plant_to_add.especie.raio_max + plant.especie.raio_max):
                return True
        return False


    def is_location_occupied_by_another_plant(self, at_coords) -> bool:
        for plant in self.__plants:
            if plant.pertence_a_area_de_ocupacao_plantacao(dadas_as_coordenadas=at_coords):
                return True
        return False


    def average_plant_age(self, year) -> float:
        if self.is_empty():
            print("\nℹ️ O parque não tem plantas.")
            return 0

        total_age = 0
        for plant in self.__plants:
            total_age += plant.idade(ano_a_verificar=year)

        return round(total_age / len(self.__plants), 2)


    def get_unique_species_list(self) -> list[str, ..., str]:
        # return list(set(plant.species for plant in self.__plants))
        lista_de_especies = list()
        for planta in self.__plants:
            lista_de_especies.append(planta.especie.nome)

        # https://datagy.io/python-count-unique-values-list/
        # 1º set() converte a lista para set (conjunto) - que
        # seguindo a teoria matemática de conjuntos elimina elementos repetidos
        # e 2º list() converte novamente para o tipo list
        return list(set(lista_de_especies))


    def num_of_unique_species(self) -> int:
        return len(self.get_unique_species_list())


    def display_plants_sorted_by_species(self) -> None:
        # https://docs.python.org/3.11/howto/sorting.html
        sorted_plants = sorted(self.__plants, key=lambda plant: plant.especie.nome)
        for plant in sorted_plants:
            print(plant)


    def display_plants_sorted_by_planting_year(self) -> None:
        # https://docs.python.org/3.11/howto/sorting.html
        sorted_plants = sorted(self.__plants, key=lambda plant: plant.ano_plantacao)
        for plant in sorted_plants:
            print(plant)


    def get_long_living_plants(self) -> list[Plant, ..., Plant]:
        # https://favtutor.com/blogs/get-current-year-python
        from datetime import date
        ano_vigente = date.today().year

        long_living_plants = list()
        for plant in self.__plants:
            if plant.idade(ano_a_verificar=ano_vigente) >= plant.especie.num_medio_anos_vida:
                long_living_plants.append(plant)

        return long_living_plants



    def __str__(self) -> str:
        return f"\nNome do parque: {self.__name}\n"                \
               f"Largura: {self.largura:.2f} m\n"                  \
               f"Comprimento: {self.comprimento:.2f} m\n"          \
               f"Área de plantação: {self.planting_area:.2f} m²\n" \
               f"Número de plantas: {len(self.__plants)}\n"






if __name__ == "__main__":
    """
    Este if permite correr o ficheiro como um
    script independente e as instruções abaixo
    não serão executas se o ficheiro for importado
    de outro ficheiro. Deste modo podemos testar a
    classe de forma isolada.
    """

    # criar instância da classe Park
    park_1 = Park(
        name        = "Central Park",
        largura     = "ejhkje",
        comprimento = 20.0
    )

    # criar instâncias da classe Species
    species_1 = Species(
        nome                = "Rosa",
        tipo_folhagem       = "caduca",
        produz_fruto        = True,
        tipo_planta         = "arbusto",
        raio_max            = 3.5,
        num_medio_anos_vida = 5
    )

    species_2 = Species(
        nome                = "Camomila",
        tipo_folhagem       = "caduca",
        produz_fruto        = True,
        tipo_planta         = "arbusto",
        raio_max            = 4.5,
        num_medio_anos_vida = 5
    )

    # criar instâncias da classe Plant
    plant_1 = Plant(
        especie            = species_1,
        localizacao_coords = (10.0, 5.0),
        ano_plantacao      = 1990
    )

    plant_2 = Plant(
        especie            = species_2,
        localizacao_coords = (9.0, 6.0),
        ano_plantacao      = 2017
    )

    plant_3 = Plant(
        especie            = species_2,
        localizacao_coords = (19.0, 2.0),
        ano_plantacao      = 2019
    )

    # adicionar plantas ao parque
    park_1.add_plant(plant_1)
    park_1.add_plant(plant_2)
    park_1.add_plant(plant_3)

    # chamar o método __str__ para obter informações sobre o parque
    print(park_1)
