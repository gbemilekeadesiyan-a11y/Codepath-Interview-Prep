
def find_last(lst, target):
	left = 0 # Initialize a left pointer to the 0th index in the list
	right = len(lst)-1 # Initialize a right pointer to the last index in the list
	result = -1
	
	while left <= right: # While left pointer is less than or equal to right pointer:
		mid = (left + right)//2 # Find the middle index of the array
		
		if lst[mid] == target: # If the value at the middle index is the target value:
			result = mid
			left = mid + 1 
            # Return the middle index
		elif lst[mid] < target: # Else if the value at the middle index is less than our target value:
			left = mid+1 # Update pointer(s) to only search right half of the list in next loop iteration
		else: # Else
			right = mid-1 # Update pointer(s) to only search left half of the list in next loop iteration
	
	return result # If we search whole list and haven't found target value, return -1
lst = [1, 3, 5, 7, 9, 11, 11, 13, 15] 
target = 11
print(find_last(lst,target))  


'''Problem 2: Factorial Cases
Given the base case and recursive case, write a function factorial() that returns the factorial of a non-negative integer n. 
The factorial of a number is the product of all numbers between 1 and n.

Base Case: The smallest number we can find a factorial of is 0. 
By definition, the factorial of 0 is 1.

Recursive Case: We can restate the problem to say that the factorial of n is n * the factorial of n-1.

def factorial(n):
	pass
Example Usage:

# Example Input: 5
Example Output:

# Expected Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120
💡 Hint: Writing Recursive Functions''' 

'''def factorial(n):
    if n == 0:
        return 1 
    elsedef sum_list(lst):

        return(n * factorial(n-1)) 

print(factorial(5))'''

'''Problem 3: Recursive Sum
Without using the built-in sum() function, write a function sum_list() 
that calculates the sum of all values in a list recursively.

What is the time complexity of this function? What is the space complexity?

def sum_list(lst):
	pass
Example Usage:

# Example Input: [1, 2, 3, 4, 5]
Example Output:

# Expected Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15''' 

'''def sum_list(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))'''



'''Problem 4: Recursive Power of 2
Given an integer n, return True if n is a power of two. 
Otherwise, return `False``.

An integer n is a power of two if there exists an integer x such that n == 2ˣ.

Solve the problem recursively. What is the time complexity of this function? What is the space complexity?

def is_power_of_two(n):
	pass
Example Usage:

print(is_power_of_two(16))
print(is_power_of_two(18))
Example Output:

True
False'''

'''def is_power_of_two(n):
    if n <= 0: #can't be a power of two
        return False
    if n == 1: #it ended up being 2/2, so it's a power of two
        return True
    if n%2 != 0: #it's an odd number, can't be a power of two
        return False
    else:
        return(is_power_of_two(n//2))

print(is_power_of_two(16))
print(is_power_of_two(18))'''

'''Problem 5: Binary Search I
Binary search is a searching algorithm that allows us to efficiently find 
the index of a given value within a sorted list. 
Given the pseudo code for binary search below, implement an iterative 
(non-recursive) implementation of binary search. 
There is also a recursive alternative that we’ll cover in the session 2 
problem set!

Evaluate the time and space complexity of your implementation.

def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list
	
	# While left pointer is less than right pointer:
		# Find the middle index of the array
		
		# If the value at the middle index is the target value:
			# Return the middle index
		# Else if the value at the middle index is less than our target value:
			# Update pointer(s) to only search right half of the list in next loop iteration
		# Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1

def binary_search(lst, target):
	pass
Example Usage:

# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
Example Output:

# Expected Output: 5
# Explanation: 11 has index 5 in the list
✨ AI Hint: Binary Search'''

'''def binary_search(lst, target):
	left = 0 # Initialize a left pointer to the 0th index in the list
	right = len(lst)-1 # Initialize a right pointer to the last index in the list
	
	while left <= right: # While left pointer is less than or equal to right pointer:
        
		mid = (left + right)//2 # Find the middle index of the array
		
		if lst[mid] == target: # If the value at the middle index is the target value:
			return mid # Return the middle index
		elif lst[mid] < target: # Else if the value at the middle index is less than our target value:
			left = mid+1 # Update pointer(s) to only search right half of the list in next loop iteration
		else: # Else
			right = mid-1 # Update pointer(s) to only search left half of the list in next loop iteration
	
	return -1 # If we search whole list and haven't found target value, return -1
              
lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(lst, target))'''

'''Problem 6: Backwards Binary Search
Generally binary search returns the index of the first occurrence of the target in the list. 
Write an updated version of binary search find_last() that, given a list that 
may contain duplicates, returns the index of the last occurrence of target.

Evaluate the time and space complexity of your function.

def find_last(lst, target):
	pass
Example Usage:

# Example Input: lst = [1, 3, 5, 7, 9, 11, 11, 13, 15], target = 11
Example Output:

# Expected Output: 6
# Explanation: The second (last) occurrence of 11 has index 6 in the list'''


def find_last(lst, target):
	left = 0 # Initialize a left pointer to the 0th index in the list
	right = len(lst)-1 # Initialize a right pointer to the last index in the list
	result = -1
	
	while left <= right: # While left pointer is less than or equal to right pointer:
		mid = (left + right)//2 # Find the middle index of the array
		
		if lst[mid] == target: # If the value at the middle index is the target value:
			result = mid
			left = mid + 1 
            # Return the middle index
		elif lst[mid] < target: # Else if the value at the middle index is less than our target value:
			left = mid+1 # Update pointer(s) to only search right half of the list in next loop iteration
		else: # Else
			right = mid-1 # Update pointer(s) to only search left half of the list in next loop iteration
	
	return result # If we search whole list and haven't found target value, return -1
lst = [1, 3, 5, 7, 9, 11, 11, 13, 15] 
target = 11
print(find_last(lst,target))

        
