import requests
from bs4 import BeautifulSoup as bs

locations = ["Ala.", "Alaska", "Ariz.", "Ark.", "Calif.", "Colo.", "Conn.", "Del", "D.C.", "Fla.", "Ga.", "Idaho", "Ill.", "Ind.", "Kans.", "Ky.", "La.", "Maine", "Mass.", "Md.", "Mich.", "Minn.", "Miss.", "Mo.", "Mont.", "N.C.", "N.H.", "N.J.", "Nebr.", "Nev", "N.Mex.", "N.Dak.", "N.Y.", "Ohio", "Okla.", "Oreg.", "Pa.", "R.I.", "S.C.", "S.Dak.", "Tenn.", "Tex.", "Utah", "Va.", "Vt.", "Wash.", "Wis.", "W.Va.", "Wyo."]

len(locations)
state_flowers = {}
for location in locations:
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

        data.update(res["results"])
    
    state_flowers[location] = list(data.keys())

# http://floranorthamerica.org/Thalictrum_thalictroides
flower_url = "http:" + data["Thalictrum thalictroides"]["fullurl"]

flower = requests.get(flower_url)

soup = bs(flower.content, "html.parser")




print(state_flowers)
print(state_flowers.keys())