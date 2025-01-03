import requests

api_key = "b4d4e12d21ecaf8b2da82b46ad1a419c"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 51.72,
    "lon": -0.83,
    "appid": api_key
}

weather_response = requests.get(OWM_endpoint, params=parameters)
weather_response.raise_for_status()
print(weather_response.json())