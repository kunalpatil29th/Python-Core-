# weather_app_sim.py

"""
Project: Weather App Simulator
Simulates fetching weather data for different cities using a mock API.
"""

weather_data = {
    "New York": {"temp": "22°C", "condition": "Sunny"},
    "London": {"temp": "15°C", "condition": "Rainy"},
    "Mumbai": {"temp": "30°C", "condition": "Humid"}
}

def get_weather(city):
    city = city.title()
    data = weather_data.get(city, "City data not available")
    if isinstance(data, dict):
        return f"Weather in {city}: {data['temp']}, {data['condition']}"
    return data

print(get_weather("mumbai"))
print(get_weather("paris"))
