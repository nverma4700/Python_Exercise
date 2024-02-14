def split_on_vowels(string):
    '''
    Split the string on the first vowel
    '''
    vowels = 'aeiou'
    for char in enumerate(string): 
        if char[1].lower() in vowels:
            split_index = char[0]
            break
    first_half, second_half = string[:split_index], string[split_index+1:]
    return ([first_half, second_half])
 

# Testing: --> uncomment below
# print(split_on_vowels('GFGaBst'))  