def search(term=''):
    pokemons=['picachu', 'charmander', 'charmeleon']

    items=[item for item in pokemons if term in item]
    return items

print(search('char'))