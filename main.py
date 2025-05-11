from dotenv import load_dotenv
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import time
from tabulate import tabulate 


load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

city = input("Destination city: ").lower()
num_days = int(input("Number of days: "))
num_places = int(input("Number of places to visit: "))


print("\n🌦️ Weather Forecast:")
weather_url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days={num_days}&aqi=no&alerts=no"
weather = requests.get(weather_url).json()

weather_data = []
for i in range(num_days):
    day = weather['forecast']['forecastday'][i]['day']
    date = datetime.strptime(weather['forecast']['forecastday'][i]['date'], "%Y-%m-%d")
    weather_data.append([
        date.strftime('%d.%m.%Y.'),
        f"{day['maxtemp_c']}°C",
        f"{day['mintemp_c']}°C",
        f"{day['avgtemp_c']}°C",
        day['condition']['text']
    ])


print(tabulate(weather_data, headers=["Date", "Max Temp", "Min Temp", "Avg Temp", "Condition"], tablefmt="grid"))
print("\n")


print("\n📌 Gathering sightseeing places...\n")
n, k = 1, 0
attractions_data = []

while n <= num_places:
    url = f"https://www.inyourpocket.com/{city}/Sightseeing?p={k}"
    r = requests.get(url)
    if r.status_code != 200:
        break

    lapa = BeautifulSoup(r.content, "html.parser")
    places = lapa.find_all("h3", class_="bl")
    addresses = lapa.find_all("span", class_="listing_address")
    attraction_types = lapa.find_all("div", class_="category cuisine")

    for name_tag, addr_tag, type_tag in zip(places, addresses, attraction_types):
        if n > num_places:
            break

        name = name_tag.get_text(strip=True)
        address = addr_tag.get_text(strip=True)
        attraction_type = type_tag.get_text(strip=True) if type_tag else "Unknown" 
        
        attractions_data.append([n, name, address, attraction_type])
        n += 1
    k += 1
    time.sleep(0.5)

print(tabulate(attractions_data, headers=["#", "Attraction", "Address", "Attraction Type"], tablefmt="grid"))

# print(attraction_type)
