from InputDataValidator import InputDataValidator
from FileIO import FileIO
from Plant import Plant

class ParkManager:
    def __init__(self, park):
        self.park = park


    def run(self):
        while True:
            print(
                f"\nGESTÃO DO PARQUE: {self.park.name}\n\n"
                "0. Listar espécies de plantas existentes para se poder plantar\n"
                "1. Adicionar planta\n"
                "2. Remover planta\n"
                "3. Listar plantas existentes no parque\n"
                "4. Mostrar área ocupada\n"
                "5. Mostrar a área disponível para plantação\n"
                "6. Mostrar o mapa do parque\n"
                "7. Estatísticas e informações\n"
                "8. Guardar o parque num ficheiro\n"
                "9. Sair (ou voltar ao menu anterior)\n"
            )

            choice = input("Escolha uma opção (1-9): ")

            # https://www.geeksforgeeks.org/python-match-case-statement/
            match choice:
                case '0':
                    self.display_existing_species()
                case '1':
                    self.add_plant()
                case '2':
                    self.remove_plant()
                case '3':
                    self.list_plants()
                case '4':
                    self.show_occupied_area()
                case '5':
                    self.show_available_planting_area()
                case '6':
                    self.show_park_map()
                case '7':
                    self.display_statistics_and_info()
                case '8':
                    self.save_to_file()
                case '9':
                    print("\nA sair... 👋")
                    break
                case _:
                    print("\n❌ Escolha inválida. Tente de novo.")


    def display_existing_species(self):
        especies_registadas = FileIO.read_species_file_and_return_dict()
        print("\nLista de espécies de plantas existentes para se poder plantar:\n")
        for especie in especies_registadas.keys():
            print(f" - {especie:<20} (raio de ocupação: {especies_registadas[especie]['max_radius']})")


    def add_plant(self):
        especie = InputDataValidator.get_species_instance_from_species_csv_file_given_a_name()
        localizacao = InputDataValidator.get_valid_location_to_plant(in_park=self.park, species_object=especie)
        ano_plantacao = InputDataValidator.get_valid_planting_year()

        nova_planta = Plant(
            especie=especie,
            localizacao_coords=localizacao,
            ano_plantacao=ano_plantacao
        )

        self.park.add_plant(planta_a_adicionar=nova_planta)


    def remove_plant(self):
        if self.park.is_empty():
            print("\nℹ️ Não é possível eliminar plantas, pois não existem plantas no parque.")
            return

        # pedir ao utilizador a localização da planta para a eliminar
        localizacao = float(input("Localização da planta a eliminar (coordenada x): ")),\
                      float(input("Localização da planta a eliminar (coordenada y): "))

        # remover planta do parque
        self.park.remove_plant(plant_location=localizacao)


    def list_plants(self):
        self.park.list_plants()


    def show_occupied_area(self):
        print(f"\nÁrea ocupada no parque: {self.park.total_area_occupied():.2f} m².")


    def show_available_planting_area(self):
        print(f"\nÁrea de plantação disponível no parque: {self.park.available_planting_area():.2f} m².")


    def show_park_map(self):
        if self.park.is_empty():
            print("\nℹ️ O parque está vazio mas ok...")

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.set_xlim((0, self.park.largura))
        ax.set_ylim((0, self.park.comprimento))
        ax.set_box_aspect(1)

        # do enunciado:
        # loc = [(5,5), (20,5), (50,50), (60,80), (70,80), (80,80)]
        # raio = [3, 2, 6, 3, 5, 4]
        # https://realpython.com/list-comprehension-python/
        loc = [plant.localizacao_coords for plant in self.park.plants]
        raio = [plant.especie.raio_max for plant in self.park.plants]

        for i in range(len(loc)):
            circle = plt.Circle(loc[i], raio[i], color='g', alpha=0.4)
            ax.add_patch(circle)
            ax.text(loc[i][0], loc[i][1], s="x", horizontalalignment='center', verticalalignment='center')
        plt.title(f'Mapa do parque: {self.park.name}')
        plt.show()

    # --------------------------------------------- BEGIN OF STATS ---------------------------------------------
    def display_statistics_and_info(self):
        while True:
            print(
                f"\nESTATÍSTICAS & INFO DO PARQUE: {self.park.name}\n\n"
                "1. Mostrar a média das idades das plantas do parque\n"
                "2. Mostrar o número de espécies diferentes\n"
                "3. Listar as espécies existentes no parque\n"
                "4. Listar todas as plantas organizadas por espécie\n"
                "5. Listar todas as plantas organizadas por ano de plantação\n"
                "6. Listar as plantas que excederam o tempo médio de vida da sua espécie\n"
                "7. Histograma por idade\n"
                "8. Histograma por espécie\n"
                "9. Voltar ao menu principal\n"
            )

            stat_choice = input("Escolha uma opção (1-9): ")

            match stat_choice:
                case '1':
                    self.display_average_age()
                case '2':
                    self.display_num_species()
                case '3':
                    self.display_species_list()
                case '4':
                    self.display_plants_by_species()
                case '5':
                    self.display_plants_by_year()
                case '6':
                    self.display_long_living_plants()
                case '7':
                    self.generate_age_histogram()
                case '8':
                    self.generate_species_histogram()
                case '9':
                    print("\nA voltar ao menu principal...👍")
                    break
                case _:
                    print("\n❌ Escolha inválida. Tente de novo.")


    def display_average_age(self):
        from datetime import date
        ano_vigente = date.today().year

        average_plant_age = self.park.average_plant_age(year=ano_vigente)

        print(f"\nA idade média das plantas do parque é: {average_plant_age:.1f} anos")


    def display_num_species(self):
        print(f"\nNúmero de espécies diferentes no parque: {self.park.num_of_unique_species()}")


    def display_species_list(self):
        if self.park.is_empty():
            print("\nℹ️ O parque está vazio! Não existe qualquer espécie plantada.")
        else:
            species_list = self.park.get_unique_species_list()
            print("\nLista de espécies no parque:")
            for especie in species_list:
                print(f" - {especie}")


    def display_plants_by_species(self):
        if self.park.is_empty():
            print("\nℹ️ O parque está vazio! Não existe qualquer espécie plantada.")
        else:
            species_list = self.park.get_unique_species_list()
            print("\nPlantas organizadas por espécies:\n")
            for especie in species_list:
                print(f"\n------------------ {especie} ------------------")
                for plant in self.park.plants:
                    if plant.especie.nome == especie:
                        print(plant)


    def display_plants_by_year(self):
        if self.park.is_empty():
            print("\nℹ️ O parque está vazio! Não existe qualquer espécie plantada.")
        else:
            print("\nPlantas organizadas por ano de plantação:")
            self.park.display_plants_sorted_by_planting_year()


    def display_long_living_plants(self):
        if self.park.is_empty():
            print("\nℹ️ O parque está vazio! Não existe qualquer espécie plantada.")
        else:
            long_living_plants = self.park.get_long_living_plants()
            if long_living_plants:
                print("\nPlantas que excederam o tempo médio de vida da sua espécie:")
                for plant in long_living_plants:
                    print(plant)
            else:
                print("\nℹ️ Não existem plantas que excederam o tempo médio de vida da sua espécie.")


    def generate_age_histogram(self):
        if self.park.is_empty():
            print("\nℹ️ O parque está vazio! Não existe qualquer espécie plantada.")
        else:
            import matplotlib.pyplot as plt

            # do enunciado:
            # labels = ['0', '2', '3', '6', '10'] # idade das plantas em anos
            # values = [3, 1, 2, 5, 3] # quantidade de plantas com 0, 2, 3, 6 e 10 anos

            from datetime import date
            ano_vigente = date.today().year
            # https://realpython.com/list-comprehension-python/
            plants_ages = [plant.idade(ano_a_verificar=ano_vigente) for plant in self.park.plants]

            # tornar os valores da lista únicos usando novamente a técnica usada anteriormente na T3
            labels = list(set(plants_ages))

            # encontrar o nº de ocurrências das idades das plantas
            values = [plants_ages.count(label) for label in labels]

            # só para debug
            # print("labels", labels)
            # print("values", values)

            plt.bar(labels, values)

            plt.title('Histograma por idade')
            plt.xlabel('Idade das plantas')
            plt.ylabel('Frequência das idades')

            plt.show()


    def generate_species_histogram(self):
        if self.park.is_empty():
            print("\nℹ️ O parque está vazio! Não existe qualquer espécie plantada.")
        else:
            import matplotlib.pyplot as plt

            # do enunciado:
            # labels = ['0', '2', '3', '6', '10'] # idade das plantas em anos
            # values = [3, 1, 2, 5, 3] # quantidade de plantas com 0, 2, 3, 6 e 10 anos

            # https://realpython.com/list-comprehension-python/
            plants_species = [plant.especie.nome for plant in self.park.plants]

            # tornar os valores da lista únicos usando novamente a técnica usada anteriormente na T3
            labels = self.park.get_unique_species_list()

            # encontrar o nº de ocurrências das idades das plantas
            values = [plants_species.count(label) for label in labels]
            # forma mais longa de fazer o mesmo
            # values = list()
            # for label in labels:
            #     values.append(plants_species.count(label))

            # print("labels", labels)
            # print("values", values)

            plt.bar(labels, values)

            plt.title('Histograma por espécies')
            plt.xlabel('Espécies das plantas')
            plt.ylabel('Frequência das espécies')

            plt.show()
    # --------------------------------------------- END OF STATS ---------------------------------------------


    def save_to_file(self):
        # if self.park.is_empty():
        #     print("\nℹ️ O parque está vazio! Não é possível guardar informação ainda.")
        # else:
        FileIO.write_park_file(park=self.park)
        print("\n✅ O ficheiro com a informação do parque foi guardado com sucesso.")




if __name__ == "__main__":
    """
    Este if permite correr o ficheiro como um
    script independente e as instruções abaixo
    não serão executadas se o ficheiro for importado
    de outro ficheiro. Deste modo podemos testar a
    classe de forma isolada.
    """

    from Park import Park

    # Criar instância da classe Park
    park_1 = Park(name="Central Park", largura=50.0, comprimento=20.0)

    # Criar instância da classe ParkManager
    park_manager = ParkManager(park=park_1)

    # Executar o menu
    park_manager.run()
