#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Calculate the sum of all elements in the array
    total_sum = sum(arr)
    
    # Find the minimum and maximum elements in the array
    min_element = min(arr)
    max_element = max(arr)
    
    # Calculate the maximum and minimum possible sums
    max_sum = total_sum - min_element
    min_sum = total_sum - max_element
    
    # Print the results
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
