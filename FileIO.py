class FileIO:

    def read_species_file_and_return_dict(species_file_path='csv_files/species.csv') -> dict:
        species_dict = dict()

        # sem o encoding="utf-8" os acentos não apareciam
        # https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python
        try:
            with open(species_file_path, mode='r', encoding="utf-8") as file:
                for line in file:
                    # https://stackoverflow.com/questions/70510297/how-to-strip-a-certain-piece-of-text-from-each-line-of-a-text-file
                    values = line.strip().split(',')

                    # https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/
                    name, foliage_type, produces_fruit, plant_type, max_radius, avg_lifespan = values

                    # adicionar elementos da linha ao dicionário
                    # species_dict[name] = [
                    #     foliage_type,
                    #     produces_fruit,
                    #     plant_type,
                    #     max_radius,
                    #     avg_lifespan
                    # ]

                    species_dict[name] = {
                        "foliage_type"   : foliage_type,
                        "produces_fruit" : bool(produces_fruit),
                        "plant_type"     : plant_type,
                        "max_radius"     : float(max_radius),
                        "avg_lifespan"   : int(avg_lifespan)
                    }
        except FileNotFoundError:
            print(f"\n❌ O ficheiro que tentou ler, com o nome '{species_file_path}', não existe!")
        except Exception as e:
            print(f"\n❌ Aconteceu um erro! --> '{e}'")
        finally:
            return species_dict


    def write_park_file(park, file_path_to_save=None) -> None:

        if not file_path_to_save:
            # .strip() remove espaços brancos extra
            # .lower() torna a string lower case
            # e o .replace(" ", "_") substitui espaços por underscores
            file_path_to_save = f"csv_files/parks/{park.name.strip().lower().replace(' ', '_')}.csv"

        with open(file_path_to_save, 'w', encoding="utf-8") as file:

            # Escrever na 1ª linha o nome, a largura e comprimento do parque
            file.write(f"{park.name},{park.largura},{park.comprimento}\n")

            # Escrever informações sobre as plantas do parque no formato dado no enunciado
            for planta in park.plants:
                file.write(
                    f"{planta.especie.nome},"
                    f"{planta.localizacao_coords[0]},"
                    f"{planta.localizacao_coords[1]},"
                    f"{planta.ano_plantacao}\n"
                )


    def get_park_from_a_file_given_a_name(park_file_name: str):
        from Park import Park
        from InputDataValidator import InputDataValidator
        from Plant import Plant

        # ler o ficheiro csv correspondente ao parque
        with open(f"csv_files/parks/{park_file_name}", mode='r', encoding="utf-8") as file:
            for line in file:
                values = line.strip().split(',')

                if len(values) == 3:
                    park_name, largura, comprimento = values

                    # criar instância da classe Park
                    park_object = Park(
                        name        = park_name,
                        largura     = float(largura),
                        comprimento = float(comprimento)
                    )
                else:
                    species_name, location_x, location_y, planting_year = values

                    species_object = InputDataValidator.get_species_object_info_give_a_species_name(species_name=species_name)

                    park_object.add_plant(
                        Plant(
                            especie            = species_object,
                            localizacao_coords = (float(location_x), float(location_y)),
                            ano_plantacao      = int(planting_year)
                        ),
                        success_prints_are_silenced=True
                    )

            return park_object




if __name__ == "__main__":
    """
    Este if permite correr o ficheiro como um
    script independente e as instruções abaixo
    não serão executadas se o ficheiro for importado
    de outro ficheiro. Deste modo podemos testar a
    classe de forma isolada.
    """

    # pretty print dos dados do ficheiro de espécies
    import pprint
    pprint.pprint(FileIO.read_species_file_and_return_dict())

