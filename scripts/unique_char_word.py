def unique_word(word):
    '''
    Returns True when all the char in a given word are
    unique, else returns False.
    '''
    word_set = set() # Empty set
    for char in word:
        if char in word_set: # Test is the character is already in the set
            return False
        word_set.add(char)

    return True