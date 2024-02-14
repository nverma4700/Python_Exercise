def remove_integers(str):
    '''
    Removes the interger from the given string
    '''
    alpha_list = []
    for char in str: 
        if char.isalpha():  # check is charcter is alphabet or not.
            alpha_list.append(char) # Adds alphabet char to the list.
    
    string_without_interger = ''.join(alpha_list) # convert the list to string.
    return string_without_interger


# Testing: --> uncomment below:
# str = "Hello123World"
# print(remove_integers(str))
            