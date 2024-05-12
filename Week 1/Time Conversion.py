#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extract hours, minutes, seconds, and AM/PM indicator
    hours, minutes, seconds = map(int, s[:-2].split(':'))
    period = s[-2:]
    
    # Adjust hours according to the period (AM or PM)
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0
    
    # Return the time in 24-hour format
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    result = timeConversion(s)
    
    fptr.write(result + '\n')
    
    fptr.close()

