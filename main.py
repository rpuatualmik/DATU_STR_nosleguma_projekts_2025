import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from tabulate import tabulate
from dotenv import load_dotenv
import time

class HashTable:
    def __init__(self):
        self.table = {}

    def add(self, key, value):
        self.table[key.lower()] = value

    def get(self, key):
        return self.table.get(key.lower())

    def items(self):
        return self.table.items()

class InvalidCityError(Exception):
    pass

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

while True:
    try:
        city = input("Destination city: ").lower()
        days = int(input("Number of days: "))
        num_places = int(input("Number of places to visit: "))

        weather_url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days={days}&aqi=no&alerts=no"
        weather = requests.get(weather_url).json()

        if "error" in weather:
            raise InvalidCityError
        
        break
    except ValueError:
        print("Input values are incorrect!")
    except InvalidCityError:
        print("Input city not found!")


weather_table = []
for i in range(days):
    day = weather['forecast']['forecastday'][i]
    date = datetime.strptime(day['date'], "%Y-%m-%d").strftime("%d.%m.%Y")
    max_temp = f"{day['day']['maxtemp_c']}°C"
    min_temp = f"{day['day']['mintemp_c']}°C"
    avg_temp = f"{day['day']['avgtemp_c']}°C"
    condition = day['day']['condition']['text'].capitalize()
    weather_table.append([date, max_temp, min_temp, avg_temp, condition])

print("\n🌦️ Weather Forecast:\n")
print(tabulate(weather_table, headers=["Date", "Max Temp", "Min Temp", "Avg Temp", "Condition"], tablefmt="fancy_grid"))

print("\n📌 Gathering sightseeing places...")
n = 1
k = 0
attractions = HashTable()

while True:
    url = f"https://www.inyourpocket.com/{city}/Sightseeing?p={k}"
    page = requests.get(url)

    if page.status_code != 200:
        break

    lapa = BeautifulSoup(page.content, "html.parser")
    body = lapa.find("body")
    names = body.find_all("h3", class_="bl")
    addresses = body.find_all("span", class_="listing_address")
    types = body.find_all("div", class_="category cuisine")

    for name_tag, addr_tag, type_tag in zip(names, addresses, types):
        if n > num_places:
            break
        name = name_tag.get_text(strip=True).title()
        address = addr_tag.get_text(strip=True)
        attraction_type = type_tag.get_text(strip=True) if type_tag else "N/A"
        attractions.add(name, (address, attraction_type))
        n += 1

    k += 1
    time.sleep(0.5)

print("\n🏙️ Sightseeing Plan:\n")
table_data = [(i+1, name.title(), *value) for i, (name, value) in enumerate(attractions.items())]
print(tabulate(table_data, headers=["#", "Name", "Address", "Type"], tablefmt="fancy_grid"))
