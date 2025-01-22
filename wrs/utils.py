import requests
import random
from datetime import datetime, timedelta 

def get_recommendations(weather_data):
    recommendations = {}

    if weather_data['temperature'] < 10:
        recommendations['outfit'] = "Heavy jacket, gloves, and a scarf."
        recommendations['activities'] = ["Stay indoors with a book", "Watch movies", "Visit a museum."]
    elif 10 <= weather_data['temperature'] < 20:
        recommendations['outfit'] = "Sweater and comfortable jeans."
        recommendations['activities'] = ["Go for a walk", "Visit a café", "Explore local attractions."]
    elif weather_data['temperature'] >= 20:
        recommendations['outfit'] = "T-shirt, shorts, and sunglasses."
        recommendations['activities'] = ["Go to the beach", "Have a picnic", "Play outdoor sports."]
    
    if "Rain" in weather_data['description']:
        recommendations['outfit'] += " Don't forget a raincoat or umbrella!"
        recommendations['activities'] = ["Stay indoors and enjoy cozy activities", "Visit a spa."]
    elif "Snow" in weather_data['description']:
        recommendations['outfit'] += " Boots and thermal wear recommended!"
        recommendations['activities'] = ["Build a snowman", "Go skiing or snowboarding."]
    
    return recommendations


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
