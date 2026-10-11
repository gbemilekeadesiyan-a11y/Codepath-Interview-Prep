"""def reverse_sentence(sentence):
    res = []
    for i in range(len(sentence)-1 , -1 , -1):
        res.append(sentence[i]) 
    return "".join(res)
        


sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))"""


"""def reverse_sentence(sentence):
    left = 0 
    right = len(sentence) -1 
    
    sentence = list(sentence)
    
    while left < right:
        sentence[left], sentence[right] = sentence[right] , sentence[left]
        left +=1
        right-= 1
    return "".join(sentence) 

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))"""

"""def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    for num in nums:
        largest = max(nums)
        smallest = min(nums)  
        if num != largest or smallest:
            return num

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))"""


"""def delete_minimum_elements(hunny_jar_sizes):
    res =[]
    while hunny_jar_sizes:
        smallest = min(hunny_jar_sizes)
        hunny_jar_sizes.remove(smallest)
        res.append((smallest))    
    return res  

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))"""


"""def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10    
        num //= 10           
    return total"""

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))
    
"""Understand:
Input: list of integers
Output: List Of Integers
Edge Cases:
    No of element in the array == 1
    No element return []
Plan: Remove from Original List and then append to the new list


"""

def delete_minimum_elements(hunny_jar_sizes):
    res = []
    if len(hunny_jar_sizes) <= 1:
        return hunny_jar_sizes
    while len(hunny_jar_sizes) > 1:
        smallest = min(hunny_jar_sizes)
        hunny_jar_sizes.remove(smallest)
        res.append(smallest)
    res.append(hunny_jar_sizes[0])
    return res


hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))
    

        
            




    
        
  
            