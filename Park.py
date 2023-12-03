class Park:
    def __init__(self, name: str, planting_area: float):
        self.__name = name
        self.__planting_area = planting_area
        self.__plants = list()


    @property
    def name(self) -> str:
        return self.__name


    @property
    def planting_area(self) -> float:
        return self.__planting_area


    @property
    def plants(self) -> list[Plant, ..., Plant]:
        return self.__plants


    def add_plant(self, planta_a_adicionar) -> None:
        if self.is_there_space_available_for_the_plant(planta_a_adicionar):
            print("Planta adicionada ao parque com sucesso.")
        else:
            print("Não há espaço suficiente para adicionar a planta.")


    def remove_plant(self, plant_location) -> None:
        for plant in self.__plants:
            if plant.localizacao_coords == plant_location:
                self.__plants.remove(plant)
                print("Planta removida com sucesso.")
                return
        print("Não foi encontrada qualquer planta na localização especificada.")



    def is_location_occupied_by_another_plant(self, at_coords) -> bool:
        for plant in self.__plants:
            if plant.localizacao_coords == at_coords:
                return True
        return False


    def total_area_occupied(self):
        pass


    def available_planting_area(self):
        pass


    def average_plant_age(self, year):
        pass


    def num_of_unique_species(self):
        pass


    def get_unique_species_list(self):
        pass


    def display_plants_sorted_by_species(self):
        pass


    def display_plants_sorted_by_planting_year(self):
        pass


    def get_long_living_plants(self):
        pass


    def list_plants(self):
        pass


    def is_empty(self):
        pass


    def is_there_space_available_for_the_plant(self, plant):
        pass


    def __str__(self) -> str:
        return f"\nNome do parque: {self.__name}\n"             \
               f"Área de plantação: {self.__planting_area}\n"   \
               f"Número de plantas: {len(self.__plants)}\n"
