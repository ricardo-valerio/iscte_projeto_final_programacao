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

    def __str__(self):
        return f"Nome da planta: {self.__especie.nome}\n"      \
               f"Localização GPS: {self.localizacao_coords}\n" \
               f"Ano de plantação: {self.__ano_plantacao}\n"



