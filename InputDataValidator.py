from FileIO import FileIO

class InputDataValidator:

    # ---------- CLASS SPECIES VALIDATIONS ------------------------------------------------------------------------------------

    def get_valid_species_name(input_text: str) -> str:
        species_name = input_text.strip().lower()
        while not isinstance(species_name, str) or species_name == "":
            try:
                species_name = input('Insira um nome válido (não pode ser vazio) para a espécie: ').strip().lower()
            except ValueError:
                continue
        return species_name

    def get_valid_follage_type(species_name, input_text: str) -> str:
        foliage_type = input_text.strip().lower()
        while not isinstance(foliage_type, str) or foliage_type == "" or foliage_type not in ("persistente", "caduca", "semicaduca"):
            try:
                foliage_type = input(f'Insira um tipo de folhagem válido ["persistente", "caduca", "semicaduca"] para a espécie {species_name}: ').strip().lower()
            except ValueError:
                continue
        return foliage_type

    def get_valid_plant_type(species_name, input_text: str) -> str:
        plant_type = input_text.strip().lower()
        while plant_type == "" or plant_type not in ("árvore", "arbusto"):
            try:
                plant_type = input(f'Insira um tipo de planta válido ["árvore", "arbusto"] para a espécie {species_name}: ').strip().lower()
            except ValueError:
                continue
        return plant_type

    def get_valid_positive_radius(species_name, input_value) -> float:
        raio_max = input_value
        while not isinstance(raio_max, float) or raio_max <= 0:
            try:
                raio_max = float(input(f'Insira um raio válido [decimal positivo] para a espécie {species_name}: '))
            except ValueError:
                continue
        return raio_max

    def get_valid_positive_avg_life(species_name, input_value) -> int:
        avg_life = input_value
        while not isinstance(avg_life, int) or avg_life <= 0:
            try:
                avg_life = int(input(f'Insira uma idade média em anos válido [inteiro positivo] para a espécie {species_name}: '))
            except ValueError:
                continue
        return avg_life


    # -----------------------------------------------------------------------------------------------------------------------------


    # ---------- CLASS PARK VALIDATIONS ------------------------------------------------------------------------------------

    def get_valid_park_height(park_name, input_value) -> float:
        park_height = input_value
        while not isinstance(park_height, float) or park_height <= 0:
            try:
                park_height = float(input(f'Insira uma largura válida [decimal positivo] para o parque {park_name}: '))
            except ValueError:
                continue
        return park_height


    def get_valid_park_width(park_name, input_value) -> float:
        park_width = input_value
        while not isinstance(park_width, float) or park_width <= 0:
            try:
                park_width = float(input(f'Insira um comprimento válido [decimal positivo] para o parque {park_name}: '))
            except ValueError:
                continue
        return park_width


    # -----------------------------------------------------------------------------------------------------------------------------



    def get_species_instance_from_species_csv_file_given_a_name():

        especies_registadas = FileIO.read_species_file_and_return_dict()

        nome_da_especie_inserida = input("Insira o nome da espécie da planta: ").lower()
        while nome_da_especie_inserida not in especies_registadas.keys():
            print("❌ Espécie inválida, por favor tente de novo.")
            nome_da_especie_inserida = input("Insira o nome da espécie da planta: ").lower()

        # print(especies_registadas[nome_da_especie_inserida])
        from Species import Species
        return Species(
            nome                = nome_da_especie_inserida,
            tipo_folhagem       = especies_registadas[nome_da_especie_inserida]["foliage_type"],
            produz_fruto        = bool(especies_registadas[nome_da_especie_inserida]["produces_fruit"]),
            tipo_planta         = especies_registadas[nome_da_especie_inserida]["plant_type"],
            raio_max            = float(especies_registadas[nome_da_especie_inserida]["max_radius"]),
            num_medio_anos_vida = int(especies_registadas[nome_da_especie_inserida]["avg_lifespan"])
        )


    def get_valid_location_to_plant(in_park, species_object) -> tuple[float, float]:
        localizacao = float(input("Localização da planta (coordenada x): ")),\
                      float(input("Localização da planta (coordenada y): "))

        while in_park.is_location_occupied_by_another_plant(at_coords=localizacao):
            print("❌ A localização inserida já está ocupada.")
            localizacao = float(input("Localização da planta (coordenada x): ")),\
                          float(input("Localização da planta (coordenada y): "))


        # verificar se existe interseção de área de ocupação
        is_there_intersection = InputDataValidator.verify_if_there_is_intersection(localizacao, in_park, species_object)

        while is_there_intersection:
            print("\n❌ Não foi possível adicionar a planta pois existia sobreposição com outra planta.\n")
            localizacao = float(input("Localização da planta (coordenada x): ")),\
                          float(input("Localização da planta (coordenada y): "))
            is_there_intersection = InputDataValidator.verify_if_there_is_intersection(localizacao, in_park, species_object)


        # verificar se está dentro dos limites do parque
        is_within_park_boundaries = InputDataValidator.verify_if_its_not_between_park_boundaries(localizacao, in_park, species_object)
        while is_within_park_boundaries:
            print("\n❌ A Localização da planta não está dentro dos limites do parque.\n")
            localizacao = float(input("Localização da planta (coordenada x): ")),\
                          float(input("Localização da planta (coordenada y): "))
            is_within_park_boundaries = InputDataValidator.verify_if_its_not_between_park_boundaries(localizacao, in_park, species_object)

        return localizacao


    def verify_if_its_not_between_park_boundaries(localizacao, in_park, species_object):
        especies_registadas = FileIO.read_species_file_and_return_dict()
        nome_da_especie_criada = species_object.nome
        return localizacao[0] + especies_registadas[nome_da_especie_criada]["max_radius"] > in_park.largura or localizacao[1] + especies_registadas[nome_da_especie_criada]["max_radius"] > in_park.comprimento


    def verify_if_there_is_intersection(localizacao, in_park, species_object):
        especies_registadas = FileIO.read_species_file_and_return_dict()
        nome_da_especie_criada = species_object.nome

        from math import sqrt as math_sqrt
        for plant in in_park.plants:
            distance_between_them = math_sqrt(
                (localizacao[0] - plant.localizacao_coords[0])**2 +
                (localizacao[1] - plant.localizacao_coords[1])**2
            )
            if distance_between_them < (especies_registadas[nome_da_especie_criada]["max_radius"] + plant.especie.raio_max):
                return True
        return False


    def get_valid_planting_year():

        from datetime import date
        ano_vigente = date.today().year

        ano_de_plantacao_inserido = int(input("Ano de plantação da planta: "))

        while ano_de_plantacao_inserido <= 0 or ano_de_plantacao_inserido > ano_vigente:
            if ano_de_plantacao_inserido <= 0:
                print("❌ Erro. O ano inserido tem de ser um valor inteiro positivo. Tente de novo.")
            else:
                print("❌ Erro. O ano inserido não pode ser maior que o ano vigente. Tente de novo.")
            ano_de_plantacao_inserido = int(input("Ano de plantação da planta: "))

        return ano_de_plantacao_inserido


    def get_park_from_file():
        nome_parque = input("Indique o nome do parque (que corresponde ao nome do ficheiro) a carregar: ")
        ficheiro_parque = nome_parque.strip().lower().replace(' ', '_') + ".csv"

        from os import listdir as list_dir
        csv_files = [f for f in list_dir(path="./csv_files/parks/") if f.endswith('.csv')]
        # print("Ficheiros CSV existentes dos parques:", csv_files)

        if ficheiro_parque in csv_files:
            # print("O parque existe em ficheiro csv.")
            return FileIO.get_park_from_a_file_given_a_name(park_file_name=ficheiro_parque)
        else:
            print("\nℹ️ O parque não existe em ficheiro csv.")
            return None



    def get_species_object_info_give_a_species_name(species_name: str):

        especies_registadas = FileIO.read_species_file_and_return_dict()
        if species_name in especies_registadas:
            from Species import Species
            return Species(
                nome                = species_name,
                tipo_folhagem       = especies_registadas[species_name]["foliage_type"],
                produz_fruto        = bool(especies_registadas[species_name]["produces_fruit"]),
                tipo_planta         = especies_registadas[species_name]["plant_type"],
                raio_max            = float(especies_registadas[species_name]["max_radius"]),
                num_medio_anos_vida = int(especies_registadas[species_name]["avg_lifespan"])
            )
        else:
            print("❌ Erro ao processar uma espécie.")


if __name__ == "__main__":
    """
    Este if permite correr o ficheiro como um
    script independente e as instruções abaixo
    não serão executadas se o ficheiro for importado
    de outro ficheiro. Deste modo podemos testar a
    classe de forma isolada.
    """

    # obter uma instância de uma Espécie a partir dos registos existentes no csv
    # print(InputDataValidator.get_species_instance_from_species_csv_file_given_a_name())


    # from Park import Park
    # obter uma localização de plantação válida num determinado parque
    # park_1 = Park(name="Central Park", planting_area=1000)
    # InputDataValidator.get_valid_location_to_plant(in_park=park_1)


    # obter ano de plantação válido
    # InputDataValidator.get_valid_planting_year()
