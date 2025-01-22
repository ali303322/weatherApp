from django.shortcuts import render
from django.conf import settings
from .utils import get_weather_data, get_weather_forecast

def weather_view(request):
    city = request.GET.get('city', 'Fes')  # Default city is London
    api_key = settings.WEATHER_API_KEY
    current_weather = get_weather_data(city, api_key)

    if current_weather is None:
        return render(request, 'weatherapp/error.html', {'message': 'Unable to fetch weather data.'})
    
    # Now fetch 5-day forecast data using current weather
    weather_forecast = get_weather_forecast(current_weather)

    # Send both current weather and forecast data to the template
    context = {
        'city': city,
        'current_weather': current_weather,
        'weather_forecast': weather_forecast
    }
   
    return render(request, 'wrs/weather.html', context)

  



