def check_armstrong_number(num):
    '''
    Check if the number is armstrong or not.
    Armstrong Number: A number that is equal to the sum of cubes of its digits
    Condition: 
    153 = 1*1*1 + 5*5*5 + 3*3*3
    '''
    sum = 0  
    for i in str(num): # coverting a number to string to interate through each element
        sum += int(i) ** 3 # converting element to integer, calculating a cube and adding them.
    if num == sum:
        return f'Number: {num} is an anrmstrong number'
    else: 
        return f'Number: {num} is not an anrmstrong number'
    
    
# Testing: --> uncomment below:    
# print(check_armstrong_number(153))