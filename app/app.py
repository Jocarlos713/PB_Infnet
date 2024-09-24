import streamlit as st
from ui import show_home_page, show_header, show_upload_download_page

def main():
    """
    Função principal que controla a navegação do aplicativo Streamlit.
    Exibe diferentes páginas com base na seleção do usuário no menu de navegação lateral.
    
    Funcionalidades:
    - Exibe o cabeçalho da aplicação.
    - Permite navegar entre diferentes páginas: Home, Sobre, Links Úteis e Upload & Download.
    """
    # Barra lateral para navegação
    st.sidebar.title("Navegação")
    page = st.sidebar.selectbox(
        "Escolha a página",
        ["Home", "Sobre", "Links Úteis", "Upload & Download"]
    )

    # Exibir o cabeçalho principal
    show_header()

    # Exibir a página selecionada
    if page == "Home":
        show_home_page()
    elif page == "Sobre":
        show_about_page()
    elif page == "Links Úteis":
        show_useful_links()
    elif page == "Upload & Download":
        show_upload_download_page()

def show_about_page():
    """
    Exibe a página 'Sobre', fornecendo uma descrição do aplicativo e suas funcionalidades.
    """
    st.write("Aplicação de monitoramento de clima e qualidade do ar usando dados da API OpenWeather.")

def show_useful_links():
    """
    Exibe a página 'Links Úteis' com uma lista de links relevantes lidos de um arquivo de texto.
    """
    try:
        # Tenta abrir o arquivo de links úteis
        with open('app/data/noticias.txt', 'r') as arquivo:
            sites = arquivo.readlines()
        # Exibe cada link na página
        for site in sites:
            st.write(site.strip())
    except FileNotFoundError:
        st.error("Arquivo 'noticias.txt' não encontrado.")
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")

if __name__ == '__main__':
    main()
