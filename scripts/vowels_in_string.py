def check_vowels_in_string(str):
    '''
    Returns the matching vowels and count of the vowels from 
    the input sting. 
    '''
    vowels = 'aeiou'
    vowels_list = []
    for char in str:
        if char.lower() in vowels:
            vowels_list.append(char)
    
    unique_vowels = set(vowels_list)
    match_count = len(vowels_list)
    return f"Matching vowels: {','.join(vowels_list)}, Unique Vowels: {','.join(unique_vowels)}, Match Count: {match_count}"

# Testing: --> uncomment below:
# str = "Hello Python World"
# print(check_vowels_in_string(str))