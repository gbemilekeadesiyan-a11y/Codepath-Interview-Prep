"""
U: 
P:
M:
I:


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array
        nums.sort()
        
        # Initialize the set of solutions
        solutions = set()
        
        # Loop over the array and check for solutions
        for i in range(len(nums)):
            # Set the target sum to 0 minus the current value
            target = 0 - nums[i]
            
            # Set the left and right pointers
            left = i + 1
            right = len(nums) - 1
            
            # Loop until the pointers cross
            while left < right:
                # Check if the sum of the values pointed to by the left and right pointers is equal to the target sum
                if nums[left] + nums[right] == target:
                    # Add the solution to the set and move the pointers
                    solutions.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    # Move the left pointer
                    left += 1
                else:
                    # Move the right pointer
                    right -= 1
                    
        # Return the list of solutions
        return list(solutions)




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize the longest length and the current length
        longest = 0
        current = 0
        
        # Initialize the dictionary of characters in the current substring
        seen = {}
        
        # Initialize the start index of the current substring
        start = 0
        
        # Loop over the string and update the current length
        for i, ch in enumerate(s):
            # Check if the character is in the dictionary of seen characters
            if ch in seen:
                # Update the longest length if needed
                longest = max(longest, current)
                
                # Update the start index of the current substring
                start = max(start, seen[ch] + 1)
            
            # Add the character to the dictionary and increment the current length
            seen[ch] = i
            current = i - start + 1
        
        # Return the longest length
        return max(longest, current)
