import requests
from bs4 import BeautifulSoup as bs

def scrapeFNA():
    locations = ["Ala.", "Alaska", "Ariz.", "Ark.", "Calif.", "Colo.", "Conn.", "Del.", "D.C.", "Fla.", "Ga.", "Hawaii", "Idaho", "Ill.", "Iowa", "Ind.", "Kans.", "Ky.", "La.", "Maine", "Mass.", "Md.", "Mich.", "Minn.", "Miss.", "Mo.", "Mont.", "N.C.", "N.H.", "N.J.", "Nebr.", "Nev.", "N.Mex.", "N.Dak.", "N.Y.", "Ohio", "Okla.", "Oreg.", "Pa.", "R.I.", "S.C.", "S.Dak.", "Tenn.", "Tex.", "Utah", "Va.", "Vt.", "Wash.", "Wis.", "W.Va.", "Wyo."]

    state_flowers = {}
    us_flowers = {}
    for location in locations:
        print(f'scraping {location}')
        # keep KEYLEN and OFFSET const
        KEYLEN = 500
        OFFSET = 0
        data = {}

        while KEYLEN == 500:
            url = f"http://floranorthamerica.org/Special:Ask/format%3Djson/sort%3D/order%3Dasc/offset%3D{OFFSET}/limit%3D500/-5B-5BDistribution::{location}-5D-5D/mainlabel%3D/prettyprint%3Dtrue/unescape%3Dtrue/searchlabel%3DJSON"

            res = requests.get(url).json()
            keys = res["results"].keys()

            KEYLEN = len(keys)
            #print(f'{OFFSET}')

            OFFSET += 500

            for key in keys:
                if key in data.keys():
                    KEYLEN = 0

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
    abbreviationToWikiName = {
        "Ala.":"Alabama", 
        "Alaska":"Alaska", 
        "Ariz.":"Arizona",
        "Ark.":"Arkansas", 
        "Calif.":"California", 
        "Colo.":"Colorado", 
        "Conn.":"Connecticut", 
        "Del.":"Delaware", 
        "D.C.": "Washington,_D.C.",
        "Fla.":"Florida", 
        "Ga.":"Georgia_(U.S._state)", 
        "Hawaii" :"Hawaii", 
        "Idaho":"Idaho", 
        "Ill.":"Illinois", 
        "Ind.":"Indiana", 
        "Iowa":"Iowa", 
        "Kans.": "Kansas", 
        "Ky.":"Kentucky", 
        "La.":"Louisiana", 
        "Maine":"Maine", 
        "Md.":"Maryland", 
        "Mass.":"Massachusetts", 
        "Mich.":"Michigan", 
        "Minn.":"Minnesota", 
        "Miss.":"Mississippi", 
        "Mo.":"Missouri", 
        "Mont.":"Montana", 
        "Nebr.":"Nebraska", 
        "Nev.":"Nevada", 
        "N.H.":"New_Hampshire", 
        "N.J.":"New_Jersey", 
        "N.Mex.":"New_Mexico", 
        "N.Y.":"New_York_(state)", 
        "N.C.":"North_Carolina", 
        "N.Dak.":"North_Dakota", 
        "Ohio":"Ohio", 
        "Okla.":"Oklahoma", 
        "Oreg.":"Oregon", 
        "Pa.":"Pennsylvania", 
        "R.I.":"Rhode_Island", 
        "S.C.":"South_Carolina", 
        "S.Dak.":"South_Dakota", 
        "Tenn.":"Tennessee", 
        "Tex.":"Texas", 
        "Utah":"Utah", 
        "Vt.":"Vermont", 
        "Va.":"Virginia", 
        "Wash.":"Washington_(state)", 
        "W.Va.":"West Virginia", 
        "Wis.":"Wisconsin", 
        "Wyo.":"Wyoming"
    }
    for location in state_flowers.keys():
        print(f"going through location: {location}")
        for flr in state_flowers[location]:
            print(f"going through flower {flr}")
            if flr in plant_dict:
                url = plant_dict[flr]['url']
                statelist = plant_dict[flr]['state']
                statelist.append(abbreviationToWikiName[location])
                plant_dict[flr] = {
                    'url': url,
                    'state': statelist
                }
            else:
                plant_dict[flr] = {
                    'url' : "http:" + us_flowers[flr]['fullurl'],
                    'state' : [abbreviationToWikiName[location]]
                }
    return plant_dict

