#!/bin/python3

import math
import os
import random
import re
import sys
import ast

def find_val(names, val):
    if not val:
        return -1
    left = 0
    right = len(names) - 1

    while left <= right:
        mid = (left + right) // 2

        if names[mid] == val:
            return mid
        elif names[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return -1
        
