import requests
import random
from datetime import datetime, timedelta

def get_weather_data(city, api_key):
    base_url = "http://api.weatherstack.com/current"
    params = {
        'access_key': api_key,
        'query': city,
        'forecast_days': 5 
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        
        if "error" in data:
            return None  # Handle cases where the API returns an error

        return {
            'temperature': data['current']['temperature'],
            'description': data['current']['weather_descriptions'][0],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_speed'],
            'icon': data['current']['weather_icons'][0]
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None



def get_weather_forecast(current_weather):
    forecast = []
    today = datetime.now()

    for i in range(1, 8):  # Simulate next 5 days
        forecast_date = today + timedelta(days=i)
        forecast.append({
            'date': forecast_date.strftime('%Y-%m-%d'),
            'temperature': current_weather['temperature'] + random.uniform(-3, 3),  # Variation
            'description': current_weather['description'],  # Reuse today's description
            'icon': current_weather['icon']  # Reuse today's icon
        })
    return forecast
