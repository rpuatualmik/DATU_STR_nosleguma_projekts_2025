from dotenv import load_dotenv
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup


# city = input("Destination city: ").lower()
city = "paris" # testa vertibas
# dienas = int(input("Number of days: "))
dienas = 5 # testa vertibas
days = str(dienas)

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")


# url = "http://api.weatherapi.com/v1/forecast.json?key=" + API_KEY + "&q=" + city + "&days=" + days + "&aqi=no&alerts=no"

# laikapstakli = requests.get(url).json() # iegust laika prognozi
# for i in range (dienas):
#     datums = str(laikapstakli['forecast']['forecastday'][i]['date'])
#     datums = datetime.strptime(datums, "%Y-%m-%d")
#     datums = datums.strftime("%d.%m.%Y")
#     print(f"{datums}, max temperature:{laikapstakli['forecast']['forecastday'][i]['day']['maxtemp_c']}\u00b0C, min temperature:{laikapstakli['forecast']['forecastday'][i]['day']['mintemp_c']}\u00b0C, average temperature:{laikapstakli['forecast']['forecastday'][i]['day']['avgtemp_c']}\u00b0C, {(laikapstakli['forecast']['forecastday'][i]['day']['condition']['text']).lower()}")


# with open('countries-codes.csv', 'r',  encoding = "utf-8", errors = 'ignore') as kodi: #iegust atbilstoso valsts kodu
#     for rinda in kodi:
#         valsts, kods_ne = rinda.split(';')
#         if valsts == laikapstakli['location']['country']:
#             kods = kods_ne.lower()
#         else:
#             pass
#18-34 gatavs kods, vienk nokomentets, lai netere API limitus ar katru testu

# kods = kods + '/' + city
kods = "fr/paris" # testesanas vertibas

links = "https://www.booking.com/attractions/searchresults/"+ kods +".en.html?adplat=www-index-web_shell_header-attraction-missing_creative-2XJT9BJTHf0ahEqma5wszk&label=gen173nr-1BCAEoggI46AdIM1gEaIoBiAEBmAEauAEXyAEM2AEB6AEBiAIBqAIDuALn2vzABsACAdICJDlmOWRkNjJjLWY2NTItNDQzMS04OGYzLTM3ZmI3YTJlMTljNNgCBeACAQ&distribution_id=2XJT9BJTHf0ahEqma5wszk&aid=304142&client_name=b-web-shell-bff"

lapa = requests.get(links)
# print(lapa.status_code)
if lapa.status_code == 200:
    lapas_saturs = BeautifulSoup(lapa.content, "html.parser")
    # print(lapas_saturs.prettify())
    
    ltr = lapas_saturs.find("div", dir="ltr")
    nos = lapas_saturs.find("body")
    div1 = nos.find("div", dir = "ltr")
    div2 = div1.find("div", class_ = "css-eyu4aa")
    div3 = div2.find("div", class_="css-ngwlx1")
    div4 = div3.find("div", class_ = "css-4pdaj4")
    div5 = div4.find("div", class_ = "css-f10ke9")
    div6 = div5.find("div", class_ = "css-1ie5gar")
    main = div6.find("main", class_ = "css-zq8daf")
    div7 = main.find("div", attrs={'data-testid': 'sr-list'})

    print(f"Found {len(div7)} attraction blocks")
    # print(div5)
    for item in div7:
        print("\n\n\n\n")

        print(item)

