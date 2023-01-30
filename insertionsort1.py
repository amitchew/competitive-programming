import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    indexx = n-2
    val = arr[-1]

    while (val < arr[indexx]) and (indexx >= 0):
        arr[indexx+1] = arr[indexx]
        print(*arr)
        indexx -= 1

    arr[indexx+1] = val
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
