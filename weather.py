from urllib import request
import json
import requests

def get_location():
    url = "http://ipinfo.io/json"
    response = request.urlopen(url)
    data = json.load(response)

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
    if data["weatherCode"] == 0:
        weather = "Unknown"
    elif data["weatherCode"] == 1000:
        weather = "Clear"
    elif data["weatherCode"] == 1001:
        weather = "Cloudy"
    elif data["weatherCode"] == 1100:
        weather = "Mostly Clear"
    elif data["weatherCode"] == 1101:
        weather = "Partly Cloudy"
    elif data["weatherCode"] == 1102:
        weather = "Mostly Cloudy"
    elif data["weatherCode"] == 2000:
        weather = "Fog"
    elif data["weatherCode"] == 2100:
        weather = "Light Fog"
    elif data["weatherCode"] == 3000:
        weather = "Light Wind"
    elif data["weatherCode"] == 3001:
        weather = "Wind"
    elif data["weatherCode"] == 3002:
        weather = "Strong Wind"
    elif data["weatherCode"] == 4000:
        weather = "Drizzle"
    elif data["weatherCode"] == 4001:
        weather = "Rain"
    elif data["weatherCode"] == 4200:
        weather = "Light Rain"
    elif data["weatherCode"] == 4201:
        weather = "Heavy Rain"
    elif data["weatherCode"] == 5000:
        weather = "Snow"
    elif data["weatherCode"] == 5001:
        weather = "Flurries"
    elif data["weatherCode"] == 5100:
        weather = "Light Snow"
    elif data["weatherCode"] == 5101:
        weather = "Heavy Snow"
    elif data["weatherCode"] == 6000:
        weather = "Freezing Drizzle"
    elif data["weatherCode"] == 6001:
        weather = "Freezing Rain"
    elif data["weatherCode"] == 6200:
        weather = "Light Freezing Rain"
    elif data["weatherCode"] == 6201:
        weather = "Heavy Freezing Rain"
    elif data["weatherCode"] == 7000:
        weather = "Ice Pellets"
    elif data["weatherCode"] == 7101:
        weather = "Heavy Ice Pellets"
    elif data["weatherCode"] == 7102:
        weather = "Light Ice Pellets"
    elif data["weatherCode"] == 8000:
        weather = "Thunderstorm"
    return weather

def print_weather(data):
    #print("Weather: ", determine_weather(data["weatherCode"]))
    print("Temperature: ", data["temperature"])
    print("Wind Speed: ", data["windSpeed"])
    print(data["weatherCode"])

def main():
    print("Getting weather information of your location...")
    coordinates = get_location()
    print_weather(get_weather(coordinates))


if __name__ == "__main__":
    main()