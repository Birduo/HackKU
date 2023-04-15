import requests
from bs4 import BeautifulSoup as bs

location = "Kans."
# keep KEYLEN and OFFSET const
KEYLEN = 500
OFFSET = 0

data = {}

while KEYLEN == 500:
    url = f"http://floranorthamerica.org/Special:Ask/format%3Djson/sort%3D/order%3Dasc/offset%3D{OFFSET}/limit%3D500/-5B-5BDistribution::{location}-5D-5D/mainlabel%3D/prettyprint%3Dtrue/unescape%3Dtrue/searchlabel%3DJSON"

    res = requests.get(url).json()
    keys = res["results"].keys()
    KEYLEN = len(keys)

    OFFSET += 500

    print("Key Length: ", KEYLEN)

    data.update(res["results"])

# http://floranorthamerica.org/Thalictrum_thalictroides
flower_url = "http:" + data["Thalictrum thalictroides"]["fullurl"]

flower = requests.get(flower_url)

soup = bs(flower.content, "html.parser")

print(soup)