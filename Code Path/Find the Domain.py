#!/bin/python3

import math
import os
import random
import re
import sys
import ast




#
# Complete the 'search' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def search(nums, target):
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        bound = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                bound = mid  # Record candidate index
                if is_first:
                    right = mid - 1  # Keep searching left to find first occurrence
                else:
                    left = mid + 1   # Keep searching right to find last occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return bound

    start = find_bound(True)
    if start == -1:
        return [-1, -1]  # Target doesn't exist
    
    end = find_bound(False)
    return [start, end]

