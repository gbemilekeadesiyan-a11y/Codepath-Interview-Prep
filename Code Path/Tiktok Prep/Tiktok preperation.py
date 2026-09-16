"""Tiktok Preperation Montage"""     


""" 
1.1 countDrops

Given an array readings, return the number of positions where a value is strictly less than the value immediately before it.

readings = [3, 1, 4, 4, 2] → 2 (1 after 3, and 2 after 4)
readings = [1, 2, 3] → 0
readings = [5, 5, 5] → 0 (equal is not a drop)
readings = [7] → 0

Constraints: 0 ≤ readings.length ≤ 100000, -10^9 ≤ readings[i] ≤ 10^9 
"""  


def countDrops(nums):
    count = 0
    for num in range(1,len(nums)):
        if nums[num] < nums[num - 1]:
            count += 1
    return count


"""
 1.4 — isMonotonic


An array is monotonic if it is entirely non-decreasing or entirely non-increasing.

Non-decreasing means nums[i] <= nums[i+1] for every i
Non-increasing means nums[i] >= nums[i+1] for every i

Given an array nums, return true if it is monotonic and false otherwise.

Example

nums = [1, 2, 2, 3] → true (non-decreasing; equal values are allowed)
nums = [6, 5, 4, 4] → true (non-increasing)
nums = [1, 3, 2] → false (goes up, then down)
nums = [1, 1, 1] → true (satisfies both at once)
nums = [7] → true

Input/Output

[execution time limit] 4 seconds (py3)
[input] array.integer nums — 1 ≤ nums.length ≤ 100000, -10^5 ≤ nums[i] ≤ 10^5
[output] boolean"""


def isMonotonic(arr):
    increasing = False
    decreasing = False

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            increasing = True
        elif arr[i] < arr[i - 1]:
            decreasing = True

    return not (increasing and decreasing) 


""" 
Problem 1.5 — longestRun

Given an array values, return the length of the longest run of consecutive equal elements.

values = [1, 1, 2, 2, 2, 3] → 3
values = [4, 5, 6] → 1
values = [8, 8] → 2
values = [7, 7, 1, 7, 7, 7] → 3 (the later run is longer)
values = [] → 0

Constraints: 0 ≤ values.length ≤ 100000
"""

def longestRun(vals):
    if not vals:
        return 0

    best = 1
    current = 1

    for i in range(1, len(vals)):
        if vals[i] == vals[i - 1]:
            current += 1
        else:
            current = 1
        best = max(best, current)

    return best   


"""LC485:
Given a binary array nums (only 0s and 1s), return the maximum number of consecutive 1s.

[1,1,0,1,1,1] → 3
[1,0,1,1,0,1] → 2
[0,0,0] → 0
[1] → 1
"""
def findMaxconsecutiveOnes(ones):
    best = 0
    current = 0
    for n in ones:
        if n == 1:
            current += 1
        else:
            current = 0
        best = max(best, current)
    return best


"""
 1.6 — isPalindrome

Description

Given a string s, return true if it reads the same forwards and backwards, and false otherwise. Assume s contains only lowercase letters.

Example

s = "racecar" → true
s = "abba" → true
s = "abc" → false
s = "a" → true
s = "" → true

Input/Output

[execution time limit] 4 seconds (py3)
[input] string s — 0 ≤ s.length ≤ 100000, lowercase letters
[output] boolean"""  

def isPalindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()] 
    left = 0 
    right = len(cleaned) -1 
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        else:
            left +=1
            right -=1
    return True



""" cleaned = [c.lower() for c in s if c.isalnum()] """  



"""This is a Two pass  
Problem 2.5 — firstUniqueChar

LeetCode 387. Worth flagging: this is the exact shape your ColorStack source described as Q2 — "two pass with a hashmap."

Description

Given a string s, return the index of the first character that appears exactly once. If there is no such character, return -1.

Example

s = "leetcode" → 0
'l' appears once, and it's first.
s = "loveleetcode" → 2
'l', 'o', and 'e' all repeat. 'v' at index 2 is the first that doesn't.
s = "aabb" → -1
s = "z" → 0

Input/Output

[execution time limit] 4 seconds (py3)
[input] string s — 1 ≤ s.length ≤ 100000, lowercase English letters
[output] integer
"""
def firstUniqueChar(s):
    counts = {}   # create a dictionary with every letter and a count

    for ch in s:
        counts[ch] = 1 + counts.get(ch, 0)   # For every character in s, add one to counts[ch] 

    for i, ch in enumerate(s):
        if counts[ch] == 1 :    # look up in counts[ch] and if any of those letters have a count of 1, return their corresponding index in s 
            return i

    return -1  



