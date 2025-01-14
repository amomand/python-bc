import requests

api_key = "b4d4e12d21ecaf8b2da82b46ad1a419c"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 51.72,
    "lon": -0.83,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data=response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella!")