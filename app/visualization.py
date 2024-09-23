import streamlit as st
import pandas as pd


def display_weather_info(weather_info):

    """
    Exibe informações do clima.
    """

    descricao = weather_info["weather"][0]["description"]
    temperatura = f"{round(weather_info['main']['temp'] - 273.15)} °C"

    coluna1, coluna2, coluna3 = st.columns(3)
    
    with coluna1:
        st.title(temperatura)
    
    with coluna3:
        icon_code = weather_info["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        st.image(icon_url)
        st.markdown(f"## {descricao}")


def display_air_quality_info(air_quality_info):

    """
    Exibe informações de qualidade do ar.
    """
    
    qualidade_ar = air_quality_info["list"][0]["main"]["aqi"]

    st.subheader("Qualidade do ar:")
    if qualidade_ar == 1:
        st.write("Qualidade do ar está boa")
    elif qualidade_ar == 2:
        st.write("Qualidade do ar está razoável")
    elif qualidade_ar == 3:
        st.write("Qualidade do ar está moderada")
    elif qualidade_ar == 4:
        st.write("Qualidade do ar está ruim")
    elif qualidade_ar == 5:
        st.write("Qualidade do ar está péssima")

    st.subheader("Concentração dos componentes do ar atmosférico em µg/m³")
    componentes = air_quality_info["list"][0]["components"]
    data = pd.DataFrame({
        "Moléculas": ["CO", "NO", "NO₂", "O₃", "SO₂", "PM₂.₅", "PM₁₀", "NH₃"],
        "Concentração": [
            componentes["co"], componentes["no"], componentes["no2"],
            componentes["o3"], componentes["so2"], componentes["pm2_5"],
            componentes["pm10"], componentes["nh3"]
        ]
    })
    data_sorted = data.sort_values(by='Concentração')
    data_sorted.set_index('Moléculas', inplace=True)
    st.dataframe(data_sorted)
