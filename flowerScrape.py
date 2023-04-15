import requests
from bs4 import BeautifulSoup

native_dict = {"Abronia_fragrans": {"URL": "http://floranorthamerica.org/Abronia_fragrans"}}

def scrapeFlower():
    for flower in native_dict.keys():
        flowerURL = native_dict[flower]["URL"]
        page = requests.get(flowerURL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="mw-content-text")
        results_elem = results.find('span', class_="statement")
        print(results_elem.text)

scrapeFlower()