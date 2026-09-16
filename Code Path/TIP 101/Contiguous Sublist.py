#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_min_sublist_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#

def find_min_sublist_sum(nums, k):
    if len(nums) <k:
        return 0
    current_window_sum = sum(nums[:k])
    min_sum = current_window_sum
    for i in range(k, len(nums)):
        current_window_sum += nums[i] - nums[i - k]
        min_sum = min(min_sum, current_window_sum) 
    return min_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    k = int(input().strip())

    result = find_min_sublist_sum(nums, k)

    fptr.write(str(result) + '\n')

    fptr.close()
