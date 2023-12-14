from FileIO import FileIO

class InputDataValidator:

    # ----------------------------- BEGIN SPECIES VALIDATIONS ---------------------------

    def get_valid_species_name(input_text: str) -> str:
        species_name = input_text.strip().lower()
        while not isinstance(species_name, str) or species_name == "":
            try:
                species_name = input('Insira um nome válido (não pode ser vazio) para a espécie: ').strip().lower()
            except ValueError:
                continue
        return species_name


    def get_valid_follage_type(species_name: str, input_text: str) -> str:
        foliage_type = input_text.strip().lower()
        while not isinstance(foliage_type, str) or foliage_type == "" or foliage_type not in ("persistente", "caduca", "semicaduca"):
            try:
                foliage_type = input(f'Insira um tipo de folhagem válido ["persistente", "caduca", "semicaduca"] para a espécie {species_name}: ').strip().lower()
            except ValueError:
                continue
        return foliage_type


    def does_it_produce_fruit(input_text: str) -> bool:
        yes_or_no = input_text.strip().lower()
        if yes_or_no in ("não", 'n', "no", "nope", '0'):
            return False
        else:
            return True


    def get_valid_plant_type(species_name: str, input_text: str) -> str:
        plant_type = input_text.strip().lower()
        while plant_type == "" or plant_type not in ("árvore", "arbusto"):
            try:
                plant_type = input(f'Insira um tipo de planta válido ["árvore", "arbusto"] para a espécie {species_name}: ').strip().lower()
            except ValueError:
                continue
        return plant_type


    def get_valid_positive_radius(species_name: str, input_value: str) -> float:
        raio_max = input_value
        try:
            raio_max = float(raio_max)

            if raio_max <= 0:
                raise Exception

        except Exception:
            while not isinstance(raio_max, float) or raio_max <= 0:
                try:
                    raio_max = float(input(f'Insira um raio válido [decimal positivo] para a espécie {species_name}: ').strip())
                except ValueError:
                    continue

        return raio_max


    def get_valid_positive_avg_life(species_name: str, input_value: str) -> int:
        avg_life = input_value
        try:
            avg_life = int(avg_life)

            if avg_life <= 0:
                raise Exception

        except Exception:
            while not isinstance(avg_life, int) or avg_life <= 0:
                try:
                    avg_life = int(input(f'Insira uma idade média em anos válido [inteiro positivo] para a espécie {species_name}: ').strip())
                except ValueError:
                    continue

        return avg_life

    # ----------------------------- END SPECIES VALIDATIONS -----------------------------



    # ----------------------------- BEGIN PARK VALIDATIONS ---------------------------

    def get_valid_park_name(input_text: str) -> str:
        park_name = input_text.strip()
        while not isinstance(park_name, str) or park_name == "" or park_name.isnumeric():
            try:
                park_name = input('Insira um nome válido (não pode ser vazio ou numérico) para o parque: ').strip()
            except ValueError:
                continue
        return park_name


    def get_valid_park_width(park_name, input_value) -> float:
        park_width = input_value
        try:
            park_width = float(park_width)

            if park_width <= 0:
                raise Exception

        except Exception:
            while not isinstance(park_width, float) or park_width <= 0:

                if not isinstance(park_width, float):
                    print("❌ Erro. O valor inserido tem de ser um decimal positivo.")
                elif park_width <= 0:
                    print("❌ Erro. O valor decimal tem de ser positivo.")

                try:
                    park_width = float(input(f'Insira uma largura válida [decimal positivo] para o parque {park_name}: ').strip())
                except ValueError:
                    continue
        return park_width


    def get_valid_park_length(park_name, park_width, input_value) -> float:
        park_length = input_value
        try:
            park_length = float(park_length)

            if park_length < park_width:
                raise Exception

        except Exception:
            while not isinstance(park_length, float) or park_length <= 0 or park_length < park_width:

                if not isinstance(park_length, float):
                    print("❌ Erro. O valor inserido tem de ser um decimal positivo.")
                elif park_length <= 0:
                    print("❌ Erro. O valor decimal tem de ser positivo.")
                else:
                    print("❌ Erro. O valor do comprimento tem de ser maior ou igual que a largura.")

                try:
                    park_length = float(input(f'Insira um comprimento válido [decimal positivo] para o parque "{park_name}": ').strip())
                except ValueError:
                    continue
        return park_length


    def get_valid_location_to_plant(in_park, species_object) -> tuple[float, float]:
        localizacao = InputDataValidator.validate_float_value(question="Localização da planta (coordenada x): "),\
                      InputDataValidator.validate_float_value(question="Localização da planta (coordenada y): ")

        # verificar se a localização dada não está dentro dos limites do parque
        is_location_not_within_park_boundaries = not in_park.is_given_location_within_park_boundaries(localizacao)

        # verificar se a localização está ocupada
        is_location_occupied = in_park.is_location_occupied_by_another_plant(at_coords=localizacao)

        # verificar se existe interseção de área de ocupação
        is_there_intersection = InputDataValidator.verify_if_there_is_intersection(localizacao, in_park, species_object)

        # verificar se a área circular da planta está dentro dos limites do parque
        is_plant_area_not_within_park_boundaries = InputDataValidator.verify_if_plant_area_is_not_between_park_boundaries(localizacao, in_park, species_object)

        while is_location_not_within_park_boundaries or \
              is_location_occupied                   or \
              is_there_intersection                  or \
              is_plant_area_not_within_park_boundaries:

            if is_location_not_within_park_boundaries:
                print(
                    f"\n❌ A localização inserida não está dentro dos limites do parque.\n"
                    f"O parque tem de largura: {in_park.largura} e comprimento: {in_park.comprimento}.\n"
                )
            elif is_location_occupied:
                print("\n❌ A localização inserida já está ocupada por outra planta.\n")
            elif is_there_intersection:
                print("\n❌ Não foi possível adicionar a planta pois existia sobreposição com outra planta.\n")
            elif is_plant_area_not_within_park_boundaries:
                especies_registadas = FileIO.read_species_file_and_return_dict()
                nome_da_especie_criada = species_object.nome
                print(
                    f"\n❌ A área da planta não ficará dentro dos limites do parque. \n"
                    f"O parque tem de largura: {in_park.largura} e comprimento: {in_park.comprimento}.\n"
                    f"A planta a adicionar ao parque tem raio: {especies_registadas[nome_da_especie_criada]['max_radius']}.\n"
                )

            localizacao = InputDataValidator.validate_float_value(question="Localização da planta (coordenada x): "),\
                          InputDataValidator.validate_float_value(question="Localização da planta (coordenada y): ")

            is_location_not_within_park_boundaries = not in_park.is_given_location_within_park_boundaries(localizacao)

            is_location_occupied = in_park.is_location_occupied_by_another_plant(at_coords=localizacao)

            is_there_intersection = InputDataValidator.verify_if_there_is_intersection(localizacao, in_park, species_object)

            is_plant_area_not_within_park_boundaries = InputDataValidator.verify_if_plant_area_is_not_between_park_boundaries(localizacao, in_park, species_object)

        return localizacao


    def verify_if_plant_area_is_not_between_park_boundaries(localizacao: tuple, in_park: object, species_object: object) -> bool:
        especies_registadas = FileIO.read_species_file_and_return_dict()
        nome_da_especie_criada = species_object.nome

        return (localizacao[0] + especies_registadas[nome_da_especie_criada]["max_radius"] >= in_park.largura or \
                localizacao[1] + especies_registadas[nome_da_especie_criada]["max_radius"] >= in_park.comprimento) or \
               (localizacao[0] - especies_registadas[nome_da_especie_criada]["max_radius"] <= 0 or \
                localizacao[1] - especies_registadas[nome_da_especie_criada]["max_radius"] <= 0)


    def verify_if_there_is_intersection(localizacao: tuple, in_park: object, species_object: object) -> bool:
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

    # ----------------------------- END PARK VALIDATIONS -----------------------------




    def get_species_instance_from_species_csv_file_given_a_name() -> object:

        especies_registadas = FileIO.read_species_file_and_return_dict()

        nome_da_especie_inserida = input("Insira o nome da espécie da planta: ").strip().lower()
        while nome_da_especie_inserida not in especies_registadas.keys():
            print("❌ Espécie inválida, por favor tente de novo.")
            nome_da_especie_inserida = input("Insira o nome da espécie da planta: ").strip().lower()

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


    def validate_float_value(question: str) -> float:
        float_value = input(question)
        try:
            float_value = float(float_value)
            if float_value <= 0:
                raise Exception
        except Exception:
            while not isinstance(float_value, float) or float_value <= 0:
                try:
                    float_value = float(input(f'Insira um [decimal positivo] para a {question}'))
                except ValueError:
                    continue
        return float_value


    def get_valid_planting_year() -> int:
        from datetime import date
        ano_vigente = date.today().year

        ano_de_plantacao_inserido = input("Ano de plantação da planta: ").strip()

        try:
            ano_de_plantacao_inserido = int(ano_de_plantacao_inserido)
            if ano_de_plantacao_inserido <= 0:
                print("❌ Erro. O ano inserido tem de ser um valor inteiro positivo. Tente de novo.")
                raise Exception
            elif ano_de_plantacao_inserido > ano_vigente:
                print("❌ Erro. O ano inserido não pode ser maior que o ano vigente. Tente de novo.")
                raise Exception
        except Exception:
            while not isinstance(ano_de_plantacao_inserido, int) or \
                  ano_de_plantacao_inserido <= 0 or \
                  ano_de_plantacao_inserido > ano_vigente:

                if not isinstance(ano_de_plantacao_inserido, int) or \
                   ano_de_plantacao_inserido <= 0:
                    print("❌ Erro. O ano inserido tem de ser um valor inteiro positivo. Tente de novo.")
                else:
                    print("❌ Erro. O ano inserido não pode ser maior que o ano vigente. Tente de novo.")

                try:
                    ano_de_plantacao_inserido = int(input("Ano de plantação da planta: ").strip())
                except ValueError:
                    continue

        return ano_de_plantacao_inserido


    def get_park_from_file() -> object or None:
        nome_parque = input("Indique o nome do parque (que corresponde ao nome do ficheiro) a carregar: ")
        ficheiro_parque = nome_parque.strip().lower().replace(' ', '_') + ".csv"

        from os import listdir as list_dir
        csv_files = [file for file in list_dir(path="./csv_files/parks/") if file.endswith('.csv')]
        # print("Ficheiros CSV existentes dos parques:", csv_files)

        if ficheiro_parque in csv_files:
            # print("O parque existe em ficheiro csv.")
            return FileIO.get_park_from_a_file_given_a_name(park_file_name=ficheiro_parque)
        else:
            print("\nℹ️ O parque não existe em ficheiro csv.")
            return None


    def get_species_object_info_given_a_species_name(species_name: str) -> object or None:
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

