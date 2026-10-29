def find_cabin_index(cabins, preferred_deck, low = 0, High = None):
    if High == None:
        High = len(cabins) - 1
    
    if low > High:
        return low
    
    mid = (low + High) // 2 
    
    if cabins[mid] == preferred_deck:
        return mid 
    elif cabins[mid] < preferred_deck:
        return find_cabin_index(cabins, preferred_deck, mid + 1 , High)
    else:
        return find_cabin_index(cabins, preferred_deck, low , mid -1 )

    
    
print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))

        



        
def findTheDifference(s, t):
    if len(s) == len(t):
        return False
    count = {}
    for char in t:
        count[char] = count.get(char, 0) + 1 
    
    for char in s:
        count[char] -= 1
        if count[char] == 0:
            del count[char]
    return list(count.keys()) [0] # ["e"]