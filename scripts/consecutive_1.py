'''
Task: Convert a decimal to binary and print out max consecutive 1s
'''

import math
import os
import random
import re
import sys

def binary_representation(n): # Convert the decimal to binary
    binary = bin(n)[2:]
    return binary

def consecutive_1(bin):
    '''
    Takes a binary number and split it to based on 0. 
    Example: 
    Decimal = 111
    Binary = 1101111
    Split on 0's = ('11', '1111')
    Return the max of the above --> 4
    '''
    max_consecutive = max(len(x) for x in bin.split('0'))
    return max_consecutive

if __name__ == '__main__':
    n = int(input().strip())
    result = consecutive_1(bin=binary_representation(n))
    print(result)