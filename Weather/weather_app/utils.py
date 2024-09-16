import requests
from django.conf import settings
from .models import WeatherData

def fetch_weather(city):
    url = f'http://api.weatherapi.com/v1/current.json?key={settings.WEATHER_API_KEY}&q={city}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def process_weather_data(city):
    data = fetch_weather(city)
    if data:
        weather_data = WeatherData.objects.create(
            city=city,
            temperature=data['current']['temp_c'],
            humidity=data['current']['humidity'],
            condition=data['current']['condition']['text'],
            wind_speed=data['current']['wind_kph']
        )
        return weather_data
    return None