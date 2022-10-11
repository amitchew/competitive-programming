#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    final = arr[-1]
    indx = n-2
    
    while (final < arr[indx]) and (indx>=0):
        arr[indx+1] = arr[indx]
        print(*arr)
        indx-=1
        
    arr[indx+1] = final
    print(*arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
