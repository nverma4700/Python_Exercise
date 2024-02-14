def three_consecutive_integer(input_list):
    '''
    Iterate through a list and find a list of 3 consecutive 
    numbers
    '''
    result = []
    for i in range(0, len(input_list)-2, 2):
        if input_list[i] == input_list[i+1] == input_list[i+2]:
            result.append(input_list[i])
    return result

def consecutive_number(input_list):
    '''
    Iterate through a list and find a list of consecutive 
    numbers
    '''
    result = []
    for i in range(len(input_list)-1):
        if input_list[i] == input_list[i+1]:
            result.append(input_list[i])
    return list(set(result))


# Testing: --> uncomment below
input_list = [1, 1, 1, 64, 23, 23, 64, 22, 22, 22]
print(three_consecutive_integer(input_list))
print(consecutive_number(input_list))
