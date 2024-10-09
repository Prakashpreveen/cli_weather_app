import requests
import datetime as dt
import sys
from dotenv import load_dotenv
import os

load_dotenv(override=True)

if len(sys.argv) < 2:
    print("Usage : python main.py city_name unit")
    sys.exit(1)

CITY = sys.argv[1]
UNIT = sys.argv[2]

if (UNIT != "metric") and (UNIT != "imperial"):
    print("UNIT can take only metric or imperial")
    sys.exit(1)

def format_datetime(datetime,unit):
    if unit == "metric":
         return dt.datetime.fromtimestamp(datetime,dt.UTC).strftime("%d/%m/%Y %H:%M:%S")
    return dt.datetime.fromtimestamp(datetime,dt.UTC).strftime("%m/%d/%Y %H:%M:%S")
    


temp_unit = "°C" if UNIT == "metric" else "°F"
wind_speed_unit = "m/s" if UNIT == "metric" else "mph"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv("API_KEY")

url = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=" + UNIT
response = requests.get(url).json()

temp = response["main"]["temp"]
feels_like = response["main"]["feels_like"]
wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_time = format_datetime((response["sys"]["sunrise"] + response["timezone"]),UNIT)
sunset_time = format_datetime((response["sys"]["sunset"] + response["timezone"]),UNIT)

print(f"Weather for {CITY.capitalize()}")
print(f"Temperature: {temp:.2f}{temp_unit}")
print(f"Feels like: {feels_like:.2f}{temp_unit}")
print(f"Humidity: {humidity} % ")
print(f"Wind Speed: {wind_speed} {wind_speed_unit}")
print(f"Description: {description}")
print(f"Sunrise Time: {sunrise_time}")
print(f"Sunset Time: {sunset_time}")