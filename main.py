
import requests
from pprint import pprint

URL = "https://superheroapi.com/api/2619421814940190/"


def search_intelligence_get(search_name, search_intelligence='intelligence'):
    list_intelligence = list()
    for i in search_name:
        url = URL + "search/" + i
        response_character = requests.get(url, timeout=1).json()["results"][0]
        list_intelligence.append({'id': response_character["id"],
                           'name': response_character["name"],
                           'intelligence': int(response_character["powerstats"][search_intelligence])})
    return list_intelligence


if __name__ == '__main__':
    search_hero = ['Hulk', 'Captain America', 'Thanos']
    power = 'intelligence'
    results = search_intelligence_get(search_hero, power)
    pprint(results)
    max_intelligence = {'id': 0, 'name': 'none', power: 0}
    for hero in results:
        if max_intelligence[power] < hero[power]:
            max_intelligence = hero
    print(f'\nГерой {max_intelligence["name"]} самый умный супергерой!!! Его интелект равен  {max_intelligence[power]}.')