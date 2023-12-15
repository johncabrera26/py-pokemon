# Create
"""
def create_pokemon(name, level, p_type):
    return {
        "name": name,
        "level": level,
        "type": p_type,
        "health": level * 10,
    }

def create_trainer(name):
    return {"name": name, "pokemon_list": []}

"""

# Attack
"""
attack_trainer(attacker, target)
"""

# Show info
"""
show_pokemon(pokemon_name)
"""

# Create Trainers
"""
ash = create_trainer("Ash", [charmander, squirtle, bulbasaur])
brock = create_trainer("Brock", [pikachu, geodude, pidgey])
"""

# Attack
"""
while True:
  option = input("What do you want to do? (attack, exit): ")

  if option == "attack":
    attack(ash, brock)
    brock(brock, ash)
    if ash.current_pokemon.health <= 0:
      ash.switch_pokemon(squirtle)
    if brock.current_pokemon.health <= 0:
      brock.switch_pokemon(pidgey)
  else:
    break
"""
