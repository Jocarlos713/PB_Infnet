import requests

def get_air_quality_data(lat, lon, api_key):

    """
    Obtém dados de qualidade do ar para uma localização específica.
    """

    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    return response.json()
