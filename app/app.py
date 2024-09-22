# MY APP FILE

import streamlit as st
import requests
import pandas as pd

# Imagem do cabeçario
st.image("https://img.freepik.com/vetores-gratis/modelo-de-banner-twitch-para-celebracao-do-dia-da-terra_23-2150198457.jpg?t=st=1724625754~exp=1724629354~hmac=b33a6b9719a9bc7bb864f17d910207549b3cfc9d14c9f6f1f5bc1c9eb6c8503a&w=1380")
st.title("Atmosfera em Foco")
st.write("Faça a consulta do clima e atmosfera em sua cidade")

# Chave utilizada nesse Projeto. A indiquei também no arquivo ".env" pois sei que o correto seria buscá-lo de lá porém não aprendi ainda a referenciá-lo 
open_weather_chave = "a825aa3b13360eba852fd894abdded41"

# Input de captura do nome da cidade pelo usuário
city_name = st.text_input("Digite o nome da cidade")

# Botão utilizado para Pesquisar as informações
botao = st.button("Pesquisar")

# Serviço que busca os dados no formato json para utilizar no projeto
def resgata_informacao():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={open_weather_chave}"
    response = requests.get(url)
    return response.json()

# Se o botão se torna "True", os processos dentro do laço são processados
if botao:
    try:
        informacoes = resgata_informacao()# Informação que pega o retorno do serviço "resgata_informaçao"
        descricao = informacoes["weather"][0]["description"]# Descrição do tempo em inglês
        temperatura = f"{round (informacoes["main"]["temp"] -273.15)} °C" # Temperatura transformada em graus Celcius pois a API fornece em graus Kelvin

        coluna1, coluna2, coluna3 = st.columns(3)# Função do Streamlit que divide a tela em tres colunas

        with coluna1:
            st.title(temperatura)# A temperatura ficará na coluna um mais ao canto esquerdo

        with coluna3: # Na coluna três ficará o ícone e a descriçao sobre a qualdiade do ar
            icon_code = informacoes["weather"][0]["icon"]# O ícone está nas informações retornadas pela função "resgata_informacao"
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            st.image(icon_url)
            st.markdown(f"## {descricao}")

        # Como a chamada da API da composição atmosférica exige a latitude e lngitude, esses dados são capturados também da função "resgata_informacao"
        latitude = informacoes["coord"]["lat"]
        longitude = informacoes["coord"]["lon"]
        url_informacao = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={open_weather_chave}"
        rep = requests.get(url_informacao).json()

        
        
        with coluna1:
            qualidade_ar = rep["list"][0]["main"]["aqi"] # A infomação de qualdiade do ar é medida de acordo com os parâmetros da plataforma que retorna um número que representa essa avaliação.

            if qualidade_ar == 1: # De acordo com o número, a informação é exibida
                st.write("Qualidade do ar está boa")
            elif qualidade_ar == 2:
                st.write("Qualidade do ar está razoável")
            elif qualidade_ar == 3:
                st.write("Qualidade do ar está moderada")
            elif qualidade_ar == 4:
                st.write("Qualidade do ar está ruim")
            elif qualidade_ar == 5:
                st.write("Qualidade do ar está Péssima")




        st.subheader("Concentração das dos componentes do ar atmosférico em µg/m³")# Título que antecede a tabela

        componentes = rep["list"][0]["components"] # variável para auxuliar a leitura das outars variáveis
        data = pd.DataFrame({
            "Moléculas" : ["CO", "NO", "NO₂", "O₃", "SO₂", "PM₂.₅", "PM₁₀", "NH₃"],# primeira coluna da tabela é a chave de um dicionário
            "Concentração": [componentes["co"],# Aqui é resgatado também da variável "informacoes"
                            componentes["no"],
                            componentes["no2"],
                            componentes["o3"],
                            componentes["so2"],
                            componentes["pm2_5"],
                            componentes["pm10"],
                            componentes["nh3"]]

        })
        data_sorted = data.sort_values(by='Concentração')# Os dados são organizadoes de acordo com a concentração
        data_sorted.set_index('Moléculas', inplace=True)# Funçao para não exibir a coluna que enumera as linhas
        st.dataframe(data_sorted)
    except:
        st.write("Cidade inválida!")

st.write("""
O Projeto tem como objetivo Exibir para o usuário dados sobre o clima e composição atmosferica para que ele possa, desde de se programar
até mesmo cuidar de sua saúde além de conscientizar a respeito do meio ambiente e sua relação com o clima.
""")
    
st.markdown( # Texto para auxliar os usuários na leitura da tabela.
    """
 #### Efeitos das moléculas em quantidades não recomendadas:
 * Carbon Monoxide (CO): Reduz a capacidade do sangue de transportar oxigênio, podendo causar dores de cabeça, fadiga e problemas cardíacos.
 * Nitrogen Monoxide (NO): Irrita as vias respiratórias e pode agravar doenças respiratórias.
 * Nitrogen Dioxide (NO₂): Irrita as vias respiratórias, agrava asma e bronquite, e aumenta o risco de doenças pulmonares e cardiovasculares.
 * Ozone (O₃): Irrita os pulmões e vias respiratórias, agravando condições respiratórias como asma.
 * Sulphur Dioxide (SO₂): Causa irritação nas vias respiratórias e tosse, e contribui para problemas pulmonares.
 * Fine Particulate Matter (PM₂.₅): Partículas pequenas que podem penetrar profundamente nos pulmões, causando problemas respiratórios e cardiovasculares.
 * Coarse Particulate Matter (PM₁₀): Partículas que causam irritação respiratória e agravam condições como asma.
 * Ammonia (NH₃): Causa irritação nos olhos, nariz e garganta, e problemas respiratórios.

    """
)

st.markdown("""### Links Úteis
O que são as mudanças climáticas?
https://brasil.un.org/pt-br/175180-o-que-s%C3%A3o-mudan%C3%A7as-clim%C3%A1ticas
            
Política Nacional sobre Mudança do Clima
https://antigo.mma.gov.br/clima/politica-nacional-sobre-mudanca-do-clima.html#:~:text=A%20Pol%C3%ADtica%20Nacional%20sobre%20Mudan%C3%A7a,das%20emiss%C3%B5es%20projetadas%20at%C3%A9%202020.
         """)


