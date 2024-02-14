def remove_ith_char(str, i):
    '''
    Remove ith char from the string
    '''
    if i == 1: 
        return str[1:] # slice the string and remove the char at index 0
    else: 
        return (str[:i-1] + str[i:]) # slice the string to two part to romove the char and add the sting back. 
    

# Testing: --> uncomment below:
# str = 'hello'
# i = 2
# print(remove_ith_char(str, i)) # returns hllo