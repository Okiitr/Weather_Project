from django.shortcuts import render
from .models import WeatherData
from .utils import *
from .forms import SearchForm


def weather_home(request):
    city = 'Hyderabad'  
    weather_data = None
    alert = None
    avg_temp = None
    avg_humidity = None

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = process_weather_data(city)
            
            if weather_data:
                recent_data = WeatherData.objects.filter(city=city).order_by('-recorded_at')[:24]
                if recent_data:
                    avg_temp = float(sum(d.temperature for d in recent_data) / len(recent_data))
                    avg_humidity = float(sum(d.humidity for d in recent_data) / len(recent_data))

                # Check for extreme conditions
                if weather_data and (weather_data.temperature > 45 or weather_data.temperature < 0):
                    alert = "Extreme Temperature Alert!"
                elif weather_data and weather_data.wind_speed > 100:
                    alert = "Extreme Wind Speed Alert!"
            else:
                alert = f"Weather data for the {city} city could not be found."
        else:
            form = SearchForm()
    else:
        form = SearchForm()
        
    context = {
        'weather_data': weather_data,
        'avg_temp': avg_temp,
        'avg_humidity': avg_humidity,
        'alert': alert,
        'form': form,  
    }
    return render(request, 'home.html', context)
