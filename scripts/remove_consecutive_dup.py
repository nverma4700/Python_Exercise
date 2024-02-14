def remove_consecutive_duplicates(input_list):
    '''
    Remove the occurrence of consecutive duplicates
    from the input list.
    '''
    last_elem = None
    new_list = []
    for elem in input_list:
        if elem != last_elem: # check if the last elem and current elem are equal or not
            new_list.append(elem) # if not then add the elem to new list
            last_elem = elem # assign current elem value to last_elem
            
    return new_list


# Testing: --> uncomment below:
input_list = [1, 4, 4, 4, 5, 6, 7, 4, 3, 3, 9]
print(remove_consecutive_duplicates(input_list))