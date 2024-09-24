import streamlit as st
import pandas as pd
import altair as alt

def show_weather_info(weather_info):
    """
    Exibe informações climáticas atuais, incluindo temperatura e descrição do clima,
    com um ícone ilustrativo.

    Parâmetros:
    weather_info (dict): Dicionário contendo as informações climáticas obtidas da API.
    """
    descricao = weather_info["weather"][0]["description"].capitalize()
    temperatura = f"{round(weather_info['main']['temp']- 273.15)} °C"
    icon_code = weather_info["weather"][0]["icon"]
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

    # Layout de duas colunas
    temp_column, icon_column = st.columns([3, 1])
    with temp_column:
        st.header("Clima Atual")
        st.write(f"**Temperatura:** {temperatura}")
        st.write(f"**Descrição:** {descricao}")
    with icon_column:
        st.image(icon_url, caption="Ícone do clima")

# Lista de níveis de qualidade do ar
AQI_LEVELS = ["Boa", "Razoável", "Moderada", "Ruim", "Péssima"]

def show_air_info(air_quality_info):
    """
    Exibe informações sobre a qualidade do ar, incluindo o índice de qualidade do ar (AQI)
    e a concentração de vários poluentes em µg/m³. Também permite o download dos dados
    e exibe um gráfico de barras com as concentrações.

    Parâmetros:
    air_quality_info (dict): Dicionário contendo as informações de qualidade do ar obtidas da API.
    """
    # Obtendo o nível de qualidade do ar
    qualidade_ar = air_quality_info["list"][0]["main"]["aqi"]
    aqi_label = AQI_LEVELS[qualidade_ar - 1]

    st.header("Qualidade do Ar")
    st.metric(label="Índice de Qualidade do Ar", value=aqi_label)

    # Exibir concentração dos componentes do ar
    st.subheader("Concentração dos Componentes do Ar (µg/m³)")
    componentes = air_quality_info["list"][0]["components"]
    data = pd.DataFrame({
        "Molécula": ["CO", "NO", "NO₂", "O₃", "SO₂", "PM₂.₅", "PM₁₀", "NH₃"],
        "Concentração (µg/m³)": [
            componentes["co"], componentes["no"], componentes["no2"],
            componentes["o3"], componentes["so2"], componentes["pm2_5"],
            componentes["pm10"], componentes["nh3"]
        ]
    }).sort_values(by="Concentração (µg/m³)", ascending=False)
    
    st.dataframe(data)

    def display_csv_download_button(data):
        """
        Exibe um botão para download dos dados de concentração dos poluentes em formato CSV.

        Parâmetros:
        data (pd.DataFrame): DataFrame contendo as concentrações dos poluentes.
        """
        csv_data = data.to_csv(index=False)
        st.download_button(
            label="Baixar dados como CSV",
            data=csv_data,
            file_name="dados_processados.csv",
            mime="text/csv"
        )

    def display_bar_chart(data):
        """
        Exibe um gráfico de barras das concentrações dos poluentes atmosféricos.

        Parâmetros:
        data (pd.DataFrame): DataFrame contendo as concentrações dos poluentes.
        """
        bar_chart = alt.Chart(data).mark_bar().encode(
            x=alt.X('Molécula', sort=None),
            y='Concentração (µg/m³)',
            color='Molécula'
        ).properties(
            width=600,
            height=400,
            title="Concentração dos Componentes do Ar"
        )
        st.altair_chart(bar_chart, use_container_width=True)

    # Exibir o botão e o gráfico
    display_csv_download_button(data)
    display_bar_chart(data)

    # Verificar e inicializar o estado da molécula selecionada
    if 'selected_molecule' not in st.session_state:
        st.session_state['selected_molecule'] = data['Molécula'].iloc[0]

    def on_molecule_select():
        """
        Função de callback para atualizar o estado da molécula selecionada
        no session_state quando o usuário muda a seleção.
        """
        st.session_state['selected_molecule'] = st.session_state['selectbox_molecule']

    # Selectbox com chave dinâmica baseada no identificador de sessão
    st.selectbox(
        "Selecione uma molécula para ver detalhes",
        data['Molécula'],
        index=data['Molécula'].tolist().index(st.session_state['selected_molecule']),
        key='selectbox_molecule',
        on_change=on_molecule_select
    )

    # Exibir detalhes da molécula selecionada
    selected_molecule = st.session_state['selected_molecule']
    concentration = data.loc[data['Molécula'] == selected_molecule, 'Concentração (µg/m³)'].values[0]
    st.write(f"**Concentração de {selected_molecule}:** {concentration} µg/m³")
