
#   Move Zeroes



""" Understand:
    - Input: List of Integers and a target Number
    - Output: the Number of index pairs that sum is less than the target Number 
    - Edge Cases: Empty List 
    
    Plan: Two pointers for each Number, left = 0 and right = len(nums) - 1
          Add nums[left] and nums[right] and check if it is lesser than target
          If so : Store the pairs in a tuple (left, right)
          len(tuple) = Output 
          
"""
def count_pairs(nums, target):
    nums = sorted(nums)
    left, right = 0, len(nums) - 1
    count = 0

    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left   
            left += 1
        else:
            right -= 1              
    return count





# Check if an array is sorted   



""" Understand:
                - Input: List of Intergers: nums
                - Ouput: This is boolean 
                - Edge Cases: Duplicaes
                - A[i] == B[(i+x) % A.length]
    Plan:
                - drops check how many times neighbouring elements are greater than their previous. If they are greater than their previous then the modulos of the amount of drops should be one
                - Essentially: nums[i] > nums[(i + 1) % n] <=1 for it to be True
"""


def is_sorted_rotated(nums):
    drops = 0
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            drops += 1
    return drops <= 1



# Sub array is equals to k


"""
UNDERSTAND:
    - Input: a list of integers (can be negative) and an integer k
    - Output: the number of continuous subarrays whose sum equals k
    - "Continuous" means elements next to each other, any length (1 to n)
    - Edge cases:
        - Empty list -> 0
        - A single number equal to k counts as a subarray
        - Negative numbers mean the same running total can appear more than once
    - Examples:
        [1,1,1], k=2  -> 2   ([1,1] at index 0-1 and [1,1] at index 1-2)
        [1,2,3], k=7  -> 0   (no stretch adds to 7)

PLAN:
    - Keep a running total (prefix sum) as I walk through the list
    - If running total now = R, and an earlier running total was R - k,
      then the numbers between those two points add up to k
    - Use a frequency map to remember how many times each running total appeared
    - Start the map with {0: 1} so subarrays starting at index 0 get counted
    - Steps:
        1. count = 0, running = 0, seen = {0: 1}
        2. For each num:
             a. running += num
             b. count += how many times (running - k) appeared before
             c. record running in seen
        3. Return count
"""

def subarray_sum(nums, k):
    count = 0
    running = 0
    seen = {0: 1}

    for num in nums:
        running += num
        count += seen.get(running - k, 0)
        seen[running] = seen.get(running, 0) + 1

    return count