## Python Version Used: 3.11.3

## Description

Projeto final da cadeira de Programação I, no ISCTE


A Gestão Verde administra diversos parques e jardins na região e está a trabalhar para otimizar as suas práticas. Com esse objetivo, pretende desenvolver um sistema que permitirá registar informações sobre plantas, espécies e parques. Esta ferramenta será fundamental para melhorar a sua eficiência e tornar os espaços ainda mais verdes. Para isso começaram por escrever um conjunto de definições e requisitos para o sistema a desenvolver, que depois enviaram para a equipa de desenvolvimento. O resultado foi a seguinte lista de requisitos:

-   Sobre a espécie de uma planta deve ser possível saber o seu nome, tipo de folhagem, se produz fruto ou não, tipo (*árvore* ou *arbusto*), raio do círculo máximo ocupado por uma planta desta espécie e número médio de anos de vida.
-   Deve ser possível registar um parque que guarda informação sobre as suas plantas. Para registar o parque é necessário o seu nome e a sua área de plantação. Inicialmente a lista de plantas deve estar vazia.
-   Deve ser possível apagar um parque, dado o seu nome.

Dado um determinado parque, deverá ser possível:

	-   registar plantas nesse parque, dada a sua espécie, localização e o ano de plantação;
	-   apagar plantas;
	-   listar as plantas existentes;
	-   saber o número de espécies diferentes;
	-   listar as espécies existentes;
	-   listar as plantas existentes, organizadas por espécie e por ano de plantação;
	-   saber a área ocupada pelas plantas;
	-   saber se há espaço para uma dada planta;
	-   saber a idade média das plantas;
	-   saber as plantas cuja idade é igual ou maior ao número médio de anos de vida da sua espécie;
	-   gerar um gráfico com a distribuição de idades das árvores;
	-   gerar um gráfico com a quantidade de plantas por espécie.

Para cada parque é definido um ponto base, a partir do qual são calculadas todas as outras posições. Uma localização indica uma posição relativa a esse ponto base e corresponde a um par de valores decimais (x, y), em que x corresponde ao número de metros para norte e y corresponde ao número de metros para oeste

* [Ver enunciado completo](https://github.com/ricardo-valerio/iscte_projeto_final_programacao/blob/main/trabalho_2023_2024.pdf)

### Dependencies

* Python version >= 3.10 because of the "match" keyword
* matplotlib (pip install matplotlib  ou  py -m pip install matplotlib)
