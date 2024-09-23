import streamlit as st
import pandas as pd
from weather_service import get_weather_data
from air_quality_service import get_air_quality_data
from visualization import display_weather_info, display_air_quality_info

# Imagem do cabeçario
st.image("https://img.freepik.com/vetores-gratis/modelo-de-banner-twitch-para-celebracao-do-dia-da-terra_23-2150198457.jpg?t=st=1724625754~exp=1724629354~hmac=b33a6b9719a9bc7bb864f17d910207549b3cfc9d14c9f6f1f5bc1c9eb6c8503a&w=1380")
st.title("Atmosfera em Foco")
st.write("Faça a consulta do clima e atmosfera em sua cidade")
from utils import api_key

# Entrada do usuário
city_name = st.text_input("Digite o nome da cidade")

# Botão de pesquisa
if st.button("Pesquisar"):
    try:
        # Obtendo informações do clima
        weather_info = get_weather_data(city_name, api_key)
        display_weather_info(weather_info)
        
        # Obtendo informações de qualidade do ar
        lat = weather_info["coord"]["lat"]
        lon = weather_info["coord"]["lon"]
        air_quality_info = get_air_quality_data(lat, lon, api_key)
        display_air_quality_info(air_quality_info)
        
    except Exception as e:
        st.error(f"Erro ao buscar informações: {e}")

# Informações adicionais e links úteis
st.write("""
O Projeto tem como objetivo exibir para o usuário dados sobre o clima e composição atmosférica para que ele possa se programar e cuidar de sua saúde, além de conscientizar sobre o meio ambiente e sua relação com o clima.
""")
st.markdown("""
### Efeitos das moléculas em quantidades não recomendadas:
* **CO**: Reduz a capacidade do sangue de transportar oxigênio, podendo causar dores de cabeça, fadiga e problemas cardíacos.
* **NO**: Irrita as vias respiratórias e pode agravar doenças respiratórias.
* **NO₂**: Irrita as vias respiratórias, agrava asma e bronquite, e aumenta o risco de doenças pulmonares e cardiovasculares.
* **O₃**: Irrita os pulmões e vias respiratórias, agravando condições respiratórias como asma.
* **SO₂**: Causa irritação nas vias respiratórias e tosse, e contribui para problemas pulmonares.
* **PM₂.₅**: Partículas pequenas que podem penetrar profundamente nos pulmões, causando problemas respiratórios e cardiovasculares.
* **PM₁₀**: Partículas que causam irritação respiratória e agravam condições como asma.
* **NH₃**: Causa irritação nos olhos, nariz e garganta, e problemas respiratórios.
""")
st.markdown("""
### Links Úteis
- [O que são as mudanças climáticas?](https://brasil.un.org/pt-br/175180-o-que-s%C3%A3o-mudan%C3%A7as-clim%C3%A1ticas)
- [Política Nacional sobre Mudança do Clima](https://antigo.mma.gov.br/clima/politica-nacional-sobre-mudanca-do-clima.html#:~:text=A%20Pol%C3%ADtica%20Nacional%20sobre%20Mudan%C3%A7a,das%20emiss%C3%B5es%20projetadas%20at%C3%A9%202020.)
""")
