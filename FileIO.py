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
                        "produces_fruit" : produces_fruit,
                        "plant_type"     : plant_type,
                        "max_radius"     : max_radius,
                        "avg_lifespan"   : avg_lifespan
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

            # Escrever na 1ª linha o nome e a área de plantação do parque
            file.write(f"{park.name},{park.planting_area}\n")

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

                if len(values) == 2:
                    park_name, planting_area = values

                    # criar instância da classe Park
                    park_object = Park(
                        name          = park_name,
                        planting_area = float(planting_area)
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



    from Park import Park
    from Species import Species
    from Plant import Plant

    # criar instância da classe Park
    park_1 = Park(
        name          = "Parque da Bela Vista",
        planting_area = 1000
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


    # escrever as informações, do parque criado, para um ficheiro
    FileIO.write_park_file(park=park_1)
