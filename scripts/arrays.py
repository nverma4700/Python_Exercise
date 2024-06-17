'''
Given an array, A, of N integers, print A's elements in reverse order as a single line of 
space-separated numbers.

Sample Input:
4
1 4 3 2

Sample output: 
2 3 4 1
'''

#!/bin/python3

import math
import os
import random
import re
import sys


# Logic 1:
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = []
    index = n-1
    for _ in range(n):
        result.append(str(arr[index]))
        index -= 1
    print(' '.join(result))

# Logic 2:
if __name__ == '__main__':
    n = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    result = ""
    for element in (arr[::-1]):
        result += f'{element}'
    print(result.strip())

# Logic 3:
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1]) # * will unpack the print out the list element