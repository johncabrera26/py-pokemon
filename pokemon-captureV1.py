import random
from urllib import request

def catch(id):

    response= request.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}/")
    
    data= response.json()

    capture_rate=data['capture_rate']
    random_number= random.randint(0,255)

    print(f"Capture eate:{capture_rate},Ramdom number: {random_number}")


    if random_number<capture_rate:
        print(f"{data['name']} capturado")
    else:
        print(f"{data['name']} escapado") 
            
catch(4)
catch(150)
catch(120)