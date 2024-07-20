'''
Task: Given a square matrix, calculate the absolute difference 
between the sums of its diagonals. 

Sample Input:
3
11 2 4
4 5 6
10 8 -12

Sample Output:
15
'''
import math
import os
import random
import re
import sys


def diagonalDifference(arr, n):
    primary_diag_sum = 0
    secondary_diag_sum = 0
    for i in range(n):
        primary_diag_sum += arr[i][i]
        '''
        primary diagonal is: 
        11
           5
            -12
        '''
        secondary_diag_sum += arr[i][n-1-i]
        '''
        secondary diagonal is:
             4
           5
        10
        '''
    return abs(primary_diag_sum - secondary_diag_sum)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip()) # length of 2D array

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')
    print(arr)
    fptr.close()
