import requests
from bs4 import BeautifulSoup as bs

def scrapeFNA():
    locations = ["Kans.", "Ala."]

    state_flowers = {}
    us_flowers = {}
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
            us_flowers.update(res['results'])
        
        state_flowers[location] = list(data.keys())

    '''
    DictFormat:
    {
    FlowerName : {
            non-sci name = value
            description = value
            state = [] //list of all states it appears in
            url = value
        }
    }
    '''

    plant_dict = {}
    for location in state_flowers.keys():
        for flr in state_flowers[location]:
            if flr in plant_dict:
                url = plant_dict[flr]['url']
                statelist = plant_dict[flr]['state']
                statelist.append(location)
                plant_dict[flr] = {
                    'url': url,
                    'state': statelist
                }
            else:
                plant_dict[flr] = {
                    'url' : "http:" + us_flowers[flr]['fullurl'],
                    'state' : [location]
                }
    return plant_dict
