# App Atmosfera em Foco
Aplicação interativa em Streamlit que exibe informações sobre o clima e a qualidade do ar de cidades ao redor do mundo, utilizando dados da API OpenWeather.

## Funcionalidades
* Consulta de Cidade: Insira o nome da cidade para buscar informações atmosféricas.
* Requisições e Exibição: Botão para realizar a busca e exibir os dados de clima e qualidade do ar.
* Tabela de Composição da Atmosfera: Exibe as concentrações de poluentes atmosféricos.
* Índice de Qualidade do Ar (AQI): Mostra a qualidade geral do ar com uma métrica visual.
* Dados Climáticos: Temperatura atual, ícone e descrição do clima.
* Gráfico de Barras: Visualiza as concentrações de poluentes em um gráfico interativo.
* Download de Dados: Botão para baixar a tabela de composição da atmosfera em formato CSV.

## Estrutura do Projeto
* app.py: Controla a navegação entre as páginas.
* ui.py: Interface do usuário, incluindo tabelas e gráficos.
* weather_service.py: Requisições à API OpenWeather.
* visualization.py: Funções de visualização de dados.

## Tecnologias Utilizadas
* Streamlit para a interface web.
* Pandas para manipulação de dados.
* Altair para visualizações gráficas.
* Requests para requisições HTTP.