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
    native_dict[native_dict_list[i][0]] = {}
    native_dict[native_dict_list[i][0]]["url"] = native_dict_list[i][1]
    native_dict[native_dict_list[i][0]]["Native States"] = native_dict_list[i][2]



def scrapeFlower():
    plant_info = {}
    print("Scrapping...")
    for flower in native_dict.keys():
        print(flower)
        flowerURL = native_dict[flower]["url"]
        page = requests.get(flowerURL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="mw-content-text")
        results_elem = results.find('span', class_="statement")
        common_names = soup.find(id="content")
        common_names_elem = common_names.find('span', "treatment-id-commonName")
        if results_elem != None:
            plant_info[flower] = {}
            if common_names_elem != None:
                plant_info[flower]["Common Name"] = common_names_elem.text
            else:
                plant_info[flower]["Common Name"] = "N/A"
            plant_info[flower]["description"] = results_elem.text
            plant_info[flower]["Native States"] = native_dict[flower]["Native States"]
    return plant_info


pd = scrapeFlower()

file = open("flower_info.txt", 'w')

for key, value in pd.items():
    valueStr = f"{value['Common Name']}\t{value['Native States'].strip()}\t{value['description'].strip()}"
    file.write(f'{key}\t{valueStr}\n')

file.close()
