"TwoSum" 
"This is the best case" 
" We are guaranteed that there is a solution, no edge cases" 
" we can check the first item in nums then minus it from the target and check if that value is in the dictionary, if it does, we then have to check it's index which takes out duplicity "
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap ={}   #index: value
        for i, n in enumerate(nums):           # This basically iterate through both value and index
            diff = target - n                  # Finding the number to add to n to get to target
            if diff in prevMap:                # Check if this difference is in prevMap
                return [prevMap[diff],i]       # if it is, we return the index of that number or difference and the index(i) of the first number(n)
            prevMap[n] = i                     # if not found, we just move on to the next number
        return                                 # Since we are guaranteed that we have a sloution, we just return nothing (No edge cases)    



    def findPair(prices, budget):
        bookeeper= {}
        for i, price in enumerate(prices):
            diff = budget - price
            if diff in bookeeper:
                return [bookeeper[diff], i] 
            bookeeper[price] = i 
        return [-1, -1]


def shoePair(shoesize, shoesum):
    sizes ={}  # index: shoesize
    for i, shoesize in enumerate(sizes):
        sub = shoesum - shoesize
        if sub in sizes:
            return [sizes[sub], i] 
        sizes[shoesize] = i
    return[-1,-1]