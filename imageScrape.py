import requests
from bs4 import BeautifulSoup

flower_file = open("native_plant_dict.txt", 'r')

flower_list = []
flower_dict = {}
for line in flower_file:
    flower_list.append(flower_file.readline())

flower_names = []
for i in range(10):
    flower_list[i] = flower_list[i].split('\t')
    flower_names.append(flower_list[i][0].replace(" ", "_"))
    
flower_links = []
for name in flower_names:
    name = "https://en.wikipedia.org/wiki/" + name
    flower_links.append(name)

def scrapeImages():
    for link in flower_links:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="mw-content-text")
        images = results.find("img")
        if link.replace("https://en.wikipedia.org/wiki/", "") in images['src']:
            flower_dict[link.replace("https://en.wikipedia.org/wiki/", "")] = "https:" + images['src']
    print(flower_dict)

scrapeImages()
