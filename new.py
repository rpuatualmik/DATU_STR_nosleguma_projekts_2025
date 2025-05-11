import requests
from bs4 import BeautifulSoup
import time

# City URL (Paris)
city = "riga"
k = 0
n = 1


# url = f"https://www.inyourpocket.com/{city}/Sightseeing?p={k}"

# lapa = requests.get(url)

while True:   
    url = f"https://www.inyourpocket.com/{city}/Sightseeing?p={k}"

    lapa = requests.get(url)

    if lapa.status_code != 200:
        if lapa.status_code != 404:
            print(f"Error fetching page {k}: Status code {lapa.status_code}")
        break
    saturs = BeautifulSoup(lapa.content, "html.parser")
    nos = saturs.find("body")
    vietas = nos.find_all("h3", class_ = "bl")
    # adrese = nos.find_all("span", class_="listing_address")
    # print(nos.prettify())


    for item in vietas:
        print(f"{n}.{str(item).lstrip('<h3 class="bl">').rstrip('</h3>')}")
        n = n + 1
    k= k+1
    time.sleep(0.5)

    print(url)
