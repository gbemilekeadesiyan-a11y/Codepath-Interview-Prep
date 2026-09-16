def create_dictionary (keys, values):
    new_dictionary ={}
    for i in range(len(keys)):
        new_dictionary[keys[i]] = values[i]
    return new_dictionary   


keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']

print(create_dictionary(keys,values))                                                                   