import requests
from bs4 import BeautifulSoup

#native_dict = {"Abronia_fragrans": {"URL": "http://floranorthamerica.org/Abronia_fragrans"}}

native_dict_file = open("native_plant_dict.txt", 'r')
native_dict_list = []
for line in native_dict_file:
    native_dict_list.append(native_dict_file.readline())

native_dict = {}
for i in range(len(native_dict_list)):
    native_dict_list[i] = native_dict_list[i].split('\t')
    native_dict[native_dict_list[i][0]] = native_dict_list[i][1]



def scrapeFlower():
    plant_info = {}
    print("Scrapping...")
    for flower in native_dict.keys():
        print(flower)
        flowerURL = native_dict[flower]
        page = requests.get(flowerURL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="mw-content-text")
        results_elem = results.find('span', class_="statement")
        if results_elem != None:
            plant_info[flower] = results_elem.text

scrapeFlower()
