class Plant:
    def __init__(self, especie, localizacao_coords, ano_plantacao):
        self.__especie = especie
        self.localizacao_coords = localizacao_coords
        self.__ano_plantacao = ano_plantacao

    @property
    def especie(self):
        return self.__especie

    @property
    def ano_plantacao(self):
        return self.__ano_plantacao

    @property
    def area_de_ocupacao(self):
        return self.__especie.area_de_ocupacao_circular

    def idade(self, ano_a_verificar):
        # perguntar aos profs qual a melhor forma de implementar
        if ano_a_verificar < self.__ano_plantacao:
            print(f"A planta só foi plantada em {self.__ano_plantacao}.")
            return None
        return ano_a_verificar - self.__ano_plantacao

    def pertence_a_area_de_ocupacao_plantacao(self, dadas_as_coordenadas):
        distancia = math_sqrt(
            (self.localizacao_coords[0] - dadas_as_coordenadas[0])**2 +
            (self.localizacao_coords[1] - dadas_as_coordenadas[1])**2
        )
        return distancia < self.__especie.raio_max

    def __str__(self):
        return f"Nome da planta: {self.__especie.nome}\n"      \
               f"Localização GPS: {self.localizacao_coords}\n" \
               f"Ano de plantação: {self.__ano_plantacao}\n"
