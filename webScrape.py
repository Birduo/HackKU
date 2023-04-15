import requests
from bs4 import BeautifulSoup

def scrapeWiki():
    #State names could be cleaned up, specifically Georgia, NY, and Washington
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia_(U.S._state)", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New_Hampshire", "New_Jersey", "New_Mexico", "New_York_(state)", "North_Carolina", "North_Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode_Island", "South_Carolina", "South_Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington_(state)", "West Virginia", "Wisconsin", "Wyoming"]
    native_plants = {} #Final dict with all data

    for state in states:
        URL = f"https://en.wikipedia.org/wiki/Category:Flora_of_{state}"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="mw-pages")

        names = []
        next_page = "initial"

        while next_page != None:
            result_elems = results.find_all('div', class_="mw-category-group")
            for result_elem in result_elems:
                name_elems = result_elem.find_all("a")
                for name_elem in name_elems:
                    name = name_elem.text
                    names.append(name)
            
            
            next_page = results.find_all(title=f"Category:Flora of {state}")
            if next_page == []:
                next_page = None
            
            if next_page != None:
                next_page = next_page[1]
                if next_page.text == "previous page":
                    next_page = None

            if next_page != None:
                next_link = "https://en.wikipedia.org" + next_page["href"]
                
                page = requests.get(next_link)
                soup = BeautifulSoup(page.content, "html.parser")
                results = soup.find(id="mw-pages")
        native_plants[state.replace("_", " ")] = names
        print(native_plants)
    return native_plants
