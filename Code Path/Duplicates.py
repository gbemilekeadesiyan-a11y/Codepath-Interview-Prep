"Duplicates"  
"return len(set(orderIds)) != len(orderIds)" # best case


def hasDuplicate(orderIds):
    seen = set() 
    for num in orderIds:
        if num in seen:
            return True
        seen.add(num) 
    return False    

"Sliding Window + Duplicate" 
# Brute:
"""def hasNearbyDuplicate(orderIds, k):
    n = len(orderIds)   # Order Id can be any length, we do not know the length
    for i in range(n):
        for j in range(i + 1, min(i + k + 1, n)):   # after we have i, we then chooose our range which is i+k+1 but min() ensures that this rane is not greater than the list
            if orderIds[i] == orderIds[j]:
                return True
    return False """


# Best Case: We only have to remove the first num in the range and add the num after the last num in the range. 
"""So the eviction target is the element at i - k, and you evict it after adding the current one.

Order matters:

Check whether the current value is already in the set → if yes, return True
Add the current value
Evict the element that has now fallen out of range"""


def hasNearbyDuplicate(orderIds, k):
    seen = set() #this is the window

    for i, num in enumerate(orderIds):   # So we gave every number in orderIds an index
        if num in seen:                  # Check if number is in seen
            return True
        seen.add(num)                    # If not we add number to seen 

        if i >= k:                      # This is then the window, this makes sure that i is like the last number in the window
            seen.discard(orderIds[i-k]) # remove the last and then go back to the start
    return False


