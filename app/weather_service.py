import requests

def get_weather_data(city_name, api_key):

    """
    Obtém os dados de clima para uma cidade específica.
    """
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    return response.json()
