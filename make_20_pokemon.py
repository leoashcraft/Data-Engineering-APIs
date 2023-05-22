pokelist = ['ditto', 'pikachu', 'mewtwo', 'diglett', 'gastly', 'geodude', 'piplup', 'caterpie', 'vaporeon', 'infernape', 'gible', 'gyarados', 'registeel', 'drapion', 'budew', 'togekiss', 'jigglypuff', 'jynx', 'roselia', 'lapras']

def get_pokemon_by_type(pokemon_list):
    pokedex = {}
    for pokemon_name in pokemon_list:
        url       = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response  = requests.get(url)
        weight    = response.json()['weight']
        abilities = []
        for ability in response.json()['abilities']:
            abilities.append(ability['ability']['name'].title())
        for t in response.json()['types']:
            pokedex.setdefault(t['type']['name'], {})[pokemon_name] = {'Abilities': abilities, 'Weight' : weight}
    return pokedex
            
get_pokemon_by_type(pokelist)