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