""" 
2.1 — validateDigitWindows

You're given a matrix numbers with 3 rows and n columns, every cell a digit from 1 to 9. A 3×3 window slides left to right, giving n - 2 positions.

Return an array of length n - 2 where element i is true if window i contains every digit from 1 to 9.

Example

numbers = [[1,2,3,2,5,7], [4,5,6,1,7,6], [7,8,9,4,8,3]] → [true, false, true, false]
"""
def validateDigitWindows(numbers):
    n = len(numbers[0])
    result = []

    for c in range(n - 2):
        cells = numbers[0][c:c+3] + numbers[1][c:c+3] + numbers[2][c:c+3]
        result.append(len(set(cells)) == 9)

    return result  


numbers = [[1,2,3,2,5,7], [4,5,6,1,7,6], [7,8,9,4,8,3]] 
validateDigitWindows(numbers)




"""
Problem 3.2 — robotPath

A robot starts at (0, 0) facing north and executes a command string:

'F' — move forward one unit in the direction it faces
'L' — turn left 90°, don't move
'R' — turn right 90°, don't move
'B' — move backward one unit without turning

Return [x, y]. North is +y, east is +x.

"FFRF" → [1, 2]
"FB" → [0, 0]
"LLF" → [0, -1]
"" → [0, 0]   

move distance is 1 in this case

Constraints: 0 ≤ commands.length ≤ 100000"""  

def robotPath(commands):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]      # North, East, South, West; it is doen this way because of the how the robot moves (positive up and positive right)
    d = 0                                      # This is like the index for finding the direction you would turn from it's mean position d = 0 (facing North) this is the state.
    x = y = 0                                  # This is the result and the exact position of the robot after displacement.  they start at the origin.

    for cmd in commands:                       # Loop through the individuaL commands in command(R,L,F,B) 
        if cmd == 'R':
            d = (d+1)% 4                       # We keep it in modulos 4 because no matter the value, it is a unit of the index's in dirs so we can know the exact direction it moves in, reminder it only turns which is like moving a unit of one   
        elif cmd == 'L':
            d = (d-1) % 4
        elif cmd == "F":
            dx , dy = dirs[d]                 # the change in the displacement of x and y values of the coordinate of that point the robot is in 
            x += dx                           # You then add it to the present values of x and y 
            y += dy 
        elif cmd =='B':
            dx, dy = dirs[d]
            x -= dx                            # you do the opposite for backward movement
            y -= dy 
    return [x, y]                              # return the current position of x and y after the transformation.  

"""
ProcessInventory

Description

A warehouse tracks a single stock level, which starts at 0 and can never exceed capacity.

You are given an array operations, where each element is a pair [type, amount]. Process them in order, applying these rules:

type = 1 — restock. Add amount to the stock. If this would push the stock above capacity, the stock becomes capacity and the excess is discarded.
type = 2 — ship. Remove amount from the stock. If the stock is less than amount, nothing is shipped, the stock is unchanged, and a failed counter is incremented by 1.
type = 3 — audit. If the stock is odd, discard one unit. If it is even, nothing happens. The amount value is ignored for this type.

Return an array [finalStock, failed] 

"""


def processInventory(operations, capacity):
    stock = 0
    failed = 0

    for op_type, amount in operations:
        if op_type == 1:
            stock = min(amount + stock, capacity)
        elif op_type == 2:
            if stock >= amount:
                stock -= amount
            else:
                failed += 1
        elif op_type == 3:
            if stock %2 != 0:
                stock -= 1

    return [stock, failed]



""" 
2.2 isValidSudokuBoard

Given a 9×9 board of characters (digits '1'–'9' or '.' for empty), return true if it's valid. Valid means: no repeated digit in any row, any column, or any of the nine 3×3 sub-boxes. Empty cells are ignored, and the board need not be solvable.

A board with two 5s in the top row → false
A board with two 8s in the same 3×3 box → false
A sparse board with no conflicts → true

Constraints: board is always 9×9.

The hard part is indexing the 3×3 boxes. (row // 3, col // 3) identifies which box a cell belongs to. That trick shows up constantly.

""" 

def isValidGroup(group):
    filled = [x for x in group if x != '.']
    return len(set(filled)) == len(filled) 

def isValidSudoku(grid):
    for r in range(9):
        if not isValidGroup(grid[r]):
            return False

    for c in range(9):
        if not isValidGroup([grid[r][c] for r in range(9)]):
            return False

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            box = grid[r][c:c+3] + grid[r+1][c:c+3] + grid[r+2][c:c+3]
            if not isValidGroup(box):
                return False

    return True