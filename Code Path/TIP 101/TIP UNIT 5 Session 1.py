# Question 1
class Pokemon:
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False  
        self.evolution = evolution
    
    def print_pokemon(self):
            print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        }) 
    
    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught == True:
            print(f" {self.name} I choose you!") 
        else:
            print(f"{self.name} is wild! catch them if you can!") 

    def add_type(self, new_type):
        self.types.append(new_type)
    
def get_by_type(my_pokemon, pokemon_type):
    matching_pokemon = []
    
    for pokemon in my_pokemon:
        if pokemon_type  in  pokemon.types:
            matching_pokemon.append(pokemon)
    
    return matching_pokemon

def get_evolutionary_line(starter_pokemon):
    evolutionary_line = []
    current_pokemon = starter_pokemon
    while current_pokemon is not None:
        evolutionary_line.append(current_pokemon.name)
        current_pokemon = current_pokemon.evolution

    return evolutionary_line

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)

print(get_evolutionary_line(charizard))  # Output: ['Charmander', 'Charmeleon', 'Charizard']
print(get_evolutionary_line(charmeleon))
    
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print([pokemon.name for pokemon in normal_pokemon])




