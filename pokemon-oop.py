# Pokemon game
# pokemons:
  # Charmander
  # Squirtle
  # Bulbasaur
  # Pikachu
  # Geodude
  # Pidgey
  # ...
# trainers:
# level: 1..100
# health: 1..100
# alive: True/False
# type: Fire, Water, Grass, Electric, Rock, Flying, etc.
  # Fire: weakness: Water, resistance: Grass
  # Water: weakness: Grass, resistance: Fire
  # Grass: weakness: Fire, resistance: Water
  # Electric: weakness: Ground, resistance: Flying
  # Rock: weakness: Ground, resistance: Flying
  # Flying: weakness: Electric, resistance: Rock



class Pokemon:
    def __init__(self, name, level, tipo, health):
        self.name = name
        self.level = level
        self.type = tipo
        self.health = health
        self.alive = True

    def __str__(self):
        return 

    def lose_health(self, damage):
        pass

    def gain_health(self, heal):
        pass

    def die(self):
        self.alive = True
        print(f"{self.name} has been knocked out!")

    def revive(self):
        self.alive = True
        print(f"{self.name} has been revived!")

    def attack(self, other):
        pass


class Trainer:
    def __init__(self, name, pokemons, current_pokemon):
        self.name = name
        self.pokemons = pokemons
        self.current_pokemon = current_pokemon

    def __str__(self):
        return f"Trainer {self.name} has the following pokemon: {self.pokemons}"

    def attack(self, other_trainer):
        print(f"{self.name}'s turn to attack!")
        self.current_pokemon.attack(other_trainer.current_pokemon)

    def switch_pokemon(self, new_pokemon):
        self.current_pokemon = new_pokemon
        print(f"Go {self.current_pokemon.name}! It's your turn!")
        #print("You don't have this pokemon!")


# Create Pokemon
# charmander = Fire("Charmander", 1, "Fire", 100)
# squirtle = Water("Squirtle", 1, "Water", 90)
# bulbasaur = Grass("Bulbasaur", 1, "Grass", 92)
# pikachu = Electric("Pikachu", 1, "Electric", 100)
# geodude = Rock("Geodude", 1, "Rock", 80)
# pidgey = Flying("Pidgey", 1, "Flying", 72)


# Create Trainers
# ash = Trainer("Ash", [charmander, squirtle, bulbasaur], charmander)
# brock = Trainer("Brock", [pikachu, geodude, pidgey], geodude)

# Attack
"""
while True:
  option = input("What do you want to do? (attack, exit): ")

  if option == "attack":
    ash.attack(brock)
    brock.attack(ash)
    print(f"❤️‍🩹 {ash.name}'s {ash.current_pokemon.name} has {ash.current_pokemon.health} health left!")
    print(f"❤️‍🩹 {brock.name}'s {brock.current_pokemon.name} has {brock.current_pokemon.health} health left!")
    if ash.current_pokemon.health <= 0:
      ash.switch_pokemon(squirtle)
    if brock.current_pokemon.health <= 0:
      brock.switch_pokemon(pidgey)
  else:
    break
"""
