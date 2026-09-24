"""def most_endangered(species_list):
    lowest_population = None
    endangered_species = None
    
    for species in species_list:
        if lowest_popuation is None  or species["population"] < lowest_population:
            lowest_population = species["population"] 
            endangered_species = species["name"]
    return endangered_species




species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))""" 


"""def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)
    count = 0
    
    for char in observed_species:
        if char in endangered_set:
            count += 1
    
    return count  



endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))"""

def navigate_research_station(station_layout, observations):
    position = {}
    for index, letter in enumerate(station_layout):
        position[letter] = index
        current_index = 0 
        total_time = 0
    
    for letter in observations:
        target_index = position[letter]
        total_time += abs(target_index - current_index)
        current_index = target_index  
    
    return total_time  



station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))




def prioritize_observations(observed_species, priority_species):
    priority_rank = {species: index for index, species in enumerate(priority_species)}
    
    priority_items = []
    non_priority_items = []
    
    for species in observed_species:
        if species in priority_species:
            priority_items.append(species)
        else:
            non_priority_items.append(species)
    
    priority_items.sort(key=lambda species: priority_rank[species])
    non_priority_items.sort()
    
    return priority_items + non_priority_items






