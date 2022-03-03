from urllib import request
import json
import requests

def get_location():
    url = "http://ipinfo.io/json"
    response = request.urlopen(url)
    data = json.load(response)
    print("You are from", data["city"], "and the weather is...")

    return data['loc']


def get_weather(coordinates):
    # Documentation for tomorrow.io: https://docs.tomorrow.io/recipes/build-your-own-weather-app-with-one-call
    # Request the temperature
    end_point = "https://api.tomorrow.io/v4/timelines"
    api_key = "nALqyNxPzcbDWp7gcyYw1bxGD5mlCjWR"

    fields = [
        "windSpeed", 
        "temperature",
        "weatherCode"]

    timesteps = ["current"]

    body = {"location": coordinates, "timesteps": timesteps, "units": "metric", "fields": fields}
    response = requests.post(f'{end_point}?apikey={api_key}', json=body)

    data = response.json()
    data = data["data"]["timelines"][0]["intervals"][0]["values"] # Could be better on parsing
    return data

def determine_weather(data):
    weather_code = data["weatherCode"]
    if weather_code == 0:
        weather = "Unknown"
    elif weather_code == 1000:
        weather = "Clear"
    elif weather_code == 1001:
        weather = "Cloudy"
    elif weather_code == 1100:
        weather = "Mostly Clear"
    elif weather_code == 1101:
        weather = "Partly Cloudy"
    elif weather_code == 1102:
        weather = "Mostly Cloudy"
    elif weather_code == 2000:
        weather = "Fog"
    elif weather_code == 2100:
        weather = "Light Fog"
    elif weather_code == 3000:
        weather = "Light Wind"
    elif weather_code == 3001:
        weather = "Wind"
    elif weather_code == 3002:
        weather = "Strong Wind"
    elif weather_code == 4000:
        weather = "Drizzle"
    elif weather_code == 4001:
        weather = "Rain"
    elif weather_code == 4200:
        weather = "Light Rain"
    elif weather_code == 4201:
        weather = "Heavy Rain"
    elif weather_code == 5000:
        weather = "Snow"
    elif weather_code == 5001:
        weather = "Flurries"
    elif weather_code == 5100:
        weather = "Light Snow"
    elif weather_code == 5101:
        weather = "Heavy Snow"
    elif weather_code == 6000:
        weather = "Freezing Drizzle"
    elif weather_code == 6001:
        weather = "Freezing Rain"
    elif weather_code == 6200:
        weather = "Light Freezing Rain"
    elif weather_code == 6201:
        weather = "Heavy Freezing Rain"
    elif weather_code == 7000:
        weather = "Ice Pellets"
    elif weather_code == 7101:
        weather = "Heavy Ice Pellets"
    elif weather_code == 7102:
        weather = "Light Ice Pellets"
    elif weather_code == 8000:
        weather = "Thunderstorm"
    return weather

def print_weather(data):
    print("Weather:", determine_weather(data))
    print("Temperature:", data["temperature"])
    print("Wind Speed:", data["windSpeed"])

def main():
    print("Getting weather information of your location...")
    coordinates = get_location()
    print_weather(get_weather(coordinates))


if __name__ == "__main__":
    main()