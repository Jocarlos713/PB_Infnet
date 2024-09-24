import requests
from datetime import datetime
import streamlit as st

# Definindo a chave da API do OpenWeather
API_KEY = "a825aa3b13360eba852fd894abdded41"

@st.cache_data(ttl=3600)
def get_weather_data(city_name):
    """
    Obtém os dados de clima para uma cidade específica utilizando a API do OpenWeather.
    Os resultados são cacheados por 1 hora para evitar consultas repetidas à API.

    Parâmetros:
    city_name (str): Nome da cidade para a qual os dados climáticos serão buscados.

    Retorno:
    dict: Dicionário contendo as informações climáticas da cidade, incluindo temperatura,
          descrição do clima, umidade, velocidade do vento, etc.

    Exceção:
    Levanta uma exceção HTTP se a requisição falhar.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

@st.cache_data(ttl=3600)
def get_air_quality_data(lat, lon):
    """
    Obtém os dados de qualidade do ar para uma localização específica (latitude e longitude)
    utilizando a API do OpenWeather. Os resultados são cacheados por 1 hora para evitar consultas
    repetidas à API.

    Parâmetros:
    lat (float): Latitude da localização para a qual os dados de qualidade do ar serão buscados.
    lon (float): Longitude da localização para a qual os dados de qualidade do ar serão buscados.

    Retorno:
    dict: Dicionário contendo as informações de qualidade do ar, incluindo índices de poluentes como CO,
          NO, NO2, O3, SO2, PM2.5, PM10, e NH3.

    Exceção:
    Levanta uma exceção HTTP se a requisição falhar.
    """
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
