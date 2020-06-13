#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findNumber(arr, k):
    # Write your code here

    # bisearch
    arr.sort()
    left = 0
    right = arr_count - 1

    ans = "NO"
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] > k:
            left = mid
        elif arr[mid] < k:
            right = mid
        else:
            ans = "YES"
            break
    
    if arr[left] == k or arr[right] == k:
        ans = "YES"
    
    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findNumber(arr, k)

    # fptr.write(result + '\n')

    fptr.close()
