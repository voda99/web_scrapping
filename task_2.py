import requests
import json
from pprint import pprint
from dotenv import load_dotenv
import os


def get_city_coords(city: str, key: str) -> dict:
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}")
    response_dict = json.loads(response.text)
    return {"lat": response_dict[0]["lat"], "lon": response_dict[0]["lon"]}


def get_city_weather(city: str, key: str) -> dict:
    coord_dict = get_city_coords(city, key)
    lon = coord_dict["lon"]
    lat = coord_dict["lat"]
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}")
    return json.loads(response.text)


load_dotenv("./.env")
key = os.environ["WEATHER_KEY"]
city = input("Please write the city to know the weather\n")
weather_dict = get_city_weather(city, key)
with open("task_2.json", "w") as f:
    json.dump(weather_dict, f, indent=2, ensure_ascii=True)
