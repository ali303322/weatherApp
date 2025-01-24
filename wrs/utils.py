import requests
import random
from datetime import datetime, timedelta 



def get_recommendations(weather_data):
    recommendations = {
        'outfit': '',
        'activities': []
    }

    # Outfit recommendations based on temperature
    if weather_data['temperature'] < 10:
        recommendations['outfit'] = "Heavy jacket, gloves, and a scarf."
        recommendations['activities'] = [
            {'activity': 'Reading', 'description': 'Stay indoors with a good book.', 'image': 'activities/reading.jpg'},
            {'activity': 'Movies', 'description': 'Watch your favorite movies.', 'image': 'activities/movie.jpg'},
            {'activity': 'Museum', 'description': 'Visit a local museum.', 'image': 'activities/museum.jpg'},
        ]
    elif 10 <= weather_data['temperature'] < 20:
        recommendations['outfit'] = "Sweater and comfortable jeans."
        recommendations['activities'] = [
            {'activity': 'Walking', 'description': 'Go for a relaxing walk.', 'image': 'activities/walking.jpg'},
            {'activity': 'Cafe', 'description': 'Visit a cozy café.', 'image': 'activities/cofee.jpg'},
            {'activity': 'Exploring', 'description': 'Explore local attractions.', 'image': 'activities/exploring.jpg'},
        ]
    elif weather_data['temperature'] >= 20:
        recommendations['outfit'] = "T-shirt, shorts, and sunglasses."
        recommendations['activities'] = [
            {'activity': 'Beach', 'description': 'Go to the beach and enjoy the sun.', 'image': 'activities/beach.jpg'},
            {'activity': 'Picnic', 'description': 'Have a picnic in the park.', 'image': 'activities/picnic.jpg'},
            {'activity': 'Outdoor Sports', 'description': 'Play outdoor sports with friends.', 'image': 'activities/outdoor.jpg'},
        ]

    # Adjust recommendations based on weather description
    if "Rain" in weather_data['description']:
        recommendations['outfit'] += " Don't forget a raincoat or umbrella!"
        recommendations['activities'] = [
            {'activity': 'Cozy Indoors', 'description': 'Stay indoors and enjoy cozy activities.', 'image': 'activities/cozy.jpg'},
            {'activity': 'Spa', 'description': 'Relax with a spa day.', 'image': 'activities/spa.jpg'},
        ]
    elif "Snow" in weather_data['description']:
        recommendations['outfit'] += " Boots and thermal wear recommended!"
        recommendations['activities'] = [
            {'activity': 'Snowman', 'description': 'Build a snowman with friends.', 'image': 'activities/snowmen.jpg'},
            {'activity': 'Skiing', 'description': 'Go skiing or snowboarding.', 'image': 'activities/skiing.jpg'},
        ]

    return recommendations

    

def get_weather_data(city, api_key):
    base_url = "http://api.weatherstack.com/current"
    params = {
        'access_key': api_key,
        'query': city,
        'forecast_days': 7
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
