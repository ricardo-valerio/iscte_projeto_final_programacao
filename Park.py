class Park:
    def __init__(self, name: str, planting_area: float):
        self.__name = name
        self.__planting_area = planting_area
        self.__plants = list()


    @property
    def name(self) -> str:
        return self.__name


    @property
    def planting_area(self):
        return self.__planting_area


    @property
    def plants(self):
        return self.__plants


    def add_plant(self, planta_a_adicionar):
        pass


    def remove_plant(self, plant_location):
        pass


    def is_location_occupied_by_another_plant(self, at_coords):
        pass


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
