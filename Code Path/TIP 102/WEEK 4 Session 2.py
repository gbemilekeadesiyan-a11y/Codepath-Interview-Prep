"""
Your day consists of various tasks, each requiring a certain amount of time. To optimize your workday, you want to find a pair of tasks that fits exactly into a specific time slot you have available. You need to identify if there is a pair of tasks whose combined time matches the available slot.

Given a list of integers representing the time required for each task and an integer representing the available time slot, write a function that returns True if there exists a pair of tasks that exactly matches the available time slot, and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

"""
U: given a list of integers (task times), we want to output T if two integers in the list == to our available_time
false if no two integers in the list == our available_time
P: two pointers method, right pointer at the end of the array
if sum of left and right pointers > available_time right -= 1
if sum of left and right pointers < available_time left += 1
if sum == return True

P: 
"""


def find_task_pair(task_times, available_time):
    left = 0
    right = len(task_times) - 1
    sum = 0
    while left < right:
        sum = task_times[left] + task_times[right]
        if sum == available_time:
            return True
        elif sum > available_time:
            right -= 1
        else:
            left += 1

    return False
        

# task_times = [30, 45, 60, 90, 120]
# available_time = 105
# print(find_task_pair(task_times, available_time))

# task_times_2 = [15, 25, 35, 45, 55]
# available_time = 100
# print(find_task_pair(task_times_2, available_time))

# task_times_3 = [20, 30, 50, 70]
# available_time = 60
# print(find_task_pair(task_times_3, available_time))

#True
#True
#False 


"""You work with clients across different time zones and often have gaps between your work sessions. You want to minimize these gaps to make your workday more efficient. You have a list of work sessions, each with a start time and an end time. Your task is to find the smallest gap between any two consecutive work sessions.

Given a list of tuples where each tuple represents a work session with a start and end time (both in 24-hour format as integers, e.g., 1300 for 1:00 PM), write a function to find the smallest gap between any two consecutive work sessions. The gap is measured in minutes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

U:  - Input: List of tuples
    - Output: An Integer
P: Iterate through the list grab the last value and the first value of the next tuple and convert to minutes 
and then put it into your min val depending on if its less than your current minimum and return min


"""


[(900, 1100), (1300, 1500), (1600, 1800)] 
[900, 1100, 1300, 1500, 1600, 1800]


# work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)] # 2D 


# helper function to convert to minutes
def to_minutes(t):
    return (t//100) *60 + t % 100 

# if 0 or None
# comparison is : if 0 or None: min_val = valOne - valTwo

def find_smallest_gap(work_sessions):
    min_val = float('inf')
    for i in range(0, len(work_sessions) - 1):
        valOne = to_minutes(work_sessions[i][1]) # previous end
        valTwo = to_minutes(work_sessions[i + 1][0]) # next start
        min_val = min(min_val, abs(valTwo - valOne))
    return min_val

    # # sessions = []
    # # x = 1
    # # for i, group in range(0, len(work_sessions)):
    # #     sessions.append(work_sessions[i])  
    # #     x = 1 - x
    # #     sessions.append(group[x])

    # # minimum_val = sessions[0]
    # # for i in range(1, len(sessions)):
    # #     minimum_val = min(minimum_val, abs(sessions[i] - sessions[i - 1]))
    # # print(sessions)
    # # print(minimum_val)
    # return None

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1300, 1500)]
print(find_smallest_gap(work_sessions_3))


"""
smallest = None
  
for i in range(1,len(work_sessions)):
  prev_end = work_sessions[i-1][1]
  curr_start = work_sessions[i][0]
  gap = curr_start - prev_end
  
  if smallest is None or gap <smallest:
    smallest = gap
return smallest


"""



"""
You travel frequently and need to keep track of your expenses. You categorize your expenses into different categories such as "Food," "Transport," "Accommodation," etc. At the end of each month, you want to calculate the total expenses for each category to better understand where your money is going.

Given a list of tuples where each tuple contains an expense category (string) and an expense amount (float), write a function that returns the expense categories and the total expenses for each category. Additionally, the function should return the category with the highest total expense.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

U: Input a list of tuples
Output: Also a tuple of a dict and the highest expense category as a string


P: Initialize a dictionary and for every string category map it to a float value in the dictionary and also 
keep track of the maximum value of the dictionary with a tuple so we can keep the string and the float value



"""
