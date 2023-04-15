import requests
from bs4 import BeautifulSoup

#native_dict = {"Abronia_fragrans": {"URL": "http://floranorthamerica.org/Abronia_fragrans"}}

native_dict_file = open("native_plant_dict.txt", 'r')

native_dict_text = native_dict_file.read()

native_list = native_dict_text.split("\n")







'''
native_dict_text = "{" + native_dict_text + "}"
native_dict = eval(native_dict_text)

def scrapeFlower():
    for flower in native_dict.keys():
        flowerURL = native_dict[flower]["URL"]
        page = requests.get(flowerURL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="mw-content-text")
        results_elem = results.find('span', class_="statement")
        print(results_elem.text)

scrapeFlower()
'''
