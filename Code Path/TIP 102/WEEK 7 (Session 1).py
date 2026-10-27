"""
Understand:
    Input: List of strings
    Output: Integer
    
    Edge cases:
Plan:
Itetrative, for loop using counter
Recursive:

Codnition: Without using len
Implement:

"""

"""def count_suits_iterative(suits):
    count = 0
    
    for item in suits:
        count +=1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    return 1 + count_suits_recursive(suits[1:])


print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))"""

def sum_stones(stones):
    
    def stone_sum(stones, i):
        if i == len(stones):
            return 0
        return stones[i] + stone_sum(stones, i + 1) 
    x = stone_sum(stones, 0)
    return x   

#print(sum_stones([5, 10, 15, 20, 25, 30]))
#print(sum_stones([12, 8, 22, 16, 10]))

#==================

# understand
# Input llist of strings
# output amount of unique strings

#Plan 
# Iterative Set and add everything from list and return length of set
# Recursive
# Create a nested function pass in the list a set and index make sure index isnt out of bounds 
# and push to set once index is at the end of the list return len

def count_suits_iterative(suits):
    unique = set(suits)
    return len(unique)


def count_suits_recursive(suits):
    unique = set()
    def recursive(index):
        if index == len(suits):
            return len(unique)
        unique.add(suits[index])
        return recursive(index + 1)
        
    return recursive(0)




# print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

def fibonacci_growth(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_growth(n-1) + fibonacci_growth(n-2)

print(fibonacci_growth(5))
print(fibonacci_growth(8))


# ==============

"""
plan:
Edge cases= power = 0, result = 1
power is negative, < 0, 1/(total_result)

"""


def power_of_four(n):
    if n == 0:
        return 1
    if n < 0:
        return 1/power_of_four(-n)
    
    if n >0:
        return 4 * power_of_four(n-1)


print(power_of_four(2))
print(power_of_four(-2))


def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]
    max_strength = strongest_avenger(strengths[1:])
    if strengths[0] < max_strength:
        return max_strength
    return strengths[0]


print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))






























