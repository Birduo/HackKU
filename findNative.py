from lab import scrapeFNA
from webScrape import scrapeWiki


def removeNonNative():
    plant_dict = scrapeFNA()
    native_plants = scrapeWiki()
    native_plant_dict = {}
    for key, value in native_plants.items():
        for flower in value:
            if flower in plant_dict.keys():
                if not ('native_states' in plant_dict[flower].keys()):
                    plant_dict[flower]['native_states'] = [key]
                else:
                    native_states = plant_dict[flower]['native_states']
                    native_states.append(key)
                    plant_dict[flower]['native_states'] = native_states
    for key, value in plant_dict.items():
        if 'native_states' in value.keys():
            new_val = {'url' : value['url'], 'native_states' : value['native_states']}
            native_plant_dict[key] = new_val
    return native_plant_dict

'''
{
SciName : {
        url: value
        native_states: [value, value]
    }
}
'''


if __name__ == "__main__":
    pd = removeNonNative()
    file = open('native_plant_dict.txt', 'w')
    for key, value in pd.items():
        valueStr = f"{value['url']}\t{value['native_states']}"
        file.write(f'{key}\t{valueStr}\n')
