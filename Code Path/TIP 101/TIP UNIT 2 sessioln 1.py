
'--------'
def all_in(a, b):
    for num in a:
        if num not in b:
            return False
    return True
lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))   


'--------'
def create_dictionary (keys, values):
    new_dictionary ={}
    for i in range(len(keys)):
        new_dictionary[keys[i]] = values[i]
    return new_dictionary 


'--------'
def print_pair(dictionary, target):
    if target in dictionary:
        print("Key: " + target)
        print("Value: " + str(dictionary[target]))
    else:
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print(print_pair(dictionary, "patrick"))
print(print_pair(dictionary, "plankton"))
print(print_pair(dictionary, "spongebob"))


'--------'
def keys_v_values(dictionary):
    key_sum = 0
    value_sum = 0
    for key, value in dictionary.items():
        key_sum += key
        value_sum += value
    if key_sum > value_sum:
        return "keys"
    elif value_sum > key_sum:
        return "values"
    else:
        return "balanced" 
    

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)  



'--------'
def restock_inventory(current_inventory, restock_list):
    for item, quantity in restock_list.items():
        if item in current_inventory:
            current_inventory[item] += quantity
        else:
            current_inventory[item] = quantity
    return current_inventory   


current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print(restock_inventory(current_inventory, restock_list))
