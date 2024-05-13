#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#
def matchingStrings(strings, queries):
    # Create a dictionary to store the counts of strings
    string_counts = {}
    
    # Count occurrences of each string in the strings array
    for string in strings:
        string_counts[string] = string_counts.get(string, 0) + 1
    
    # Initialize a list to store the results
    results = []
    
    # Count occurrences of each query in the strings array
    for query in queries:
        results.append(string_counts.get(query, 0))
    
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())
    strings = [input() for _ in range(strings_count)]

    queries_count = int(input().strip())
    queries = [input() for _ in range(queries_count)]

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
