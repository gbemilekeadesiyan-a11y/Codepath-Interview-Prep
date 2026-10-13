class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
		# Valid catchphrase < 20 chars length and alpha+whitespace
        if len(new_catchphrase) < 20 and new_catchphrase.replace(" ","").isalpha():
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")
    
    def add_item(self, item_name):
        if item_name in ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]:
            self.furniture.append(item_name)

    def print_inventory(self):
        if len(self.furniture) == 0:
            print("Inventory empty")
        inventory = {}
        for item in self.furniture:
            if item not in inventory:
                inventory[item] = 1
            else:
                inventory[item] += 1

        output = []
        for item, quantity in inventory.items():
            output.append(f"{item}: {quantity}")
        print(", ".join(output))

        
        print(inventory)

def of_personality_type(townies, personality_type):
    matches = []

    for villager in townies:
        if villager.personality == personality_type:
            matches.append(villager.name)  
    return matches


def message_received(start_villager, target_villager):
    curr = start_villager
    while curr != None:
        if curr == target_villager:
            return True
        curr = curr.neighbor
    return False


#.get(item, default value if you can't get it)
# inventory[item] = inventory.get(item, 0) + 1
# Negligible time saved from lookup via using if/else statements
"""
# Prob 1
apollo = Villager("Apollo", "Eagle", "pah")

# Prob 2
bones = Villager("Bones", "Dog", "yip yip")
print(bones.greet_player("Samuel"))

# Prob 3
bones = Villager("Bones", "Dog", "ruff it up")
print(bones.greet_player("Samia"))

# Prob 4
alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

# Prob 5
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)
alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()

# Prob 7
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
# Prob 8
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))
"""