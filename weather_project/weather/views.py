from django.shortcuts import render
from .forms import WeatherForm
from .models import WeatherCity

import requests
from geopy.geocoders import Nominatim


def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="weather")
    location = geolocator.geocode(city_name)
    if location:
        return (location.latitude, location.longitude)
    return None

def index(request):
    weather_data = None
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid(): 
            city = form.cleaned_data['city']
            access_key = 'bba32021-f783-413c-b9ee-cc8bbc5b04c5'
            headers = {'X-Yandex-Weather-Key': access_key}
            cooridinates = get_coordinates(city)
            if cooridinates:
                response = requests.get(f"https://api.weather.yandex.ru/v2/forecast?lat={cooridinates[0]}&lon={cooridinates[1]}&lang=ru_RU", headers=headers)
                if response.status_code == 200:
                    weather_data = response.json()
                    WeatherCity.objects.get_or_create(city=city)
            else:
                weather_data = {'error': 'Не удалось получить данные о погоде'}
    else:
        form = WeatherForm()

    return render(request, 'weather/index.html', {'weather_data': weather_data, 'form': form})
