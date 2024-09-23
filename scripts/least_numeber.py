def least_number(num):
    '''
    For a given number, return the least number for that range. 
    Example: Num 128990 --> returns 100000
    '''
    digit_str = str(num)
    least_num = digit_str[0] + '0'* (len(digit_str)-1)
    return(least_num)


# Testing: --> uncomment below
num = 128990
print(least_number(num))