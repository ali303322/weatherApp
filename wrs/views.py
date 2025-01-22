from django.shortcuts import render
from django.conf import settings
from .utils import get_weather_data

def weather_view(request):
    city = request.GET.get('city', 'London')  # Default city is London
    api_key = settings.WEATHER_API_KEY
    weather_data = get_weather_data(city, api_key)

    context = {
        'city': city,
        'weather_data': weather_data
    }
    return render(request, 'wrs/weather.html', context)

  



