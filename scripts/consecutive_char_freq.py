def consecutive_char_freq(string):
    '''
    Retuns a list of freq of all the consecutive character 
    in the input string.
    '''
    result = []
    count = 1
    for i in range(len(string) - 1): # range(len(string) - 1) to iterate to [i+1]
        if string[i] == string[i+1]: # character are consecutive
            count += 1 
        else:
            result.append(count) # if character are not consecutive, append the count to list
            count = 1 # reset the count to 1
    
    return result


# Testing: --> uncomment below:
# string = "geekksforgggeeks"
# print(consecutive_char_freq(string))