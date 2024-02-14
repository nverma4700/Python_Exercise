def least_number(num):
    '''
    For a given number, return the least number for that range. 
    Example: Num 128990 --> returns 100000
    '''
    digit = list(str(num))
    for i in range(1, len(digit)):
        digit[i] = '0'
    
    least_digit = ''.join(digit)
    return int(least_digit)


# Testing: --> uncomment below
# num = 128990
# print(least_number(num))