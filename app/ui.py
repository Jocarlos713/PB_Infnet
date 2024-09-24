import streamlit as st
from weather_service import get_weather_data, get_air_quality_data
from visualization import show_weather_info, show_air_info
import pandas as pd

def show_header():
    """
    Exibe o cabeçalho principal da aplicação, incluindo uma imagem de banner,
    o título e uma breve descrição da funcionalidade do aplicativo.
    """
    st.image("https://img.freepik.com/vetores-gratis/modelo-de-banner-twitch-para-celebracao-do-dia-da-terra_23-2150198457.jpg")
    st.title("Atmosfera em Foco")
    st.write("Faça a consulta do clima e atmosfera em sua cidade")

def show_home_page():
    """
    Exibe a página inicial da aplicação, onde o usuário pode buscar informações
    climáticas e de qualidade do ar para uma cidade específica. As informações
    são armazenadas no `session_state` para persistência durante a sessão.

    Funcionalidades:
    - Entrada de texto para o nome da cidade.
    - Botão para buscar informações climáticas e de qualidade do ar.
    - Exibição dos dados obtidos.
    """
    # Inicializar o estado da cidade se não existir
    if 'city_name' not in st.session_state:
        st.session_state['city_name'] = ''
    if 'weather_info' not in st.session_state:
        st.session_state['weather_info'] = None
    if 'air_quality_info' not in st.session_state:
        st.session_state['air_quality_info'] = None

    # Entrada do usuário para o nome da cidade
    city_name = st.text_input("Digite o nome da cidade", value=st.session_state['city_name'])

    # Quando o botão é pressionado, os dados são salvos no session_state
    if st.button("Pesquisar"):
        st.session_state['city_name'] = city_name
        try:
            # Obtendo informações do clima
            weather_info = get_weather_data(city_name)
            st.session_state['weather_info'] = weather_info  # Salva os dados do clima no session_state
            
            # Obtendo informações de qualidade do ar
            lat, lon = weather_info["coord"]["lat"], weather_info["coord"]["lon"]
            air_quality_info = get_air_quality_data(lat, lon)
            st.session_state['air_quality_info'] = air_quality_info  # Salva os dados de qualidade do ar no session_state

        except Exception as e:
            st.error(f"Erro ao buscar informações: {e}")

    # Exibir dados salvos no session_state se existirem
    if st.session_state['weather_info'] and st.session_state['air_quality_info']:
        show_weather_info(st.session_state['weather_info'])
        show_air_info(st.session_state['air_quality_info'])

def show_upload_download_page():
    """
    Exibe a página de upload e download de arquivos CSV. Permite ao usuário carregar
    arquivos CSV para complementar as informações da aplicação. Os dados carregados
    são armazenados no `session_state` e podem ser baixados novamente.

    Funcionalidades:
    - Upload de arquivos CSV.
    - Exibição dos dados carregados.
    - Opção de download dos dados processados.
    """
    st.header("Upload & Download de Arquivos CSV")

    # Upload de arquivo CSV
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])
    if uploaded_file is not None:
        try:
            # Carregar o CSV para um DataFrame
            df = pd.read_csv(uploaded_file)
            st.session_state['uploaded_data'] = df  # Armazenar os dados no session_state
            st.success("Arquivo carregado com sucesso!")
            st.write("Dados carregados:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {e}")

    # Exibir dados do arquivo carregado, se existirem
    if 'uploaded_data' in st.session_state:
        st.subheader("Dados do Arquivo Carregado")
        st.dataframe(st.session_state['uploaded_data'])

        # Opção de download do arquivo carregado
        csv = st.session_state['uploaded_data'].to_csv(index=False)
        st.download_button(
            label="Baixar dados como CSV",
            data=csv,
            file_name="dados_processados.csv",
            mime="text/csv"
        )

