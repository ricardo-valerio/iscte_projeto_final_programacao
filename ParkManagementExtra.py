from Park import Park
from Species import Species
from Plant import Plant
from FileIO import FileIO
from ParkManager import ParkManager
from InputDataValidator import InputDataValidator

class ParkManagementExtra:
    def __init__(self):
        self.parks = list()


    def run(self):
        while True:
            print(
                f"\n------- SISTEMA DE GESTÃO DOS PARQUES -------\n\n"
                "0. Adicionar espécie\n"
                "1. Adicionar parque\n"
                "2. Carregar parque de um ficheiro\n"
                "3. Remover parque\n"
                "4. Listar parques\n"
                "5. Gerir parque\n"
                "6. Sair\n"
            )

            choice = input("Escolha uma opção (1-6): ")

            # https://www.geeksforgeeks.org/python-match-case-statement/
            match choice:
                case '0':
                    self.add_species()
                case '1':
                    self.add_park()
                case '2':
                    self.load_park_from_file()
                case '3':
                    self.remove_park()
                case '4':
                    self.list_parks()
                case '5':
                    self.manage_park()
                case '6':
                    print("\nA sair... 👋")
                    break
                case _:
                    print("\n❌ Escolha inválida. Tente de novo.")

    def add_species(self):
        nome_especie = InputDataValidator.get_valid_species_name(
                            input_text=input("Insira o nome da espécie a adicionar ao sistema: ")
                       )
        especies_registadas = FileIO.read_species_file_and_return_dict()

        while nome_especie in especies_registadas.keys():
            nome_especie = InputDataValidator.get_valid_species_name(
                                input_text=input("Essa espécie já existe no sistema, por favor insira o nome de outra espécie a adicionar ao sistema: ")
                            )

        tipo_folhagem = InputDataValidator.get_valid_follage_type(
                            species_name=nome_especie,
                            input_text=input("Insira o tipo de folhagem ['persistente', 'caduca', 'semicaduca']: ")
                        )
        produz_fruto = InputDataValidator.does_it_produce_fruit(
                            input_text=input("Produz fruto? (s/n): ")
                       )

        tipo_planta = InputDataValidator.get_valid_plant_type(
                            species_name=nome_especie,
                            input_text=input("Insira o tipo de planta ['árvore', 'arbusto']: ")
                      )

        max_radius = InputDataValidator.get_valid_positive_radius(
                            species_name=nome_especie,
                            input_value=input("Insira o raio da área circular de ocupação da espécie: ")
                     )
        # print("ora ora max_radius:", max_radius)

        num_medio_anos_vida = InputDataValidator.get_valid_positive_avg_life(
                                    species_name=nome_especie,
                                    input_value=input("Insira o nº médio de anos de vida da espécie: ")
                              )
        # print("ora ora num_medio_anos_vida:", num_medio_anos_vida)

        added_with_success = FileIO.add_species_to_file(
                                nome_especie,
                                tipo_folhagem,
                                produz_fruto,
                                tipo_planta,
                                max_radius,
                                num_medio_anos_vida
                             )

        if added_with_success:
            print("\n✅ Espécie adicionada ao sistema com sucesso.")
        else:
            print("\n❌ Erro ao adicionar espécie ao sistema.")



    def add_park(self) -> None:
        nome_parque = InputDataValidator.get_valid_park_name(
                         input_text=input("Insira o nome do parque: ")
                      )
        largura_parque = InputDataValidator.get_valid_park_width(
                            park_name=nome_parque,
                            input_value=input("Insira a largura do parque (metros): ")
                         )
        comprimento_parque = InputDataValidator.get_valid_park_length(
                                park_name=nome_parque,
                                park_width=largura_parque,
                                input_value=input("Insira o comprimento do parque (metros): ")
                             )
        novo_parque = Park(name=nome_parque, largura=largura_parque, comprimento=comprimento_parque)
        self.parks.append(novo_parque)
        print("\n✅ Parque adicionado ao sistema com sucesso.")


    def load_park_from_file(self):
        novo_parque = InputDataValidator.get_park_from_file()
        if novo_parque:
            if novo_parque.name in [park.name for park in self.parks]:
                print("\nℹ️ O parque inserido já existe no sistema.")
            else:
                self.parks.append(novo_parque)
                print("\n✅ Parque carregado no sistema com sucesso.")
        else:
            print("\n❌ Erro ao carregar o parque.")


    def remove_park(self) -> None:
        if len(self.parks) == 0:
            print("\nℹ️ Não é possível remover parques pois o sistema não tem parques.")
            return

        nome_parque = input("Indique o nome do parque a remover: ").lower()
        for park in self.parks:
            if nome_parque == park.name.lower():
                self.parks.remove(park)
                print("\n✅ Parque removido do sistema com sucesso.")
                return

        print("\nℹ️ O nome do parque inserido não existe no sistema.")


    def list_parks(self):
        if len(self.parks) == 0:
            print("\nℹ️ O sistema não tem parques.")
            return

        print("\nLista de parques no sistema:")
        for park in self.parks:
            print(park)


    def manage_park(self):
        if len(self.parks) == 0:
            print("\nℹ️ O sistema não tem parques.")
            return

        nome_parque = input("Indique o nome do parque a gerir: ")
        for park in self.parks:
            if nome_parque.lower() == park.name.lower():
                park_manager = ParkManager(park=park)
                park_manager.run()
                return

        print(f"\nℹ️ O sistema não qualquer parque chamado '{nome_parque}'.")





if __name__ == "__main__":
    """
    Este if permite correr o ficheiro como um
    script independente e as instruções abaixo
    não serão executadas se o ficheiro for importado
    de outro ficheiro. Deste modo podemos testar a
    classe de forma isolada.
    """

    park_manager = ParkManagementExtra()
    park_manager.run()
