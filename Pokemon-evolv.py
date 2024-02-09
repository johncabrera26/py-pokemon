from urllib import request

def evolve(id):
        #specie .>https://pokeapi.co/api/v2/pokemon-species/{id/}
    response=request.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}/")
    species= response.json()   

    evolution_url= species['evolution_chain']['url']

    response = request.get(evolution_url)
    evolution= response.json()


    evolve(4) # charmander
